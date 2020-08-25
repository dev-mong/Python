student_number = 12
#학생의 번호를 출력합니다.
#print(student_number);
#del student_number #변수 삭제 키워드
print('학생번호 : ',student_number)

st_number_str=str(student_number) #문자여롤 변경해주느 형 변환 함수  str()

print(type(student_number)) #변수의 타입 확인
print(type(st_number_str)) #변수 타입 확인

number_list1=range(10) #0~9까지의 숫자 리스트 반환
number_list2=range(5,10) #5~9 까지의 숫자 리스트 반환
number_list3=range(0,10,2) #0~9 까지의 짝수 숫자 리스트 반환

print('number_list1 : ',number_list1)
print('number_list2 : ',number_list2)
print('number_list3 : ',number_list3)

#리스트 출력
for i in number_list3:
    print(i)

a=1
b='1'
c=1.0
d=[1]
print(type(d))