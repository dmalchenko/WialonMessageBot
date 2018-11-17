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
    async def add_client(cls, user_id, hash):
        query = insert(cls)
        ins = query.values(user_id=user_id, cnt=0, hash=hash)
        return await DBManager().query_execute(ins)

    @staticmethod
    async def create_client(user_id, hash):
        return await Client.add_client(user_id=user_id, hash=hash)
