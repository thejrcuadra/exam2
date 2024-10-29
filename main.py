class Student():
    def __init__(self, studentId, name, score):
        self._studentId = studentId
        self._name = name
        self._score = score

    def details(self):
        print(f"Student ID: {self._studentId}, Student Name: {self._name}, Student Score: {self._score}")

class Classroom():
    def __init__(self):
        self._classroom = []

    def addStudent(self, student):
        if student not in self._classroom:
            self._classroom.append(student)
            print(f"{student._name} has been added to the system.")
        else:
            print(f"{student._name} is already in the system.")

    def searchStudent(self, studentId):
        for student in self._classroom:
            if student._studentId == studentId:
                return student.details()
        print("Student not found.")
    
    def sortStudents(self):
        scores = []
        for student in self._classroom:
            scores.append([student._name, student._score])

        for x in range(len(scores)):
            min = x 
            for y in range(x + 1, len(scores)):
                # if there is, switching the values
                if scores[y][1] > scores[min][1]:
                    min = y
            
            scores[x], scores[min] = scores[min], scores[x]

        print(scores)
    
def main():
    james = Student("339", "James Bond", "77")
    michael = Student("290", "Michael Jackson", "85")
    bill = Student("621", "Bill Gates", "97")

    english = Classroom()

    english.addStudent(james)
    english.addStudent(michael)
    english.addStudent(bill)

    english.sortStudents()
    english.searchStudent("290")
    english.searchStudent("000")

main()