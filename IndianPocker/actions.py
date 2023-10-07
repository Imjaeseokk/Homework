import random

end = 0
userTurn = True
comAct = None
userAct = None
def user(comAct):
    if not comAct is None:
        print("상대방의 action은", comAct,"입니다")
    action = input("fold?call?raise?(0/1/2): ")
    return action

def computer(userAct):
    if not userAct is None:
        print("User의 Action은",userAct,"입니다")
        actions = ["fold","call","raise"]
    else:
        actions = ["fold","bet"]
    action = actions[random.randint(0,len(actions)-1)]

if not userTurn:
    comAct = computer()
while not end:
    userAct = user(comAct)
    comAct = computer()
    if userAct in ["Fold","Call"] or comAct in ["Fold","Call"]:
        print(userAct,comAct)
        end = True