# Reflection — Nguyễn Đình Trường

1. **Vai trò và phần mình làm**  
   Mình phụ trách Build AI cho bản demo lập lịch đi chơi của gia đình.  
   Mình tích hợp lời gọi OpenAI và lấy số token từ phản hồi API trong [`codebase/ai.py`](../codebase/ai.py) (`66a2f2a`).  
   Mình cải tiến phần đọc yêu cầu và xếp lịch trong [`codebase/agent.py`](../codebase/agent.py), đồng thời bổ sung [kiểm thử hồi quy](../tests/test_agent_validation.py) (`68cbbf8`, `22b186f`).  
   Mình rút gọn hướng dẫn cài đặt và chạy trong [`README.md`](../README.md) (`68cbbf8`).  
   Mình lưu kết quả đánh giá [lượt 2](../eval/run-2.csv) (`83ae882`) và cập nhật [lượt 3](../eval/run-3.csv) (`f537aff`).  
   Mình chạy mô phỏng và ghi [tóm tắt chi phí](../cost/simulate-1-summary.md) (`22b186f`).

2. **AI hỗ trợ mình thế nào**  
   Mình dùng GitHub Copilot trong VS Code để gợi ý sửa prompt trích xuất, kiểm tra đầu vào và viết ca kiểm thử hồi quy.  
   Mình đối chiếu các gợi ý với [`spec.md`](../spec.md) và bộ câu thử, rồi chỉnh cách hỏi lại khi thiếu thông tin hoặc khi yêu cầu cần làm rõ.  
   Chẳng hạn, với `K26`, câu hỏi chung về chi phí được xử lý bằng cách hỏi thêm mức ngân sách và các thông tin cần để lập lịch. Mình ghi lại cách dùng Copilot trong [`docs/ai-usage.md`](../docs/ai-usage.md) (`d93528e`).

3. **Một câu thử trượt và điều mình học được**  
   Ở câu `K01` lượt 1, gia đình muốn đi từ 9h đến 17h và bé thích động vật, trò nước.  
   Mô hình xếp `P10` lúc 15:30 dù điểm này đóng cửa lúc 15:00, đồng thời chỉ chừa 10 phút di chuyển từ `P06` trong khi cần 15 phút.  
   Từ lỗi này, mình học được cách phân việc cho mô hình và Python. Mô hình đề xuất điểm chơi theo sở thích, còn Python tính khung giờ theo dữ liệu và kiểm tra lịch trước khi trả lời. Xem [`eval/report.md`](../eval/report.md).
