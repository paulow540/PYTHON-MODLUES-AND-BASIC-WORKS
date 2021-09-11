# print("my name is paul")
# name = "paul"
# age = str(12)
# personal_info = name + age 
# print(personal_info)

# personal_info = {"name":"paul","age":12,"price":20000000000000000000000,"weight":55.56,"good":12j}
# print(type(personal_info))
# print(personal_info["name"])

class Motor:
    def __init__(self):
        self.name = "BMW"
        self.call()


    def call(self):
        print(self.name)


class Small_motor(Motor):
    def __init__(self,paul):
        super().__init__()    
        self.smcar("mike")

    def smcar(self,paul):
        print(self.name,paul)
                
# my = Small_motor("paul")
# data typ

# name = dict(name="Tony Johnson", level=300, course="mechanical engineering", subjects=10)
# nam = {"nam":"pa","ag":33}

# print(name)
# print(type(name))
# print(nam)


def callcallcall(hello):
    """this function is telling us how to add two numbers """
    first_number =int(input("Enter a number here>>"))
    second_number = int(input("Enter a number here>>"))
    total = first_number + second_number
   
    print(total)
    print(hello)

# call()












