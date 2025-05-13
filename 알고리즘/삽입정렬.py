datas = [4, 6, 2, 7, 8, 5, 0, 1]

flag = False
c = 1

for i in range(1, len(datas)):
    # j = 현재 위치
    # prev = 이전 위치
    prev = i - 1
    # 현재 위치부터 0번째까지
    for j in range(i, 0, -1):
        # 현재 위치의 데이터가 이전 위치의 데이터보다 크면 교환하지 않음
        # 이전 위치인 prev가 1보다 작으면(데이터 벗어남) 데이터 교환(첫 번째라는 의미)
        if (datas[j] > datas[prev]) or (prev < 0):
            break
        else:
            print(f"{datas[j]}가 {datas[prev]} 보다 작음 데이터 교환")
            print(datas, '=>', end=' ')
            # 만약 현재 데이터가 이전 데이터보다 작으면 데이터 교환
            datas[j], datas[prev] = datas[prev], datas[j]
            print(datas)
            flag = True
        # 다음 데이터 비교를 위해 prev - 1
        prev -= 1
    
    if flag:
        print(f"\n{c}회전: {datas}")
        flag = False
        c += 1