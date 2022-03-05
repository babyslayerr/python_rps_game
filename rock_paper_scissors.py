
import os 
from random import choice


def RPS(user,computer,result):
    if user == '가위':
        if computer == user:
            result[1] += 1 #비김
            print('비겼습니다.')
        elif computer == '바위':
            result[2] += 1 #짐
            print('졌습니다.')
        elif computer == '보':
            result[0] += 1 #이김
            print('이겼습니다.')
    if user == '바위':
        if computer == user:
            result[1] += 1  #비김
            print('비겼습니다.')
        elif computer == '보':
            result[2] += 1 #짐
            print('졌습니다.')
        elif computer == '가위':
            result[0] += 1 #이김
            print('이겼습니다.')
    if user == '보':
        if computer == user:
            result[1] += 1  #비김
            print('비겼습니다.')
        elif computer == '가위':
            result[2] += 1 #짐
            print('졌습니다.')
        elif computer == '바위':
            result[0] += 1 #이김
            print('이겼습니다.')


# main

z = ['승리','무승부','패배']

while True:
    N = input() # 1: 가위바위보 실행 2:게임기록 3:종료
    if N == '1':            # 가위바위보 실행
        result = [0,0,0] #index win draw lose
        while True:
            c = choice(['가위','바위','보'])
            u = input("가위 바위 보 중에 입력하세요(종료 입력시 종료) ")
            if u == '종료': break
            if u not in ['가위','바위','보']:
                print('정확한 값을 입력하세요')
                continue
            if u == '종료': break
            RPS(u,c,result)
        with open("rock_paper_scissors_record",'a') as r:
            res = '{} {} {} \n'.format(result[0], result[1], result[2])
            r.writelines(list(res))

    elif N == '2':                  # 가위바위보 기록
        with open("rock_paper_scissors_record",'r') as w:
            w_word = w.readlines()
            for i in w_word:
                j = i.split()
                print('{} : {}, {} : {}, {} : {}'.format(z[0],j[0],z[1],j[1],z[2],j[2]))
            
    elif N == '3':  
        break     
    else:
        print('잘못된 값입니다. 1, 2, 3 중에 입력하세요')


