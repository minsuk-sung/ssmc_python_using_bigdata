'''
2. 여러개의 데이터 ( 연속 데이터, 시퀀스 데이터 )
     - 리스트 : []
        - 순서가 존재
        - 인덱스가 존재(0,1,2,...)
        - 값의 중복허용
'''
nums = None # None : 값이 없다

nums = [] # 이렇게만 해도 리스트 생성 
print(nums, type(nums),len(nums))

# 리스트 객체 생성
# 동적으로 생성되는 방식
# 반복 작업시 안정적인 방식임 
nums = list() # 새로운걸 만들어서 쓰고 싶다면 이렇게 해야함
print(nums, type(nums),len(nums)) # 위와 동일한 결과가 나옴

#10이하 양의 홀수 정수들의 리스트 생성
nums = [1,3,5,7,9]
print(nums, type(nums),len(nums))

anis = ['dog','cat','bird']
print(anis, type(anis),len(anis))

# list의 구성원들의 타입도 동일해야하는가? (X)
# 어차피 파이썬의 모든 건 객체이기 때문에 상관없음
ext = [1,2,4,'dog','cat']
print(ext,type(ext),len(ext)) 

# 차원이 달라지면
nums = [1,3,5,7,9,[1,2,3]]
print(nums, type(nums),len(nums)) # 다른 차원이 섞여 있어도 어차피 객체이기 때문에

#######################################################################

# indexing : 변수명[인덱스]
# 기존에 하던것과 동일하게 하면 된다 
# nums 리스트에 7 값을 출력하시오
print(nums[3])
# nums 리스트에서 2값을 출력하시오
print(nums[-1]) # 여기서 결과값은 리스트인데
print(nums[-1][1]) # 차원이 줄었음...2차원에서 1차원으로...백터에서 스칼라로...

#######################################################################

# slicing : 변수명[시작인덱스 : 끝인덱스 : 스텝]
nums = [1,3,5,7,9]
# 3,5,7만 획득한 리스트를 출력
print( nums[1:4] )
# 어차피 원본은 그대로 보존됨
print(nums[1:-1])
print(nums[:])

# 구성원 1을 2로 변경하고 싶을때? 원본 수정
nums[0] = 2
print(nums)

# 범위를 변경하고 싶을때
nums[1:-1] = 'A'
print(nums) # 3개의 범위가 단일값으로 변경됨, 범위값을 대입하는 값을 치환됨 ( 갯수가 줄어들수도 있음)

# 삭제
nums = [1,3,5,7,9]
print(nums)
# 0번째 데이터를 삭제할때 -> 참조를 하지 않게 함
# 인덱스의 변화를 일으킴 + 원본도 변경됨
del nums[0]
print(nums)
# 범위 삭제
del nums[:2]
print(nums)
# 값이 일치하면 삭제
nums.remove(7) 
print(nums)
# 싹다 날리고 싶을 경우 clear()를 사용함
nums.clear()
print(nums)

# 추가
nums.append(100)
print(nums)
nums.append([1,2]) # 무조건 늘리는거, 걍 추가할 내용을 한덩어리로 보고 덩어리째 구성원으로
print(nums)
nums.extend([3,4]) # 확장성, 구조를 유지하면서 list의 구성원으로 넣어버리는거
print(nums)

# 정렬 => 원본 변경됨 ( 엥간하면 사본에서 정렬하는게 유리할 수 있음 ) 
nums = [23,2,32,4,546,576,6,45434,34,87,4665,34536,34433,8976,56]
nums.sort() # 아무것도 없으면 오름차순으로 정렬
print(nums)
nums.sort(reverse = True) # True는 첫글자 대문자 조심, 내림차순으로 정렬
print(nums)

#######################################################################