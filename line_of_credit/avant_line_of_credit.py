def total(string):
    newlist = string.split()
    sumtotal = 0.0
    for item in newlist:
        try:
            itemhere = float(item)
            sumtotal+=itemhere
        except:
            continue
    return sumtotal   

def monthlyactivity(interest, principal, apr, limit):
    print "enter day number and transactions on that day, in order. Enter day as 31 to end simulation for this month"
    day = 0
    prevday = 0
    while day<30:
        day = int(input("enter day number: "))
        if day == 31:
            newinterest = (day-prevday) * (apr/365) * principal
            interest+=newinterest
            break
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
                    principal = 0
                if principal>limit:
                    principal = limit
    return [interest, principal]



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
    result = monthlyactivity(interest, principal, apr, limit)
    interest = result[0]
    principal = result[1]
    print principal+interest