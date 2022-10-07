import time
n = int(input("Input positive number for a 'CountDown' or negative number for a 'CountUp' "))

while n>0:
    time.sleep(1)
    n -= 1
    print(n)

while n<0: 
    time.sleep(1)
    n += 1
    print(n)
if (n == 0):
    print("Breakout!")
