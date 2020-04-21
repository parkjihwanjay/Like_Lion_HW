#Question1
def deter_oddeven(number):
    number = int(number)
    if number%2 ==0:
        print("even number")
        return "even number"
    else :
        print("odd number")
        return "odd number"

deter_oddeven(1)
deter_oddeven(2)

#Question2
def gugudan_even():
    for i1 in (2,4,6,8):
        for i2 in range(1, 10):
            print("%d * %d = %d" %(i1, i2,i1*i2))
    return

def gugudan_odd():
    for i1 in (1,3,5,7,9):
        for i2 in range(1,10):
            print("%d * %d = %d" %(i1, i2,i1*i2))
    return

def oddevenmultip(number):
    number = int(number)
    if number%2 ==1:
        gugudan_odd() 
    else :
        gugudan_even()
    return
    
oddevenmultip(1)
oddevenmultip(2)



#Question3

def Question3(num):
    
    i=1
    while (i<=num):
        for i2 in range(1, 10):
            print("%d 곱하기 %d = %d" %(i,i2, i*i2 ))
        i+=1
        
Question3(int(input("숫자를 넣어주세요!")))