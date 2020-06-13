
class_num = int(input("How many classes do you have? "))
num = 0

standard = ['std', 'standard', 'default', 'easy', 'ez', 'def']
honors = ['honors', 'ap', 'advanced placement', 'hard', 'advanced', 'adv']
gpas = []

while num < class_num:
    level = input("Is your class standard or Honors/AP? ")
    if level.lower() in standard:
        grade = int(input("What is your grade? (As a percentage, minus the percentage sign: 96 or 24) "))
        if grade <= 100:
            if grade >= 97:
                gpas.append(4.3)
            elif grade >= 93:
                gpas.append(4.0)
            elif grade >= 90:
                gpas.append(3.7)
            elif grade >= 87:
                gpas.append(3.3)
            elif grade >= 83:
                gpas.append(3.0)
            elif grade >= 80:
                gpas.append(2.7)
            elif grade >= 77:
                gpas.append(2.3)
            elif grade >= 73:
                gpas.append(2.0)
            elif grade >= 70:
                gpas.append(1.7)
            elif grade >= 67:
                gpas.append(1.3)
            elif grade >= 63:
                gpas.append(1.0)
            elif grade >= 60:
                gpas.append(0.7)
            elif grade >= 0:
                gpas.append(0)
            elif grade < 0:
                print("Uh... How'd you manage that, buddy?")
        else:
            print("That's not a valid grade, silly!")
        num = num + 1
    elif level.lower() in honors:
        grade = int(input("What is your grade? (As a percentage, minus the percentage sign: 96 or 24) "))
        if grade < 100:
            if grade >= 97:
                gpas.append(4.8)
            elif grade >= 93:
                gpas.append(4.5)
            elif grade >= 90:
                gpas.append(4.2)
            elif grade >= 87:
                gpas.append(3.8)
            elif grade >= 83:
                gpas.append(3.5)
            elif grade >= 80:
                gpas.append(3.2)
            elif grade >= 77:
                gpas.append(2.8)
            elif grade >= 73:
                gpas.append(2.5)
            elif grade >= 70:
                gpas.append(2.2)
            elif grade >= 67:
                gpas.append(1.8)
            elif grade >= 63:
                gpas.append(1.5)
            elif grade >= 60:
                gpas.append(1.2)
            elif grade >= 0:
                gpas.append(0)
        else:
            print("That's not a valid grade, silly!")
        num = num + 1
    else:
        print("That is not an option.")

sum = 0
for gpa in gpas:
    sum = round(sum + gpa, 1)

if gpa <= 4:
    print(f"Here's your weighted GPA: {round(sum/class_num, 1)}")
elif gpa > 4:
    print(f"Here's your weighted GPA: {round(sum/class_num,2)}")
