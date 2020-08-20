# This accomplishes the challenge version of Assignment 2 by asking for user input and storing in tuples -> lists until done, then printing each letter with the inputted names.

nameTupleList = []
nameTypes = ("addressee", "candidate", "sender")
inputStr = ""
exitStr = "done"

# Inputs names from the user until they type "done" when prompted.
letterNum = 1
while(inputStr != exitStr):
    print(f"Letter #{letterNum}\n")
    letterNum += 1

    addressee = input(f"Please enter a {nameTypes[0]} name: ")
    candidate = input(f"Please enter a {nameTypes[1]} name: ")
    sender = input(f"Please enter a {nameTypes[2]} name: ")

    nameTuple = (addressee, candidate, sender)
    nameTupleList.append(nameTuple)

    inputStr = input(f"Enter '{exitStr}' to exit and print, or anything else to continue: ")
    print("\n")

# Outputs letters in the specified format
for tup in nameTupleList:
    print("\nDear %s,\nI would like you to vote for %s\nbecause I think %s is best for\nthis country.\nSincerely,\n%s\n\n" % (tup[0], tup[1], tup[1], tup[2]))

""" A RECORDING OF THE RUN
Letter #1

Please enter a addressee name: Addressee 1
Please enter a candidate name: Candidate 1
Please enter a sender name: Sender 1
Enter 'done' to exit and print, or anything else to continue: q


Letter #2

Please enter a addressee name: Addressee 2
Please enter a candidate name: Candidate 2
Please enter a sender name: Sender 2
Enter 'done' to exit and print, or anything else to continue: q


Letter #3

Please enter a addressee name: Addressee 3
Please enter a candidate name: Candidate 3
Please enter a sender name: Sender 3
Enter 'done' to exit and print, or anything else to continue: q


Letter #4

Please enter a addressee name: Addressee 4
Please enter a candidate name: Candidate 4
Please enter a sender name: Sender 4
Enter 'done' to exit and print, or anything else to continue: done



Dear Addressee 1,
I would like you to vote for Candidate 1
because I think Candidate 1 is best for
this country.
Sincerely, 
Sender 1



Dear Addressee 2,
I would like you to vote for Candidate 2
because I think Candidate 2 is best for
this country.
Sincerely,
Sender 2



Dear Addressee 3,
I would like you to vote for Candidate 3
because I think Candidate 3 is best for
this country.
Sincerely,
Sender 3



Dear Addressee 4,
I would like you to vote for Candidate 4
because I think Candidate 4 is best for
this country.
Sincerely,
Sender 4


"""