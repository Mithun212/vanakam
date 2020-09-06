def score():
    try:
        r = int(input(">>"))
    except:
        print("give a value of int type between 0 and 6")
        return score()
    if r in range(0, 7):
        print("okay")
        return r
    else:
        print("give a number between 0 and 6")
        return score()


def match(t1name, t2name, x):
    wicket = x
    n = wicket
    s = 0
    while wicket <= n and wicket != 0:
        print(f"team {t2name}'s turn to bowl")
        bowler = score()
        print(f"team {t1name}'s turn to bat")
        batsman = score()
        if bowler != batsman:
            s += batsman
            print(f"{t1name} total score is {s}")
        elif bowler == batsman:
            wicket -= 1
            print(f"its a wicket....! {t1name} still got {wicket} wickets left ")
            if wicket == 0:
                print(f"team {t1name} is out of wickets and has scored {s}")
                return int(s), t1name
                # break
