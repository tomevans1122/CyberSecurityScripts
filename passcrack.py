import random
import pyautogui

#characters the while loop will iterate through
character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_lst = list(character)

password = pyautogui.password("Enter password here: ")

guess_password = ''
while (guess_password != password):
    guess_password = random.choices(character_lst, k = len(password))

    print(">>>>"+str(guess_password)+"<<<<<")

    if (guess_password==list(password)):
        print("Your password is:" +"".join(guess_password))
        break
