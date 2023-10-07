import random

numbers = {1:"A",2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"J",12:"Q",13:"K"}
values = {v:k for k,v in numbers.items()}
# types = ["c","d","h","s"]
cards = sorted([i for i in range(1,11)]*2)
isUserTurn = random.getrandbits(1)
userChip = 40
comChip = 40
# print(cards)

def getCard(): # card draw
    # number = random.randint(1,13)
    number = random.randint(1,len(cards))  # indian pocker
    # type = random.randint(0,3)
    return cards.pop(number-1)

def firstAction(isUserTurn,uChip,cChip,bChip,cCard):
    if isUserTurn:
        action = bool(int(input("포기하시겠습니까? 베팅하시겠습니까? (0: 포기, 1: 베팅)\n: ")))
        if not action:
            cChip += bChip
            status = "Fold"
            bChip = 0
        else:
            userBet = int(input("얼마나 베팅하시겠습니까? :"))
            bChip += userBet
            uChip -= userBet
            status = "Bet"
    else:
        # 유저 카드에 따라 컴퓨터가 베팅할 확률 정의해야함, 일단 난수로
        # highRate = cCard / 5 #(0.0~2.0)
        # betRate = highRate * random.random()
        betRate = random.random()
        if betRate >= 0.5:
            comBet = random.randint(1,4)
            bChip += comBet
            cChip -= comBet
            status = "Bet"
        else:
            uChip += bChip
            status = "Fold"
            bChip = 0

    return uChip,cChip,status,bChip

def compareCard(userCard,comCard):
    if userCard > comCard:
        return 1 # User Win
    elif userCard < comCard:
        return 0 # Computer Win
    else:
        return -1 # Draw

i = 0
while i < 10:
    betChip = 0

    userCard = getCard()
    comCard = getCard()
    userChip -= 1
    comChip -= 1
    betChip = 2
    print("Computers Card is", comCard)
    # betting func
    userChip,comChip,status,betChip = firstAction(isUserTurn,userChip,comChip,betChip,comCard)
    if status == "Bet":
        print("betting된 상황입니다")
        print("User's Chip:", userChip, "Computer's Chip:", comChip, "Bet: ", betChip)
        if isUserTurn:      # user가 bet 했으니까 computer가 action
            pass
        else:               # computer가 bet 했으니까 user가 action
            print("")
        # 이후에 상대방이 포기/콜/레이즈 하는지 확인
    elif status == "Fold":
        #해당 턴이 종료됨
        print("User's Chip:",userChip,"Computer's Chip:",comChip,"Bet: ",betChip)


    # if compareCard(userCard,comCard) == 1:
    #     print("You Win")
    # elif compareCard(userCard,comCard) == 0:
    #     print("You lose")
    # else:
    #     print("Draw")


    # cycle
    isUserTurn = not isUserTurn
    i += 1
    # print("is Users Turn?",isUserTurn)