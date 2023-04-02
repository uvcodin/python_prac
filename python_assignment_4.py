#RECURSION

def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


#LAMBDA FUNCTION

greet_user = lambda name : print('Hey there,', name)

greet_user('Yuvi')          #prints "Yuvi"

#Reading Mode

f = open("test_file.txt","r")
data=f.read()
print(data)
hello there

#Writting Mode

file = open("test_file.txt","w")
data=file.write("hello again")
file.close()

#Append Mode
# Open the file in append mode
with open('test_file.txt', 'a') as file:
    file.write('\nbye')
