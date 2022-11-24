""" Skills Demo 1 (Programming)
Author: Alex Vlasa
Date: 23/11/2022
"""
#interger set-up
school = (input("Please Enter Your School's Name. "))
addy1 = (input("Please Enter Your School's Address [Line 1] "))
addy2 = (input("Please Enter Your School's Address [Line 2] "))
addy3 = (input("Please Enter Your School's Address [Line 3] "))
#variable set-up
#while statement to ensure program doesnt crash when inputting characters which are not numbers
while True:
    try:
        student = int(input("How Many Students Are Travelling? "))
    except ValueError:
        #user must try again
        continue
    else:
      break
        #user passed
while True:
    try:
        teacher = int(input("How Many Teachers Are Travelling? "))
        #user must try again
    except ValueError:
        continue
    else:
      break
        #user passed
while True:
    try:
        hotel = int(input("How Many Nights Will You Be Staying? ")) 
        #user must try again
    except ValueError:
        continue
    else:   
        break
        #loop ends
 
#int set-up
flight = 267.67
flightnum = (student+teacher)
flightcost = round(flightnum*flight,2)
 
#flight caluclations
if student>=20:
  num1=int(student/20)
  num2=round(num1,0)
  # ^^^ rounding to 0 decimal places, whole number
  tflight=(teacher-num2)
elif student<20:
  tflight=(teacher-0)
varflight=(tflight+student)
finflight=round(varflight*flight, 2)
discount=(num2*flight)
#finflight is the total money for flights
# ^^^ as to not make space between euro and finflight variable
 
#hotel calculations
num3 = (student*39.50)
var1 = (student%4)
surchargestudent = round(var1*8.40,2)
num4 = (teacher*59.50)
var2 = (teacher%2)
surchargeteacher = round(var2*15.40,2)
finalsurcharge = (surchargestudent+surchargeteacher)
finhotelstu = (num3*hotel)
finhoteltea = (num4*hotel)
subtotal = (finhotelstu+finhoteltea+flightcost)
# ^^^ surcharge calculations
hotelfinalstudent = round(student*39.50,2)
hotelfinalteacher = round(teacher*59.50,2)
sfinalhoteldays = round(hotelfinalstudent*hotel,2)
tfinalhoteldays = round(hotelfinalteacher*hotel,2)
hotelfinal = round(hotelfinalstudent+hotelfinalteacher,2)
# ^^^ final hotel figures
finaltotal=(subtotal+var1+var2-discount)
 
#invoice loop
while True:
    try:
        invoice = int(input("Please Input Your Invoice Number: "))
    except ValueError:
        #user must try again
        continue
    else:
        pad=(f'{invoice:04}')
        # ^^^ padding with 0's 
        #user passed
        break
#loop ends
#invoice visual
#part one (title-tour details)
print("\n\n")
print('{:^90}'.format("REBEL TOURS LTD"))
print('{:>70}'.format("Invoice No:"),("\t   "),("<{}>").format(pad))
print('{:>64}'.format("Date:"),("\t\t\t<Date>"))
print(("\n"),'{:>10}'.format("School Name:"),("\t\t\t<{}>").format(school))
print('{:>9}'.format("Address:"),("\t\t\t\t<{}>").format(addy1))
print('{:>9}'.format("\t"),("\t\t\t<{}>").format(addy2),("\n"),'{:>9}'.format("\t"),("\t\t\t<{}>").format(addy3))
print(("\n"),'{:>10}'.format("No. Of Nights:"),("\t\t<{}>").format(hotel),("\n\n"),('{:>10}'.format("Tour Details:")))
#part two (flights)
print(("\n\n"),'{:8}'.format("Flights:"),('{:>40}'.format("< No. Of People:")),(flightnum),("{}").format(">"),'{:>26}'.format("<€{}>").format(flightcost))
print('{:8}'.format(" Student Accomodation:"),('{:>29}'.format("< No. Of Students:")),(student),("{}").format(">"),'{:>24}'.format("<€{}>").format(finhotelstu))
print('{:8}'.format(" Teacher Accomodation:"),('{:>29}'.format("< No. Of Teachers:")),(teacher),("{}").format(">"),'{:>24}'.format("<€{}>").format(finhoteltea))
print(("\n"),('{:>86}'.format("━━━━━━━━━━━━━━")),("\n"),('{:>61}'.format("Subtotal:")),'{:>18}'.format("<€{}>").format(subtotal))
#part three (surcharge)
print(("\n\n"),'{:8}'.format("Surcharge:"))
print('{:8}'.format(" Student Accomodation:"),('{:>29}'.format("< No. Of Empty Beds:")),(var1),("{}").format(">"),'{:>24}'.format("<€{}>").format(surchargestudent))
print('{:8}'.format(" Teacher Accomodation:"),('{:>29}'.format("< No. Of Empty Beds:")),(var2),("{}").format(">"),'{:>24}'.format("<€{}>").format(surchargeteacher))
#discount
#if else statement determines if a discount section is printed on the statement
if num2<=1:
  print(("\n\n"),'{:8}'.format("Discount:"))
  print('{:8}'.format(" Free Teacher Flights:"),('{:>32}'.format("< No. Of Free Teachers:")),(num2),("{}").format(">"),'{:>22}'.format("<-€{}>").format(discount))
  print(("\n"),('{:>86}'.format("━━━━━━━━━━━━━━")),("\n"))
  print(('{:>63}'.format("Total:")),'{:>18}'.format("<€{}>").format(finaltotal)) #discount is displayed
else:
  print(("\n"),('{:>86}'.format("━━━━━━━━━━━━━━")),("\n"))
  print(('{:>63}'.format("Total:")),'{:>17}'.format("<€{}>").format(finaltotal)) #discount applied
