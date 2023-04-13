import os

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
    def __init__(self, db_path='database/kiosk.db'):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)    # if file does not exist, create the file
        db_uri = 'sqlite:///' + db_path                         # merge the path to create a uri
        engine = create_engine(db_uri)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)



    def create_user(self, id_number, first_name, last_name, password):
        """Create user account

        Args:
            id_number (string): user id_number
            first_name (string): user first_name
            last_name (string): user last_name
            password (string): user password

        Returns:
            object: instance of a user
        """
        session = self.Session()
        user = User(id_number=id_number, first_name=first_name, last_name=last_name, password=password)
        session.add(user)
        session.commit()
        session.close()
        return user

    # Function to read user
    def read_user(self, id_number):
        session = self.Session()
        user = session.query(User).filter(User.id_number == id_number).first()
        session.close()
        return user


    # 
    def update_user(self, id_number, first_name=None, last_name=None, password=None):
        session = self.Session()
        user = session.query(User).filter(User.id_number == id_number).first()
        if user:
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if password:
                user.password = password
            session.commit()
        session.close()
        return user

    def delete_user(self, id_number):
        session = self.Session()
        user = session.query(User).filter(User.id_number == id_number).first()
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return True
        session.close()
        return False
