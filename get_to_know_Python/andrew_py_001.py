from random import randint
print ('gost game')
feeling_brave=True
score=0
while feeling_brave:
    ghost_door=randint(1, 3)
    print('three doors ahead...')
    print('a gost behind one.')
    print('which door do you open?')
    door=input('1, 2, or 3?')
    door_num=int(door)
    
    if door_num==ghost_door:
        print('GHOST!')
        feeling_brave=False
    else:
        print('no ghost!')
        print('you enter the next room.')
        score=score+1
print('run away!')
print('game over! you scored',score)    
