desiredResponse1=4
desiredResponse2=5
desiredResponse3=1
desiredResponse4=4
desiredResponse5=3
questionWeight1=4
questionWeight2=6
questionWeight3=3
questionWeight4=5
questionWeight5=2
def validate(response):
    while not response.isdigit():
        print("The input \""+response+"\" is not a number from 1 to 5. Please enter a number from 1 to 5.")
        print("")
        response=input("Do you agree or disagree? Enter your response number here: ")
        print("")
    while int(response)<1 or int(response)>5:
        print("The input \""+response+"\" is not a number from 1 to 5. Please enter a number from 1 to 5.")
        print("")
        response=input("Do you agree or disagree? Enter your response number here: ")
        print("")
    else:
        print("Response Recorded.")
        print("")
        return response
print("")
print("--------------------------------------------------------------------------------")
print("Welcome to Spencer's MatchMaker!")
print("--------------------------------------------------------------------------------")
print("")
print("Answer the following questions with a number ranging from 1 to 5. 5 represents \nstrongly agree and 1 represents strongly disagree. This will determine wether \nor not we would make a good pair or not.")
print("")
print("--------------------------------------------------------------------------------")
print("")
print("Question 1: ")
print("")
print("Cats are great pets.")
print("")
userResponse1=input("Do you agree or disagree? Enter your response number here: ")
print("")
userResponse1=validate(userResponse1)
print("--------------------------------------------------------------------------------")
print("")
print("Question 2: ")
print("")
print("Apple makes the best computers.")
print("")
userResponse2=input("Do you agree or disagree? Enter your response number here: ")
print("")
userResponse2=validate(userResponse2)
print("--------------------------------------------------------------------------------")
print("")
print("Question 3: ")
print("")
print("Sodexo serves great food.")
print("")
userResponse3=input("Do you agree or disagree? Enter your response number here: ")
print("")
userResponse3=validate(userResponse3)
print("--------------------------------------------------------------------------------")
print("")
print("Question 4: ")
print("")
print("Riding in an airplane is fun.")
print("")
userResponse4=input("Do you agree or disagree? Enter your response number here: ")
print("")
userResponse4=validate(userResponse4)
print("--------------------------------------------------------------------------------")
print("")
print("Question 5: ")
print("")
print("Living on campus at Lewis University is fun.")
print("")
userResponse5=input("Do you agree or disagree? Enter your response number here: ")
print("")
userResponse5=validate(userResponse5)
print("--------------------------------------------------------------------------------")
print("")
similarity1=5-abs(int(userResponse1)-desiredResponse1)
similarity2=5-abs(int(userResponse2)-desiredResponse2)
similarity3=5-abs(int(userResponse3)-desiredResponse3)
similarity4=5-abs(int(userResponse4)-desiredResponse4)
similarity5=5-abs(int(userResponse5)-desiredResponse5)
weighted1=similarity1*questionWeight1
weighted2=similarity2*questionWeight2
weighted3=similarity3*questionWeight3
weighted4=similarity4*questionWeight4
weighted5=similarity5*questionWeight5
compatibilityPercent=weighted1+weighted2+weighted3+weighted4+weighted5
print("Results: Compatibility level is "+str(compatibilityPercent)+"%.")
print("")
if compatibilityPercent>85:
    print("Wanna be my roomate?")
elif compatibilityPercent>65:
    print("Let's text in our free time.")
else:
    print("I'm filing a restraining order.")
print("")
print("--------------------------------------------------------------------------------")