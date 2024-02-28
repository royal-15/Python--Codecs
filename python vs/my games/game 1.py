import win32com.client
from random import randint 
def get_random_even_number():
    for i in range(0, 10):
        n = randint(2, 1003)
        if (n % 2 == 0):
            return n 
            
num = get_random_even_number()
# print(num)

speaker = win32com.client.Dispatch("SAPI.Spvoice")
speaker.speak("enter 0 if you have done what i said")
speaker.speak("Pick any number that you want but not enter that number")
ready = int(input(":"))
if ready == 0:
    speaker.speak("so you have picked a number")
    speaker.speak("then now multiply that number by 2")
    ready = int(input(":"))
    if ready == 0:
        print(f"add {num}")
        speaker.speak(f"add {num} to your calculated number")
        ready = int(input(":"))
        if ready == 0:
            speaker.speak("give oneof your friend half of your calculated number")
            ready = int(input(":"))
            if ready == 0:
                speaker.speak("minus your starting choosen number in your current calculated number")
                ready = int(input(":"))
                if ready == 0:
                    print(f"Answer {num / 2}")
                    speaker.speak(f"is your current remaining number {num / 2}")
                    speaker.speak("if i'm wrong i will try to improve my skills")