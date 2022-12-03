from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


database_engine = create_engine('sqlite:///memory?check_same_thread=False', echo=True)
BaseModel = declarative_base()
DatabaseSession = sessionmaker()
DatabaseSession.configure(bind=database_engine)
database_session = DatabaseSession()



