# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Hạng mục | Công cụ AI sử dụng | AI hỗ trợ thực hiện | Cách kiểm tra / xác nhận của con người | Người thực hiện |
|---|---|---|---|---|
| Code bản chạy thử | GitHub Copilot trong VS Code; Claude Code (Hiếu) | Hiếu: viết bản cải tiến sau lượt 1 trong `agent.py` (code xếp giờ, hỏi lại câu mơ hồ, mặc định khu/người lớn) và sửa 3 test theo hành vi mới. Trường: dùng Copilot gợi ý sửa workflow, validator và test hồi quy | Chạy 22 test, chạy thử 17 câu bằng model giả và 3 câu bằng `gpt-4o-mini`, kiểm mọi lịch qua `kiem_lich_trinh`; Trường rà code, đối chiếu test/benchmark và duyệt thay đổi | Hiếu · Trường |
| Prompt / thiết kế lời gọi mô hình | GitHub Copilot trong VS Code | Gợi ý cải thiện trích xuất yêu cầu, hỏi lại và từ chối | Trường đối chiếu `spec.md` và benchmark | Trường |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code (Hiếu) | Viết script Python đếm `responses.csv` (tỉ lệ lỡ điểm, theo vai, câu 3 × câu 5, cỡ nhóm 3,04) | Đếm lại trên cả 26 phản hồi; sửa 1 lần đếm sai (4/6 → 3/6 nhóm gia đình); số trong `summary.md` khớp script | Hiếu |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |

| Viết câu thử (benchmark) | Claude Code (Hiếu) · *(Cường điền phần K01–K17)* | Soạn nháp K18–K30 từ khảo sát và ca biên của dữ liệu | Mỗi câu thử có `source`; số trong `pass_criterion` (tổng vé, điểm bị loại) tính lại bằng `tinh_tong_tien` / `tra_diem_choi`; chỉ thêm, không sửa câu cũ | Hiếu · Cường |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Claude Code (Hiếu) | Soạn nháp `summary.md`, spec §2 (impact), §9, §10, canvas, slide | Mọi số trỏ về file gốc; nguồn số lượt khách (VnEconomy 11/08/2025) mở trang gốc kiểm; phần ngược giả thuyết giữ lại | Hiếu |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
