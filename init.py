# -*- coding: utf8 -*-
import asyncio
import config

from modules.dbmanager.DBManager import DBManager

DBManager().set_settings(config.db)


async def drop_table_client():
    query = 'DROP TABLE IF EXISTS client'
    return await DBManager().query_execute(query)


async def create_table_client():
    query = '''
            CREATE TABLE client (
            id serial PRIMARY KEY,
            user_id bigint,
            hash varchar(32),
            cnt integer,
        )
    '''
    return await DBManager().query_execute(query)


async def index_table_client():
    query = '''CREATE INDEX ON client(user_id)'''
    return await DBManager().query_execute(query)


async def drop_table_message():
    query = 'DROP TABLE IF EXISTS message'
    return await DBManager().query_execute(query)


async def create_table_message():
    query = '''
            CREATE TABLE message (
            id serial PRIMARY KEY,
            user_id bigint,
            title varchar(4096),
        )
    '''
    return await DBManager().query_execute(query)


async def index_table_message():
    query = '''CREATE INDEX ON message(user_id)'''
    return await DBManager().query_execute(query)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(drop_table_client())
    loop.run_until_complete(create_table_client())
    loop.run_until_complete(index_table_client())
    loop.run_until_complete(drop_table_message())
    loop.run_until_complete(create_table_message())
    loop.run_until_complete(index_table_message())
    loop.close()
