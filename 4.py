start = int(input("Моля въведете начална стойност на диапазона: "))
end = int(input("Моля въведете крайна стойност на диапазона: "))
primeList = []

for num in range(start, end+1):
    prime = True
    for i in range(2,num):
        if(num%i==0):
            prime = False
    if prime:
        primeList.append(num)


print(f"Простите числа в диапазона {start} - {end}:", end="")
for i in range(0, len(primeList)):
    print(primeList[i], end=" ")
print()

print(f"Минималното просто число е: {min(primeList)}")
print(f"Максималното просто число е:  {max(primeList)}")
avg = sum(primeList) / len(primeList)
print(f"Средноаритметичното на простите числа е: {avg:.2f}")