num1 = 42 #variable declaration > integers, no need to declare using var , = is sufficent
num2 = 2.3 #variable declaration > float
boolean = True #data types >  boolean
string = 'Hello World' #data types >  string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#objects
fruit = ('blueberry', 'strawberry', 'banana')#not sure 
print(type(fruit))#function call? ah this prints the type of data of fruit in this case a tuple
print(pizza_toppings[1])#console log index array
pizza_toppings.append('Mushrooms')#will use append method to add mushrooms string
print(person['name'])#will go to the object and print the value under the key 'name'
person['name'] = 'George'#updates the value of the name in person object
person['eye_color'] = 'blue'#updates the value of the eyecolor in the person obect 
print(fruit[2]) #console logs the value of index 2 in the fruit array? Not sure about the () vs [] yet, okay its the tuple class.

if num1 > 45: #conditional statement if/else, doesnt use {} like javascript replaced with :also no ()
    print("It's greater")#console log string in the () if condition is met
else:
    print("It's lower")

if len(string) < 5: #conditional statement with if/ else if / else, len may be like the .length method
    print("It's a short word!")#console log the string in the () if condition is met
elif len(string) > 15: # checks the amount of characters in the variable labeled string
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop  since range is one number maybe if x is  0-5 will print x
    print(x)
for x in range(2,5): #for loop will go from 2-5 range, like var i = 0; i < 3; i++ will run 3 loops
    print(x)
for x in range(2,10,3): #not sure what this range is with three numbers .. hmm. ok, starts at 2 adds 3 each loop until breaks the condition < 10
    print(x)
x = 0
while(x < 5):#while loop
    print(x)
    x += 1 #for while loop must indicate the increment . seems like for loops default to increment ++

pizza_toppings.pop() #remove method at end of an array
pizza_toppings.pop(1) #wow, mauybe can remove an value at a selected index , in this case index 1

print(person)#will print the person object to the console
person.pop('eye_color')#will use the .pop method to remove 'eye_color' from the object
print(person)#will print the updated object

for topping in pizza_toppings:#conditional for loop
    if topping == 'Pepperoni':
        continue  #continue onto next lines?
    print('After 1st if statement')
    if topping == 'Olives':
        break  #stops for loop if topping == 'olives' is met

def print_hello_ten_times():#def must be to "def-ine" a function
    for num in range(10):
        print('Hello')

print_hello_ten_times()#function call 

def print_hello_x_times(x):#function with parameter
    for num in range(x):
        print('Hello')

print_hello_x_times(4)#passes in an argument value of 4 into the print_hello_x_times function

def print_hello_x_or_ten_times(x = 10): #unsure about this one (x=10)?
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) #this wont run until the num3 variable is defined.
# num3 = 72
# fruit[0] = 'cranberry' #tuples are immutable
# print(person['favorite_team']) #favorite_team is not in the person object
# print(pizza_toppings[7]) #there is no index 7 of the pizza_toppings array
# print(boolean) #not sure about this one 
# fruit.append('raspberry') #cannot add to the fruit tuple
# fruit.pop(1) #cannot delete from tuple