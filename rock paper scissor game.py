print('GAME')
import random

print("Welcome to the rock paper scissor game")
attempts=1
computer_point=0
your_point=0
while (attempts<=10):
      lst=["r","p","s"]
      ran=random.choice(lst)
      x=input("For rock press 'r'\nFor paper press 'p'\nFor scissor press 's'\nChoose your option:  ")
      x=x.lower()
      if x=='r' and ran=='r':
            print("Tie")
            print("You chose rock and computer also chose rock!")
            print("Nobody gets point")
      elif x=='p' and ran=='p':
            print("Tie")
            print("You chose paper and computer also chose paper!")
            print("So Nobody gets point")
      elif x=='s' and ran=='s':
            print("Tie")
            print("You chose scissor and computer also chose scissor!")
            print(" So Nobody gets point")
      elif x=='r' and ran=='p':
            computer_point+=1
            print("You chose rock but computer chose paper")
            print("So Computer Won the Round")
      elif x=='r' and ran=='s':
            your_point+=1
            print("Computer chose scissor but yu chose rock")
            print("So You Won the Round")
      elif x=='p' and ran=='s':
            computer_point+=1
            print("You chose rpaper but computer chose scissor")
            print("So Computer Won the Round")
      elif ran=='r' and x=='p':
            your_point+=1
            print("Computer chose rock but chose paper")
            print("So You Won the Round")
      elif ran=='r' and x=='s':
            computer_point+=1
            print("Computer chose rock but chose scissor")
            print("So Computer Won the Round")
      elif ran=='p' and x=='s':
            computer_point+=1
            print("Computer chose paper but chose scissor")
            print("So Computer Won the Round")
      else:
            print("invalid Input")
            continue
      attempts+=1
print(f"your score: {your_point} \ncomputer's score: {computer_point}")
if computer_point>your_point:
      print("computer won and you lost\n")
elif your_point>computer_point:
      print("you won and computer lost")
else:
      print("It was a tie")
attempts+=1
if attempts>10:
      print("game over")
      
            
            
      
      
      
      
      
