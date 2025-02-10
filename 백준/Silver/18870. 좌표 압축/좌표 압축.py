import sys

# ✅ 입력 처리
n = int(input())
coords_data = list(map(int, sys.stdin.readline().split()))

# ✅ 좌표 압축을 위한 딕셔너리 생성 (Key: 좌표 값, Value: 등장 인덱스 리스트)
coord_dic = {}
for index, coord in enumerate(coords_data):
    coord_dic.setdefault(coord, []).append(index)

# ✅ Key(좌표)를 정렬하여 순위 매기기
sorted_coords = sorted(coord_dic.keys())  # ✅ 정렬된 Key 리스트

# ✅ 결과 저장 리스트
result = [0] * n

# ✅ 좌표 순위를 할당
for rank, key in enumerate(sorted_coords):
    for i in coord_dic[key]:
        result[i] = rank  # ✅ 해당 좌표의 원래 위치에 정렬 순위 할당

# ✅ 결과 출력
print(*result)
