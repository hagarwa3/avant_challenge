def total(string):          # this method is just to convert our input of a list of transactions into a sum
    newlist = string.split()
    sumtotal = 0.0
    for item in newlist:
        try:
            itemhere = float(item)
            sumtotal+=itemhere
        except:
            continue
    return sumtotal   

def monthlyactivity(interest, principal, apr, limit, totalprin):
    print "enter day number from this month and transactions on that day, in order. Enter day as 31 to end simulation for this month,"
    day = 0
    prevday = 0
    while day<31:
        day = int(input("enter day number: "))
        if day == 31:
            newinterest = (day-prevday) * (apr/365) * principal
            interest+=newinterest
            totalprin+=principal
            check = int(input("would you like to end the entire simulation? Enter 1 for 'yes' and 0 for 'no':"))
            if check ==1:
                break
            else:
                principal = 0.0
                day = 0
                prevday = 0
                print "at the end of this month, total pending = $" + str(totalprin+interest)
                continue
                
        else:
            if(day>31) or (day<=prevday):
                day = prevday
                print "your day was either before the previous day or more than 31. Retry entering the day"
                continue
            else:
                withdrawals = raw_input("enter all withdrawals separated by spaces, no dollar signs: ")
                withdrawals = total(withdrawals)
                deposits = raw_input("enter all deposits separated by spaces, no dollar signs: ")
                deposits = total(deposits)
                activity = withdrawals - deposits
                newinterest = (day-prevday) * (apr/365) * principal
                interest+=newinterest
                prevday = day
                principal = principal + activity
                if principal<0:
                    print "your deposit was too much and $" + str(-1*activity) +  " of it has been returned"
                    principal = 0
                if principal>limit:
                    print "your withdrawal was too much and $" + str(activity-limit) + " of it has been declined"
                    principal = limit
    return [interest, principal, totalprin]



def main():
    try:    
        apr = float(input("Enter apr: " ))
    except:
        apr = 0.25
    try:    
        limit = float(input("enter credit limit: "))
    except:
        limit = 1000.0
    principal = 0.0
    interest = 0.0
    totalprin = 0.0
    result = monthlyactivity(interest, principal, apr, limit, totalprin)
    interest = result[0]
    principal = result[1]
    totalprin = result[2]
    print "at the end of your entire credit history for this account, total payable = $" + str(totalprin+interest)
    
main()