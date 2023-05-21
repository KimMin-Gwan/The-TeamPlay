import tkinter as tk
from tkinter.font import Font

root = tk.Tk()

canvas_width = 300
canvas_height = 200

# Canvas 생성
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

text = "This is a long text that needs to be wrapped to the next line if it exceeds the wrap length."
wraplength = 250  # 한 줄의 최대 너비

# 텍스트 출력
lines = []
current_line = ""
words = text.split()

font = Font(family="Arial", size=20)  # 폰트 설정
for word in words:
    if font.measure(current_line + " " + word) <= wraplength:
        current_line += " " + word
    else:
        lines.append(current_line)
        current_line = word

lines.append(current_line)

y = 50  # 시작 y 좌표
for line in lines:
    canvas.create_text(canvas_width // 2, y, text=line, font=font, anchor=tk.CENTER)
    y += 30  # 줄 간격 조정

root.mainloop()

