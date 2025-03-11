## 명함 관리 프로그램 작성
# 1. 명함입력, 2. 명함수정, 3. 명함삭제
# 4. 명함목록보기, 5.종료

display = ('''
-----------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제 4. 명함목록보기, 5.종료
-----------------------------------------------------------
메뉴를 선택하세요 >>> ''')

business_card = []
menu = ''

while True :
    menu = input(display)
    if menu == '1':
        print('(명함입력)')
        print("명함 정보를 입력하세요:")
        name = input("이름: ")
        phone = input("전화번호: ")
        belong = input("소속 : ")

        card = [name,phone,belong]
        business_card.append(card)
        print(f"{name}님의 명함이 입력되었습니다.")
        print(card)

    elif menu == '2':
        print('명함수정')
        Q1 = input('수정할 명함이 있습니까? (Y / N)')
        if Q1 == 'Y' :
            name1 = input("수정할 사람의 이름을 입력하시오.")
            if name1 in name_card in business_card : 
                found = name_card.index(name1)
                email_card[found] = input('새 이메일 :')
                phone_card[found] = input('새 전화번호 :')
                belong_card[found] = input('새 소속 :')
                print(f"'{name}'님의 명함이 수정되었습니다.")
                print(name_card[found], email_card[found], phone_card[found], belong_card[found])
            else : 
                print("해당 이름의 명함을 찾을 수 없습니다.")
    elif menu == '3':
        print('명함삭제')
        if not business_card :
            print("삭제할 명함이 없습니다.")
        else :
             remove_name = input('삭제할 명함 이름을 입력하시오')
             
             for i in range(len(business_card)) :
                if business_card[i][0] == remove_name :
                    index = i
                    print(f"'{remove_name}'님의 명함을 삭제하시겠습니까? ")
                    answer = input("예 / 아니요 ")
                    if answer == '예' :
                        del business_card[index]
                        print(f"'{remove_name}'님의 명함이 삭제되었습니다.")
                    else :
                        print("삭제를 취소합니다.")
                break
             print("해당 이름의 명함을 찾을 수 없습니다.")
    elif menu == '4':
        print('명함목록보기')

    elif menu == '5':
        print('프로그램 종료')
        break
    else :
        print('메뉴선택을 잘못함.')