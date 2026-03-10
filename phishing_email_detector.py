# FILE NAME - phishing_email_detector.py

# NAME: Amy Nuessle
# DATE: March 3, 2026
# BRIEF DESCRIPTION: Write a program that analyzes an email subject line to detect phishing attempts



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
user_input = input("Enter the email subject line: ")
print()
print("SECURITY ASSESSMENT:")

# check each phishing indicator and track if any were found - sought help from builder
found = False

if "urgent" in user_input.lower():
    print("HIGH RISK: Possible phishing attempt.")
    found = True

if "immediate action required" in user_input.lower():
    print("HIGH RISK: Possible phishing attempt.")
    found = True

if "win" in user_input.lower():
    print("MEDIUM RISK: Suspicious offer detected.")
    found = True

if "free" in user_input.lower():
    print("MEDIUM RISK: Suspicious offer detected.")
    found = True

if "password reset" in user_input.lower():
    print("LOW RISK: Verify legitimacy with sender.")
    found = True

# if no indicators were triggered, let the user know - sought help from builder
if not found:
    print("No phishing indicators detected.")


print("------------------------")
print(f"Analyzed subject: \"{user_input}\"")
#this was my only struggle, getting the user input to print properly



########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the email subject line: Meeting on Friday

SECURITY ASSESSMENT:
No phishing indicators detected.
------------------------
Analyzed subject: "Meeting on Friday"
'''

'''
Enter the email subject line: URGENT REQUEST FOR BANK TRANSFER

SECURITY ASSESSMENT:
HIGH RISK: Possible phishing attempt.
------------------------
Analyzed subject: "URGENT REQUEST FOR BANK TRANSFER"
'''

'''
Enter the email subject line: All I do is win win win no matter what

SECURITY ASSESSMENT:
MEDIUM RISK: Suspicious offer detected.
------------------------
Analyzed subject: "All I do is win win win no matter what"
'''

'''
Enter the email subject line: Did you request a password reset?

SECURITY ASSESSMENT:
LOW RISK: Verify legitimacy with sender.
------------------------
Analyzed subject: "Did you request a password reset?"
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Was using `in` difficult or was it natural? it was natural! once I played with the pylance suggesttions, I got it!







'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[X] I wrote the initial draft of the software but had AI help me make it better. 
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.
#only needed help with the final print statement making progress!!


It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[X] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
