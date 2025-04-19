from plyer import notification
import time


if __name__ == '__main__':
 while True:
  notification.notify(
   title="*** Take Rest ***",
   message= "jay",
   app_icon="", 
   timeout=5)
 time.sleep(10)

