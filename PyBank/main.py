import csv

csvpath = r"PyBank\Resources\budget_data.csv"


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    counter =0
    profit_losses_total = 0
    net_transition = 0
    greatest_increase_proAmount =0
    greatest_decrease_proAmount=0
    




    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        counter = counter+1
        profit_losses_total += int(row[1])
        current_month = row[0]
        current_profit = int(row[1])
       
        if counter > 1:
            net_transition += current_profit - previous_profit
            profit_differrence = (current_profit - previous_profit)
          
            if greatest_increase_proAmount < profit_differrence : 
                greatest_increase_proAmount = profit_differrence
                greatest_increase_datMon = current_month
            if greatest_decrease_proAmount > profit_differrence : 
                greatest_decrease_proAmount = profit_differrence
                greatest_decrease_datMon = current_month

     
        previous_month = current_month
        previous_profit = current_profit
        

       
    average_change = net_transition/(counter - 1)
    print("The total number of months included in the dataset = " + str(counter))
    print("The net total amount of Profit/Losses over the entire period = $" + str(profit_losses_total))
    print("Average  Change: $" + str(format(average_change,'.2f')))
    print( "Greatest Increase in Profits " + str(greatest_increase_datMon) + " ($" + str(greatest_increase_proAmount) + ")")
    print( "Greatest decrease in Profits " + str(greatest_decrease_datMon) + " ($" + str(greatest_decrease_proAmount) + ")")

output_file = open(r"PyBank\Analysis\budget_data_output.txt",'w')

outputStr = [ "\nFinancial Analysis"
              "\n--------------------------------------------"
             "\nThe total number of months included in the dataset = " + str(counter),
              "\nThe net total amount of Profit/Losses over the entire period = $" + str(profit_losses_total),
             "\nAverage  Change: $" + str(format(average_change,'.2f')),
             "\nGreatest Increase in Profits:  " + str(greatest_increase_datMon) + " ($" + str(greatest_increase_proAmount) + ")",
             "\nGreatest decrease in Profits:  " + str(greatest_decrease_datMon) + " ($" + str(greatest_decrease_proAmount) + ")"  ]

output_file.writelines(outputStr)
output_file.close