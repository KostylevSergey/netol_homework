
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def who_is_better(self, student):
        if isinstance(student, Student):
            if self.average() > student.average():
                return f'У {self.name} {self.surname} средний балл выше'
            elif self.average() == student.average():
                return f'Средний балл одинаковый'
            else:
                return f'У {student.name} {student.surname} средний балл выше'

    def average(self):
        average_grade = 0
        grade_count = 0
        for course, grade_list in self.grades.items():
            for grade in grade_list:
                average_grade += grade
                grade_count += 1
        if grade_count == 0:
            return 'У студента нет оценок'
        else:
            return average_grade / grade_count

    def courses(self):
        course_flow = ''
        for course in self.courses_in_progress:
            if course == self.courses_in_progress[-1]:
                course_flow += f'{course}'
            else:
                course_flow += f'{course}, '
        return course_flow

    def courses_finished(self):
        course_flow = ''
        for course in self.finished_courses:
            if course == self.finished_courses[-1]:
                course_flow += f'{course}'
            else:
                course_flow += f'{course}, '
        return course_flow

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.average()}\nКурсы в процессе обучения: {self.courses()}\nЗавершенные курсы: {self.courses_finished()}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average(self):
        average_grade = 0
        grade_count = 0
        for course, grade_list in self.grades.items():
            for grade in grade_list:
                average_grade += grade
                grade_count += 1
        if grade_count == 0:
            return 'У лектора нет оценок'
        else:
            return average_grade / grade_count

    def who_is_better(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if self.average() > lecturer.average():
                return f'У {self.name} {self.surname} средний балл выше'
            elif self.average() == lecturer.average():
                return f'Средний балл одинаковый'
            else:
                return f'У {lecturer.name} {lecturer.surname} средний балл выше'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.average()}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

# Какие есть курсы: git , python

student_list = []

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_2 = Student('Bill', 'Gates', 'male')

student_list.append(student_1)
student_list.append(student_2)


lecturer_list = []

lecturer_1 = Lecturer('Bob', 'Michaels')
lecturer_2 = Lecturer('Rob', 'Schneider')

lecturer_1.courses_attached.append('Git')
lecturer_2.courses_attached.append('Python')

lecturer_list.append(lecturer_1)
lecturer_list.append(lecturer_2)


reviewer_1 = Reviewer('Clark', 'Kent')
reviewer_2 = Reviewer('Cal', 'El')

reviewer_1.courses_attached.append("Git")
reviewer_2.courses_attached.append('Python')


student_1.courses_in_progress.append('Git')
student_2.courses_in_progress.append('Git')
student_1.courses_in_progress.append('Python')
student_2.courses_in_progress.append('Python')


reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 9)

reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 5)


student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_2.rate_lecturer(lecturer_1, 'Git', 7)

student_1.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Python', 10)

print(reviewer_1)
print(lecturer_1)
print(student_1)

print(student_1.who_is_better(student_2))
print(lecturer_1.who_is_better(lecturer_2))

def students_avg(lst):
    average = 0
    count = 0
    for student_grade in lst:
        average += student_grade.average()
        count += 1
    return average / count

def lecturers_avg(lst):
    average = 0
    count = 0
    for lecturer_grade in lst:
        average += lecturer_grade.average()
        count += 1
    return average / count

print(f'Средний балл всех студентов: {students_avg(student_list)}')
print(f'Средний балл всех лекторов: {lecturers_avg(lecturer_list)}')











