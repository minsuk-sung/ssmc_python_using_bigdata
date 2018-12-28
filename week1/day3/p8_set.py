'''
2. 여러개의 데이터 ( 연속 데이터, 시퀀스 데이터 )
     - 집합 : 
        - 값의 중복 제거시 사용함, 값을 고유(unique)하게 
        - 성향상 list가 더 적합함 그래서 주로 리스트의 구성원의 중복제거시 사용 
        - dict하고는 관련이 좀 떨어짐
'''

a = 'hello world!!'

b = set(a) #  중복은 제거하고 순서는 정렬X
print(b) # {' ', 'w', 'r', 'l', 'o', 'd', 'e', '!', 'h'}

c = list(b) # 중괄호가 대괄호로 바뀜
print(c) # ' ', 'w', 'r', 'l', 'o', 'd', 'e', '!', 'h']

c.sort()
print(c)

####################################################

a = set( [1,3,5,7,9,2,6,5,5] )
b = set( [2,4,6,8,1,5,4,4] )
print(a,b)

# 합집합
print(a.union(b))

# 교집합
print(a.intersection(b))

# 차집합 -> 어디에서 빼느냐가 중요해서 방향이 중요함
print(a.difference(b)) # a - b
print(b.difference(a)) # b - a

# 나중에는 Numpy,Pandas와 같은 라이브러리가 더 성능이 좋아서 내장함수는 안 쓰게 될 것
