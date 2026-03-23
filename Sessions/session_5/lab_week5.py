# # Exercise 1 Task 1: Simple Inheritance

# class Vehicle:
#     def __init__(self, colour, weight, max_speed, form_factor):
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed
#         self.form_factor = form_factor

#     def move(self):
#         print(f"The Car is driving at {self.max_speed} km/h")

# car = Vehicle("Red", 1500, 200, "Toyota")
# car.move()

# # Exercise 2 TAsk 1: Super() function

# class Vehicle:
#     def __init__(self, colour, weight, max_speed, form_factor):
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed
#         self.form_factor = form_factor

#     def move(self):
#         print(f"The vehicle is driving at {self.max_speed} km/h")


# class Car(Vehicle):
#     def __init__(self, colour, weight, max_speed, form_factor):
#         super().__init__(colour, weight, max_speed, form_factor)

#     def move(self):
#         print(f"The car is driving at {self.max_speed} km/h")


# class Electric(Car):
#     def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, max_range):
#         super().__init__(colour, weight, max_speed, form_factor)
#         self.battery_capacity = battery_capacity
#         self.max_range = max_range

#     def move(self, speed):
#         print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")


# class Petrol(Car):
#     def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, max_range):
#         super().__init__(colour, weight, max_speed, form_factor)
#         self.fuel_capacity = fuel_capacity
#         self.max_range = max_range

#     def move(self, speed):
#         print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km")


# electric_car = Electric("Blue", 1800, 250, "Tesla", 100, 100)
# electric_car.move(110)

# petrol_car = Petrol("Red", 2000, 200, "Ford", 60, 650)
# petrol_car.move(180)


# # Exercise 3 : **kwargs

# class Vehicle:
#     def __init__(self, colour, weight, max_speed, form_factor):
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed
#         self.form_factor = form_factor

#     def move(self):
#         print(f"The vehicle is driving at {self.max_speed} km/h")

# class Plane(Vehicle):
#     def __init__(self, wingspan, **kwargs):
#         super().__init__(**kwargs)
#         self.wingspan = wingspan

#     def move(self):
#         print(f"The plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters")

# class Propeller(Plane):
#     def __init__(self, propeller_diameter, **kwargs):
#         super().__init__(**kwargs)
#         self.propeller_diameter = propeller_diameter

#     def move(self):
#         print(f"The propeller plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters and a propeller diameter of {self.propeller_diameter} meters")

# class Jet(Plane):
#     def __init__(self, jet_engine_thrust, **kwargs):
#         super().__init__(**kwargs)
#         self.jet_engine_thrust = jet_engine_thrust

#     def move(self):
#         print(f"The jet plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters and a jet engine thrust of {self.jet_engine_thrust} kN")

# propeller_plane = Propeller(wingspan=30, propeller_diameter=5, colour="White", weight=5000, max_speed=300, form_factor="Boeing")
# propeller_plane.move()

# jet_plane = Jet(wingspan=35, jet_engine_thrust=200, colour="Silver", weight=8000, max_speed=900, form_factor="Airbus")
# jet_plane.move()


# # Multiple Inheritance

# class Vehicle:
#     def __init__(self, colour, weight, max_speed, form_factor, **kwargs):
#         self.colour = colour
#         self.weight = weight
#         self.max_speed = max_speed
#         self.form_factor = form_factor

#         for key, value in kwargs.items():
#             setattr(self, key, value)

#     def move(self):
#         print(f"The vehicle is moving at {self.max_speed} km/h")

# class Car(Vehicle):
#     def __init__(self, colour, weight, max_speed, form_factor, **kwargs):
#         super().__init__(colour=colour, weight=weight, max_speed=max_speed, form_factor=form_factor, **kwargs)

#     def move(self):
#         print(f"The car is driving at {self.max_speed} km/h")

# class Plane(Vehicle):
#     def __init__(self, wingspan, **kwargs):
#         super().__init__(**kwargs)
#         self.wingspan = wingspan

#     def move(self):
#         print(f"The plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters")

# class FlyingCar(Car, Plane):
#     def __init__(self, colour, weight, max_speed, form_factor, wingspan, **kwargs):
#         super().__init__(colour=colour, weight=weight, max_speed=max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)

#     def move(self, speed):
#         print(f"The flying car is moving at {speed} km/h with a wingspan of {self.wingspan} meters")
        
# flying_car = FlyingCar(colour="Red", weight=1500, max_speed=200, form_factor="Futuristic", wingspan=20)
# flying_car.move(100)


# Exercise : Polymorphism 

class Animal:
    def move(self):
        print("The animal is moving")

class Dog(Animal):
    def move(self):
        print("The dog is running")

class Bird(Animal):
    def move(self):
        print("The bird is flying")

class Fish(Animal):
    def move(self):
        print("The fish is swimming")

animals = [Animal(), Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()


