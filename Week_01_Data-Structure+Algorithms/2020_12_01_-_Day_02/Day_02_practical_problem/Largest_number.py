'''
가장 큰 수

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
'''

# 다른 사람 풀이 참고함

numbers = [6, 10, 2]   # return "6210"
numbers = [3, 30, 34, 5, 9]   # return "9534330"

def solution(numbers):
    # map() 함수를 사용하여 numbers의 정수형 숫자를 문자열로 변경
    numbers = list(map(str, numbers))

    # 숫자를 문자로 바꾼 후 정렬을 하면
    # index 0부터 차례대로 숫자의 대소를 비교하여 정렬하게 됨
    # ex) 9, 12, 13, 122, 91   =>   91, 9, 13, 122, 12
    # 비교 자릿 수를 맞추기 위해 
    # 각 숫자(문자형으로 치환된)를 늘려서 비교를 해주면(문제에서는 각 원소가 1,000 이하이므로 *3)
    # 일의 자리 수인 index 0 과 다른 길이를 가진 원소들과 비교가 가능하다
    # key 인자를 이용하여 정렬 기준 정해줌
    numbers = sorted(numbers, key = lambda x : x * 3, reverse=True)

    # 리스트 내 모든 원소가 0 일 경우에 
    # 그냥 ''.join()으로 출력하면 '0000 -' 이 되기 때문에
    # 숫자로 변형하여 0으로 만든 후 다시 문자열로 반환
    return str(int(''.join(numbers)))

print(solution(numbers))