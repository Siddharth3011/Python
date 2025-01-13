subj1 = int(input("Enter the marks student get: "))
subj2 = int(input("Enter the marks student get: "))
subj3 = int(input("Enter the marks student get: "))

total_percentage = ((subj1 + subj2 + subj3)*100)/300
if(total_percentage>=40 and subj1>= 33 and subj2>=33 and subj3>=33):
    print("you are pass, with percentage:", total_percentage)

else:
    print("You fail")