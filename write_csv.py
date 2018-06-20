import csv

data = [["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]]

with open("./data.csv", "w", newline='') as f:
    w = csv.writer(f,delimiter=",")
    #for i in range(3):
        #w.writerow(data[i])
    for content in data:
        w.writerow(content)