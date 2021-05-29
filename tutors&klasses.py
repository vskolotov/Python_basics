"""
Есть два списка.
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <class>)
"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']

tutor_class = ((tutors[i], classes[i]) if i < len(classes) else (tutors[i], None) for i in range(len(tutors)))

for i in range(8):
    print(next(tutor_class))
