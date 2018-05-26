row = 5
i = 1
j = 1
while i <= row:
    j = row-i
    print(" "*j,end="")
    print("*"*(2*i-1))
    i += 1
while row < i < (2*row):
    j = i-row
    print(" "*j,end="")
    print("*"*(2*(2*row-i)-1))
    i += 1