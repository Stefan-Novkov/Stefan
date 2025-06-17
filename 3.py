num_of_rows = int(input("Enter rolls(positive number): "))
while num_of_rows < 1:
    num_of_rows= int(input("Enter a valid number of rolls:"))

symbol = str(input("Enter a symbol:"))
for i in range (num_of_rows,0, -1):
    print(" ".join([symbol] * i))

print()
print(f"{symbol} "* num_of_rows)
for i in range(num_of_rows -1, 0, -1):
    if(i==1):
        print(f"{symbol} ")
        break

    print(symbol, end="")

    for i in range(i-2,0,-1):
        print(f"  ", end="")

    print(' ',  end="")
    print(symbol)





