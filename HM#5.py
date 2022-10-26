# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """
class Laptop:
    def __init__(self):
        display = Battery('To save battery - turn down the brightness')
        bluetooth = Battery('To save battery - turn off bluetooth')
        storage = Battery('To save battery - clean storage')
        self.part = [display.component, bluetooth.component, storage.component]


class Battery:
    def __init__(self, component):
        self.component = component


notebook = Laptop()
print('#1', notebook.part)


# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """
class Guitar:
    def __init__(self, body):
        self.body = body


class GuitarString:
    def __init__(self, e, a, d):
        self.first = e
        self.second = a
        self.third = d


notty = GuitarString(e='E', d="D", a="A")
music = Guitar(notty)
print('\n#2')

# 3
# class Calc:
#     """
#     Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
#     """


class Calc:
    def __init__(self, three, four, five):
        self.three = three
        self.four = four
        self.five = five

    def add_nums1(self):
        return self.three + self.four + self.five

# 3.2 with only one method
    @staticmethod
    def add_nums(one=1, two=2, three=3):
        return one + two + three


print('\n#3.1 add nums:', Calc.add_nums())
calcul = Calc(three=3, four=4, five=5)
print('\n#3.1 add nums:', calcul.add_nums1())


# 4*.
# class Pasta:
#     """
#     Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
#     Він повинен мати 2 методи:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """
class Pasta:
    #__slots__ = ('ingredients')
    ingredients = []

    def __init__(self, ingredients):
        self.ingredients = ingredients
        print(f'pasta_ingredients will equal to {self.ingredients}')

    @classmethod
    def carbonara(cls):
        cls.ingredients = ['forcemeat', 'tomatoes']
        return f'pasta_carbonara.ingredients will equal to {cls.ingredients}'

    @classmethod
    def bolognaise(cls):
        cls.ingredients = ['bacon', 'parmesan', 'eggs']
        return f'pasta_bolognaise.ingredients will equal to {cls.ingredients}'


print('\n#4:')
pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.carbonara()
print(pasta_2)
pasta_3 = Pasta.bolognaise()
print(pasta_3)


# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """
class Concert:
    max_visitors_num = 50

    @classmethod
    def checking(cls, arg):
        return arg <= cls.max_visitors_num

    def __init__(self, counts):
        self.counts = Concert.max_visitors_num
        if self.checking(counts):
            self.counts = counts

    def visitors_count(self):
        return self.counts


print('\n#5')
concert = Concert(20)
concert2 = Concert(200)
print('<=50: ', concert.visitors_count())
print('=>50: ', concert2.visitors_count())  # 50


# 6.
# class AddressBookDataClass:
#     """
# Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


print('\n#6')
Man_256 = AddressBookDataClass(256, 'Roberto Uno', '+44030202', 'str.Street', 'rob.cav@mail.com', '18/01/1990', 32 )
print(Man_256)


# 7. Create the same class (6) but using NamedTuple
import collections
AddressBookData2 = collections.namedtuple('AddressBook', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
object_211 = AddressBookData2('211', 'Jonathan Verdo', '+333333', 'Italy', 'r2@gmail.com', '01/01/1980', 42)
print('\n#7')
print(object_211[0:])


# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
#     """
class AddressBookData3:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
         self.all = [key, name, phone_number, address, email, birthday, age]

    def print_adress_info(self):
        print(f'AddressBook(key={self.all[0]}, name= {self.all[1]}, phone_number={self.all[2]}, address={self.all[3]},'
               f' email={self.all[4]}, birthday= {self.all[5]}, age={self.all[6]}')


AddressBoook = AddressBookData3('a111', 'Bob2', 'call+38096****', 'Detroit4', 'email5@com', '6 February 1999', 'great7')
print('\n#8', AddressBoook)


# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"
class Person:
    def __init__(self, name="John", age=36, country="USA"):
        self.name = name
        self.age = age
        self.country = country


print('\n#9.1')
a1 = Person()
a1.age = 88
print(a1.age)


class Person2:
    def __init__(self, name="John", age=36, country="USA"):
        self.name = name
        self.age = age
        self.country = country

    def set_age(self, age2):
        self.age = age2

    def get_person(self):
        return self.name, self.age, self.country


print('\n#9.2')
b2 = Person2()
b2.set_age(44)
print(b2.age)
print(b2.get_person())


# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

class Student:

    def __init__(self, name='Petro', id=0):
        self.name = name
        self.id = id


student = Student()
print('\n#10 Before -', f'name:{student.name}, id:{student.id}')
setattr(student, 'email', 'mail@com')
print('After -', f"email: {student.email}")
setattr(student, 'email', 'gmail@ua')
print('After.getattr - ' + getattr(student, 'email', 'Write by hand'))
