# MorphAI — Lập lịch một ngày ở khu vui chơi

Prototype lập lịch dựa trên nhóm đi, khung giờ, ngân sách và sở thích. Model trích xuất yêu cầu và đề xuất hoạt động; code kiểm tra lịch, ràng buộc nhóm và tự tính tổng chi phí.

## Yêu cầu

- Python 3.10 trở lên (khuyến nghị).
- Không cần cài thêm package.
- API key OpenAI để chạy model thật. Không có key, ứng dụng chạy chế độ giả (token bằng 0); không tính lượt giả là kết quả đánh giá model.

## Cài đặt và chạy

1. Tạo `.env` từ `.env.example`:

   ```powershell
   Copy-Item .env.example .env
   ```

2. Điền cấu hình trong `.env` (không dùng dấu ngoặc kép):

   ```text
   MODEL_PROVIDER=openai
   MODEL_NAME=gpt-4o-mini
   API_KEY=<API key của nhóm>
   ```

3. Chạy ứng dụng:

   ```powershell
   python run.py
   ```

   Kiểm tra API và token: `python run.py eval --try`. Kiểm tra bộ benchmark: `python run.py check`. Chạy test: `python -m unittest discover -s tests -p "test_*.py"`.

`.env` được `.gitignore` loại trừ. Không commit, gửi lên chat hoặc đưa API key vào ảnh chụp. Hướng dẫn nối model: [docs/connect-model.md](docs/connect-model.md).

## Cách nhập yêu cầu

Gửi đủ thông tin trong cùng một tin nhắn; có thể viết thành nhiều câu. Agent cần tên khu, ngày đi, ngân sách, khung giờ, tuổi và chiều cao của từng người. Sở thích là tùy chọn. Nếu thiếu thông tin, agent sẽ hỏi lại; agent hiện không nhớ dữ liệu giữa các tin nhắn, vì vậy hãy gửi lại đủ yêu cầu khi bổ sung.

Ví dụ:

> Gia đình có 2 người lớn: 32 tuổi cao 170cm và 30 tuổi cao 160cm; bé 5 tuổi cao 110cm. Đi Khu vui chơi Mẫu ngày 2026-11-29, từ 09:00 đến 17:00, ngân sách 4 triệu. Bé thích động vật và trò nước.

Agent trả lời cho người dùng và kèm JSON `lich` đọc được bằng code. JSON chỉ có lịch đã qua kiểm tra; nếu không có lịch hợp lệ, `lich` là danh sách rỗng.

## Giới hạn bản demo

- Chỉ có catalog synthetic cho **Khu vui chơi Mẫu**. Phải nêu tên khu; agent không tự mặc định khu khi thiếu thông tin và từ chối khu ngoài dữ liệu.
- Dữ liệu không được xác nhận bởi khu vui chơi thật. Không dùng để thay thế thông tin chính thức.
- Agent không đặt vé, thanh toán, đọc ảnh hoặc lưu trạng thái hội thoại nhiều lượt.

Tài liệu và rubric Hackathon: [de-bai/README.md](de-bai/README.md).
