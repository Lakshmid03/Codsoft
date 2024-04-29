import random
global wincount
global lostcount
Data_list=['rock','paper','scissor']
wincount=0
lostcount=0
def check_result(input_value,random_value):
    global wincount
    global lostcount
    if input_value.lower()=='rock' and random_value == 'scissor':
        print("System choice is \n",random_value)
        print('Hurray! You won\n')
        wincount+=1
              
    elif input_value.lower()=='paper' and random_value == 'rock':
        print("System choice is \n",random_value)
        print('Hurray! You won\n')
        wincount+=1
        
    elif input_value.lower()== 'scissor' and random_value == 'paper':
        print("System choice is \n",random_value)
        print('Hurray! You won\n')
        wincount+=1
    else:
        print("System choice is \n",random_value)
        print('Sorry you lost the game\n')
        lostcount+=1
while True:
    random_choice=random.choice(Data_list)
    input_choice=input("Enter your choice Rock, paper, or Scissors\n")
    check_result(input_choice, random_choice)
    print(f'You won {wincount} system won {lostcount}\n\n')
    if input('Do you want to play again\n if yes enter Y \n if No enter N\n').lower() =='y':
        continue
    else:
        print("Game ended")
        break
        
        
        
