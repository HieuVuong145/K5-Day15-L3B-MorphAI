# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code (Hiếu) · Antigravity (Thanh) · *(Trường điền phần của mình)* | Hiếu: viết bản cải tiến sau lượt 1 trong `agent.py` (code xếp giờ, hỏi lại câu mơ hồ, mặc định khu/người lớn) và sửa 3 test theo hành vi mới · Thanh: viết `codebase/tools.py` (6 công cụ chỉ đọc) và `tests/test_tools.py` | Hiếu: chạy 22 test, thử 17 câu model giả và 3 câu `gpt-4o-mini`, kiểm mọi lịch qua `kiem_lich_trinh`; Trường duyệt · Thanh: kiểm tay 8 ràng buộc cứng + công thức combo/phụ phí và chạy 9/9 test `test_tools.py` | Hiếu · Trường · Thanh |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code (Hiếu) | Viết script Python đếm `responses.csv` (tỉ lệ lỡ điểm, theo vai, câu 3 × câu 5, cỡ nhóm 3,04) | Đếm lại trên cả 26 phản hồi; sửa 1 lần đếm sai (4/6 → 3/6 nhóm gia đình); số trong `summary.md` khớp script | Hiếu |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Claude Code (Hiếu) · *(Cường điền phần K01–K17)* | Soạn nháp K18–K30 từ khảo sát và ca biên của dữ liệu | Mỗi câu thử có `source`; số trong `pass_criterion` (tổng vé, điểm bị loại) tính lại bằng `tinh_tong_tien` / `tra_diem_choi`; chỉ thêm, không sửa câu cũ | Hiếu · Cường |
| Sinh data `synthetic` (nếu có) | Antigravity (Thanh) | Viết script `data/generate_data.py` sinh 5 file trong `data/` và soạn nháp `data/DATA_CARD.md`, `cost/personas.yaml` | Seed `20261127` · kiểm tay 28 điểm, 8 show, bảng vé lẻ/combo, ma trận 7×7, 5 ngày thời tiết; sửa `DATA_CARD.md` bỏ mục review Google Maps; sửa `personas.yaml` từ Gemini sang `gpt-4o-mini` / `gpt-6.1-terra` | Thanh |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Claude Code (Hiếu) | Soạn nháp `summary.md`, spec §2 (impact), §9, §10, canvas, slide | Mọi số trỏ về file gốc; nguồn số lượt khách (VnEconomy 11/08/2025) mở trang gốc kiểm; phần ngược giả thuyết giữ lại | Hiếu |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
