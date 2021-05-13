from celery import  Celery

app = Celery("demo")
# 通过Celery 实例配置加载
app.config_from_object("celery_app.celeryconfig")