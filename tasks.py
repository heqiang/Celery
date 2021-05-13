import time
from celery import  Celery



app  =Celery("my_task",broker="redis://localhost:6379/0",backend="redis://localhost:6379/0")

@app.task
def add(x,y):
    print("enter add func")
    time.sleep(4)
    return  x+y

