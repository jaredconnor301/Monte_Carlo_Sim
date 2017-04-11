import random
import matplotlib
import matplotlib.pyplot as plt
import time

lower_bust = 31.325
higher_profit = 63.208

sample_size = 100
starting_funds = 10000
wager_size = 100
wager_count = 10000

# Creating the Dice function - used to create a random integer between 1-100
def dice_roll():
    roll = random.randint(1, 100)

    if roll == 100:
        return False

    elif roll <= 50:
        return False

    elif 100 > roll > 50:
        return True

#Creating the simple bettor function - used to model a bettor that just bets a fixed amount
#Visualizing bettors - using MatplotLib to understand the trajectory of some bettors
def simple_bettor(funds, initial_wager, wager_count,color):
    value = funds
    wager = initial_wager
    '''
    global simple_busts
    global simple_profits
    '''

    wX = []
    vY = []

    current_wager = 1

    while current_wager <= wager_count:
        if dice_roll():
            value += wager
            wX.append(current_wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(current_wager)
            vY.append(value)

        current_wager += 1

    if value <= 0:
        value = "Broke"
        simple_busts += 1

    #print("Funds: " + str(value))
    plt.plot(wX,vY,color)


    #Profit Tracking
    if value > funds:
        simple_profits += 1

    plt.plot(wX,vY,color)
    plt.axhline(0, color="r")
    plt.ylabel("Account Value")
    plt.xlabel("Wager Count")

'''
x = 0

while x < 100:
    simple_bettor(starting_funds,wager_size,wager_count, 'c')
    x += 1

plt.show()
'''

#Creating the simple bettor function - used to model a bettor that just bets a fixed amount
#Visualizing bettors - using MatplotLib to understand the trajectory of some bettors
def double_bettor(funds, initial_wager, wager_count, color):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    current_wager = 1

    global double_busts
    global double_profits


    previous_wager_result = 'win'
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager_result == 'win':
            #print("We wont the last wager, great")

            if dice_roll():
                value += int(wager)
                #print(value)
                wX.append(current_wager)
                vY.append(value)

            else:
                value -= int(wager)
                previous_wager_result = 'loss'
                #print(value)
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)


                if value <= 0:
                    #print("We went broke after" + str(current_wager) + "best")
                    double_busts += 1
                    break


        elif previous_wager_result == 'loss':
            #print("We lost the last one so we will be smart and double!")

            if dice_roll():
                wager = previous_wager_amount * 2

                #Preventing Debt issue
                if (value - wager) < 0:
                    wager = value

                #print("we won" + wager)
                value += int(wager)

                #print(value)
                wager = initial_wager
                previous_wager_result = "win"
                wX.append(current_wager)
                vY.append(value)

            else:
                wager = previous_wager_amount * 2

                #Preventing Debt issue
                if (value - wager) < 0:
                    wager = value

                #print("We lost" + wager)
                value -= int(wager)

                if value <= 0:
                    #print("We went broke after" + str(current_wager) + "bets")
                    double_busts += 1
                    break

                #print(value)
                previous_wager_result = "loss"
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

        current_wager += 1

    #print("Funds: " + str(value))
    plt.plot(wX,vY,color)

    '''
    #Profit Tracking
    if value > funds:
        double_profits += 1
    '''

'''
x = 0

while x < 100:
    double_bettor(10000, 1000, 100, 'r')
    x += 1

plt.show()
'''


def multiple_bettor(funds, initial_wager, wager_count):
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    current_wager = 1
    previous_wager_result = 'win'

    while current_wager <= wager_count:
        if previous_wager_result == 'win':
            #print("We wont the last wager, great")

            if dice_roll():
                value += int(wager)
                #print(value)
                wX.append(current_wager)
                vY.append(value)

            else:
                value -= int(wager)
                previous_wager_result = 'loss'
                #print(value)
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

                if value <= 0:
                    #print("We went broke after" + str(current_wager) + "best")
                    multiple_busts += 1
                    break

        elif previous_wager_result == 'loss':
            #print("We lost the last one so we will be smart and double!")

            if dice_roll():
                wager = previous_wager_amount * random_multiple

                #Preventing Debt issue
                if (value - wager) < 0:
                    wager = value

                #print("we won" + wager)
                value += int(wager)

                #print(value)
                wager = initial_wager
                previous_wager_result = "win"
                wX.append(current_wager)
                vY.append(value)

            else:
                wager = previous_wager_amount * random_multiple

                #Preventing Debt issue
                if (value - wager) < 0:
                    wager = value

                #print("We lost" + wager)
                value -= int(wager)

                if value <= 0:
                    #print("We went broke after" + str(current_wager) + "bets")
                    multiple_busts += 1
                    break

                #print(value)
                previous_wager_result = "loss"
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

        current_wager += 1

    #print("Funds: " + str(value))
    #plt.plot(wX,vY,color)

    #Profit Tracking
    if value > funds:
        multiple_profits += 1


x = 0

#simple_busts = 0.0
#double_busts = 0.0
#simple_profits = 0.0
#double_profits = 0.0


while True:
    multiple_busts = 0.0
    multiple_profits = 0.0

    multiple_sample_size = 100000
    current_sample = 1

    random_multiple = random.uniform(0.1, 10.0)

    while current_sample <= multiple_sample_size:
        multiple_bettor(starting_funds, wager_size, wager_count)
        current_sample += 1

    if ((multiple_busts/multiple_sample_size) * 100.00 < lower_bust) and ((multiple_profits/multiple_sample_size)*100.00 < higher_profit):
        print("###############################")
        print("We found the winner! It was: " + str(random_multiple))
        print("Lower bust to beat: " + str(lower_bust))
        print("Higher profit to beat: " + str(higher_profit))
        print("Lower bust rate to beat: " + str((multiple_busts/sample_size)*100.00))
        print("Higher Profit rate to beat: " + str((multiple_profits/sample_size)*100.00))
        print("###############################")

    else:
        print("Passing")
        pass

#print("Death Rate: " + str(broke_count/float(x) * 100)
#print("Survival Rate: " + str(100 - ((broke_count/float(x))*100)))


plt.axhline(0, color="r")
plt.ylabel("Account Value")
plt.xlabel("Wager Count")
#plt.show()
