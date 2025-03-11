


Resident_number = input("주민번호를 입력하세요. :")
Resident_number1 = Resident_number.strip()
Resident_number2 = Resident_number.replace("-","")
gender = Resident_number2[6]
gender2 = gender.replace("1", "남자").replace("2", "여자").replace("3", "남자").replace("4", "여자")


print('숫자 갯수 : ', len(Resident_number2))
print(Resident_number2[:6] + "-******")
print('생년월일 : ', Resident_number2[0:2],'년', Resident_number2[2:4],'월', Resident_number2[4:6],'일')
print("성별 : ", gender2)

