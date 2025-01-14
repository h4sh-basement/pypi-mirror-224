#coding: utf-8
from flask import current_app
import os
from datetime import datetime, timedelta
from json import dumps, loads
import requests
from loguru import logger 
from notifiers import get_notifier
import pycountry 
from emoji import emojize
from esentity.models import TdsCampaign, TdsHit, Page, Activity
from esentity.telegram import telegram_api
import time
import ipaddress
from celery import shared_task


@shared_task
def add_vote(activity):
    logger.info('Add Vote: {0}'.format(activity))

    objs, total = Page.get(_id=activity['casino_id'])
    if total == 1:
        obj = objs.pop()
        _res = []
        _found = False
        _update = True

        hash = Activity.generate_id(activity['ip'], activity['ua'], activity['cid'])
        hash_dt = Activity.generate_id(activity['createdon'], activity['ip'], activity['ua'], activity['cid'])

        for item in obj.comments:
            if 'hash' in item and item['hash'] in [hash, hash_dt]:
                if not item['is_disable']:
                    item['publishedon'] = activity['createdon'] 
                    item['rate'] = activity['rate']

                    item['comment_pros'] = activity['pros']
                    item['comment_cons'] = activity['cons']
                    item['author'] = activity['name']
                else:
                    logger.info('Vote found: {0}, but is_disable'.format(item['hash']))
                    _update = False
                _found = True
            _res.append(item)
        
        if not _found:
            _res.insert(0, {
                'is_disable': False,
                'publishedon': activity['createdon'],
                'ip': activity['ip'],
                'country': activity['country_iso'],
                'hash': hash,

                'rate': activity['rate'],
                'comment_pros': activity.get('pros'),
                'comment_cons': activity.get('cons'),
                'author': activity.get('name'),
            })                

        if _update:
            obj.comments = sorted(_res, key=lambda d: d['publishedon'])
            resp, obj = Page.put(obj._id, obj.to_dict(), _signal=False)
            logger.info('Update casino [{1}]: {0}'.format(resp, obj.title))


@shared_task
def send_notify(msg, channel='default'):
    n = get_notifier('telegram')

    bots = current_app.config['TELEGRAM_TOKEN']
    _c = None
    if isinstance(bots, dict):
        if channel in bots:
            _c = bots[channel]
    elif isinstance(bots, str):
        _c = bots

    if _c:
        for cid in current_app.config['TELEGRAM_RECIPIENTS']:
            res = n.notify(
                message=f"[{current_app.config['TELEGRAM_PREFIX_MESSAGE']}] {emojize(msg)}", 
                token=_c, 
                chat_id=cid,
                disable_web_page_preview=True,
                disable_notification=True,
            )
            logger.info('Notify response: {0}'.format(res))


@shared_task
def send_email(template, to, subject, tv):
    _res = None
    _endpoint = current_app.config['MAIL_ENDPOINT']
    logger.info(f'Send email by: {_endpoint}')

    if 'mailgun.net/v3/' in _endpoint:
        _res = requests.post(
            _endpoint,
            auth=("api", current_app.config['MAIL_TOKEN']),
            data={"from": current_app.config['MAIL_FROM'],
                "to": to,
                "subject": subject,
                "template": template,
                "h:X-Mailgun-Variables": dumps(tv)})
    elif 'api.elasticemail.com/v4/' in _endpoint:
        _project = os.environ.get('PROJECT', 'project')
        _data = {
            "Recipients": {
                "To": [to]
            },
            "Content": {
                "Merge": tv,
                "From": current_app.config['MAIL_FROM'],
                "ReplyTo": current_app.config['MAIL_FROM'],
                "Subject": subject,
                "TemplateName": f"{_project}.{template}"
            }
        }

        _res = requests.post(
            _endpoint, 
            headers={'X-ElasticEmail-ApiKey': current_app.config['MAIL_TOKEN']},
            json=_data
        )

    if _res != None:
        logger.info(f'API response code: {_res.status_code}, content: {_res.json()}')
        
        if _res.status_code in [200]:
            logger.info(f'Email ({template}) send result: {_res.json()}')
        else:
            logger.info(f'Email ({template}) response: {_res.status_code}')


@shared_task
def tdscampaign_bots(data, section):

    def process_item(v, k):
        current_app.redis.sadd(f'tds_bots_{k}', v)

    for item in data:
        s = item
        if not '#' in s:
            if section == 'ip':
                if '-' in s:
                    min, max = s.split('-')
                    min = ipaddress.ip_address(min)
                    max = ipaddress.ip_address(max)
                    if min.version == 4 and max.version == 4 and min < max:
                        i = 0
                        while min <= max:
                            _v = ipaddress.ip_address(min) + i
                            logger.info(f'ip_address found: {_v}')
                            process_item(int(_v), 'ip')
                            i += 1
                else:
                    try:
                        ip_obj = ipaddress.ip_address(s)
                        if ip_obj.version == 4:
                            logger.info(f'ip_address found: {ip_obj}')
                            process_item(int(ip_obj), 'ip')
                    except ValueError:
                        try:
                            network = ipaddress.ip_network(s)
                            logger.info(f'ip_network found: {network}, hosts: {network.num_addresses}')

                            for _ip in network:
                                if _ip.version == 4:
                                    logger.info(f'ip_address found: {_ip}')
                                    process_item(int(_ip), 'ip')

                        except ValueError:
                            pass
            elif section == 'ua':
                logger.info(f'ua found: {s}')
                process_item(s, 'ua')


@shared_task
def tdscampaign_setup(id, campaign):
    logger.info('Setup TDS campaign: {0}'.format(campaign['name']))
    key = '{0}{1}'.format(campaign['domain'], campaign['alias'])
    current_app.redis.hset('tds_channels_url', id, key)

    if campaign['is_active']:
        campaign['id'] = id
        current_app.redis.hset('tds_channels', key, dumps(campaign, default=str))
        logger.info('Add campaign')
    else:
        current_app.redis.hdel('tds_channels', key)
        logger.info('Remove campaign')


@shared_task
def tdscampaign_clear(id):
    logger.info('Clear campaign stats: {0}'.format(id))
    campaigns, total = TdsCampaign.get(_id=id)
    if total == 1:
        campaign = campaigns.pop()
        if not campaign.is_active:
            hits, total = TdsHit.get(
                campaign_id=campaign._id,
                _process=False, 
                _source=False, 
                _all=True,
            )
            logger.info(f'Hits for remove: {total}')
            for item in hits:
                resp = TdsHit.delete(item['_id'], _refresh=False)
                logger.info(f'Hit removed: {resp}')

            current_app.redis.delete(f"tds_uniq_{campaign.alias}")
            logger.info(f'Uniq stack for {campaign.alias} removed')
        else:
            logger.warning(f'Campaign {campaign.name} is active, only disabled may by cleared')


@shared_task
def tdscampaign_hit(_doc):
    logger.info(f'Process TDS click: {_doc}')

    _cn = pycountry.countries.get(alpha_2=_doc['country_iso'])
    _doc['country'] = _cn.name if _cn else 'United Kingdom'

    resp, _ = TdsHit.put(TdsHit.generate_id(_doc['ip'], _doc['click_id']), _doc, _refresh=False, _signal=False)
    logger.info(f'Hit response: {resp}')

    _a = ''
    if _doc['action'] == '404':
        _a = ', 404'
    elif _doc['action'] in ['http', 'campaign', 'js']:
        _a = f", url: {_doc['url']}"

    msg = f"Hit: {_doc['campaign_name']} | {_doc['stream_name']} [{_doc['click_id']}], IP: {_doc['ip']} [{_doc['country_iso'].upper()}], is_bot: {_doc['is_bot']}{_a}"
    send_notify.apply_async(args=[msg])


@shared_task
def backup(indices, prefix):
    host = '{0}:{1}'.format(os.environ.get('ES', 'localhost'), 9200)
    logger.info('Process Snapshot Elasticsearch: {0}'.format(host))

    snap = f"{prefix}{datetime.utcnow().strftime('%Y-%m-%d')}"
    logger.info('Snap: {0}'.format(snap))

    snap_url = 'http://{0}/_snapshot/backup/{1}'.format(host, snap)

    r = requests.get(snap_url)
    if r.status_code == 200:
        r = requests.delete(snap_url)        
        logger.info('Snapshot {0} already exist, remove it: {1}'.format(snap, r.json()))

    if indices:
        r = requests.put(snap_url, json={'indices': indices})
        logger.info('Snapshot create: {0}, response: {1}'.format(r.status_code, r.json()))

        if r.status_code == 200:
            while True:
                time.sleep(5)
                r = requests.get(snap_url)
                res = r.json()

                for item in res['snapshots']:
                    if item['snapshot'] == snap:
                        if item['state'] == 'SUCCESS':
                            logger.info('Snapshot created: {0}'.format(res))

                            wl = [snap] + ['{1}{0}'.format((datetime.utcnow()-timedelta(days=i)).strftime('%Y-%m-%d'), prefix) for i in [1, 2, 3, 4, 5]]
                            logger.info('Actual Snaps: {0}'.format(wl))

                            snaps_url = 'http://{0}/_snapshot/backup/_all'.format(host)
                            r = requests.get(snaps_url)
                            if r.status_code == 200:
                                res = r.json()
                                for item in res['snapshots']:
                                    if prefix in item['snapshot'] and item['snapshot'] not in wl:
                                        snap_url = 'http://{0}/_snapshot/backup/{1}'.format(host, item['snapshot'])
                                        r = requests.delete(snap_url)        
                                        logger.info('Remove old snapshot: {0}'.format(item['snapshot']))
                            return
                        else:
                            logger.info('Snapshot {0} status: {1}'.format(snap, item['state']))
                        break


@shared_task
def process_tg_message(domain, bot_id, message):
    # delete_chat_photo
    # group_chat_created
    # supergroup_chat_created
    # channel_chat_created

    _data = current_app.redis.hget('tg_webhooks', f'{domain}:{bot_id}')
    if _data:
        _jobs = loads(_data)
        logger.info(f'Webhook jobs found: {_jobs}')

        uid = message['update_id']
        msg = message['message']
        mid = msg['message_id']
        cid = msg['chat']['id']

        logger.info(f'Process message, bot: {bot_id}, update_id: {uid}')
        logger.info(f'Message body: {msg}')

        if 'spectator' in _jobs['modules']:
            job = _jobs['jobs'].get(str(cid))
            if job:
                logger.info(f'Job for {cid} found: {job}')
                if job['job_remove_system_msg'] and ('new_chat_title' in msg or 'left_chat_member' in msg or 'new_chat_member' in msg or 'new_chat_photo' in msg):
                    telegram_api(_jobs['token'], 'deleteMessage', json={'chat_id': cid, 'message_id': mid})
                    logger.info(f"Message {mid} in {msg['chat']['title']} removed")
            else:
                logger.info(f'Job for {cid} not found')
    else:
        logger.info(f'Webhook disable or not found, bot_id: {bot_id}, domain: {domain}')
