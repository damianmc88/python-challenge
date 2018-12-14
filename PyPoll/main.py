import os
import csv
from collections import Counter

with open('C:/Users/damia/Desktop/UDEN201811DATA3/Week3/HW/Instructions/PyPoll/Resources/election_data.csv') as f:
    reader = csv.reader(f)
    next(reader)
    
    candidate = []
    total = 0
    
    for row in reader:
        total += 1
        candidate.append(row[2])
    
    khan_totals = (candidate.count("Khan"))
    correy_totals = (candidate.count("Correy"))
    li_totals = (candidate.count("Li"))
    otooley_totals = (candidate.count("O'Tooley"))
    
    c = Counter(candidate)
    winner = c.most_common(1)[0][0]
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print("-------------------------")
    print(f"Khan: {round((khan_totals / total) * 100, 3)}% ({khan_totals})")
    print(f"Correy: {round((correy_totals / total) * 100, 3)}% ({correy_totals})")
    print(f"Li: {round((li_totals / total) * 100, 3)}% ({li_totals})")
    print(f"O'Tooley: {round((otooley_totals / total) * 100, 3)}% ({otooley_totals})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")