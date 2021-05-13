import time
from tasks import  add
from celery_app import task1,task2


task1.add.delay(3,5)
task2.multiply.delay(3,5)
print("end")

# if __name__ == '__main__':
#      print("start task")
#      result = add.delay(2,8)
#      while not result.ready():
#          print(result.get())
#          break