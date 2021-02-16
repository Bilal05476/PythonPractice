import sqlite3

conn = sqlite3.connect('votesdb.sqlite')
cur = conn.cursor()

# cur.executescript(
# '''
# DROP TABLE IF EXISTS Votes;
# DROP TABLE IF EXISTS VOTES;

# CREATE TABLE Votes (Party TEXT, Vote INTEGER);
# CREATE TABLE CNIC (Cnic TEXT)''')


PTI = 0
PMLN = 0
PPP = 0
print("Welcome to E Voting System of Islamic Republic Of Pakistan\n")

cnicData = open("cnic.txt", "r")
CnicData = cnicData.read().split(sep=" ")
# print(NadraData)

partyData = open("party.txt", "r")
PartyData = partyData.read().split(sep=" ")
# print(PartyData)

votedData = open("voted.txt", "r")
VotedData = votedData.read().split(sep=" ")
# print(VotedData)

cnic = input("Enter Your Valid CNIC Number without dashes(-) = ")

##Check if cnic not in database e.g voted.txt
if cnic not in VotedData:
    #Check if cnic in the NadraData e.g cnic.txt     
    if cnic in CnicData:
        votedData = open("voted.txt", 'a')
        votedData.write(cnic + " ")
        VotedData.append(cnic)
        vote = int(input("\nFor PTI Type 1\nFor PPP Type 2\nFor PMLN Type 3\nEnter Your Vote: "))
        if vote == 1:
            PTI += 1
            elect = "PTI"
        elif vote == 2:
            PPP += 1
            elect = "PPP"
        elif vote == 3:
            PMLN += 1
            elect = "PMLN"
        else:
            print("You Entered Wrong Voting Number")
            exit()
    #Apply if cnic not in database e.g cnic.txt      
    elif cnic not in CnicData:
        print("You are not eligible for voting or you are under age or may be you insert invalid CNIC Number :(")
        exit()
    
#Apply if cnic already in database e.g Voted.txt
else:
    print("You already Voted")
    exit()

#Apply If Voting Successful
print("\nThank You For Voting")


##Insert Party name in Data base

for item in PartyData:
    party = item

    cur.execute('SELECT Vote FROM Votes WHERE Party = ? ', (party,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Votes (Party, Vote)
                VALUES (?, 0)''', (party,))
    else:
        cur.execute('UPDATE Votes SET Vote = Vote + 1 WHERE Party = ?', (elect,))
        conn.commit()

#Update Database

# cur.execute('UPDATE Votes SET Vote = Vote + 1 WHERE Party = ?', (vote,))
# conn.commit()

#Insert CNIC in Data base    
for item in VotedData:
    voter = item

cur.execute('SELECT Cnic FROM CNIC WHERE Cnic = ? ', (voter,))
row = cur.fetchone()
if row is None:
    cur.execute('''INSERT INTO CNIC (Cnic) VALUES (?)''', (voter,))
else:
    cur.execute('UPDATE CNIC SET Cnic = ? ', (voter,))

conn.commit()

cur.close()