class Student():
    def __init__ (self, name, gps, age, group):
        self.name = name
        self.age = age
        self.gps = gps
        self.group = group


    def StudentData(self):
        return 'ФИО: ' + self.name, 'Возраст: ' + self.age, 'Город: ' + self.gps , 'Группа: ' + self.group

student1 = Student ('Мышкин Владимир','Атырау','18','АиУ-19р/о')
student2 = Student ('Алмат Изимов', 'Атырау', '18', 'Аиу-19р/o')
student3 = Student ('Каймулдиев Данияр', 'Атырау', '18', 'Аиу-19р/o')
student4 = Student ('Кубашева Дильназ','Атырау','18','АиУ-19р/о')
student5 = Student ('Маскар Махамбет','Жанаозен','18','АиУ-19р/о')

print(*(student1.StudentData()), sep='\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(*(student2.StudentData()), sep='\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(*(student3.StudentData()), sep='\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(*(student4.StudentData()), sep='\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(*(student5.StudentData()), sep='\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
