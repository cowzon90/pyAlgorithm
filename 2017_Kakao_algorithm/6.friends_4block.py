# 프렌즈4블록(난이도: 상)
#region Description
# 블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
# 만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.
#
# 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
#
# 만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
#
# 위 초기 배치를 문자로 표시하면 아래와 같다.
# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ
# 각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다
# 입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.
#endregion

#region Input
# 입력 형식
# 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
# 2 ≦ n, m ≦ 30
# board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
#endregion

#region Output
# 출력 형식
# 입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.
#endregion

#region Sample input and output
# 입출력 예제
# m	n	board	answer
# 4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
# 6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
#endregion

def make_board(board:list):

    board_ = []

    for row in board:
        row_ = []
        for char in row:
            row_.append(char)

        board_.append(row_)

    return board_

def find_4block(board:list):

    find_list = []

    for h in range(0, len(board) - 1):
        for w in range(0, len(board[0]) - 1):

            if (board[h][w] == board[h][w+1]) & \
                (board[h][w] == board[h+1][w]) & \
                (board[h+1][w] == board[h+1][w+1]):

                for i in range(h, h + 2):
                    for j in range(w, w + 2):
                        if find_list.__contains__([i,j]):
                            pass
                        else:
                            find_list.append([i,j])

    for item in find_list:
        board[item[0]][item[1]] = ""

    return board

def update_board(board:list):

    h = len(board)
    w = len(board[0])

    for right in range(0, w):
        for up in range(h - 1, -1, -1):

            if board[up][right] != "":
                pass
            else:

                for i in range(up, 0, -1):
                    board[i][right] = board[i+1][right]
                board[0][right] = ""

    return board

board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

board = make_board(board)
print(board)

board = find_4block(board)
print(board)

board = update_board(board)
print(board)