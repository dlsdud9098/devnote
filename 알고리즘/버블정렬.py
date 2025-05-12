datas = [4, 6, 2, 7, 8, 5, 0, 1]

# 0번 부터 시작함
for i in range(len(datas)):
    # (0,1), (1,2), (2,3)... 이런식으로 비교함
    # 다음에 비교 다하면 i + 1되면서
    # (1,2), (2,3), (3,4)... 비교함
    for j in range(1, len(datas)-i):
        # 조건을 만족(이전 위치가 현재 위치보다 크면)하면 위치 변경
        if datas[j-1] > datas[j]:
            print(f"{datas[j-1]} 이(가) {datas[j]} 보다 큼으로 변경")
            print(datas, '=>', end=' ')
            datas[j-1], datas[j] = datas[j], datas[j-1]
            print(datas)
            print()
            
    print(f"{i+1}회전: {datas}")
    print()

# 결과
print(f"결과: {datas}")