class Student:
    def __init__(self, student_id, name, grade):
        self.student_id=student_id
        self.name=name
        self.grade=grade

    def display_info(self):
        print(f"\nStudent ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}")

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id=teacher_id
        self.name=name
        self.subject=subject

    def display_info(self):
        print(f"\nTeacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}")

class Course:
    def __init__(self, course_code, course_name, teacher, students):
        self.course_code=course_code
        self.course_name=course_name
        self.teacher=teacher
        self.students=students

    def display_info(self):
        print(f"\nCourse Code: {self.course_code}, Course Name: {self.course_name}")
        print("\nTeacher:")
        self.teacher.display_info()
        print("\nStudents:")
        for student in self.students:
            student.display_info()
            
class SaveData:
    def __init__(self,path):
        self.path="contents.txt"

    def write(self,content):
        with open(self.path,"w") as file:
            file.write(content)
            return true    

def main():
    students=[]
    teachers=[]
    courses=[]
    print("""1.Student_form/details 
    2. Teacher_form/details
    3.Course-form/details""")
    cho=int(input("\nEnter your choice:"))
    if cho==1:
        num_students=int(input("\nEnter the number of Students:"))
        for i in range(num_students):
            student_id=input(f"\nEnter Student {i+1} ID: ")
            name=input(f"\nEnter Student {i+1} Name: ")
            grade=input(f"\nEnter Student {i+1} Grade: ")
            students.append(Student(student_id, name, grade))
            print("\nRegistration Successful")
    elif cho==2:
        num_teachers=int(input("\nEnter the number of Teachers: "))
        for i in range(num_teachers):
            teacher_id=input(f"\nEnter Teacher {i+1} ID: ")
            name=input(f"\nEnter Teacher {i+1} Name: ")
            subject=input(f"\nEnter Teacher {i+1} Subject: ")
            teachers.append(Teacher(teacher_id, name, subject))
            print("\nRegistration Successful")
    
    elif cho==3:
        num_courses=int(input("\nEnter the number of Courses: "))
        for i in range(num_courses):
            course_code=input(f"\nEnter Course {i+1} Code: ")
            course_name=input(f"\nEnter Course {i+1} Name: ")
            teacher_index=int(input("\nEnter the index of the teacher for this course: "))
            teacher=teachers[teacher_index]
            student_indices=input("\nEnter the indices of students for this course (comma seperated): ")
            student_indices=student_indices.split(",")
            students_for_course=[students[int(index)] for index in student_indices]
            courses.append(Course(course_code, course_name, teacher, students_for_course))
            print("\nRegistration Successful")
        else:
            print("\nInvalid Input")
            
if __name__=="__main__":
    main()          
