import sys
sys.stdin = open('input.txt', 'r')

MAX_LEN = 128

SIZE_TABLE = {
    'BOOL' : 1,
    'SHORT': 2,
    'FLOAT': 4,
    'INT': 8,
    'LONG': 16,
}

def solve(inputs):
    answer = ""
    cnt = 0
    for input in inputs:
        size = SIZE_TABLE[input]
        if size < 8:
            if cnt % size != 0: # 8이하인 애들 첫 시작 처리
                                # short는 2의 배수, float는 4의 배수
                                # short는 2의 배수 자리에서 시작. float는 4의 배수 자리에서 시작.
                for _ in range(size - cnt % size): # size배수로 맞추기
                    answer += '.'
                    cnt += 1
                    if cnt >= MAX_LEN: # 128자리 넘어가면 HALT
                        print("HALT")
                        return
            for i in range(size):
                answer += '#'
                cnt += 1
                if cnt >= MAX_LEN:
                    print("HALT")
                    return
                if cnt % 8 == 0:
                    answer += ','
        else:
            if cnt % 8 != 0:    # 8이상인 애들 첫 시작 처리
                for _ in range(8 - cnt % 8): # 8배수로 맞추기
                    answer += '.'
                    cnt += 1
                    if cnt >= MAX_LEN:
                        print("HALT")
                        return
                    if cnt % 8 == 0:
                        answer += ','
            for i in range(size): # 8이상인 애들 처리
                answer += '#'
                cnt += 1
                if cnt >= MAX_LEN:
                    print("HALT")
                    return
                if cnt % 8 == 0:
                    answer += ','

    if cnt % 8 != 0: # 마지막 8배수로 맞추기
        for _ in range(8 - cnt % 8):
            answer += '.'
            cnt += 1
            if cnt >= MAX_LEN:
                print("HALT")
                return
            
    if answer[-1] == ',': # 마지막 쉼표 제거
        print(answer[:-1])
    else:
        print(answer)

for _ in range(4):
    solve(input().split())