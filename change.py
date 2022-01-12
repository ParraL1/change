#Author: Lilliana Parra
# Github user: ParraL1
# Date: 01/11/2022
# Description: Program asks user for a number of cents from 0 to 99 and outputs number of coins
print("Please enter an amount in cents less than a dollar.")
num_1= float(input())
print("Your change will be:")
print("Q:",round(num_1 // 25))
num_1=num_1%25
print("D:",round(num_1 // 10))
num_1=num_1%10
print("N:",round(num_1 // 5))
num_1=num_1%5
print("P:",round(num_1 // 1))