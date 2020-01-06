N, M = input().split()
N = int(N) # 행
M = int(M) # 열

board = [[0]*M for i in range(N)]

for k in range(N):
        board[k]= input()


min = 1000000



for start_row in range(N-7): 

    for start_col in range(M-7):
        cnt = 0 

        init_str = board[start_row][start_col]

        if init_str == 'B':
            base1 = "BWBWBWBW"
            base2 = "WBWBWBWB"
        else:
            base1 = "WBWBWBWB"
            base2 = "BWBWBWBW"

        for row in range(start_row, start_row+8): # row 8개
            if row == 0 or row % 2 == 0 : # row가 짝수(0포함)

                sample = board[row][start_col:start_col+8] # 해당하는 row 문자열을 뽑아냄.

                # 문자열 간 비교
                for index in range(8):
                    if sample[index] != base1[index]:
                        cnt +=1

            else: # row가 홀수
                sample = board[row][start_col:start_col + 8]  # row당 col 8개

                # 문자열 간 비교
                for index in range(8):
                    if sample[index] != base2[index]:
                        cnt += 1

        if cnt < min:
            min = cnt


print(min)




