# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами
# increase_speed, break_speed, mileage_info
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print(f'increase_speed: IDK, but max_speed = {self.max_speed}km/h')

    def break_speed(self):
        pass

    def mileage_info(self):
        print(f'mileage_info:{self.mileage}km')

    # def info(self):
    #     print(f'max:{self.max_speed}, mileage {self.mileage}')


print('#1 class Vehicle:')
car = Vehicle(200, 32000)
car.increase_speed()
car.mileage_info()
#car.info()


# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle
# і матиме власний метод seating_capacity
class Bus(Vehicle):

    def __init__(self, max_speed, mileage, places):
        super().__init__(max_speed, mileage)
        self.place = places

    def seating_capacity(self):
        print(f'number of places:{self.place}')
    # def info(self):
    #     super().info()
    #     self.seating_capacity()


print('\n#2 my Busik:')
myBus = Bus(140, 50000, 30)
myBus.seating_capacity()
myBus.increase_speed()
myBus.mileage_info()
# myBus.info()


# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
print("\n#3 Class 'Bus' is subclass of 'Vehicle'?:", issubclass(Bus, Vehicle))


# 4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
print('\n#4')
school_bus = Bus(160, 32000, places=40)
school_bus.seating_capacity()
school_bus.mileage_info()
print('#4 Object "school_bus" belongs to class "Vehicle": ', isinstance(school_bus, Vehicle))
print('#4 Object "school_bus" belongs to class "Bus":', isinstance(school_bus, Bus))


# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та
# методами school_address, main_subject

class School:

    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self):
        print(f'School in our city with id={self.get_school_id}')

    def main_subject(self):
        pass


# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
class SchoolBus(Bus, School):

    def __init__(self, max_speed, mileage, places, get_school_id, number_of_students):
        super(). __init__(max_speed, mileage, places)
        School.__init__(self, get_school_id, number_of_students)
        #print(self.__class__.__mro__)

    def seating_capacity(self):
        super().seating_capacity()
        print("Nobody should stay")

    def school_address(self):
        super().school_address()
        print('Welcome to School ')

    def bus_school_color(self):
        print('Colour of School Bus - yellow')


print('\n#6 class SchoolBus')
b1 = SchoolBus(90, 18300, 45, '#210', '230tutors')
b1.seating_capacity()
b1.school_address()


# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat.
# Створіть два екземпляри: від Ведмідь і від Вовк,
# створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.
print('\n#7 Polimorfism')

class Bear:

    def eat(self):
        print('Bear eats honey')


class Wolf:

    def eat(self):
        print('Wolf eats meat auf')


WhiteBear = Bear()
WhiteWolf = Wolf()

for predator in (WhiteBear, WhiteWolf):
    predator.eat()


# Магічні методи:
# Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть
# новий екземпляр цього класу, лише коли population > 1500,
# інакше повертається повідомлення: "Your city is too small".
# Підказка: використовуєте для цього завдання магічні методи
class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __gt__(self, population2=1500):
        if self.population > population2:
            return f"City - {self.name} with {self.population} population"
        else:
            return 'Your city is too small'


print('\n#8.1 Magic methods')
gorodok = City('Vishneve', population=8000)
print(gorodok.__gt__())
village = City('Jablukivka', population=1200)
print(village.__gt__())

#Attempt №2
class CityNew:

    def __new__(cls, name: str, pop: int):
        if pop < 1500:
            return RuntimeError, "City is too small"
        else:
            instance = super().__new__(cls)
            return instance

    def __init__(self, name, pop):
        self.name = name
        self.pop = pop
        print ("City -", name, pop)


print('\n#8.2 Magic methods:')
Gorod = CityNew('Izjum', 5000)
print(Gorod)
Negorod = CityNew('Grusheve', 1200)
print("\nCe City?", Negorod)





