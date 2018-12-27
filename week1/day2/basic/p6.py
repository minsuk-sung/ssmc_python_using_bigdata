'''
2. 여러개의 데이터 ( 연속 데이터, 시퀀스 데이터 )
     - 딕셔너리 : {}
        - 순서가 없다
        - 데이터 자체가 키(key):값(value) 의 세트로 구성
        - 오로지 키만으로 구분, 키값은 중복되면 안됨
        - 키에 매칭되는 값은 중복되도 ok => DB 연동해서 Query 수행할때 결과물 ( [딕셔너리,딕셔너리] )
'''
dic = {}
print(dic, type(dic), len(dic))
dic = dict()
print(dic, type(dic), len(dic))

########################################################################

dic = {
    'name' : 'multi',
    'age' : 10
}
print(dic,type(dic),len(dic))
# 'multi'라는 값을 출력하시오
print(dic['name'],dic['age']) # indexing을 할 수 없으니까 대신 이렇게 처리함
# 딕셔너리의 인덱싱은 변수명[키(key)]로 할 수 있다. 순서가 없기 때문에

# 요소 추가
dic[1] = 'hi' # 1이 의미하는건 dict라는 딕셔너리의 키값이 1이고, 값이 'hi'라는 요소를 추가하란 뜻
print(dic)
# 여기서 중요한건 딕셔너리에서 중요한건 키값은 꼭 문자열일 필요가 없음
# 주로 문자열이 편리해서 주로 많이 사용
print(dic[1]) 

# 슬라이싱 -> X
# 뎍서너리는 구조적으로 순서가 없기 때문에 안됨 
# 데이터가 많아지면 키가 어떤 것이 있는지 모를 수도 있음

print(dic.keys()) # 딕셔너리에서 키만 모으는 내장함수 -> 결과는 리스트 형태로 보임
print(dic.values()) # 딕셔너리에서 값만 모으는 내장함수 -> 결과는 리스트 형태로 보임

########################################################################