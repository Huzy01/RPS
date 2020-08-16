
from random import randint
player=input("select rock (r), paper(p), scissors(s)")



print(player, "vs", end=' ')

chosen = randint(1,3)
#print(chosen)


if chosen==1:
    computer="r"
elif chosen == 2:
  computer="p"
else:
  computer = "s" 
  
print(computer)

if player==computer:
  print('DRAW!')
  
elif player=='r' and computer=='s':
  print('You Wins!')
  
elif player=='s' and computer=='r':
  print('Computer Win!')

elif player=='p' and computer=='r':
  print('You Win!')
  
elif player=='p' and computer=='s':
  print('Computer Wins')
