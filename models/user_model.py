from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id_number = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)

class UserDatabase:
    def __init__(self, db_uri='sqlite:///example.db'):
        engine = create_engine(db_uri)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def create_user(self, first_name, last_name, id_number, password):
        session = self.Session()
        user = User(first_name=first_name, last_name=last_name, id_number=id_number, password=password)
        session.add(user)
        session.commit()
        session.close()
        return user

    def read_user(self, id):
        session = self.Session()
        user = session.query(User).filter(User.id == id).first()
        session.close()
        return user

    def update_user(self, id, first_name=None, last_name=None, id_number=None, password=None):
        session = self.Session()
        user = session.query(User).filter(User.id == id).first()
        if user:
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if id_number:
                user.id_number = id_number
            if password:
                user.password = password
            session.commit()
        session.close()
        return user

    def delete_user(self, id):
        session = self.Session()
        user = session.query(User).filter(User.id == id).first()
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return True
        session.close()
        return False
