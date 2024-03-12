from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
try:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sachin@localhost:5432/fastapi"

    engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()
    print("Database Connection Successful...!")

    Base.metadata.create_all(bind=engine)


except Exception as e:
    print("Unable to connect to Database :", e)
        


