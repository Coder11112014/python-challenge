import csv

csvpath = r"PyPoll\Resources\election_data.csv"


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   
    csv_header = next(csvreader)

    votes_count = 0
    Candidate_list =[]
    winner_amount = 0
    winner_name = ""

    percentage_votes = 0
  

    # Read each row of data after the header
    for row in csvreader:
        votes_count += 1
        Candidate_list.append(row[2])


    Candidates_name_unique = list(set(Candidate_list))
    Candidates_dict = {}
    for item in Candidates_name_unique:
        Candidates_dict[item] = Candidate_list.count(item)

    output_file = open(r"PyPoll\Analysis\Voters_data_output.txt",'w')
    
    outputStr = ["Election Results",
                "\n--------------------------------------------",
                "\nTotal Votes: " + str(votes_count),
                "\n--------------------------------------------"
                ]

    for candidate in Candidates_dict:
        myvote = Candidates_dict[candidate]
        percentage_votes = (myvote/votes_count)*100
        
        if percentage_votes > winner_amount:
            winner_amount = percentage_votes
            winner_name = candidate

        outputStr.append(f"\n{candidate}:  {str(round(percentage_votes, 3))}% ({myvote})")
        print(f"\n{candidate}:  {str(round(percentage_votes, 3))}% ({myvote})")

    outputStr.append("\n--------------------------------------------")
    outputStr.append("\nWinner: " + winner_name)
    outputStr.append("\n--------------------------------------------")
    output_file.writelines(outputStr)
    output_file.close

print(outputStr)
# print(Candidate_list)
# print(Candidates_name_unique)
# print(Candidates_dict)
