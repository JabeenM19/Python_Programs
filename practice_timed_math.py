import random
import time

min_operands= 2
max_operands = 10
operators = ['+','-','*']
total_problems = 10


def generate_problem():
    left_operand = random.randint(min_operands,max_operands)
    right_operand = random.randint(min_operands,max_operands)
    operator = random.choice(operators) 
    expr = str(left_operand) + str(operator)+ str(right_operand)
    ans =  eval(expr)
    return expr,ans
generate_problem()

input("Press enter to start")
start_time = time.time()
correct = 0
wrong = 0
for i in range(total_problems):
    expr,ans = generate_problem()
    while True:
        guess = input("Problem"+" " +str(i+1)+" "+"."+" "+expr+" "+"="+" ")
        if guess== str(ans):
            correct += 1
            break
        if guess != str(ans):
            wrong +=1
            print("Incorrect")
            break
end_time = time.time()
total_time = round((end_time-start_time),2)
print("Test completed in ", total_time, "seconds","and your score is",correct,"out of 10")