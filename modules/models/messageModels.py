from sqlalchemy import Column, Integer, String, BIGINT, insert
from modules.dbmanager import DBManager
from .baseModels import Base, BaseModel


# Object message
class Message(Base, BaseModel):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    user_id = Column(BIGINT, nullable=False)
    message = Column(String)

    @classmethod
    async def add_message(cls, user_id, message):
        query = insert(cls)
        ins = query.values(user_id=user_id, cntmessage=message)
        return await DBManager().query_execute(ins)

    @staticmethod
    async def create_user(user_id, message):
        return await Message.add_message(user_id=user_id, message=message)
