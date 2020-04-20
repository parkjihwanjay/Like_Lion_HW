Problem='''
과제 1. 별찍기 (4월 24일까지)
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*

과제 2. 구구단 (4월 24일까지)
- 구구단 2단을 출력해보세요!

과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 24일까지)

과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 24일까지)
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

과제 5. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
- 이미지 자율
- 까먹기전에 해주세요~

'''
#Problem1
print("Problem1 \n")
iter_num = 10
for num in range(0,10):
    print("*"*(iter_num-num))
    print("\n")

#Problem2
print("Problem2 \n")
for num in range(1, 10):
    print("2 곱하기 "+str(num)+" 은 "+ str(num*2))
    print("\n")

#Problem3
print("Problem3 \n")
num=1
result =0
while(num<1001):
    if(num%3==0):
        result+=num
    num +=1
print(result)
print("\n")

#Problem4
print("Problem4 \n")
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
Sum_score = 0
for score in mutsa_scores:
    Sum_score += score

average_score = Sum_score/(len(mutsa_scores))
print(average_score)

#Prloblem5
print("Problem5-1 \n")

phonenum = input("전화번호가 무엇인가요?")
phonenum_result = ""
for i in range(0, len(phonenum)):
    try:
        if str(type(int(phonenum[i]))) == "<class 'int'>":
            phonenum_result = phonenum_result + str(phonenum[i])
    except:
        continue
    
print(phonenum_result)
print("\n")

print("Problem5-2 \n")
name = input("이름이 무엇인가요?")
name_array = name.split(" ")
Lastname = name_array[0]
Firstname = name_array[1]

Lastname = Lastname.title()

Firstname = Firstname.title()

print("first name: "+ Lastname +" "+ "First Name"+ Firstname)