from tkinter import *

root = Tk()
root.title("ASD GPA Calculator")

title = Label(text="ASD GPA Calculator", font="verdana 16 bold", padx="10")
class_num_label = Label(text="How many classes do you have? (As an integer 8 or less)", justify=LEFT, padx="2")
class_num_entry = Entry()

class1_type = StringVar(root)

enter_gpa = Label(text="What grade did you get in the course? (As an integer--36, 82, etc.)", padx="2")
class1_label = Label(text="Enter the first grade.")
class1_entry = Entry()
class1_dropdown = OptionMenu(root, class1_type, "Standard", "Honors/AP")
class2_label = Label(text="Enter the second grade.")
class2_entry = Entry()
class3_label = Label(text="Enter the third grade.")
class3_entry = Entry()
class4_label = Label(text="Enter the fourth grade.")
class4_entry = Entry()
class5_label = Label(text="Enter the fifth grade.")
class5_entry = Entry()
class6_label = Label(text="Enter the sixth grade.")
class6_entry = Entry()
class7_label = Label(text="Enter the seventh grade.")
class7_entry = Entry()
class8_label = Label(text="Enter the eighth grade.")
class8_entry = Entry()

enter_class1 = Button(text="Enter")
enter_class2 = Button(text="Enter")
enter_class3 = Button(text="Enter")
enter_class4 = Button(text="Enter")
enter_class5 = Button(text="Enter")
enter_class6 = Button(text="Enter")
enter_class7 = Button(text="Enter")
enter_class8 = Button(text="Enter")

error_label = Label(text="Error. Please try again.", fg="red")

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
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        class1_dropdown.grid(column=2, row=4, sticky="w", padx=2)

        class2_label.grid(column=0, row=5, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=6, sticky="ew", padx=2)

        class3_label.grid(column=0, row=7, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=8, sticky="ew", padx=2)

        class4_label.grid(column=0, row=9, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=10, sticky="ew", padx=2)

        class5_label.grid(column=0, row=11, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=12, sticky="ew", padx=2)
        enter_class5.grid(column=1, row=12, sticky="w", padx=2)

        class6_label.grid(column=0, row=13, sticky="w", columnspan=3)
        class6_entry.grid(column=0, row=14, sticky="ew", padx=2)
        enter_class6.grid(column=1, row=14, sticky="w", padx=2)

        class7_label.grid(column=0, row=15, sticky="w", columnspan=3)
        class7_entry.grid(column=0, row=16, sticky="ew", padx=2)
        enter_class7.grid(column=1, row=16, sticky="w", padx=2)

        class8_label.grid(column=0, row=17, sticky="w", columnspan=3)
        class8_entry.grid(column=0, row=18, sticky="ew", padx=2)
        enter_class8.grid(column=1, row=18, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 7:
        error_label.grid_remove()
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        enter_class1.grid(column=1, row=4, sticky="w", padx=2)

        class2_label.grid(column=0, row=5, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=6, sticky="ew", padx=2)
        enter_class2.grid(column=1, row=6, sticky="w", padx=2)

        class3_label.grid(column=0, row=7, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=8, sticky="ew", padx=2)
        enter_class3.grid(column=1, row=8, sticky="w", padx=2)

        class4_label.grid(column=0, row=9, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=10, sticky="ew", padx=2)
        enter_class4.grid(column=1, row=10, sticky="w", padx=2)

        class5_label.grid(column=0, row=11, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=12, sticky="ew", padx=2)
        enter_class5.grid(column=1, row=12, sticky="w", padx=2)

        class6_label.grid(column=0, row=13, sticky="w", columnspan=3)
        class6_entry.grid(column=0, row=14, sticky="ew", padx=2)
        enter_class6.grid(column=1, row=14, sticky="w", padx=2)

        class7_label.grid(column=0, row=15, sticky="w", columnspan=3)
        class7_entry.grid(column=0, row=16, sticky="ew", padx=2)
        enter_class7.grid(column=1, row=16, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 6:
        error_label.grid_remove()
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        enter_class1.grid(column=1, row=4, sticky="w", padx=2)

        class2_label.grid(column=0, row=5, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=6, sticky="ew", padx=2)
        enter_class2.grid(column=1, row=6, sticky="w", padx=2)

        class3_label.grid(column=0, row=7, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=8, sticky="ew", padx=2)
        enter_class3.grid(column=1, row=8, sticky="w", padx=2)

        class4_label.grid(column=0, row=9, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=10, sticky="ew", padx=2)
        enter_class4.grid(column=1, row=10, sticky="w", padx=2)

        class5_label.grid(column=0, row=11, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=12, sticky="ew", padx=2)
        enter_class5.grid(column=1, row=12, sticky="w", padx=2)

        class6_label.grid(column=0, row=13, sticky="w", columnspan=3)
        class6_entry.grid(column=0, row=14, sticky="ew", padx=2)
        enter_class6.grid(column=1, row=14, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 5:
        error_label.grid_remove()
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        enter_class1.grid(column=1, row=4, sticky="w", padx=2)

        class2_label.grid(column=0, row=5, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=6, sticky="ew", padx=2)
        enter_class2.grid(column=1, row=6, sticky="w", padx=2)

        class3_label.grid(column=0, row=7, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=8, sticky="ew", padx=2)
        enter_class3.grid(column=1, row=8, sticky="w", padx=2)

        class4_label.grid(column=0, row=9, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=10, sticky="ew", padx=2)
        enter_class4.grid(column=1, row=10, sticky="w", padx=2)

        class5_label.grid(column=0, row=11, sticky="w", columnspan=3)
        class5_entry.grid(column=0, row=12, sticky="ew", padx=2)
        enter_class5.grid(column=1, row=12, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 4:
        error_label.grid_remove()
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        enter_class1.grid(column=1, row=4, sticky="w", padx=2)

        class2_label.grid(column=0, row=5, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=6, sticky="ew", padx=2)
        enter_class2.grid(column=1, row=6, sticky="w", padx=2)

        class3_label.grid(column=0, row=7, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=8, sticky="ew", padx=2)
        enter_class3.grid(column=1, row=8, sticky="w", padx=2)

        class4_label.grid(column=0, row=9, sticky="w", columnspan=3)
        class4_entry.grid(column=0, row=10, sticky="ew", padx=2)
        enter_class4.grid(column=1, row=10, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 3:
        error_label.grid_remove()
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        enter_class1.grid(column=1, row=4, sticky="w", padx=2)

        class2_label.grid(column=0, row=5, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=6, sticky="ew", padx=2)
        enter_class2.grid(column=1, row=6, sticky="w", padx=2)

        class3_label.grid(column=0, row=7, sticky="w", columnspan=3)
        class3_entry.grid(column=0, row=8, sticky="ew", padx=2)
        enter_class3.grid(column=1, row=8, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 2:
        error_label.grid_remove()
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        enter_class1.grid(column=1, row=4, sticky="w", padx=2)

        class2_label.grid(column=0, row=5, sticky="w", columnspan=3)
        class2_entry.grid(column=0, row=6, sticky="ew", padx=2)
        enter_class2.grid(column=1, row=6, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)

    elif class_num == 1:
        error_label.grid_remove()
        class1_label.grid(column=0, row=3, sticky="w", columnspan=3)
        class1_entry.grid(column=0, row=4, sticky="ew", padx=2)
        enter_class1.grid(column=1, row=4, sticky="w", padx=2)

        class_num_entry.config(state=DISABLED)
        error_label.grid(column=0, row=3, sticky="w", columnspan=2)
enter1 = Button(text="Enter", command=create_class_entry)

title.grid(column=0, row=0, sticky="ew", columnspan=3)
class_num_label.grid(column=0, row=1, sticky="w", columnspan=3)
class_num_entry.grid(column=0, row=2, sticky="ew", padx=2)
enter1.grid(column=1, row=2, sticky="w", padx=2)

root.mainloop()