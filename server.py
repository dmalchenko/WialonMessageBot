# -*- coding: utf8 -*-
import asyncio
import hashlib
import telebot
import config
from modules.dbmanager.DBManager import DBManager
from modules.models import Client
from aiohttp import web

bot = telebot.AsyncTeleBot(config.token)


def get_user_hash(user_id):
    user_id = user_id + 4579
    return hashlib.md5(user_id.to_bytes(4, 'big')).hexdigest()


async def handle_bot(request):
    data = await request.json()
    print(data)

    if 'message' not in data or 'text' not in data['message'] or 'chat' not in data['message']:
        return web.Response(status=200)

    user_id = int(data['message']['chat']['id'])
    hash = get_user_hash(user_id)

    client = await Client.select_by_user_id(user_id)
    if client is None:
        await Client.create_client(user_id, hash)

    client_url = config.callback_url % hash
    bot.send_message(user_id, client_url)
    return web.Response(status=200)


async def handle_wialon(request):
    hash = request.rel_url.query['hash']
    client = await Client.select_by_hash(hash)
    if client is None:
        return web.Response(status=404, text='Client with this hash not found')
    print(client['user_id'])
    return web.Response(status=200, text='Client found')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    DBManager().set_settings(config.db)
    app = web.Application()
    app.add_routes([
        web.get('/notify', handle_wialon),
        web.post('/index', handle_bot)
    ])
    app.on_shutdown.append(DBManager().on_shutdown)

    try:
        web.run_app(app, port=8801, shutdown_timeout=1)
    finally:
        loop.close()
