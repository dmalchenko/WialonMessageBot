from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, insert, any_

from modules.dbmanager.DBManager import DBManager

Base = declarative_base()


# BaseModel for db_models
class BaseModel(object):
    @classmethod
    async def select_by_id(cls, item_id: int):
        query = select([cls]).where(cls.id == int(item_id))
        return await DBManager().query_fetchrow(query)

    @classmethod
    async def select_by_user_id(cls, item_id: int):
        query = select([cls]).where(cls.user_id == int(item_id))
        return await DBManager().query_fetchrow(query)

    @classmethod
    async def select_by_ids(cls, item_ids: list):
        query = select([cls])
        if item_ids:
            query = query.where(cls.id == any_(item_ids))
        return await DBManager().query_fetch(query)

    @classmethod
    async def select_all(cls):
        return await DBManager().query_fetch(select([cls]))