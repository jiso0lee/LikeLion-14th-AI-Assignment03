# 3
# numpy.array를 이용하여 패턴 출력 (반복문 사용)
import numpy as np
arr = np.zeros((7,7), dtype = int)
arr[::2, 1::2] = 1
arr[1::2, ::2] = 1

for row in range(7):
    for col in range(7):
        print(arr[row, col], end= "")
    print()