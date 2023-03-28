import csv
filepath = "../Resources/election_data.csv"

#open file
with open (filepath, 'r') as file:
 csvReader = csv.reader(file)
    #print(csvReader)
 votes = 0

#create an empty candidates list for count
 candidates = []

#create and empty candidate votes dict
 cand_votes = {}
 next(csvReader)

#loop through the csv
 for row in csvReader:
    candidate = row[2]

#add candidate to the list if they are not already there
    if candidate not in candidates:
        candidates.append(candidate)
        #print(candidates)

#add candidate as the key and #of occurances as the value
    cand_votes[candidate] = cand_votes.get(candidate, 0) + 1
    votes += 1

#loop through candidates to output on file
    with open('election_analysis.txt', 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Total Votes: {votes}\n")
        output_file.write("---------------------------\n")

    #calculate the percentage for ea candidate and write to the file
        for key, value in cand_votes.items():
            perc = (value / votes) * 100
            output_file.write(f"{key}: {perc:0.3f}% ({value})\n")
            
        output_file.write("-----------------------------\n")
    
    #get the max vote by checking what candidate has the most votes and write to the file
        max_vote = max(cand_votes.values())
        for key, value in cand_votes.items():
         if value == max_vote:
            output_file.write(f"Winner:{key}")
            break
        output_file.write("------------------------------\n")

    #print results

    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {votes}")
    print("----------------------------")

#calculate the percentage for ea candidate
    for key, value in cand_votes.items():
        perc = (value / votes) * 100
        print(f"{key}: {perc:0.3f}% ({value})")
    print("--------------------------------")

#get the max vote by checking what candidate has the most votes
    max_vote = max(cand_votes.values())
    for key, value in cand_votes.items():
     if value == max_vote:
        print(f"Winner:{key}")
        break
     
    print("----------------------------")





