import random 

print "Hello. This is TNB Magazine's Top 5 Best Places to Work List:"

toplist = ['FunCo', 'PositiveCo', 'HonestCo', 'GrindCo', 'TeamCo'] #creates an array called "toplist" containing the top 5 list of companies
count = len(toplist) #determines number of values in the array
print toplist

print "What is your company's name?"
company = raw_input("Company Name: ") #assigns the company name you entered into a variable called "company"

companyids = [] 
for i in range(count): #uses a loop to create an array of numbers from 1 to x; x being the length of the "toplist" array
	companyids.append(i) #each number represents a label positioning for each value in the "toplist" array
random.shuffle(companyids) #the number labels are randomly shuffled in the "companyids" array

for i in range(count): #determines whether values in the "toplist" array contains your company's name in a randomized manner, by using the shuffled label positioning array, "companyids"
	if (toplist[companyids[i]] == company):  
		print "Your company is in the top 5 list!"
		break
	elif (toplist[companyids[i]] != company and i==count-1):
		print "Your company is not in the top 5 list." 
