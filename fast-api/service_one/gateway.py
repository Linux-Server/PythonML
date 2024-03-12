from fastapi import FastAPI
#!/usr/bin/env python
import pika



app = FastAPI()


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Helllo cdscswc!')

@app.get("/login")
def root():
    return {"message": "User logged In"}