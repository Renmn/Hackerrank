class Person(object):
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores
        
        def calculate(self):
        num_score = sum(self.scores)/len(self.scores)

        if num_score >=90:
            letter_score = 'O'
        elif  num_score >=80:
            letter_score ='E'
        elif  num_score >=70:
            letter_score ='A'
        elif  num_score >=55:
            letter_score ='P'
        elif  num_score >=40:
            letter_score ='D'
        else:
            letter_score = 'T'
        
        return letter_score
