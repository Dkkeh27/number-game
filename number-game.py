
# 숫자 맞추기 게임

import tkinter as tk
import tkinter.scrolledtext as tkst
import random

# 윈도우 생성
root = tk.Tk()

# 윈도우 창 설정
root.title    ("숫자 맞추기 게임")  # 윈도우 타이틀
root.geometry ("700x620+100+100")   # 해상도 700x620
root.config   (bg="lavender")       # 배경 색
root.resizable(False, False)        # 윈도우 크기 고정


# 전역변수
cnt      = 0   # 시도 횟수
r_num    = 0   # 랜덤 숫자
user_num = 0   # 유저 숫자
rank     = 0   # 기록 순서
MIN      = 0   # 최솟값
MAX      = 0   # 최댓값


#------  함수 선언부  ------#

#위젯 상태 변경1 (게임 시작 시)
def set_widget_state1():
    radio_easy.config   (state="disabled")  # 난이도 쉬움    비활성화
    radio_normal.config (state="disabled")  # 난이도 보통    비활성화
    radio_hard.config   (state="disabled")  # 난이도 어려움  비활성화
    tk_start.config     (state="disabled")  # 시작버튼       비활성화
    tk_entry.config     (state="normal")    # 입력창         활성화
    tk_input.config     (state="normal")    # 입력버튼       활성화
    tk_cancel.config    (state="normal")    # 지우기버튼     활성화
    tk_hint.config      (state="normal")    # 힌트버튼       활성화
    tk_count.config     (text=f"시도 횟수: {cnt}")

#위젯 상태 변경2 (게임 종료 시) (위젯 상태 변경1의 반대인 함수)
def set_widget_state2():
    radio_easy.config   (state="normal")    # 난이도 쉬움    활성화
    radio_normal.config (state="normal")    # 난이도 보통    활성화
    radio_hard.config   (state="normal")    # 난이도 어려움  활성화
    tk_start.config     (state="normal")    # 시작버튼       활성화
    tk_entry.config     (state="disabled")  # 입력창         비활성화
    tk_input.config     (state="disabled")  # 입력버튼       비활성화
    tk_cancel.config    (state="disabled")  # 지우기버튼     비활성화
    tk_hint.config      (state="disabled")  # 힌트버튼       비활성화

# 시도횟수 증가 후 출력
def count_up():
    global cnt
    cnt = cnt + 1
    tk_count.config(text=f"시도 횟수: {cnt}")  # .config : 위젯 수정

# 랜덤 숫자 생성
def set_random(mode_num):
    if mode_num == 1:
        n = random.randint(1, 49)   # 난이도 쉬움이면   1 ~ 49 난수 생성
    if mode_num == 2:
        n = random.randint(1, 99)   # 난이도 보통이면   1 ~ 99 난수 생성
    elif mode_num == 3:
        n = random.randint(1, 999)  # 난이도 어려움이면 1 ~ 999 난수 생성
    return n

# 범위창에 범위 출력
def set_tk_range():
    pass

# 로그창에 텍스트 출력 (print 함수와 동일한 기능)
def print_tk_log():
    pass

# 레코드(기록창)에 텍스트 출력
def print_tk_record():
    pass

# 입력창 비우기
def clear_tk_entry():
    pass

# 로그창 비우기
def clear_tk_log():
    pass

# 입력버튼이 클릭됐을 때
def clicked_tk_input():
    pass

# 시작하기버튼이 클릭됐을 때
def clicked_tk_start():
    pass

# 힌트버튼이 클릭됐을 때
def clicked_tk_hint():
    pass


# 학번 이름 표시 레이블 (프레임 없음)
label_name = tk.Label(root, text="학번: 20222237, 이름: 김지민", width=0, height=0, \
                        fg="black", bg="white", relief="solid", font=("Arial", 25))
label_name.pack(pady=16) 


# 메인 프레임 생성
frame_main = tk.Frame(root, width=680, height=540, relief="solid", bd=1)
frame_main.pack()

# 게임 소개 레이블 (in 메인프레임)
label_info = tk.Label(frame_main, text="숫자 맞추기 게임에 오신 것을 환영합니다.", \
                        width=0, height=0, fg="blue", font=("Arial", 18))
label_info.place(x=130, y=15)

# 서브 프레임 생성 (in 메인프레임)
frame_sub = tk.Frame(frame_main, relief="solid", bd=0)
frame_sub.place(x=10, y=60)

# 난이도 선택 프레임, 버튼 생성 (in 서브프레임)
frame_level  = tk.LabelFrame(frame_sub, text="난이도")

mode_var     = tk.IntVar() # 라디오 버튼 값
radio_easy   = tk.Radiobutton(frame_level, text="쉬움",   width=6, value=1, variable=mode_var) # 쉬움 모드 값   == 1
radio_normal = tk.Radiobutton(frame_level, text="보통",   width=6, value=2, variable=mode_var) # 보통 모드 값   == 2
radio_hard   = tk.Radiobutton(frame_level, text="어려움", width=6, value=3, variable=mode_var) # 어려움 모드 값 == 3

radio_easy.deselect()           #쉬움   체크해제
radio_normal.select()           #보통   체크
radio_hard.deselect()           #어려움 체크해제

radio_easy.pack  (side="left")  #왼쪽 정렬
radio_normal.pack(side="left")
radio_hard.pack  (side="left")

# 위젯 생성 (입력창, 입력버튼, 지우기버튼, 기록창, 시작하기버튼, 힌트버튼, 횟수창, 범위창, 로그창) (in 서브프레임)
tk_entry  = tk.Entry          (frame_sub, width=30, state="disabled")
tk_input  = tk.Button         (frame_sub, text="입력",     overrelief="solid", width=8,  command=lambda: clicked_tk_input(mode_var.get()), state="disabled")
tk_cancel = tk.Button         (frame_sub, text="지우기",   overrelief="solid", width=8,  command=clear_tk_entry,   state="disabled")
tk_record = tkst.ScrolledText (frame_sub, width=29, height=22, font=("Arial", 12), state="disabled")
tk_start  = tk.Button         (frame_sub, text="시작하기", overrelief="solid", width=40, command=lambda: clicked_tk_start(mode_var.get()))
tk_hint   = tk.Button         (frame_sub, text="힌트",     overrelief="solid", width=8,  command=clicked_tk_hint,  state="disabled")
tk_count  = tk.Label          (frame_sub, text="", width=23, height=0, fg="black", bg="white", font=("Arial", 12))
tk_range  = tk.Label          (frame_sub, text="", width=15, height=0, fg="black", bg="white", font=("Arial", 12))
tk_log    = tkst.ScrolledText (frame_sub, width=32, height=15, font=10, state="disabled")

# 행렬 배치
frame_level.grid (row=1, column=1)                                  # 1행   1열
tk_entry.grid    (row=2, column=1, ipady=4, padx=4, pady=5)         # 2행   1열
tk_input.grid    (row=2, column=2, ipady=4, padx=4)                 # 2행   2열
tk_cancel.grid   (row=2, column=3, ipady=4, padx=4)                 # 2행   3열
tk_record.grid   (row=2, column=4, rowspan=4,    ipady=4, padx=6)   # 2~5행 4열
tk_start.grid    (row=3, column=1, columnspan=2, ipady=4, pady=5)   # 3행   1~2열
tk_hint.grid     (row=3, column=3, ipady=4)                         # 3행   3열
tk_count.grid    (row=4, column=1, ipady=4, pady=5)                 # 4행   1열
tk_range.grid    (row=4, column=2, columnspan=2, ipady=4, pady=5)   # 4행   2~3열
tk_log.grid      (row=5, column=1, columnspan=3)                    # 5행   1열


root.mainloop()

