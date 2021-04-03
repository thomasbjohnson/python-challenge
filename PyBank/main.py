import os
import csv

#creates the csv path
csv_path = os.path.join('Resources', 'budget_data.csv')

#create the list to hold the results
months = []
net_total = []
pl_change = []

# read the csv 
with open(csv_path, newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    #skips the header 
    next(budget_data)
    
    for row in budget_data:
        #add the months
        months.append(row[0])

        #add the net total
        net_total.append(float(row[1])) 

    #loop through Profit/Loss column to find change between months
    for i in range(1,len(net_total)):
        pl_change.append(net_total[i] - net_total[i-1])   
        
        # max_pl_change_date = str(month[pl_change.index(max(pl_change))])
#count the total number of months    
total_months = len(months)
# print(str(total_months))
#calculate the total P&L over the period
total_pl = sum(net_total)
# print(str(total_pl))
#Calculate the changes in P&L over the period, then find the average of changes
ave_change = sum(pl_change)/len(pl_change)
# print(str(ave_change))
#Calculate the greatest increase in profits (date and amount) over the period
    #
max_pl_change = max(pl_change)
date_max = str(months[pl_change.index(max_pl_change)])
#Calculate the greatest decrease in losses (date and amount) over the period
min_pl_change = min(pl_change)
date_min = str(months[pl_change.index(min_pl_change)])


print(f"Python Challenge")
print("Financial Analysis")
print("-------------------------------")
print("Total Months:  " + str(total_months))
print(f"Average Change:  $" + str(ave_change))
