#import file
import csv
#open budget data file
with open('budget_data.txt') as csvfile:
 reader  = csv.DictReader(csvfile)
 #assign xs as profit/loss column
 xs = []
 for row in reader:
     x = int(row['Profit/Losses'])
     xs.append(x)
#calculate financials
x_avg = sum(xs) / len (xs)
x_sum = sum(xs)
x_len = len(xs)
x_max = max(xs)
x_min = min(xs)

#print financial analysis
print ("Financial Analysis")
print("---------------------")
print (f"Number of Months:{x_len} ")


print  ('Total: $' + format(x_sum, ',.2f'))
print(('Average Change: $' + format(x_avg, ',.2f')))
print ('Highest Amount: $' + format(x_max, ',.2f'))
print ('Lowest Amount: $' + format(x_min, ',.2f'))



    
   
    
  