# Reflection — Vũ Quang Thanh

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Mình phụ trách mảng **Data · Công cụ · Chi phí** (Người 3). Mình dựng bộ dữ liệu `synthetic` (`SEED = 20261127`, tham chiếu khung giờ và giá vé VinWonders Nha Trang) qua `data/generate_data.py` sinh 5 file trong `data/` và hoàn thiện `data/DATA_CARD.md` (`c3dcbd6`, `ed6ed56`, `ff79797`).
   Mình hiện thực 6 công cụ chỉ đọc trong `codebase/tools.py` (`tra_diem_choi`, `tra_lich_show`, `uoc_thoi_gian_di`, `tra_thoi_tiet`, `tinh_tong_tien`, `kiem_lich_trinh`) kèm 9 unit test ở `tests/test_tools.py` (`c3dcbd6`).
   Ở CP3–CP4, mình chấm chéo độc lập 5 output của `eval/run-1.csv` khớp 5/5 với Cường (`eval/README.md` §3) và viết `cost/personas.yaml` bám khảo sát câu 1 (`n = 26`), số lượt khách ở `spec.md` §2 cùng giá `gpt-4o-mini` / `gpt-6.1-terra` (`3264e56`, `afd3b96`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Mình dùng **Antigravity** để hỗ trợ viết script `data/generate_data.py`, cài đặt logic kiểm tra 8 ràng buộc cứng trong `codebase/tools.py`, viết `tests/test_tools.py`, soạn `data/DATA_CARD.md` và cấu hình `cost/personas.yaml`.
   Chỗ phải kiểm và sửa lại: trong `DATA_CARD.md` bản đầu, AI tự đưa thêm mục "Review Google Maps" dù nhóm đã bỏ phần này nên mình yêu cầu xoá (`ff79797`); ở `cost/personas.yaml` bản CP3, AI điền 2 model Gemini không khớp với model nhóm dùng thật nên đến CP4 mình sửa lại sang `gpt-4o-mini` và `gpt-6.1-terra` (`afd3b96`) và gắn `users` theo `spec.md` §2.
   Toàn bộ 28 điểm chơi, 8 show, bảng vé lẻ/combo, ma trận di chuyển và 9 test case đều được mình kiểm tay và chạy `unittest` xác nhận sau khi AI sinh.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   Ở lượt 1 (`eval/run-1.csv`), `K05` (gia đình có bé 5 tuổi đi ngày 28/11 có mưa chiều) trượt ngay bước tách input: người lớn không ghi chiều cao nên model tách thành `0 cm` rồi bị validator đầu vào chặn (`< 50 cm`), chưa đi tới bước lọc mưa của `kiem_lich_trinh`. Sang lượt 2 (`eval/run-2.csv`), `K24` vẫn trượt vì bước trích xuất nhận nhầm tên quán `P28` thành khu vui chơi khác thay vì kiểm tra cờ `nguon_qua_cu` trong Khu vui chơi Mẫu.
   Bài học rút ra: bộ công cụ `kiem_lich_trinh` phía sau có chặt đến đâu thì chỉ một lỗi ở bước chuẩn hoá đầu vào cũng khiến luồng rẽ sai nhánh và không bao giờ chạm tới hàm kiểm tra; vì vậy cần kiểm soát kỹ cả bước trích xuất/mặc định trước khi gọi công cụ.
