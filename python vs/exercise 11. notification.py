import time
from plyer import notification as n
while True:
    n.notify(
        title = "That's enough. It's time to take a break!",
        message = "you have passed 2hr while working",
        app_icon = "C:\\Users\\DELL\\Desktop\\icons\\ico\\coffee.ico",
        timeout = 8
    )
    time.sleep((60*60)*2)

