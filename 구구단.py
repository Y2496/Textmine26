# 구구단 함수
def gugudan (dan):
    print(f'[구구단{dan}단]')
    for i in range(1,10):
        print(1)

# 정수형 List의 총 합 구하기.
numlist = [1, 43, 25, 33]
def getsum(numlist):
    sum = 0
    for num in numlist :
        sum += num
        return sum

    sum = getsum(numlist)
    print(sum)


    numlist = list(map(int,input("총 합을 구할 숫자 목록 : ").split()))
sum = getsum(numlist)
print(sum)

# Local -> Global -> built-in
str1 = '전역 변수'
len = 5
lenghh = len(str1)
print(length)

# 함수의 반환 값을 여러 개로 만들기 -> 실제로는 반환 값은 한 개임.
def add_and_mul(a,b):
    sum = a + b
    mul - a * b
    return sum, Mul

result = add_and_mul(3,4)
print(result)
sum, mul 

sum, _ = add_and_mul(3,4)
print(sum)
(7,12)
7,12
7

# 입력된 N까지의 정수를 합하는 함수
def sum


# Sum(N)을 재귀 함수로 만들기
def sum_recursive(N):
    #base condition
    if N == 1: return 1

    # 재귀적인 분해, 조합
    return sum_recursive(N-1) + N

print(sum_recursive(3))

# Factorial을 Recursive로 계산
def fact_r(N):
    # Base condition
    if N <= 1 : return 1

    #recursive

# BOJ 10870 : 피보나치 수 5
# 피보나치수를 Recursive