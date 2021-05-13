from datetime import timedelta
from celery.schedules import crontab
BROKER_URL="redis://localhost:6379/0"


CELERY_RESULT_BACKEND="redis://localhost:6379/0"

CELERY_TIMEZONE = "Asia/Shanghai"

# 导入指定的任务模块
CELERY_IMPORTS =(
    'celery_app.task1',
    'celery_app.task2'
)


CELERYBEAT_SCHEDULE = {
    "task1":{
        "task":"celery_app.task1.add",
        "schedule":timedelta(seconds=10),# 每10s执行一次
        "args":(2,8)
    },
    "task2":{
        "task": "celery_app.task2.multiply",
        "schedule":crontab(hour=17,minute=32),  # 每天定时执行
        "args": (2, 8)
    }
}