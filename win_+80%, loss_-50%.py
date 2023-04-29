import random
import time
times = int(input("Wie viele Runden?"))
wins_loss = 0
loss = 0
win = 0
balance = 100

while times > 0:
    coin = random.randint(0, 1)
    if coin == 1:
        times = times - 1
        win = win + 1
        wins_loss = wins_loss + 1
        print("Kopf")
        balance = balance * 1.8
        print(balance)
        if balance == 0:
            break
    elif coin == 0:
        times = times - 1
        loss = loss - 1
        wins_loss = wins_loss - 1
        print("Zahl")
        balance = balance * 0.5
        print(balance)
        if balance == 0:
            break
print("win_loss:", wins_loss)
print("wins:", win)
print("loss:", loss)
