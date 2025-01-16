from gtts import gTTS
import os
import pygame
import time

def speak_message(value, sender, receiver):
    # Nội dung câu cần đọc
    message = f"Đã nhận tiền chuyển khoản {value} từ {sender} đến {receiver}"

    # Tạo giọng nói tiếng Việt
    tts = gTTS(text=message, lang='vi')

    # Đặt tên file tạm thời
    temp_audio_file = "temp_audio.mp3"

    # Lưu giọng nói vào file tạm thời
    tts.save(temp_audio_file)

    # Phát âm thanh trực tiếp từ file
    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_file)
    pygame.mixer.music.play()

    # Đợi cho âm thanh kết thúc
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Thêm một chút thời gian chờ để phát âm thanh

    # Dừng âm thanh và bộ trộn sau khi phát xong
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # Đợi một khoảng thời gian ngắn để chắc chắn âm thanh đã kết thúc trước khi xóa file
    time.sleep(1)  # Chờ 1 giây trước khi xóa

    # Xóa file tạm sau khi phát xong
    os.remove(temp_audio_file)

if __name__ == "__main__":
    # Nhập các tham số từ người dùng
    value = input("Nhập số tiền: ")
    sender = input("Nhập tên người gửi: ")
    receiver = input("Nhập tên người nhận: ")

    # Gọi hàm đọc giọng nói
    speak_message(value, sender, receiver)
