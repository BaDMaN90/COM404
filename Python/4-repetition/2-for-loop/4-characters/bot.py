print("What strange markings do you see?")
symbols = input()
print("Identifying...")

for x in range(0, len(symbols), 1):
    print("index ", x+1,":",symbols[x])
print("Done!")