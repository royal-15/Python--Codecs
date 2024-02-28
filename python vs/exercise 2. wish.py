import time
timestamp = int(time.strftime('%H'))

#print(timestamp)
#timestamp = int(time.strftime('%H'))
#print(timestamp)
#timestamp = int(time.strftime('%M'))
#print(timestamp)
#timestamp = int(time.strftime('%S'))
#print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

if (timestamp <= 3):
    print("this is midnight time, go to bed!")
elif (timestamp <= 11):
    print("this is morning time, have a good morning!")
elif (timestamp <= 15):
    print("this is afternoon time, have a good afternoon!")
elif (timestamp <= 19):
    print("this is evening time, have a good evening!")
else:
    print("this is night time, have a good sleep!")
    