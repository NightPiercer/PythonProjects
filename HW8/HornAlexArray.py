Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> cars = ["Ford", "Chrysler", "Dodge", "Ram", "Jeep", "Chevy", "Gmc"]
>>> print(cars)
['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'Gmc']
>>> len(cars)
7
>>> cars.append("Buick")
>>> print(cars)
['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'Gmc', 'Buick']
>>> cars[4]
'Jeep'
>>> cars[3] = "Toyota"
>>> print(cars)
['Ford', 'Chrysler', 'Dodge', 'Toyota', 'Jeep', 'Chevy', 'Gmc', 'Buick']
>>> cars.pop(4)
'Jeep'
>>> print(cars)
['Ford', 'Chrysler', 'Dodge', 'Toyota', 'Chevy', 'Gmc', 'Buick']
>>> cars.sort()
>>> print(cars)
['Buick', 'Chevy', 'Chrysler', 'Dodge', 'Ford', 'Gmc', 'Toyota']
>>> cars.reverse()
>>> print(cars)
['Toyota', 'Gmc', 'Ford', 'Dodge', 'Chrysler', 'Chevy', 'Buick']
>>> carslength = len(cars)
>>> print(carslength)
7
>>> print("My array is " + str(carslength) + " elements long.")
My array is 7 elements long.