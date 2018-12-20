import google
for url in google.search("red sox", num=5, stop=1):
    print(url)