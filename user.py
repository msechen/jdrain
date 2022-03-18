#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
import datetime
import os
import re
import sys
import time

from telethon import events, TelegramClient

from .. import chat_id, jdbot, logger, API_ID, API_HASH, PROXY_START, proxy, JD_DIR, TOKEN
from ..bot.utils import cmd, V4, QL, CONFIG_SH_FILE, get_cks, AUTH_FILE
from ..diy.utils import getbean, rwcon, my_chat_id, myzdjr_chatIds, shoptokenIds

bot_id = int(TOKEN.split(":")[0])

client = TelegramClient("user", API_ID, API_HASH, proxy=proxy, connection_retries=None).start() if PROXY_START else TelegramClient("user", API_ID, API_HASH, connection_retries=None).start()


@client.on(events.NewMessage(chats=[bot_id, my_chat_id], from_users=chat_id, pattern=r"^user(\?|\？)$"))
async def user(event):
    try:
        msg = await jdbot.send_message(chat_id, r'`user.py`监控已正常启动！')
        await asyncio.sleep(5)
        await jdbot.delete_messages(chat_id, msg)
    except Exception as e:
        title = "【💥错误💥】"
        name = "文件名：" + os.path.split(__file__)[-1].split(".")[0]
        function = "函数名：" + sys._getframe().f_code.co_name
        tip = '建议百度/谷歌进行查询'
        await jdbot.send_message(chat_id, f"{title}\n\n{name}\n{function}\n错误原因：{str(e)}\n\n{tip}")
        logger.error(f"错误--->{str(e)}")


@client.on(events.NewMessage(chats=[-1001728533280, bot_id, myzdjr_chatIds], pattern=r'export\s(computer_activityId|comm_activityIDList|jd_mhurlList|jd_nzmhurl|wish_appIdArrList|jd_redrain_half_url|jd_redrain_url|M_WX_COLLECT_CARD_URL|jd_cjhy_activityId|jd_zdjr_activityId).*=(".*"|\'.*\')'))
async def activityID(event):
    try:
        text = event.message.text
        if "computer_activityId" in text:
            name = "电脑配件"
        elif "comm_activityIDList" in text:
            name = "jdjoy_open通用ID任务"
        elif "jd_mhurlList" in text:
            name = "盲盒任务抽京豆"
        elif "jd_nzmhurl" in text:
            name = "女装盲盒抽京豆"
        elif "wish_appIdArrList" in text:
            name = "许愿池抽奖机"
        elif "jd_redrain_url" in text:
            name = "整点京豆雨"
        elif "jd_redrain_half_url" in text:
            name = "半点京豆雨"
        elif "M_WX_COLLECT_CARD_URL" in text:
            name = "集卡任务"
        elif "jd_cjhy_activityId" in text:
            name = "cj组队瓜分"
        elif "jd_zdjr_activityId" in text:
            name = "lz组队瓜分"
        else:
            return
        msg = await jdbot.send_message(chat_id, f'【监控】 监测到`{name}` 环境变量！')
        messages = event.message.text.split("\n")
        change = ""
        for message in messages:
            if "export " not in message:
                continue
            kv = message.replace("export ", "")
            key = kv.split("=")[0]
            value = re.findall(r'"([^"]*)"', kv)[0]
            configs = rwcon("str")
            if kv in configs:
                continue
            if key in configs:
                configs = re.sub(f'{key}=("|\').*("|\')', kv, configs)
                change += f"【替换】 `{name}` 环境变量成功\n`{kv}`\n\n"
                msg = await jdbot.edit_message(msg, change)
            else:
                if V4:
                    end_line = 0
                    configs = rwcon("list")
                    for config in configs:
                        if "第五区域" in config and "↑" in config:
                            end_line = configs.index(config) - 1
                            break
                    configs.insert(end_line, f'export {key}="{value}"\n')
                else:
                    configs = rwcon("str")
                    configs += f'export {key}="{value}"\n'
                change += f"【新增】 `{name}` 环境变量成功\n`{kv}`\n\n"
                msg = await jdbot.edit_message(msg, change)
            rwcon(configs)
        if len(change) == 0:
            await jdbot.edit_message(msg, f"【取消】 `{name}` 环境变量无需改动！")
            return
        try:
            if "computer_activityId" in event.message.text:
                await cmd('otask /jd/own/raw/jd_computer.js now')
            elif "comm_activityIDList" in event.message.text:
                await cmd('otask /jd/own/raw/jd_joyjd_open.js now')
            elif "jd_mhurlList" in event.message.text:
                await cmd('otask /jd/own/raw/jd_mhtask.js now')
            elif "jd_nzmhurl" in event.message.text:
                await cmd('otask /jd/own/raw/jd_nzmh.js now')
            elif "wish_appIdArrList" in event.message.text:
                await cmd('otask /jd/own/raw/jd_wish.js now')
            elif "M_WX_COLLECT_CARD_URL" in event.message.text:
                await cmd('otask /jd/own/raw/m_jd_wx_collectCard.js now')
            elif "jd_cjhy_activityId" in event.message.text:
                await cmd('otask /jd/own/raw/jd_cjzdgf.js now')
            elif "jd_zdjr_activityId" in event.message.text:
                await cmd('otask /jd/own/raw/jd_zdjr.js now')
            elif "jd_redrain_url" in event.message.text:
                msg = await jdbot.send_message(chat_id, r'`更换整点雨url完毕\n请定时任务0 0 * * * jtask jd_redrain now')
                await asyncio.sleep(1)
                await jdbot.delete_messages(chat_id, msg)
            elif "jd_redrain_half_url" in event.message.text:
                msg = await jdbot.send_message(chat_id, r'`更换半点雨url完毕\n请定时任务30 21,22 * * * jtask jd_redrain_half now')
                await asyncio.sleep(1)
                await jdbot.delete_messages(chat_id, msg)
            else:
                await jdbot.edit_message(msg, f"看到这行字,是有严重BUG!")
        except ImportError:
            pass
    except Exception as e:
        title = "【💥错误💥】"
        name = "文件名：" + os.path.split(__file__)[-1].split(".")[0]
        function = "函数名：" + sys._getframe().f_code.co_name
        tip = '建议百度/谷歌进行查询'
        await jdbot.send_message(chat_id, f"{title}\n\n{name}\n{function}\n错误原因：{str(e)}\n\n{tip}")
        logger.error(f"错误--->{str(e)}")
