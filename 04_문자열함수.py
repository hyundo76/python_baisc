a = 'happy'
a.count('a')
# 이메일 주소를 입력받습니다. 입력 시 ***@** 형태입니다.
# 입력 받아서 아이다만 출력해 주세요

email_adress = 0
email_adress = str(input("이메일 주소를 입력해줘 (예: ***@**) : ")) 
b = email_adress.find('@')
print("ID : ", email_adress[ :b])

# 이메일 주소를 입력받습니다. 입력 시 ***@** 형태입니다.
# 입력 받아서 아이다만 출력해 주세요.가 내 임무다.
#이메일 주소를 받을 변수를 설정한다.
#변수 이름을 email_address로 설정한다.
#해당 변수에 이메일 주소를 요청한다.
#이메일주소를 문자열로 받는다.
#이메일 주소 중 아이디로 나눌 수 있는 지점을 확인한다.
#@의 위치를 파악한다.
#해당 위치를 변수로 설정한다.
#@의 뒷 부분을 제외한 앞부분을 슬라이싱을 통해 뽑는다.
#슬라이싱한 값을 print를 통해 표현한다.

email = input('메일 주소 입력해 >>')
print('값은 5~20 범위에서',len(email))
print('값은 1이 나와야 됨', email.count('@'))
index = email.index('@')
data = email[:index]
print(data)


#주민등록 번호를 입력받아서 다음을 출력해줍니다.
#  성별(남자, 여자)출력
#  생년월일(00년 2월 1일생)
#  뒤자리 숫자를 첫 글자는 그대로 나머지는 *로 변경해서 출력
#  입력 시 글자 앞, 뒤로 공백이 포함될 수 있다. 공백에 대한 처리도 해야함.

# 주민번호를 받을 변수(Resident number)를 생성
# 받은 변수의 앞 뒤 공백 및 -를 제거하고, 13자리를 확인
#  13자리가 맞는 지 확인한다.

Resident_number = input("주민번호를 입력하세요. :")
Resident_number1 = Resident_number.strip()
Resident_number2 = Resident_number.replace("-","")
gender = Resident_number2[6]
gender2 = gender.replace("1", "남자").replace("2", "여자").replace("3", "남자").replace("4", "여자").replace(gender, "알 수 없음")


print('숫자 갯수 : ', len(Resident_number2))
print(Resident_number2[:6] + "-******")
print('생년월일 : ', Resident_number2[0],Resident_number2[1],'년', Resident_number2[2],Resident_number2[3],'월', Resident_number2[4],Resident_number2[5],'일')
print("성별 : ", gender2)



