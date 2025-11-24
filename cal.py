import csv
file= "grades.csv"
#create file if not exists
try:
    open(file,"r")
except FileNotFoundError:
    with open(file,"w",newline="")as f:
        writer=csv.writer(f)
        writer.writerow(["name","total marks","percentage","grade","status"])

def calculate_grade(percentage):
    """return grade based on percentage."""
    if percentage >=90:
        return "A"
    elif percentage >=75:
        return"B"
    elif percentage >=50:
        return "C"
    else:
        return "Fail"

def add_student_result():
    print("\n--ADD STUDENT RESULT--")
    name=input("enter student name")
    subjects=int(input("enter number of subjects:"))
    marks=[]

    for i in range(subjects):
        score = float(input(f"enter marks for subject{i+1}:"))
        marks.append(score)
    total = sum(marks)
    max_total= subjects*100
    percentage=(total/ max_total)*100
    grade= calculate_grade(percentage)
    status= "pass" if grade != "Fail"\
    else "fail"

    print("\n---RESULT GENERATED---")
    print(f"name:{name}")
    print(f"total marks :{total}")
    print(f"percentage:{percentage:.2f}%")
    print(f"grade:{grade}")
    print(f"status:{status}")

#save to file
    with open(file,"a",newline="")as f :
        writer = csv.writer(f)
        writer.writerow([name,total,f"{percentage:.2f}%", grade, status])
        print("\nrecord saved successfully! \n")

def view_all_results():
    print("\n---ALL STUDENT RESULTS---")
    with open(file,"r")as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    print()

def search_student():
    print("\n---SEARCH STUDENT RESULT ---")
    name=input("enter student name to search :").lower()
    found= False
    with open(file,"r")as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row["name"].lower()== name:
                found = True
                print("\nResult Found:")
                print(f"Name: {row['name']}")
                print(f"Total Marks: {row['total marks']}")
                print(f"Percentage: {row['percentage']}")
                print(f"Grade: {row['grade']}")
                print(f"Status: {row['status']}")
                break # Break after finding the first match
    if not found :
        print("no record found for that student.\n")

def main_menu():
    while True:
        print("====== GRADE CALCULATOR MENU ======")
        print("1. Add Student Result")
        print("2. View All Results")
        print("3. Search student result")
        print("4. exit")

        choice = input("enter your choice :")

        if choice == "1":
            add_student_result()
        elif choice == "2":
            view_all_results()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("exiting the program...")
            break
        else :
            print("invalid choice ! please try again.\n")

#start program
main_menu()