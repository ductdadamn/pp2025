# Global data structures 
students = []  # List to store student tuples (id, name, dob)
courses = []   # List to store course tuples (id, name)
marks = {}     # Dictionary: {course_id: {student_id: mark}}

# --- INPUT FUNCTIONS --- 

def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_information():
    num = input_number_of_students()
    for _ in range(num): 
        print(f"\nStudent {_+1}:")
        s_id = input("  ID: ")
        s_name = input("  Name: ")
        s_dob = input("  DoB (DD/MM/YYYY): ")
        # Using a tuple for fixed student data 
        students.append((s_id, s_name, s_dob))

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    num = input_number_of_courses()
    for _ in range(num): 
        print(f"\nCourse {_+1}:")
        c_id = input("  ID: ")
        c_name = input("  Name: ")
        # Using a tuple for fixed course data
        courses.append((c_id, c_name))

def input_marks():
    if not courses:
        print("Error: No courses available.")
        return
    
    list_courses()
    course_id = input("\nEnter Course ID to input marks for: ")
    
    # Check if course exists
    course_exists = any(c[0] == course_id for c in courses)
    if not course_exists:
        print("Invalid Course ID.")
        return

    # Initialize nested dictionary for this course if not exists 
    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nEntering marks for course: {course_id}")
    for s_id, s_name, _ in students: 
        score = float(input(f"  Mark for {s_name} (ID: {s_id}): "))
        marks[course_id][s_id] = score 

# --- LISTING FUNCTIONS --- 

def list_courses():
    print("\n--- List of Courses ---")
    for c_id, c_name in courses: 
        print(f"ID: {c_id} | Name: {c_name}")

def list_students():
    print("\n--- List of Students ---")
    for s_id, s_name, s_dob in students: 
        print(f"ID: {s_id} | Name: {s_name} | DoB: {s_dob}")

def show_student_marks():
    list_courses()
    course_id = input("\nEnter Course ID to view marks: ")
    
    if course_id in marks: 
        print(f"\n--- Marks for Course {course_id} ---")
        for s_id, score in marks[course_id].items(): 
            # Find student name from ID
            name = next((s[1] for s in students if s[0] == s_id), "Unknown")
            print(f"Student: {name} ({s_id}) | Mark: {score}")
    else:
        print("No marks recorded for this course.")

# --- MAIN EXECUTION ---

def main():
    input_student_information()
    input_course_information()
    
    while True:
        print("\n--- Student Mark Management ---")
        print("1. List Students")
        print("2. List Courses")
        print("3. Input Marks for a Course")
        print("4. Show Marks for a Course")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1': list_students()
        elif choice == '2': list_courses()
        elif choice == '3': input_marks()
        elif choice == '4': show_student_marks()
        elif choice == '5': break 
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()