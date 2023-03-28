import csv
filepath = "../Resources/budget_data.csv"

#open file
with open(filepath, 'r') as file:
    csvReader = csv.reader(file)
    months = 0
    net = 0 
    next(csvReader)
    profits = []
    dates = []

#loop through csv and keep count of the values
    for row in csvReader:
         net += int (row[1])
         months += 1
         dates.append(row[0])
         profits.append(int(row[1]))

 #create a list of changes
    change = []
    for i in range (len (profits) - 1):
        change.append(profits[i+1] - profits[i])
        #print (change)
#calculate the greatest increase in profits/losses
    greatest_increment = max(change)
#calculate the greatest decrease in profits/losses
    greatest_decrease = min(change)

    max_date = ""
    min_date = ""

 #find the date for the greatest changes
    for i in range(len(profits) - 1):
        if profits[i+1] - profits[i] == greatest_increment:
            max_date = dates[i +1]
        if profits[i+1] - profits[i] == greatest_decrease:
            min_date = dates[i +1];
    total = 0

 #calculate avg change
    for num in  change:
        total +=num
    avg_chg = total / len(change)
    #print (avg_chg)

#print output 
print("Financial Analysis")
print("-----------------------------")

print("Total Months:", months)
print(f"Total: ${net}")
print(f"Average Change: ${avg_chg: 0.2f}")
print(f"Greatest Increase in profits: {max_date} (${greatest_increment})")
print(f"Greatest Decrease in profits: {min_date} (${greatest_decrease})")

#write to separate file
with open('budget_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------\n")
    output_file.write(f"Total Months: {months}\n")
    output_file.write(f"Total: ${net}\n")
    output_file.write(f"Average Change: ${avg_chg: 0.2f}\n")
    output_file.write(f"Greatest Increase in profits: {max_date} (${greatest_increment})\n")
    output_file.write(f"Greatest Decrease in profits: {min_date} (${greatest_decrease})\n")






    



