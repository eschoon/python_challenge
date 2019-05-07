#import polling data
import csv
with open ('election_data.txt') as csvfile: 
    reader = csv.DictReader(csvfile)
#assign columns 
    xs = []
    for row in reader:
        x = (row['Candidate'])
        xs.append(x)
    xd = []
    for row in reader:
        d = (row['Voter ID'])
        xd.append(d)
    xt = []
    for row in reader: 
        t = (row['County'])
        xt.append(t)
#calculate total votes, candidate votes and candidate percentage
votes = len(xs)
khan_votes = xs.count("Khan")
khan_percentage = round((khan_votes/votes),5)
correy_votes = xs.count("Correy")
correy_percentage = round((correy_votes/votes),5)
li_votes = xs.count("Li")
li_percentage = round((li_votes/votes),5)
otooley_votes = xs.count("O\'Tooley")
otooley_percentage = round((otooley_votes/votes),5)


#print election results

print("Election Results")
print ("---------------")
print (f"Total Votes: {votes} ")

print('Khan: {:.2%}.'.format(khan_percentage),(f'{khan_votes}'))
print('Li: {:.2%}.'.format(li_percentage), (f'{li_votes}'))
print("Correy: {:.2%}.".format(correy_percentage),(f"{correy_votes}"))
print('O\'Tooley: {:.2%}.'.format(otooley_percentage), (f'{otooley_votes}'))

#Calculate winner of election
if khan_votes > li_votes and correy_votes and otooley_votes:
    print("Winner: Khan")
elif li_votes > khan_votes and correy_votes and otooley_votes:
    print("Winner: Li")
elif correy_votes > khan_votes and li_votes and otooley_votes:
    print("Winner: Correy")
elif otooley_votes > khan_votes and li_votes and otooley_votes:
    print("Winner: O\'Tooley")