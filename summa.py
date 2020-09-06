import random
import time
from python import match

n = random.randint(0, 9)
# print(n)
if n in [0, 2, 4, 6, 8]:
    n = 0
else:
    n = 1
# print(n)
coin = ["head", "tail"]
# hd = ["head", "tail", "Head", "Tail", "HEAD", "TAIL"]
# print(coin[n])
team = []


def wick():
    try:
        w = int(input("number of wickets: "))
    except:
        print("give a value of int type: ")
        return wick()
    if w in range(1, 11):
        return w
    else:
        print("""
        wicket should not be 0 and should not exceed 10.
        it should be of type int
        """)
        return wick()


wic = wick()

for i in range(2):
    x = input("give your team a name: ")
    team.append(x)
print(team)


def tos():
    hd = ["head", "tail", "Head", "Tail", "HEAD", "TAIL"]
    i = input(f"team {team[n]} choose btw head and tail: ")
    if i in hd:
        return i
    else:
        print("choose a value between head/tail: ")
        return tos()


toss = tos()

print("tossing the coin....")
# time.sleep(3)
a = ["bat", "Bat", "BAT"]
b = ["bowl", "Bowl", "BOWL"]
count = 0
s1 = (0, "")
s2 = (0, "")
for i in range(2):
    if toss == coin[n] and count == 0:
        chosen = input(f"{team[n]} won the toss and choose to? ")
        # if chosen in a and chosen in b:

        count += 1
        if chosen in a:
            s1 = match(team[n], team[n-1], wic)
            print("""

first innings is over

            """)
            # time.sleep(3)
            if count == 1:
                s2 = match(team[n-1], team[n], wic)
                break
        elif chosen in b:
            s1 = match(team[n-1], team[n], wic)
            print("""

first innings is over

            """)
            time.sleep(3)
            if count == 1:
                s2 = match(team[n], team[n-1], wic)
                break
    elif toss != coin[n] and count == 0:
        chosen = input(f"{team[n]} lost the toss and {team[n-1]} chooses to? ")
        count += 1
        if chosen in a:
            s1 = match(team[n-1], team[n], wic)
            print("""

first innings is over

            """)
            time.sleep(3)
            if count == 1:
                s2 = match(team[n], team[n-1], wic)
                break
        elif chosen in b:
            s1 = match(team[n], team[n-1], wic)
            print("""

first innings is over

            """)
            time.sleep(3)
            if count == 1:
                s2 = match(team[n-1], team[n], wic)
                break

if s1[0] > s2[0]:
    print(f"{s1[1]} won the match")
