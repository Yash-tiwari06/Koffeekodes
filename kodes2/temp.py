class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def celsius_to_fahrenheit(self, celsius):
        print(celsius * 9/5 + 32)
    
    def fahrenheit_to_celsius(self, fahrenheit):
        print(fahrenheit - 32) * 5/9


temp = Temperature(10)
temp.celsius_to_fahrenheit(10)
temp.fahrenheit_to_celsius(25)