import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def KBC():
    speaker.speak("Enter your answer bitween (1-4) or 0 to quit")
    questions = [
        ["Which is the single largest internal organ by mass in the human body?","Liver", "Gallbladder", "Kidney", "Stomach",1],
        ["Which of these is a non-renewable source of energy?","Solar power", "Hydro power", "Wind power", "Natural gas",4],
        ["Which of these does the carpenter use to smoothen the surface of a wooden furniture?","Butter paper", "Silver paper", "Tissue paper", "Sandpaper",4],
        ["A video clip from Manikarnika: The Queen of Jhansi, starring Kangana Ranaut was shown?","Jhansi", "Gwalior", "Jaipur", "Varanasi",4],
        ["Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?","Virat Kohli","Sunil Gavaskar","VVS laxman","Rahul Dravid",1],
        ["Ranthambore, Sariska and Keoladeo Ghana are all names of what?","National Parks","Goosebumps","Mountains","Rivers",1],
        ["India's official entry to Oscars 2021, ” Jallikattu ” is, a film in which language?","Hindi","Punjabi","Kannada","Malayalam",4],
        ["Which of the following companies was originally started as a loom manufacturing unit in 1909?","Suzuki","CEAT","Honda","Mercedes",1],
        ["What is the profession of Kabir in the film Kabir Singh?","Engineer","Cricketor","Athlete","Doctor",4],
        ["Which state is the largest producer of sugarcane in India?","Maharashtra","Karnataka","Madhya Pradesh","Uttar Pradesh",4],
        ["Which of these colors when mixed with red will produce the color orange?","Violet","Green","Orange","Yellow",4],
        ["Which part of the plant absorbs water and nutrients from the soil?","Stem","Buds","Leafs","Root",4],
        ["Who of the following personalities is not married to a sports person?","Anushka Sharma","Sakshi Singh Rawat","Mahesh Bhupathi","Sharmila Tagore",3],
        ["Jafdarabadi, Surti, Neely Ravi, Bhadavari, Nagpuri, Mehsana and Toda are all of the breeds of which animal?","Cow","Hen","Goat","Buffalo",4],
        ["Which ingredient is mixed in milk is a popular home remedy for healing any internal injury?","Lemon","Honey","Almond","Turmeric",4]
    ]
    levels = [" ₹ 1,000"," ₹ 2,000"," ₹ 3,000"," ₹ 5,000"," ₹ 10,000"," ₹ 20,000"," ₹ 40,000"," ₹ 80,000"," ₹ 160,000"," ₹ 320,000"," ₹ 640,000"," ₹ 1,250,000"," ₹ 5,000,000"," ₹ 1 crore"," ₹ 7 crore"]
    money ="₹ 0"
    for i in range(0,len(questions)):
        print(f"\n-: your question for {levels[i]} is :-\n")
        speaker.speak(f"your question for {levels[i]} is")
        print(questions[i][0],"\n")
        speaker.speak(questions[i][0])
        speaker.speak("your options are")
        print(f"1. {questions[i][1]}")
        speaker.speak(f"1. {questions[i][1]}")
        print(f"2. {questions[i][2]}")
        speaker.speak(f"2. {questions[i][2]}")
        print(f"3. {questions[i][3]}")
        speaker.speak(f"3. {questions[i][3]}")
        print(f"4. {questions[i][4]}\n")
        speaker.speak(f"and 4. {questions[i][4]}")
        reply = int(input(": "))
        if (reply > 4):
            raise ValueError("you must pick an answer between (1-4)")
        elif (reply == 0):
            print("Quited.\n")
            speaker.speak("You quit the game")
            money = levels[i-1]
            break
        elif (reply == questions[i][-1]):
            print(f"(✔) Correct answer! You have won {levels[i]}\n")
            speaker.speak(f"Correct answer! You have won {levels[i]}")
            print("------------------------------------------------\n")
            if (i == 4):
                money = levels[4]
            elif(i == 9):
                money = levels[9]
            elif(i == 14):
                money = levels[14]
        else:
            print("\n(✘) Wrong answer!")
            speaker.speak("Wrong answer")
            speaker.speak("The right answer is")
            print(f"\n: {questions[i][-1]}  {questions[i][questions[i][-1]]}")
            speaker.speak(f"{questions[i][questions[i][-1]]}")
            break
    print(f"Your take home money is:{money}")
    speaker.speak(f"Your take home money is:{money}")

# if __name__ == "__main__":
#     mood = input("Wanna play KBC ?\ntype \" y \" for Yes or \" n \" for No: ")
#     if (mood == "y"):
#         print("The game is started.")
#         if __name__ == "__main__":
#             KBC()
#     elif(mood == "n"):
#         print("The game did not start.")
#         exit()
#     else:
#         raise ValueError("must enter answer in y or n")

if __name__ == "__main__":
    KBC()
