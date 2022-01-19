print('Welcome to the Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: In school, Albert Einstein failed most of the subjects, except for physics and math.?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Bill Gates is the founder of Amazon.? ')
    if answer.lower()=='no':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Mice have more bones than humans.?')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')