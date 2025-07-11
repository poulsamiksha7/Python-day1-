#Q1. Greet the user
print("Hello World")
#Q2. Add two numbers
a=5
b=10
c=a+b
print(c)
#Q3. Simple Calculator
a=5
b=10
c=a+b
print(c)
d=a-b
print(d)
e=a*b
print(e)
f=a/b
print(f)
#Q4. Swap two numbers
a=5
b=10
temp=a
a=b
b=temp
print(a)
print(b)
#Q5. Convert Celsius to Fahreheit
celsius = int(input("Enter the temperature in celsius: "))
fahereheit = (celsius * 9/5) + 32
print(fahereheit)
#Q6 Area of circle
radius = int(input("Enter the number"))
print(3.14*radius**2)
#Q7. Simple Intrest Calculator
principal = int(input("Enter the number"))
rate = int(input("Enter the number"))
time = int(input("Enter time period"))
Simple_intrest=  (principal * rate * time) / 100
print(Simple_intrest)
#Q8. Check odd or even
number = int(input("Enter Number"))
if number%2==0:
    print("The number is even")
else :
   print("The number is odd") 
#Q9. Find Square and Cube
n = int(input("Enter your number"))
square = n**2
cube= n**3
print(square)
print(cube)
#Q10. Accept user name, age, city and print profile
username = input("Enter your name")
age = int(input("Enter yout age"))
city = input("Enter your city")
profile = print(f"Your {username} , {age} and {city}.This is your profile.")