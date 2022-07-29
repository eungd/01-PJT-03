import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())


for x in range(T) :
    N = int(input())
    earnings = input().split()
    earnings_ = map(int, earnings)
    earning = list(earnings_) #소득에 대해 리스트로 형변환
    mean = sum(earning) / len(earning)

    under_average = [] # 평균보다 적은 사람 리스트 초기화

    for i in range(N):
        if earning[i] <= mean :
            result = under_average.append(earning[i]) #입력마다 평균보다 적은 사람들 리스트 쌓기 
    
    number = len(under_average) # 평균보다 적은 사람들 수
    print(f'#{x+1} {number}')