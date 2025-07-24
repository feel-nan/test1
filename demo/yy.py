import tkinter as tk
from time import strftime

def update_time():
    # 获取当前时间并格式化
    current_time = strftime('%H:%M:%S %p')
    # 更新标签显示的时间
    clock_label.config(text=current_time)
    # 每隔 1000 毫秒（即 1 秒）调用一次 update_time 函数
    clock_label.after(1000, update_time)

# 创建主窗口
root = tk.Tk()
root.title("数字时钟")

# 创建显示时间的标签
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
clock_label.pack(anchor='center')

# 调用更新时间的函数
update_time()

# 进入主事件循环
root.mainloop()
