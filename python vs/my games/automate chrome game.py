import pyautogui
from PIL import Image, ImageGrab
import time


def hitkey(key):
    pyautogui.press(key)


def iscolide(data):
    # Rectangle for cactus :-
    for i in range(355, 365):
        for j in range(426, 505):
            if data[i, j] > 150:
                hitkey("up")
                return

    # Rectangle for birds :-
    for i in range(371, 381):
        for j in range(300, 423):
            if data[i, j] > 150:
                hitkey("down")
                return


if __name__ == "__main__":
    print("Hey... dino game about to start in 3 seconds")
    time.sleep(3)
    hitkey("up")
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        iscolide(data)

        # # Rectangle for cactus :-
        # for i in range(415, 425):
        #     for j in range(426, 505):
        #         data[i, j] = 0

        # # Rectangle for birds :-
        # for i in range(426, 436):
        #     for j in range(300, 423):
        #         data[i, j] = 71

        # image.show()
        # break
