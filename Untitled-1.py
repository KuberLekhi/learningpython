import time 
name = input ("what is your name ?\n")
if name.lower() == 'kuber':
   print("You are not welcome here, Goodbye!")
   exit()
menu = "\n-tea\n-coffee\n-juice\n-milk"
print ("Hello " + name + ", I hope you're doing good. What would you like to have from our menu?" + menu )
order = input()
print ("Great choice " + name + ", How many " + order + "'s would you like?") 
quantity = int(input())
print ("Okay " + name + ", Your order will arrive shortly")
if order == 'tea' : 
   price = 50
elif order == 'milk': 
   price = 70 
elif order == 'juice': 
   price = 90
elif order == 'coffee':
   price = 100
else :
   price = 200
time.sleep(3)
print("How was your " + order + " " + name + "?" )
response = input()
bill = price*quantity
print("I'm glad you found your " + order + " " + response + "\nYour total will be " + str(bill) + "rs" )
