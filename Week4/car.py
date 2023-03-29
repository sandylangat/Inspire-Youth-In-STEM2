class car:
    def __init__ (self,model,make,year_of_manufacture,engine_capacity):
       self.model = model
       self.make = make
       self.year = year_of_manufacture
       self.engine_capacity = engine_capacity



#getters
    def get_model(self):
        return self.model

    def get_make(self):
        return self.make

    def get_year_of_manufacture(self):
        return self.year_of_manufacture

    def get_engine_capacity(self):
        return self.engine_capacity

#setters --> set the atttributes
    def set_model(self,model):
        self.model = model
    def set_make(self,make):
        self.make = make
    def set_year_of_manufacture(self,year_of_manufacture):
        self.year_of_manufacture = year_of_manufacture
    def set_engine_capacity(self,engine_capacity):
        self.engine_capacity = engine_capacity






#objects : instance of the class
car1 = car("demio","nissan",2018,1300)
car2 = car("hilus","toyota",2020,3500)
car3 = car("passat","vw",2009,2600)


car3.set_model(2009)
car2.set_model(2020)
car1.set_model(2018)

print(car1.get_model())
print(car2.get_model())
print(car3.get_model())

print(car1.get_make())
print(car2.get_make())
print(car3.get_make())

print(car1.get_year_of_manufacture())
print(car2.get_year_of_manufacture())
print(car3.get_year_of_manufacture())

print(car1.get_engine_capacity())
print(car2.get_engine_capacity())
print(car3.get_engine_capacity())












