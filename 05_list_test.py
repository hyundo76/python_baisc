a = [1, 2, 3, ['a', 'b',[1,3,5],'c']]
print(a)
print(type(a))
print(a[0])
print(a[3][1])

#3, 5리스트 도출
print(a[3][2][1:])

jumin = '000212-4111111'
print(jumin.split())

# 리스트 지우기
del a[3]
print(a)

# a 리스트 전체 다 삭제
del a
print(a)

# 리스트에 요소 추가 - append
a = [1,2,3]
a.append('qqq')
print(a)

# append는 뒤에 붙이고 insert는 원하는 위치에 붙일 수 있음.
a.insert(0,'aaa')
print(a)

a = [1,4,3,2]
a.reverse()
print(a)

a.pop(a.index('2'))