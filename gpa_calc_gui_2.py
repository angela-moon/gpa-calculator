from tkinter import *

root = Tk()
root.title("ASD GPA Calculator")

title = Label(text="ASD GPA Calculator", font="verdana 16 bold", padx="10")

### Phase 1: Entering the number of classes
class_num_label = Label(text="How many classes do you have? (As an integer 8 or less)", justify=LEFT, padx="2")
class_num_entry = Entry()

### Phase 2: Entering your grades

# Variables for the dropdown menu
class1_type = StringVar(root)
class2_type = StringVar(root)
class3_type = StringVar(root)
class4_type = StringVar(root)
class5_type = StringVar(root)
class6_type = StringVar(root)
class7_type = StringVar(root)
class8_type = StringVar(root)

enter_gpa = Label(text="What grade did you get in the course? (As an integer--36, 82, etc.)", font="helvetica 9 bold",
                  padx="2")

# Initializing widgets for each class (Instructions, entry box, type dropdown)
class1_label = Label(text="Enter the first grade and choose the class type in the dropdown menu.")
class1_entry = Entry()
class1_dropdown = OptionMenu(root, class1_type, "Standard", "Honors/AP")

class2_label = Label(text="Enter the second grade and choose the class type in the dropdown menu.")
class2_entry = Entry()
class2_dropdown = OptionMenu(root, class2_type, "Standard", "Honors/AP")

class3_label = Label(text="Enter the third grade and choose the class type in the dropdown menu.")
class3_entry = Entry()
class3_dropdown = OptionMenu(root, class3_type, "Standard", "Honors/AP")

class4_label = Label(text="Enter the fourth grade and choose the class type in the dropdown menu.")
class4_entry = Entry()
class4_dropdown = OptionMenu(root, class4_type, "Standard", "Honors/AP")

class5_label = Label(text="Enter the fifth grade and choose the class type in the dropdown menu.")
class5_entry = Entry()
class5_dropdown = OptionMenu(root, class5_type, "Standard", "Honors/AP")

class6_label = Label(text="Enter the sixth grade and choose the class type in the dropdown menu.")
class6_entry = Entry()
class6_dropdown = OptionMenu(root, class6_type, "Standard", "Honors/AP")

class7_label = Label(text="Enter the seventh grade and choose the class type in the dropdown menu.")
class7_entry = Entry()
class7_dropdown = OptionMenu(root, class7_type, "Standard", "Honors/AP")

class8_label = Label(text="Enter the eighth grade and choose the class type in the dropdown menu.")
class8_entry = Entry()
class8_dropdown = OptionMenu(root, class8_type, "Standard", "Honors/AP")

error_label = Label(text="Error. Please try again.", fg="red")

# Restart button
def restart():
    class_num_entry.config(state=NORMAL)
    class_num_entry.delete(0, END)

    enter_gpa.grid_remove()
    enter_grades.grid_remove()

    class1_label.grid_remove()
    class1_entry.grid_remove()
    class1_dropdown.grid_remove()

    class2_label.grid_remove()
    class2_entry.grid_remove()
    class2_dropdown.grid_remove()

    class3_label.grid_remove()
    class3_entry.grid_remove()
    class3_dropdown.grid_remove()

    class4_label.grid_remove()
    class4_entry.grid_remove()
    class4_dropdown.grid_remove()

    class5_label.grid_remove()
    class5_entry.grid_remove()
    class5_dropdown.grid_remove()

    class6_label.grid_remove()
    class6_entry.grid_remove()
    class6_dropdown.grid_remove()

    class7_label.grid_remove()
    class7_entry.grid_remove()
    class7_dropdown.grid_remove()

    class8_label.grid_remove()
    class8_entry.grid_remove()
    class8_dropdown.grid_remove()

restart = Button(text="Restart", command=restart)

# Create class entry definition for the first Enter button
class_num = 0

def create_class_entry():
    global class_num
    try:
        class_num = int(class_num_entry.get())
    except ValueError:
        error_label.grid(column=0, row=3, sticky="w", columnspan=3)

    if (class_num < 1) or (class_num > 8):
        error_label.grid(column=0, row=3, sticky="w", columnspan=3)

    elif class_num == 8:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        class2_label.grid(column=0, row=6, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=7, sticky="ew", padx=2)
        class2_dropdown.grid(column=1, row=7, sticky="w", padx=2)

        class3_label.grid(column=0, row=8, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=9, sticky="ew", padx=2)
        class3_dropdown.grid(column=1, row=9, sticky="w", padx=2)

        class4_label.grid(column=0, row=10, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=11, sticky="ew", padx=2)
        class4_dropdown.grid(column=1, row=11, sticky="w", padx=2)

        class5_label.grid(column=0, row=12, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=13, sticky="ew", padx=2)
        class5_dropdown.grid(column=1, row=13, sticky="w", padx=2)

        class6_label.grid(column=0, row=14, sticky="w", columnspan=3)
        class6_entry.grid(column=0, row=15, sticky="ew", padx=2)
        class6_dropdown.grid(column=1, row=15, sticky="w", padx=2)

        class7_label.grid(column=0, row=16, sticky="w", columnspan=3)
        class7_entry.grid(column=0, row=17, sticky="ew", padx=2)
        class7_dropdown.grid(column=1, row=17, sticky="w", padx=2)

        class8_label.grid(column=0, row=18, sticky="w", columnspan=3)
        class8_entry.grid(column=0, row=19, sticky="ew", padx=2)
        class8_dropdown.grid(column=1, row=19, sticky="w", padx=2)

        enter_grades.grid(column=2, row=19, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 7:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        class2_label.grid(column=0, row=6, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=7, sticky="ew", padx=2)
        class2_dropdown.grid(column=1, row=7, sticky="w", padx=2)

        class3_label.grid(column=0, row=8, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=9, sticky="ew", padx=2)
        class3_dropdown.grid(column=1, row=9, sticky="w", padx=2)

        class4_label.grid(column=0, row=10, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=11, sticky="ew", padx=2)
        class4_dropdown.grid(column=1, row=11, sticky="w", padx=2)

        class5_label.grid(column=0, row=12, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=13, sticky="ew", padx=2)
        class5_dropdown.grid(column=1, row=13, sticky="w", padx=2)

        class6_label.grid(column=0, row=14, sticky="w", columnspan=3)
        class6_entry.grid(column=0, row=15, sticky="ew", padx=2)
        class6_dropdown.grid(column=1, row=15, sticky="w", padx=2)

        class7_label.grid(column=0, row=16, sticky="w", columnspan=3)
        class7_entry.grid(column=0, row=17, sticky="ew", padx=2)
        class7_dropdown.grid(column=1, row=17, sticky="w", padx=2)

        enter_grades.grid(column=2, row=17, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 6:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        class2_label.grid(column=0, row=6, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=7, sticky="ew", padx=2)
        class2_dropdown.grid(column=1, row=7, sticky="w", padx=2)

        class3_label.grid(column=0, row=8, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=9, sticky="ew", padx=2)
        class3_dropdown.grid(column=1, row=9, sticky="w", padx=2)

        class4_label.grid(column=0, row=10, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=11, sticky="ew", padx=2)
        class4_dropdown.grid(column=1, row=11, sticky="w", padx=2)

        class5_label.grid(column=0, row=12, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=13, sticky="ew", padx=2)
        class5_dropdown.grid(column=1, row=13, sticky="w", padx=2)

        class6_label.grid(column=0, row=14, sticky="w", columnspan=3)
        class6_entry.grid(column=0, row=15, sticky="ew", padx=2)
        class6_dropdown.grid(column=1, row=15, sticky="w", padx=2)

        enter_grades.grid(column=2, row=15, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 5:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        class2_label.grid(column=0, row=6, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=7, sticky="ew", padx=2)
        class2_dropdown.grid(column=1, row=7, sticky="w", padx=2)

        class3_label.grid(column=0, row=8, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=9, sticky="ew", padx=2)
        class3_dropdown.grid(column=1, row=9, sticky="w", padx=2)

        class4_label.grid(column=0, row=10, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=11, sticky="ew", padx=2)
        class4_dropdown.grid(column=1, row=11, sticky="w", padx=2)

        class5_label.grid(column=0, row=12, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=13, sticky="ew", padx=2)
        class5_dropdown.grid(column=1, row=13, sticky="w", padx=2)

        enter_grades.grid(column=2, row=13, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 4:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        class2_label.grid(column=0, row=6, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=7, sticky="ew", padx=2)
        class2_dropdown.grid(column=1, row=7, sticky="w", padx=2)

        class3_label.grid(column=0, row=8, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=9, sticky="ew", padx=2)
        class3_dropdown.grid(column=1, row=9, sticky="w", padx=2)

        class4_label.grid(column=0, row=10, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=11, sticky="ew", padx=2)
        class4_dropdown.grid(column=1, row=11, sticky="w", padx=2)

        enter_grades.grid(column=2, row=11, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 3:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        class2_label.grid(column=0, row=6, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=7, sticky="ew", padx=2)
        class2_dropdown.grid(column=1, row=7, sticky="w", padx=2)

        class3_label.grid(column=0, row=8, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=9, sticky="ew", padx=2)
        class3_dropdown.grid(column=1, row=9, sticky="w", padx=2)

        enter_grades.grid(column=2, row=9, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 2:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        class2_label.grid(column=0, row=6, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=7, sticky="ew", padx=2)
        class2_dropdown.grid(column=1, row=7, sticky="w", padx=2)

        enter_grades.grid(column=2, row=7, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 1:
        error_label.grid_remove()

        enter_gpa.grid(column=0, row=3, sticky="W", columnspan=3)
        class1_label.grid(column=0, row=4, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=5, sticky="ew", padx=2)
        class1_dropdown.grid(column=1, row=5, sticky="w", padx=2)

        enter_grades.grid(column=2, row=5, columnspan=2, padx=2)

        class_num_entry.config(state=DISABLED)

class_num_enter = Button(text="Enter", command=create_class_entry)

### Phase 3: Calculating the GPA
def calculate_grade():
    global class1_type
    global class2_type
    global class3_type
    global class4_type
    global class5_type
    global class6_type
    global class7_type
    global class8_type

    stand = "<tkinter.StringVar object at 0x03AFF520>"
    hon = "<tkinter.StringVar object at 0x03AFFAC0>"

    if class_num == 8:
        class1_grade = int(class1_entry.get())
        class2_grade = int(class2_entry.get())
        class3_grade = int(class3_entry.get())
        class4_grade = int(class4_entry.get())
        class5_grade = int(class5_entry.get())
        class6_grade = int(class6_entry.get())
        class7_grade = int(class7_entry.get())
        class8_grade = int(class8_entry.get())

        grades = {class1_grade: class1_type, class2_grade: class2_type, class3_grade: class3_type,
                  class4_grade: class4_type,
                  class5_grade: class5_type, class6_grade: class6_type, class7_grade: class7_type,
                  class8_grade: class8_type}
    elif class_num == 7:
        class1_grade = int(class1_entry.get())
        class2_grade = int(class2_entry.get())
        class3_grade = int(class3_entry.get())
        class4_grade = int(class4_entry.get())
        class5_grade = int(class5_entry.get())
        class6_grade = int(class6_entry.get())
        class7_grade = int(class7_entry.get())

        grades = {class1_grade: class1_type, class2_grade: class2_type, class3_grade: class3_type,
                  class4_grade: class4_type,
                  class5_grade: class5_type, class6_grade: class6_type, class7_grade: class7_type}
    elif class_num == 6:
        class1_grade = int(class1_entry.get())
        class2_grade = int(class2_entry.get())
        class3_grade = int(class3_entry.get())
        class4_grade = int(class4_entry.get())
        class5_grade = int(class5_entry.get())
        class6_grade = int(class6_entry.get())

        grades = {class1_grade: class1_type, class2_grade: class2_type, class3_grade: class3_type,
                  class4_grade: class4_type,
                  class5_grade: class5_type, class6_grade: class6_type}
    elif class_num == 5:
        class1_grade = int(class1_entry.get())
        class2_grade = int(class2_entry.get())
        class3_grade = int(class3_entry.get())
        class4_grade = int(class4_entry.get())
        class5_grade = int(class5_entry.get())

        grades = {class1_grade: class1_type, class2_grade: class2_type, class3_grade: class3_type,
                  class4_grade: class4_type,
                  class5_grade: class5_type}
    elif class_num == 4:
        class1_grade = int(class1_entry.get())
        class2_grade = int(class2_entry.get())
        class3_grade = int(class3_entry.get())
        class4_grade = int(class4_entry.get())

        grades = {class1_grade: class1_type, class2_grade: class2_type, class3_grade: class3_type,
                  class4_grade: class4_type}
    elif class_num == 3:
        class1_grade = int(class1_entry.get())
        class2_grade = int(class2_entry.get())
        class3_grade = int(class3_entry.get())

        grades = {class1_grade: class1_type, class2_grade: class2_type, class3_grade: class3_type}
    elif class_num == 2:
        class1_grade = int(class1_entry.get())
        class2_grade = int(class2_entry.get())

        grades = {class1_grade: class1_type, class2_grade: class2_type}
    elif class_num == 1:
        class1_grade = int(class1_entry.get())

        grades = {class1_grade: class1_type}

    gpas = []

    for grade in grades:
        if grades[grade]==stand:
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
            else:
                error_label.grid(column=0, row=20, sticky="w", columnspan=3)
        elif grades[grade]==hon:
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
                error_label.grid(column=0, row=20, sticky="w", columnspan=3)

enter_grades = Button(text="Enter grades", padx="35", command=calculate_grade)


title.grid(column=0, row=0, sticky="ew", columnspan=3)
class_num_label.grid(column=0, row=1, sticky="w", columnspan=3)
class_num_entry.grid(column=0, row=2, sticky="ew", padx=2)
class_num_enter.grid(column=1, row=2, sticky="w", padx=2)
restart.grid(column=0, row=20, columnspan=3, sticky="w", padx=2)

root.mainloop()