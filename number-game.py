
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



root.mainloop()

