string = input("Input word to vowel count")


print(*map(string.lower().count, "aeiou"))