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

