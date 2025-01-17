import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os
import pygame
import time

def speak_message(value, sender, receiver):
    message = f"Đã nhận tiền chuyển khoản {value} từ {sender} đến {receiver}"
    tts = gTTS(text=message, lang='vi')
    temp_audio_file = "temp_audio.mp3"
    tts.save(temp_audio_file)
    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    time.sleep(1)
    os.remove(temp_audio_file)

def submit():
    value = value_entry.get()
    sender = sender_entry.get()
    receiver = receiver_entry.get()
    if not value or not sender or not receiver:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")
    else:
        speak_message(value, sender, receiver)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển khoản thông báo")

# Nhãn và ô nhập cho số tiền
tk.Label(root, text="Số tiền:").grid(row=0, column=0, padx=10, pady=10)
value_entry = tk.Entry(root)
value_entry.grid(row=0, column=1, padx=10, pady=10)

# Nhãn và ô nhập cho người gửi
tk.Label(root, text="Người gửi:").grid(row=1, column=0, padx=10, pady=10)
sender_entry = tk.Entry(root)
sender_entry.grid(row=1, column=1, padx=10, pady=10)

# Nhãn và ô nhập cho người nhận
tk.Label(root, text="Người nhận:").grid(row=2, column=0, padx=10, pady=10)
receiver_entry = tk.Entry(root)
receiver_entry.grid(row=2, column=1, padx=10, pady=10)

# Nút gửi
submit_button = tk.Button(root, text="Gửi", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Căn giữa cửa sổ chính
center_window(root)

# Chạy giao diện
root.mainloop()
