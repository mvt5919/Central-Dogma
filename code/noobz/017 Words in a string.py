string = input("Input word to count")


print(*map(string.lower().count, " "))