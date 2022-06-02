from email import message
from socket import timeout
from turtle import title
import psutil
from plyer import notification
import time
import tkinter as TK
#from psutil we will import the sensor-battery class and that we will have the battery remaining
while(True):
    battery=psutil.sensors_battery()
    plugged=battery.power_plugged
    percent=battery.percent
    
    if percent<=30 and plugged!=True:
       notification.notify(
        title="Battery Percentage",
        message=str(percent)+"% Battery Remaining",
        timeout=10
    )
    #After every 60 mins it will show the battery percentage
    time.sleep(60*60)
    continue