##this a program that takes students and their marks and sorts them and returns 
##sorted marks from in descending order 
print ('welcome to the school marks grader\n ')
students = int(input('enter the number of students you want to enter\n '))
StudentsMarks = []
for i in range (students):
    studentname = input('enter the name of the student\n')
    studentmarks = int(input('enter the students marks\n'))
    StudentsMarks.append((studentname , studentmarks))
#print(StudentsMarks)

def sortmarks():
    for i in range (len(StudentsMarks)):
        for j in range(i+1,len(StudentsMarks)):
                if StudentsMarks[i][1] < StudentsMarks[j][1]:
                    temp = StudentsMarks[i]
                    StudentsMarks[i] = StudentsMarks[j]
                    StudentsMarks[j] = temp
                j = 1

sortmarks()
for x in range (len(StudentsMarks)):

     print((StudentsMarks[x][0]).capitalize(), '-' ,StudentsMarks[x][1])
