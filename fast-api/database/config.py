from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
def connect_postgres():
    # Database configuration
    # postgresql://postgres:axomium1234@database-1.cwlixsy5zjqr.ap-south-1.rds.amazonaws.com:5432/sreshma
    try:
        DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" + \
                       f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        Base = declarative_base()
    except Exception as e:
        print(e)
