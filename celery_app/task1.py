import  time
from celery_app import app
from celery_app import topdoduban

@app.task
def topdouban():
    topdoduban.douban()