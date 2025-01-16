# Text to Speech Python Project

Dự án này cho phép tạo âm thanh từ văn bản bằng tiếng Việt sử dụng thư viện `gTTS` và `pygame`.

## Yêu cầu

Để chạy dự án này, bạn cần cài đặt các thư viện sau:

-   Python 3.x
-   gTTS
-   pygame

## Cài đặt

Thực hiện các bước sau để cài đặt và chạy dự án:

1. **Cài đặt Python**: Đảm bảo bạn đã cài đặt Python 3.x. Nếu chưa, tải và cài đặt từ [Python.org](https://www.python.org/downloads/).

2. **Tạo môi trường ảo (tuỳ chọn)**: Để giữ cho các thư viện cài đặt không xung đột với các dự án khác, bạn nên tạo một môi trường ảo.

    ```sh
    python -m venv env
    source env/bin/activate  # Đối với Windows: `env\Scripts\activate`
    ```

3. **Cài đặt các thư viện cần thiết**:
    ```sh
    pip install gTTS pygame
    ```
4. **Chạy ứng dụng**:
    ```sh
    python app.py
    ```

## Sử dụng

Khi chạy ứng dụng, bạn sẽ được yêu cầu nhập số tiền, tên người gửi và tên người nhận. Ứng dụng sẽ tạo âm thanh từ thông tin bạn cung cấp.
