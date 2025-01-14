class Student: #we have created a class called students, class has to be lowercase, and Student has to start with capital letter
    def __init__(self, name, age, grade, height): #self = student and this whole function is to initialize
        self.name = name # now we are binding the values of the class
        self.age = age # have to do these steps
        self.grade = grade
        self.height = height


    def __str__ (self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Height: {self.height}"

new_student = Student("Suraya", 24, "A", 168)
old_student = Student("Yousif", 2, "A", 60)



print(new_student)

