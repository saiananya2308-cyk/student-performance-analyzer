students=[
    {"name":"Priya", "marks":91},
    {"name":"Rahul", "marks":91},
    {"name":"Kiran", "marks":35},
    {"name":"Meera", "marks":40}
    ]
#Calculates the average marks of all students
def calculate_average(students):
    total = 0
    for student in students:
        total = total + student["marks"]
    average = total/len(students)
    return average
#Finds the highest marks among all students
def find_highest(students):
    highest = students[0]["marks"]
    for student in students:
        if student["marks"] > highest:
            highest = student["marks"]
    return highest
#Finds the lowest marks among all students
def find_lowest(students):
    lowest = students[0]["marks"]
    for student in students:
        if student["marks"] < lowest:
            lowest = student["marks"]
    return lowest
#Finds the toppers among all students
def find_toppers(students):
    highest = students[0]["marks"]
    toppers = []
    for student in students:
        if student["marks"] > highest:
            highest = student["marks"]
            toppers.clear()
            toppers.append(student["name"])
        elif student["marks"] == highest:
            toppers.append(student["name"])
    return toppers
#Finds the lowest scorers among all students
def find_lowest_students(students):
    lowest = students[0]["marks"]
    lowest_students = []
    for student in students:
        if student["marks"] < lowest:
            lowest = student["marks"]
            lowest_students.clear()
            lowest_students.append(student["name"])
        elif student["marks"] == lowest:
            lowest_students.append(student["name"])
    return lowest_students
#Counts the number of students who passed
def count_passed(students):
    passed = 0
    for student in students:
        if student["marks"] >= 40:
            passed = passed + 1
    return passed
#Counts the number of students who failed
def count_failed(students):
    failed = 0
    for student in students:
        if student["marks"] < 40:
            failed = failed + 1
    return failed
#Generates the complete student performance report
def analyze_students(students):
    average = calculate_average(students)
    highest = find_highest(students)
    lowest = find_lowest(students)
    toppers = find_toppers(students)
    lowest_students = find_lowest_students(students)
    passed = count_passed(students)
    failed = count_failed(students)
    print("STUDENT PERFORMANCE REPORT")
    print("--------------------------")
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Toppers:", toppers)
    print("Lowest Scorers:", lowest_students)
    print("Passed:", passed)
    print("Failed:", failed)
#Runs the student performance analyzer
analyze_students(students)

        

    
    
