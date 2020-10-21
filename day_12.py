class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNumber,score):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.score=score
    def calculate(self):
        avg_score=sum(self.score)/len(self.score)
        if avg_score>=90 and avg_score<=100:
            letter="O"
        elif avg_score>=80 and avg_score<90:
            letter="E"
        elif avg_score>=70 and avg_score<80:
            letter="A"
        elif avg_score>=55 and avg_score<70:
            letter="P"
        elif avg_score>40 and avg_score<55:
            letter="D"
        elif avg_score<40:
            letter="T"
        return letter   


line = input().split()
