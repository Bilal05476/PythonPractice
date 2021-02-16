PTI = 0
PMLN = 0
PPP = 0
print("Welcome to E Voting System of Islamic Republic Of Pakistan\n")
fileData = open("cnic.txt", "r")
NadraData = fileData.read().split(sep=" ")
##print(NadraData)
cnic = input("Enter Your Valid CNIC Number without dashes(-) = ")

if cnic in NadraData:
    vote = int(input("\nFor PTI Type 1\nFor PPP Type 2\nFor PMLN Type 3\nEnter Your Vote: "))
    if vote == 1:
        PTI += 1
    elif vote == 2:
        PPP += 1
    elif vote == 3:
        PMLN += 1
    else:
        print("You are Selecting Wrong Voting Number")
        exit()
elif cnic not in NadraData:
    print("You are not eligible for voting or you are under age or may be you insert invalid CNIC Number :(")
    exit()

print("Thank you for Voting :)\n" + "PTI Votes: " + str(PTI) + "\nPPP Votes: " + str(PPP) + "\nPMLN Votes: " + str(PMLN) )
# NadraData = open("demofile.txt", "r")
# print(NadraData.read())