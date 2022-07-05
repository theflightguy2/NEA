from coremodules import *
import csv
#login unit
counter = 1
authed = False
while counter <= 3 and authed == False:
    print('User 1: ')
    us1_uname = input('Enter Your Username: ')
    us1_pwrd = input('Enter your Password: ')

    rslt = login(username=us1_uname, password=us1_pwrd)
    print(rslt)
    if rslt == False:
        print('Incorrect!')
        counter += 1
    else:
        print('Authorised!')
        authed = True

if counter > 3:
    print('Max Attempts Reached!')
    quit()


counter = 1
while counter <= 3:
    print('User 2: ')
    us2_uname = input('Enter Your Username: ')
    us2_pwrd = input('Enter your Password: ')

    rslt = login(us2_uname, us2_pwrd)
    if rslt == False:
        print('Incorrect!')
        counter += 1
    else:
        print('Authorised!')
        break

if counter > 3:
    print('Max Attempts Reached!')
    quit()

###complete login

###rounds
score_us1 = 0
score_us2 = 0
roundnum = 1
while roundnum < 6:
    print('Round {0}!!'.format(roundnum))
    us1_decision = input('User 1! Press 1 to roll 2 dice, Press 2 to quit')
    if us1_decision == '1':
        us1_r1 = randomgen()
        us1_r2 = randomgen()
        print('You rolled {0}, and {1}'.format(us1_r1, us1_r2))

        score_us1 += (us1_r1 + us1_r2)

        if evenorodd(score_us1) == True:
            print('WOW! Youre total is even, heres an extra 10 points')
            score_us1 += 10
        else:
            print('OOPS! Thats an odd total I see... -5 for you')
            score_us1 -= 5

        if us1_r1 == us1_r2:
            print('LUCKY YOU! Thats a double, heres an extra roll.')
            us1_extra1 = randomgen()
            print('You rolled: {0}'.format(us1_extra1))
            print('+{0} to your points!'.format(us1_extra1))
        
        print('Total for User 1 at Round {0}: {1}'.format(roundnum, score_us1 ))


    else: quit()

    us2_decision = input('User 2! Press 1 to roll 2 dice, Press 2 to quit')
    if us2_decision == '1':
        us2_r1 = randomgen()
        us2_r2 = randomgen()
        print('You rolled {0}, and {1}'.format(us2_r1, us2_r2))

        score_us2 += (us2_r1 + us2_r2)

        if evenorodd(score_us2) == True:
            print('WOW! Youre total is even, heres an extra 10 points')
            score_us2 += 10
        else:
            print('OOPS! Thats an odd total I see... -5 for you')
            score_us2 -= 5

        if us2_r1 == us2_r2:
            print('LUCKY YOU! Thats a double, heres an extra roll.')
            us2_extra1 = randomgen()
            print('You rolled: {0}'.format(us2_extra1))
            print('+{0} to your points!'.format(us2_extra1))
        print('Total for User 2 at Round {0}: {1}'.format(roundnum, score_us2 ))
    else: quit()
    roundnum += 1
for x in range(0,5):
    print('.')

print('User 1 scored a total {0} points'.format(score_us1))
print('User 2 scored a total {0} points'.format(score_us2))

##score checker
winner = ''
if score_us1 > score_us2:
    winner = us1_uname
    winningscore = score_us1
elif score_us2 > score_us1:
    winner = us2_uname
    winningscore = score_us2
else:
    print('Oops! Youre scores are equal! Extra Round I say!')
    us1_extra_decision = input('User 1... press 1 to roll, press 2 to forfeit: ')
    if us1_extra_decision == '1':
        us1_extra2 = randomgen()
        print('You rolled a {0}'.format(us1_extra2))
    else:
        print('You give up? WIMP! User 2 WINS!!!')
        winner = us2_uname
        winningscore = score_us2
    us2_extra_decision = input('User 1... press 1 to roll, press 2 to forfeit: ')
    if us2_extra_decision == '1':
        us2_extra2 = randomgen()
        print('You rolled a {0}'.format(us2_extra2))
    else:
        print('You give up? WIMP! User 1 WINS!!!')
        winner = us1_uname
        winningscore = score_us1


print('Drumroll please .')
for x in range(0,5):
    print('.')

print('AND THE WINNER IS: {0}, with {1} points'.format(winner, winningscore))
for x in range(0,5):
    print('.')
##upto all good :)
with open('playersdata.csv', 'a+') as playersdata:
    writer = csv.writer(playersdata)
    reader = csv.reader(playersdata)
    tobeappend = []
    tobeappend.append(winner)
    tobeappend.append(winningscore)
    writer.writerow(tobeappend)
    counter = 0

    try:
        while counter < 5:
            print('Previous WINNERS Wall of Fame:')
            listofvals = list(reader)
            print(listofvals[0])
            counter += 1
    except:
        pass

#####error found in writing and reading... implement awaiting     








