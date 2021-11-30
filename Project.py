#Charity Fun Run

def main():
    
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    gender = input('Enter your gender(male or female): ')
    distanceRan = float(input('How far did you run?(miles): '))
    minutes = int(input('How long did you run for?(minutes): '))
    seconds = int(input('How long did you run for?(seconds): '))
    answer = "yes"
    gearList = ''
    
    while (answer == "yes"):
        gearList += input('Enter an item of gear you used: ') + ', '
        answer = input('Do you have another item of gear to enter?(yes or no): ')
    
    reachedCheckpoints = checkpointsReached(distanceRan)
    moneyRaised = reachedCheckpoints * amountPerKm(gender)
    categoryAssignment = category(distanceRan)
    pacePerMile = pace(minutes, seconds, distanceRan)
    output(firstName, lastName, gender, distanceRan, minutes, seconds, gearList, moneyRaised, reachedCheckpoints, categoryAssignment, pacePerMile)

def checkpointsReached(distanceRan):
    CHECKPOINT_DISTANCE = 1.5
    return distanceRan // CHECKPOINT_DISTANCE

def amountPerKm(gender):
    if (gender == "male") :
        return 5
    else:
        return 10

def category(distanceRan):
    if (distanceRan >= 10):
        return "Elite"
    if (distanceRan < 10):
        return "Fun"
    
def pace(minutes, seconds, distanceRan):
    k = 1
    totalSec = 0
    for k in range(minutes):
        totalSec += 60
    totalSec += seconds
    minPerMile = (totalSec/60) // distanceRan
    secPerMile = (totalSec - (minPerMile*60*distanceRan)) // distanceRan
    return str(minPerMile) + " min " + str(secPerMile) + " sec" 
    
            
def output(firstName, lastName, gender, distanceRan, minutes, seconds, gearList, moneyRaised, reachedCheckpoints, categoryAssignment, pacePerMile):
    print()
    print("Name: ", firstName, ' ', lastName)
    print("Gender: ", gender)
    print("Distance Ran: ", distanceRan, " miles")
    print("Time Ran: ", minutes, " minutes and ", seconds, "seconds")
    print("Pace per mile: ", pacePerMile)
    print("Gear List: ", gearList)
    print("Category: ", categoryAssignment) 
    print('You raised: ', moneyRaised, '$', 'for charity', 'by reaching ', reachedCheckpoints, ' checkpoints.' )
        
main()
    
