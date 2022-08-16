######   Students Registration System   ###### 

# Registered Students List, empty at start
Students = []   

# Courses list, to be offered
Courses = ["Artifical Intelligence", "Blockchain", "Cloud Computing"] 

#printing
# ******************************************
# ****** Students Registration System ******
# ******************************************
print("\n"+"*"*42+"\n"+"*"*6 + " Students Registration System "+ "*"*6 + "\n"+ "*"*42)

# Taking students input from user
while True:
    userinput = input("Want to register? Yes:Y / No:N\n")
    if len(userinput) == 1 and userinput == 'N' or userinput == 'n':
        print ("\n" + "*"*73 + "\n" + " "*7 + " Congratulations!!! all students are registered in PIAIC. " + " "*8)
        break
    elif len(userinput) == 1 and userinput == 'Y' or userinput == 'y':
        # Object of a new student going to register      
        new_student = {
            "Name": input('Enter your name: '),     
            "Age": input('Enter your age: '),      
            "Email": input('Enter your email: '),   
            "Phone": input('Enter your phone: '),   
            "Address": input('Enter your address: '), 
            # Courses are taken separately through provided list.
            "Courses": [],
        }
        
        print("*"*3 + " Enter comma separated ids for your desired courses " + "*"*3 + "\n")
        course_number = 1
        # Printing all the available courses list
        for course in Courses:    
            print(f'\tID: {course_number}\tCourse Name: {course}\n')
            course_number+=1 

        # User selection for desired courses
        new_student_courses = input('e.g. "1, 2" or "1,2" for Artificial Intelligence, Blockchain\n ') 

        # Adding user's selected courses to its profile
        for id in new_student_courses:
            if id == '1' or id == '2' or id == '3':
                new_student["Courses"].append(Courses[int(id)-1])

        # Adding the new student to all registered students list
        Students.append(new_student)

    # If user enter's the wrong input will
    else:
        print('Wrong Input!')

print("*"*73 + "\n")

# Printing all registered students list
print_counter = 1
for student in Students:
    print('*'*21+'')
    print('*'*3 + f' Student no. {print_counter} ' + '*'*3)
    print('*'*21+'\n')
    # Printing details of a single student
    for key,value in student.items():
        print(f'{key}: {value}')
    print_counter+=1
print('\n')
