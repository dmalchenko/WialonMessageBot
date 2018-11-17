# -*- coding: utf8 -*-
import asyncio
import hashlib
import telebot
import config
from modules.dbmanager.DBManager import DBManager
from modules.models import Client
from aiohttp import web

bot = telebot.AsyncTeleBot(config.token)


async def handle_bot(request):
    data = await request.json()
    print(data)

    if 'message' not in data or 'text' not in data['message'] or 'chat' not in data['message']:
        return web.Response(status=200)

    user_id = int(data['message']['chat']['id'])

    client = await Client.select_by_user_id(user_id)
    if client is None:
        await Client.create_client(user_id)

    client_url = config.callback_url % hashlib.md5(user_id).hexdigest()
    bot.send_message(user_id, client_url)
    return web.Response(status=200)


async def handle_wialon(request):
    return web.Response(status=200, text='WLN!!!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    DBManager().set_settings(config.db)
    app = web.Application()
    app.add_routes([
        web.get('/index', handle_wialon),
        web.post('/index', handle_bot)
    ])
    app.on_shutdown.append(DBManager().on_shutdown)

    try:
        web.run_app(app, port=8801, shutdown_timeout=1)
    finally:
        loop.close()
