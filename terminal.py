stamina = 0
HP = 100
alienhp = 180
import random
#introduce
print("Hi welcome to explore new planet")
print("Now we're landing on a new planet. We should explore now, What should we do first  ")
print("1. Explore now \n2. Stay down ")
ans = int(input("your answer : "))
if ans == 1 :
    stamina += 5
    print(f" stamina: {stamina}")
    print(f" HP: {HP}")
elif ans == 2 :
    stamina += 1
    print(f" stamina: {stamina}")
    print(f" HP: {HP}")
else :
    print('please choose 1 ro 2')

#meet alien : add while for loop fight
while HP > 0 and alienhp > 0:
    print ('Ho no! We meet alien')
    print ('1. ran out! \n2. fight!')
    ans = int(input("your answer : "))
    if ans == 1 :
        alien = random.randint(10,30)
        print(f"The alien tries to catch you with power {alien}!")
        if stamina >= alien :
            stamina -= alien
            print(f"You escaped! Remaining stamina: {stamina}")
        else :
            HP -= alien
            if HP >= 0 :
                print(f"You couldn't run fast enough. HP: {HP}, Stamina: {stamina}")
            else :
                print(f"You couldn't run fast enough. HP: {0}, Stamina: {stamina}")
    elif ans == 2 :
        #we fight
        attack = random.randint(50,80)
        alienhp -= attack
        print(f"You fought bravely! You dealt {attack} damage to the alien.")
        print(f"Alien's HP: {alienhp}")
        #alien attack
        print('Oh! I think we should fight back.')
        alienattack = random.randint(50,70)
        HP -= alienattack
        print(f"The alien strikes back! You lose {alienattack} HP.")
        if HP >= 0 :
            print(f"Your HP: {HP}")
        else :
            print(f"Your HP: {0}")
    else :
        print('please choose 1 ro 2')
#chack end game
if HP <= 0:
    print("\nYou were defeated by the alien. Game Over.")
elif alienhp <= 0:
    print("\nYou defeated the alien! You win!")
    print(f"Your HP: {HP}, Stamina: {stamina}, Alien HP: {alienhp}")
