#속성, 메소드, 인스턴스, 객체에 대해서 용어 구분 잘하기.

class FourCal:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        self.addcount = 0
        self.subcount = 0
        self.mulcount = 0
        self.divcount = 0

    def add(self, n1, n2):
        self.addcount +=1
        result = n1 + n2
        return result

    def sub(self, n1, n2):
        self.subcount+=1
        result = n1 - n2
        return result
    
    def mul(self, n1, n2):
        self.mulcount+=1
        result = n1*n2
        return result
    
    def div(self, n1, n2):
        self.divcount+=1
        if (n2 == 0):
            print("Error!")
            return None
        result = n1/n2
        return result

    def ShowCount(self):
        print("덧셈: "+ str(self.addcount)+"\n")
        print("뺄셈: "+ str(self.subcount)+ "\n")
        print("곱하기: "+ str(self.mulcount)+ "\n")
        print("나누기: "+ str(self.divcount)+ "\n")

calculator = FourCal("YeongBeom Heo", "26", "Korea University")


print(calculator.add(3,4))
print(calculator.sub(3,4))
print(calculator.mul(3,4))
print(calculator.div(3,4))
print(calculator.ShowCount())
print(calculator.add(3,2))
print(calculator.add(3,2))
print(calculator.ShowCount())


print(calculator.age)
print(calculator.name)
print(calculator.school)


