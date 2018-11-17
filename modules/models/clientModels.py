import hashlib
from sqlalchemy import Column, Integer, BIGINT, String, insert
from modules.dbmanager import DBManager
from .baseModels import Base, BaseModel


# Object client
class Client(Base, BaseModel):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    user_id = Column(BIGINT, nullable=False)
    hash = Column(String)
    cnt = Column(Integer, default=0)

    @classmethod
    async def add_client(cls, user_id):
        query = insert(cls)
        ins = query.values(user_id=user_id, cnt=0, hash=hashlib.md5(user_id).hexdigest())
        return await DBManager().query_execute(ins)

    @staticmethod
    async def create_client(user_id):
        return await Client.add_client(user_id=user_id)
