def factorial_without_recursion(number):
    temp = 1
    while(number > 0):
        temp = temp * number
        number = number - 1
    print('Factorial of', number,'is: ')
    print(temp)

if __name__ == '__main__':
    userInput = int(input('Enter the number to find its factorial: '))
    print('Factorial of', userInput, 'is:', factorial(userInput))
    factorial_without_recursion(userInput)
