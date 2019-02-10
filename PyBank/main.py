import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

CumulativeTotal=0
SumTotal=0
SumChanges=0
PLChange=0
PriorPeriodProfit=0
RowCounter=0
NumberOfChanges = RowCounter - 1

TotalMonths = []
CumulativePL = []
PLChanges = []



with open(csvpath,newline='',encoding='UTF-8') as budget_data:

    csvreader = csv.reader(budget_data,delimiter=",")
    header = next(csvreader)
    #Create lists out of dataset.  This will make it easier to count number of months, and to 
    #calculate changes.
    for row in csvreader:
        TotalMonths.append(row[0])
        CumulativePL.append(int(row[1]))
        
    #Calculate the changes in PL from the gross PL amounts and store in a new list:
    for i in range(len(CumulativePL)-1):
        PLChanges.append(CumulativePL[i+1]-CumulativePL[i])

    #Calculate max and min changes
    MaxIncrease = max(PLChanges)
    MaxDecrease = min(PLChanges)

    #Get Index for Max and Min so can use it to pick out the month.  Need to add one because changes list is shorter.
    MaxIncreaseInd = PLChanges.index(max(PLChanges))
    MinIncreaseInd = PLChanges.index(min(PLChanges))

    #Get the actual months of the Max and Min

    MaxIncreaseMonth = TotalMonths[MaxIncreaseInd]
    MaxDecreaseMonth = TotalMonths[MinIncreaseInd]

    #Calculate the Average Change
    AverageChange= round(sum(PLChanges)/len(PLChanges),2)

    print()
    print("Financial Analysis")
    print("--------------------------")
    print()
    print(f'Total Months: {len(TotalMonths)}')
    print(f'Total Profit (or Loss): ${sum(CumulativePL)}')
    print(f"Average Change: {AverageChange}")
    print(f'Greatest Increase in Profits: {MaxIncreaseMonth} (${(str(MaxIncrease))})')
    print(f'Greatest Decrease in Profits: {MaxDecreaseMonth} (${(str(MaxDecrease))})')
    






