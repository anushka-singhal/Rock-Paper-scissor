import random
max_attempt = 3
sum1 =0
sum2 = 0
for attempt in range(max_attempt):
    computer = random.choice([1,2,3])
    you = int(input("Enter 1 for rock , 2 for scissor and 3 for paper"))
    if computer == 1 and you == 1:
        print("tie")
        
    elif computer == 1 and you == 2:
        print("1 point for player 1")
        sum1 += 1
        
    elif computer == 1 and you == 3:
        print("1 point for player 2")
        sum2 += 1
        
    elif computer == 2 and you == 1:
        print("1 point for player 2")
        sum2 += 1
        
    elif computer == 2 and you == 2:
        print("tie")
        
    elif computer == 2 and you == 3:
        print("1 point for player 1")
        sum1 += 1
        
    elif computer == 3 and you == 1:
        print("1 point for player 1")
        sum1 += 1
        
    elif computer == 3 and you == 2:
        print("1 point for player 2")
        sum2 += 1
        
    elif computer == 3 and you == 3:
        print("tie")
        
    print(f'total points for computer is , {sum1}')
    print(f'total points for you is ,{sum2}')

if sum1 == sum2:
    print("tie")
elif sum1 > sum2:
    print("computer won")
else:
    print("you won")