def monthlyactivity(interest, principal, apr, limit, totalprin):
    print "enter day number from this month and transactions on that day, in order. Enter day as 31 to end simulation for this month,"
    day = 0
    prevday = 0
    while day<31:
        day = int(input("enter day number: "))
        if day == 31:
            newinterest = (day-prevday) * (apr/365) * principal
            interest+=newinterest
            totalprin=principal
            check = int(input("would you like to end the entire simulation? Enter 1 for 'yes' and 0 for 'no':"))
            if check ==1:
                break
            else:
                #principal = 0.0
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
                newinterest = (day-prevday) * (apr/365) * principal
                interest+=newinterest
                counter = 0 
                transact =0
                activity = 0
                print "enter transactions now. Eg, for deposit of $100, type '-100', and for withdrawal of $100, type '100'. Enter 0 for ending this day's transactions"
                while (counter==0 or transact!=0):
                    counter = 1
                    try:
                        transact = float(input("transaction: "))
                        if transact == 0.0:
                            break
                    except:
                        break
                    else:
                        if principal+transact<0:
                            print "your deposit was too much and $" + str(-1*(principal+transact)) +  " of it has been returned"
                            principal = 0
                        elif principal+transact>limit:
                            print "your withdrawal was too much and $" + str(transact) + " has been declined"
                        else:
                            activity+=transact
                            principal+=transact
                prevday = day
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