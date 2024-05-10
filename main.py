# import pickle

# class Student:
#     def __init__(self, name, age, gpa):
#         self.name = name
#         self.age = age
#         self.gpa = gpa
        

# def save_students(student, filename):
#     with open(filename, "wb") as file:
#         return pickle.dump(student, file)
    
# def load_student(filename):
#     with open(filename, "wb") as file:
#         return pickle.load(file)
    
# student1 = Student("Загадин", 16, 4.2)
# student2 = Student("Ярослав", 17, 3.2)
# student3 = Student("Олег", 17, 2.2)

# list_student = [student1, student2, student3]
# save_students(list_student, "Студенты.bin


import cv2

cap = cv2.VideoCapture(0)

for i in range(30):
    cap.read()
 
ret, frame = cap.read()

cv2.imwrite('cam.png', frame)   

cap.release()
