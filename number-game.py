
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

root.mainloop()

