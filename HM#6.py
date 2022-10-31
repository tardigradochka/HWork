#
# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
# Example:
class FibonacciNumbers:
    def __init__(self, quantity):
        self.qty = quantity
        self.number = 0
        self.number2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.number3 = self.number2 + self.number
            self.number = self.number2
            self.number2 = self.number2 + 1 if self.number2 == 0 else self.number3

            self.qty -= 1
            return self.number
        else:
            raise StopIteration

for i in FibonacciNumbers(10):
    print(i)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
#
# 2.* Implement generator for Fibonacci numbers
def fibo(count):
    num = 0
    num2 = 0
    while count > 0:
        num3 = num + num2
        num = num2
        num2 = num3 if num2 != 0 else num2 + 1
        count -= 1
        yield num

print('\n#2 IMPLEMENT GENERATOR')
gen_impl = fibo(13)
for elem in gen_impl:
    print(elem)

# 3. Write generator expression that returns square numbers of integers from 0 to 10
gen_expr = (x ** 2 for x in range(11))
print('\n#3 GENERATOR EXPRESSION')
for x in gen_expr:
    print(x)

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import abstractmethod, ABC

class Laptop (ABC):

    @abstractmethod
    def screen(self):
        print('Hello')

    @abstractmethod
    def keyboard(self):
        print('Print')

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError

class HPLaptop(Laptop):

    def __init__(self):
        self.parametrs = {}

    def screen(self):
        return 'Hello'

    def keyboard(self):
        print('Print')

    def touchpad(self):
        print('Touch')

    def webcam(self):
        print('Smile')

    def ports(self):
        print('Open')

    def dynamics(self):
        print('Listen')


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.


class Car (ABC):

    def drive(self):
        print('Drive')

    def stop(self):
        print('Stop')

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError


