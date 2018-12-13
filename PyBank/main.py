import os
import csv
data = []
with open('C:/Users/damia/Desktop/UDEN201811DATA3/Week3/HW/Instructions/PyBank/Resources/budget_data.csv') as f:
    reader = csv.reader(f)
    next(reader)
    months=0
    total=0
    for row in reader:
        months+=1
        data.append(row)
        total+=int(row[1])
        pairs = []
    for index, val in enumerate(data):
        try:
            pairs.append((val[1], data[index + 1][1],val[0]))
        except IndexError:
            pass

    diffs = []
    combo=[]
    for pair in pairs:
        first, second, third = pair
        diff = int(second) - int(first)
        diffs.append(diff)
        combo.append([third,diff])
    for i in range(len(combo)):
        if combo[i][1]==max(diffs):
            max_month=combo[i+1][0]
        if combo[i][1]==min(diffs):
            min_month=combo[i+1][0]
    print("Financial Analysis")
    print("-------------------------") 
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(sum(diffs) / len(diffs), 2)}")
    print(f"Greatest Increase in Profits: {max_month} (${max(diffs)})")
    print(f"Greatest Decrease in Profits: {min_month} (${min(diffs)})")
