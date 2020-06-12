#These are some basic functions I wrote to practice implementing recursion.

history = []

def solve(input, history):
    if(history.count(input) == 2):
        print(history)
        print("This is not a happy number. " + str(input) + "repeated itself.")
        return False

    if(input == 1):
        print(history)
        print("This is a happy number.")
        return True
    else:
        newVar = 0
        a = [int(i) for i in str(input)]
        
        for i in a:
            newVar += i ** 2
            
        history.append(newVar)
        solve(newVar, history)


def reverseString(input, answer):
    if(len(input) == 0):
        print(answer)
    else:
        answer = answer + input[-1]
        input = input[:-1]
        reverseString(input, answer)

reverseString("hello", "")
        
