num = int(input("N:"))
 
while num < 1:
    num(int(input("Enter positive number")))

sum =  0
fact = 0

for i in range(1, num + 1):
    if (i % 2 == 1): 
        sum += i
    if (i % 2 == 0):
        if (i == 2):
            fact = 1
        fact *= i

print(f"Сумата е: {sum}, произведението е: {fact}")


