class Score():
    def __init__(self, a,b):
        self.sub_name = a
        self.score = b

class Student():
    def __init__(self, scores, name):
        self.all_scores = scores
        self.name = name

    def average(self):
        sum = 0
        for i in self.all_scores:
            sum += i.score
        average = sum/len(self.all_scores)
        return average

    def printscores(self):
        print(f"student: {self.name}")
        for i in self.all_scores:
            print(f"{i.sub_name} : {i.score}")
    
def ClassAverage(students, subjects):
    all_sum = 0
    all_avg = 0
    for k in subjects:
        sub_avg = 0
        sub_sum = 0
        count = 0
        for i in students:
            for j in i.all_scores:
                if j.sub_name == k:
                    sub_sum += j.score
                    count += 1
        sub_avg = sub_sum / count
        all_sum += sub_avg
    all_avg = all_sum / len(subjects)
    return all_avg




s1 = Student([Score('Math',80),Score('Eng',90),Score('Sci',100)],'Mehan')
s2 = Student([Score('Math',20),Score('Eng',40),Score('Sci',60)],'Mahesh')
s3 = Student([Score('Math',30),Score('Eng',50),Score('Sci',70)],'Mohanapriya')

print(s1.average())

allstudents = [s1,s2,s3]
subjects = ['Math','Eng','Sci']

print(ClassAverage(allstudents,subjects))

s1.printscores()