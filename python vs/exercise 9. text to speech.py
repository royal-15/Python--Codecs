import win32com.client as wc

speaker = wc.Dispatch("SAPI.SpVoice")

# a = input("Enter your text\n")
# speaker.speak(a)

l = ["hey there", "how are you"]
for i in l:
    speaker.speak(i)