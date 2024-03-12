from fastapi import FastAPI
import os
from dotenv import load_dotenv
from database import config
load_dotenv()
app = FastAPI()

@app.get("/")
def root():
    api_key = os.getenv('NAME')
    print(api_key)
    config.connect_postgres()
    return "Hello World"