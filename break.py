qs =["What is your name?",
     "What is your favorite color?",
     "what is your quest?"]

n = 0
while True:
    print("Type q to quiet")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
    