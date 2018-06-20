ans = [1,3,55,18]
while True:
    user_ans = input("enter your number ")
    if user_ans == "q":
        break
    try:
        user_ans = int(user_ans)
    except ValueError:
        print("type a number or q to quiet")
    if user_ans in ans:
        print("Right!")
    else:
        print("Uncorrect\^^/")