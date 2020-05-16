import math
import time
print('Hello, welcome to CalcuFrame, here we use the game\'s algorithms to find out your EHP (Effective hit points) and total Damage reduction!')
nominal_armor = int(input('What is your frame\'s nominal armor? (Nominal armor is what you see in the stats menu)\n>'))
divisor = nominal_armor + 300
dr = nominal_armor / divisor * 100 // 1
damage_taken = 100 - dr
print('Your damage reduction is %s percent, this means you only take %s percent of all damage you are dealt!' % (dr, damage_taken))
cont = input('Would you like to go on to calculate EHP? y/n\n>')
if cont == 'y':
    nominal_health = int(input('To find out your EHP we will need your nominal health as well, what is it?\n>'))
    ehp = nominal_health * ((nominal_armor + 300) / 300) // 1
    print('Your Effective Hit Points are %s!' % ehp)
    time.sleep(1)
    print('We hope this has helped make your life easier!')
else:
    input('We hope this has helped make your life easier!')
