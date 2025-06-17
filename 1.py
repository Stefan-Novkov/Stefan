num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print("Числото е кратно на 3 и на 5")
elif num % 5 == 0:
    print("Числото е кратно на 5")
elif num % 3 == 0 :
    print("Числото е кратно на 3")
else :
    print("Числото не е кратно нито на 3, нито на 5.")


