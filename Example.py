
import random
import time

times = int(input("Wie viele Runden?"))

wins_loss = 0
loss_count = 0
win_count = 0
#put here the amount to win
win = 
#Put here the amount to lose
loss = 
#put here the start balance
balance = 100



while times > 0:
    coin = random.randint(0, 1)
    if coin == 1:
        times = times - 1
        win_count = win_count + 1
        wins_loss = wins_loss + 1
        print("Kopf")
        balance = balance * win
        print(balance)
        if balance == 0:
            break
    elif coin == 0:
        times = times - 1
        loss_count = loss_count - 1
        wins_loss = wins_loss - 1
        print("Zahl")
        balance = balance * loss
        print(balance)
        if balance == 0:
            break

print("win_loss:", wins_loss)
print("wins:", win)
print("loss:", loss)
