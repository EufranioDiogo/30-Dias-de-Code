class Person:
    	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores

    def calculate(self):
        total = 0

        for score in scores:
            total += score

        total = total // len(scores)
    
        if total < 40:
            return 'T'
        if total < 55:
            return 'D'
        if total < 70:
            return 'P'
        if total < 80:
            return 'A'
        if total < 90:
            return 'E'
        return 'O'

    def printPerson(self):
        print(f'Name: {self.lastName}, {self.firstName}\nID: {self.idNum}')


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())