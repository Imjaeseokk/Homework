import random

numbers = {1: "A", 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: "J", 12: "Q", 13: "K"}
values = {v: k for k, v in numbers.items()}
# types = ["c","d","h","s"]
cards = sorted([i for i in range(1, 11)] * 2)
isUserTurn = True
# isUserTurn = random.getrandbits(1)
userChip = 40
comChip = 40

def getCard():  # card draw
    # number = random.randint(1,13)
    number = random.randint(1, len(cards))  # indian pocker
    # type = random.randint(0,3)
    return cards.pop(number - 1)


def compareCard(userCard, comCard):
    if userCard > comCard:
        return 1  # User Win
    elif userCard < comCard:
        return 0  # Computer Win
    else:
        return -1  # Draw

def user(comAct,userChip,comAddChip):
    userAddChip = 0
    if not comAct is None:
        actions = ["Fold","Call","Raise"]
        action = actions[int(input("Fold?Call?Raise?(0/1/2): "))]

    elif comAct is None:
        actions = ["Fold","Bet"]
        action = actions[int(input("Fold?Bet?(0/1): "))]

    if action in ["Bet","Raise"]:       # bet or raise 할 때
        userAddChip = int(input("몇 개의 Chip을 베팅하시겠습니까?"))
        userChip -= userAddChip
        print(action, "하셨습니다, 베팅한 Chips는", userAddChip, "입니다")

    if action == "Call":                # computer가 raise하고 call 할 때
        userChip -= comAddChip
        userAddChip = comAddChip
        print(action,"하셨습니다")

    if action == "Fold":
        print("Fold 하셨습니다")
    return action, userChip, userAddChip

def computer(userAct,comChip,userAddChip):
    comAddChip = 0
    if not userAct is None:
        actions = ["Fold","Call","Raise"]
    else:
        actions = ["Fold","Bet"]
    action = actions[random.randint(0, len(actions) - 1)]


    if action in ["Raise","Bet"]:
        comAddChip = random.randint(1,4) + userAddChip
        while comChip < comAddChip:
            comAddChip = random.randint(1, 4) + userAddChip
        comChip -= comAddChip
        print(f"Computer는{comAddChip}개{action}했습니다")

    if action == "Call":
        comChip -= userAddChip
        comAddChip = userAddChip
        print("Computer는", action, "했습니다")

    if action == "Fold":
        print("Computer는 Fold 했습니다")

    return action,comChip, comAddChip

def foldCheck(user,comp):
    if user == "Fold":
        return False
    elif comp == "Fold":
        return True
    else:
        return None

i = 0
while i < 10:
    if len(cards) == 0:
        cards = sorted([i for i in range(1, 11)] * 2)
    print(cards)
    betChip = 0
    comAct = None
    userAct = None
    end = False
    isUserWin = None
    isCalled = None
    userCard = getCard()
    comCard = getCard()

    print(f"\n기본베팅 전, 베팅된 칩: {betChip}, User Chip: {userChip} Computer Chip: {comChip}")
    userChip -= 1           # 기본 베팅
    comChip -= 1            # 기본 베팅
    betChip = 2             # 기본 베팅된 칩

    userAddChip = 0
    comAddChip = 0


    print("상대방의 Card는",comCard,"입니다")
    if isUserTurn:
        while not end:
            userAct, userChip, userAddChip = user(comAct, userChip, comAddChip)
            isUserWin = foldCheck(userAct, comAct)

            betChip = betChip + userAddChip
            print(betChip, userChip, comChip)
            comAddChip = 0

            if not isUserWin is None:
                break
            if userAct == "Call":
                isCalled = True
                break

            comAct, comChip, comAddChip = computer(userAct, comChip, userAddChip)
            isUserWin = foldCheck(userAct, comAct)

            betChip = betChip+ comAddChip
            print(betChip, userChip, comChip)
            userAddChip = 0

            if not isUserWin is None:
                break
            if comAct == "Call":
                isCalled = True
                break

    elif not isUserTurn:
        while not end:
            comAct, comChip, comAddChip = computer(userAct, comChip, userAddChip)
            isUserWin = foldCheck(userAct, comAct)

            betChip = betChip  + comAddChip
            print(betChip, userChip, comChip)
            userAddChip = 0

            print(isUserWin)
            if not isUserWin is None:
                break
            if comAct == "Call":
                isCalled = True
                break

            userAct, userChip, userAddChip = user(comAct, userChip, comAddChip)
            isUserWin = foldCheck(userAct, comAct)

            betChip = betChip + userAddChip
            print(betChip, userChip, comChip)
            comAddChip = 0


            if not isUserWin is None:
                break
            if userAct == "Call":
                isCalled = True
                break

    if isCalled:
        print("card:", userCard,comCard)
        if compareCard(userCard,comCard) == 1:
            userChip += betChip
        elif compareCard(userCard,comCard) == 0:
            comChip += betChip
        else:
            userChip += betChip // 2
            comChip += betChip // 2
        print(f"\n기본베팅 전, 베팅된 칩: {betChip}, User Chip: {userChip} Computer Chip: {comChip}")
        print(f"{i + 1}번째 Turn 종료했습니다.")
        continue

    if isUserWin:
        userChip += betChip
    elif isUserWin is False:
        comChip += betChip
    else:
        userChip += betChip//2
        comChip += betChip//2

    print(f"{i+1}번째 Turn 종료했습니다.")
    isUserTurn = not isUserTurn
    i += 1
