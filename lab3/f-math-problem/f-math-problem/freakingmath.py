from random import *

def generate_quiz():
    op = choice(['+','+','+','+','-','-','-','*','/'])
    err = choice([-1,0,0,1])
    x = randint(1,10)
    y = randint(1,10)
    from eval import calc
    dis_play_result = calc(x,y,op) + err
    infor_list = [x,y,op,dis_play_result]
    return infor_list

def check_answer(x, y, op, result, user_choice):
    from eval import calc
    result_real = calc(x,y,op)
    if result_real == result and user_choice == True:
        return True
    if result_real != result and user_choice == False:
        return True
    else:
        return False
