from random import randint

def rps():
    l = ["rock","paper","sciser"] #  0 = rock , 1 = paper , 2 = sciser

    print("\n(Enter 0 for rock, 1 for paper or 2 for sciser)\n")
    
    i = 1
    while True:
        print(f"Round ({i})\n")
        u = int(input("Your move: "))

        if(u > 2):
            raise ValueError("Must enter 0 , 1 or 2")
        elif(u < 0):
            raise ValueError("Must enter 0 , 1 or 2")

        b = randint(0,2)
        print(f"\nBots move: ({b}) {l[b]}")

        if(b == u):
            print("\nIts a draw\n")
        elif(b == 0 and u == 1):
            print("\nYou win\n")
        elif(b == 1 and u == 2):
            print("\nYou win\n")
        elif(b == 2 and u == 0):
            print("\nYou win\n")
        else:
            print("\nYou lose\n")
        print("----------------------------------\n")
        i = i + 1
            
rps()