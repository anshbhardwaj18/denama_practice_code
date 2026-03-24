# OBJECT ORIENTED PROGRAMMING IN PYTHON.
# QUES-1 BASIC CLASS OR OBJECT.
# CREATE A CAR CLASS WITH ATTRIBUTES LIKE BRAND AND MODEL. THEN CREATE AN INSTANCE OF THIS CLASS.
# class Car:
#     def __init__(self, userbrand, usermodel):
#         self.brand = userbrand
#         self.model = usermodel

# my_car = Car("Range Rover", "Autobiography")
# print(my_car.brand)
# print(my_car.model)
# ******************************************************************************

# QUES-2 CLASS METHOD AND SELF
# ADD A METHOD TO THE CAR CLASS THAT DISPLAYS THE FULL NAME OF THE CAR(BRAND AND MODEL)
# class Car:
#     def __init__(self, userbrand, usermodel):
#         self.brand = userbrand
#         self.model = usermodel
#     def fullname(self):        
#         return f"{self.brand} {self.model}"
# my_car = Car("Rnage Rover", "Autobiography")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())
# *********************************************************************************

# QUES-3 INHERITANCE
# CREATE AN ELECTRIC CAR CLASS THAT INHERITS FROM THE CLASS CAR AND HAS AN ADDITIONAL ATTRIBUTE battery_size
# class Car:
#     def __init__(self, userbrand, usermodel):
#         self.brand = userbrand
#         self.model = usermodel
#     def fullname(self):
#         return f"{self.brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.fullname())
# ********************************************************************************
# QUES-4 ENCAPSULATION
# MODIFY THE CAR CLASS TO ENCAPSULATE THE BRAND ATTRIBUTE, MAKING IT PRIVATE, PROVIDE A BETTER METHOD
# class Car:
#     def __init__(self, userbrand, usermodel):
#         self.__brand = userbrand
#         self.model = usermodel
#     def get_brand(self):
#         return self.__brand + " !"
#     def set_brand(self, userbrand):
#          self.__brand = userbrand
#          return self.__brand
#     def fullname(self):
#         return f"{self.__brand}"
# class Aeroplane(Car):
#     pass
# class ElectricCar(Aeroplane):
#     def __init__(b, brand, model):
#         super().__init__(brand, model)
#         b.battery_size = "20KWH"
#         # return battery_size

# my_tesla = ElectricCar("Tesla", "Model S")
# # print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.set_brand("Wagonar")) 
# print(my_tesla.battery_size)
# *********************************************************************************

# QUES-5 POLYMORPHISM
# DEMONSTRATE POLYMORPHISM BY DEFINING A METHOD FUEL_TYPE IN BOTH CAR AND ELECTRIC CAR CLASSES, BUT WITH VARIABLE BEHAVIOUR
# class Car:
#     def __init__(self, userbrand, usermodel):
#         self.__brand = userbrand
#         self.model = usermodel

#     def get_brand(self):
#         return self.__brand + " !"
    
#     def fullname(self):
#         return f"{self.__brand} {self.model}"
    
#     def fuel_type(self):
#         return "Petrol or Deisel"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# # print(my_tesla.model)
# print(my_tesla.fuel_type())
# safari = Car("Tata", "Safari")
# print(safari.fuel_type())

# QUES-6 CLASS VARIABLE
# ADD A CLASS VARIABLE TO CAR THAT KEEPS TRACK OF THE NUMBER OF CARS CREATED
# class Car:
#     total_car = 0
#     def __init__(self, userbrand, usermodel):
#         self.__brand = userbrand
#         self.model = usermodel
#         Car.total_car += 1
#     def get_brand(self):
#         return self.__brand + " !"
#     def fullname(self):
#         return f"{self.__brand} {self.model}"
#     def fuel_type(self):
#         return "Petrol or Deisel"
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#     def fuel_type(self):
#         return "Electric Charge"
# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# safari = Car("Tata", "Safari")
# safariThree = Car("Tata", "Nexon")
# print(Car.total_car)
# ************************************************************************
# QUES-7 STATIC METHOD
# ADD A STATIC METHOD TO THE CAR CLASS THAT RETURNS A GENERAL DISCRIPTION OF A CAR.
class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel
        Car.total_car += 1
    def get_car(self):
        return self.__brand + " !"
    def fullname(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Deisel"
    @staticmethod
    def general_discription():
        return "Car is means of transport"
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
my_car = Car("Tata", "Safari")
# print(my_car.general_discription())
print(Car.general_discription())
# ***************************************************************************
# QUES-8 PROPERTY DECORATERS
# USE A PROPERTY DECORATER IN THE CAR CLASS TO MAKE THE MODEL ATTRIBUTE READ-ONLY
# class Car:
#     total_car = 0
#     def __init__(self, userbrand, usermodel):
#         self.__brand = userbrand
#         self.__model = usermodel
#         Car.total_car += 1
#     def get_car(self):
#         return self.__brand + " !"
#     def full_name(self):
#         return f"{self.brand} {self.__model}"
#     def fuel_type(self):
#         return "Petrol or Deisel"
#     @staticmethod
#     def general_discription():
#         return "Car is means of transport"
#     @property
#     def model(self):
#         return self.__model
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#     def fuel_type(self):
#         return "Electric Charge"
# my_car = Car("Tata", "Safari")
# print(my_car.model)
# **********************************************************************

# QUES-9 CLASS INHERITANCE AND ISINSTANCE() FUNCTION
# DEMONSTRATE THE USE OF ISINSTANCE() TO CHECK IF my_tesla IS AN INSTANCE OF Car AND ElectricCar
# class Car:
#     def __init__(self, userbrand, usermodel):
#         self.__brand = userbrand
#         self.__model = usermodel
#     def get_car(self):
#         return self.__brand + " !"
#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
#     def fuel_type(self):
#         return "Petrol or Deisel"
#     @staticmethod
#     def general_discription():
#         return "Car is means of transport"
#     @property
#     def model(self):
#         return self.__model
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#     def fuel_type(self):
#         return "Electric Charge"
# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# ************************************************************************
# QUES-10 MULTIPLE INHERITANCE
# CREATE TWO CLASSES BATTERY AND ENGINE, AND LET THE ELECTRICCAR CLASS INHERIT FROM BOTH, DEMONSTRATING MULTIPKE INHERITANCE
class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_car += 1
    def get_car(self):
        return self.__brand + " !"
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "Petrol and Engine"
    @staticmethod
    def general_discription():
        return "Car is means of Transport"
    @property
    def model(self):
        return self.__model
class Battery:
    def battery_info(self):
        return "This is a battery"
class Engine:
    def engine_info(self):
        return "This is a engine"
class ElectricCar(Battery, Engine, Car):
    pass
my_new_tesla = ElectricCar("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())