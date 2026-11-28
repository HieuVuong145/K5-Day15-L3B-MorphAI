# Reflection — Vương Toàn Minh Hiếu

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Đội trưởng. Mình làm phần bằng chứng pain: phỏng vấn P1–P6 (`evidence/interviews/`, commit `653a6c7`, `1920152`), khảo sát n = 26 và tổng hợp ở `evidence/summary.md`. Mình viết bảng impact có nguồn ở `spec.md` §2 (137.100 nhóm/tháng × 65,4% × 15–30 phút).
   Mình soạn bản nháp CP2 gồm 16 câu thử, 6 metric và chuẩn "đạt" (`fd5489b`), sau đó mở rộng lên 30 câu với K18–K30 (`7a63036`).
   Sau lượt 1, mình viết cải tiến trong `codebase/agent.py` (`39dc497`): code xếp giờ (`_Planner`), mặc định khu/người lớn có công bố, câu mơ hồ thì hỏi lại. Kết quả tăng từ 6/30 lên 22/30.
   Ngoài ra mình làm canvas, `spec.md` §3, §9, §10 và slide.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Mình dùng Claude Code để viết script đếm `responses.csv`, soạn nháp K18–K30, viết code cải tiến sau lượt 1, soạn nháp `summary.md`, impact và slide.
   Chỗ phải sửa: script đếm sai số nhóm gia đình lỡ điểm (4/6), mình đếm lại trên đủ 26 dòng thì ra 3/6. Mọi con số trong `pass_criterion` của K18–K30, mình tính lại bằng chính `tinh_tong_tien` / `tra_diem_choi` chứ không tin số AI viết. Nguồn 5 triệu lượt khách/năm, mình mở trang VnEconomy gốc để kiểm.
   Lúc soát slide, AI phát hiện trang 4 mô tả demo theo output cũ, không khớp code đang chạy, nên mình sửa sau CP4 (`spec.md` §10).
   Mình không dùng AI để tạo người phỏng vấn, trích dẫn hay câu trả lời khảo sát.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   Ở lượt 1, `K01` (gia đình có bé 5 tuổi) trượt vì model tự điền giờ: show S01 diễn 10:30 bị xếp 11:00, một chặng đi cần 12 phút chỉ được chừa 2 phút. Cho model tự sửa 1 vòng vẫn sai, và cả 8 câu `thuong` đều trượt.
   Bài học: phần nào là số cố định trong dữ liệu (giờ show, giờ mở, thời gian đi) thì để code tính, còn AI chỉ giữ phần cần phán đoán (chọn điểm nào, thứ tự nào). Chuyển việc xếp giờ sang code thì `thuong` từ 0/8 lên 8/8.
   Cái giá của thay đổi này: `K16` từ đạt thành trượt, `tu_choi` giảm từ 3/5 xuống 2/5. Mỗi lần sửa phải chạy lại cả bộ câu thử, vì sửa đúng chỗ này vẫn có thể làm hỏng chỗ khác.
