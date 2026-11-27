# Data card — dữ liệu bản chạy thử dùng

> Track C1: Lịch trình một ngày ở khu vui chơi (`Khu vui chơi Mẫu`). Bản CP2 (Người 3 — Thanh).

## Dataset 1 · Dữ liệu vận hành khu vui chơi mẫu (`park.json`, `shows.json`, `tickets.json`, `travel_times.csv`, `weather.json`)

| Thuộc tính | Nội dung |
|---|---|
| Dùng để làm gì | Nguồn dữ liệu chỉ đọc cho 6 công cụ trong `codebase/tools.py` (`tra_diem_choi`, `tra_lich_show`, `uoc_thoi_gian_di`, `tra_thoi_tiet`, `tinh_tong_tien`, `kiem_lich_trinh`). |
| Từ đâu | Sinh có seed (`SEED = 20261127`) bằng script `data/generate_data.py`. Khung giờ mở cửa (`08:30–20:00`) và cơ cấu giá vé dựng tham chiếu trang công khai của **VinWonders Nha Trang** (`https://vinwonders.com/vi/vinwonders-nha-trang/`, xem ngày `2026-11-27`). |
| Xử lý những bước gì | Gắn mã định danh (`P01`–`P28`, `S01`–`S08`), phân 7 khu vực, gắn cờ `synthetic: true` và `updated_at`, cài sẵn các trường hợp biên/chỗ khó theo Phụ lục C và `spec.md` §4:<br>- Điểm đóng cửa sớm lúc `15:00` (`Cong_Vien_Nuoc`, `Vuon_Thu_Sinh_Thai`).<br>- Giới hạn tuổi, chiều cao (`≥ 120 cm`, `≥ 140 cm`) và yêu cầu người lớn đi cùng (`adult_required_under_cm`).<br>- 4 điểm có phụ phí ngoài vé cổng (`100.000–250.000đ`).<br>- 2 điểm tên gần giống nhau (`P15` *Vòng quay Bầu Trời* ngoài trời ≥ 120 cm vs `P16` *Vòng quay Mặt Trời* trong nhà mọi chiều cao).<br>- 1 điểm cố ý đặt `updated_at: "2026-10-01"` (> 30 ngày) để kiểm tra chặn rủi ro nguồn quá cũ.<br>- 2 show chỉ diễn cuối tuần; 4 show ngoài trời huỷ khi mưa.<br>- Vé miễn phí `< 100 cm`, vé chiều tối sau `16:00`, và 2 gói combo rẻ hơn mua lẻ.<br>- Cặp khu `Cong_Vien_Nuoc` ↔ `Doi_Cam_Giac_Manh` cách nhau `25` phút; ngày `2026-11-28` mưa chiều và `2026-11-30` mưa cả ngày. |
| Số dòng / số đoạn | - `data/park.json`: **28** điểm chơi (7 khu vực)<br>- `data/shows.json`: **8** show biểu diễn<br>- `data/tickets.json`: **3** nhóm giá lẻ (`free`, `child_or_senior`, `adult`) + **2** combo<br>- `data/travel_times.csv`: ma trận **7×7** khu vực (49 ô)<br>- `data/weather.json`: **5** ngày (`2026-11-28` → `2026-12-02`) × 4 khung giờ (**20** khung) |
| Phiên bản / ngày lấy | `2026-11-27` (riêng `P28` cố ý đặt `2026-10-01` để test kiểm tra nguồn cũ). |
| Nhãn | `synthetic` — **không dùng làm bằng chứng pain**. |
| Kiểm tra thủ công | Người sinh & kiểm: **Thanh** — đã kiểm tay toàn bộ 28 điểm, 8 show, bảng vé, ma trận 7×7, 5 ngày thời tiết và xác nhận qua `tests/test_tools.py` (9/9 test pass). |
| Giới hạn | Dữ liệu giả lập chưa mô phỏng thời gian xếp hàng thực tế tại từng trò, thay đổi giá theo mùa/đại lý, hoặc bảo trì đột xuất ngoài lịch mẫu. |

## Dataset 2 · Dữ liệu người dùng thực tế (Phỏng vấn & Khảo sát)

| Thuộc tính | Nội dung |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain người dùng (`evidence/summary.md`), tính tham số impact (`spec.md` §2), làm nguồn cho bộ câu thử (`eval/benchmark.csv`) và phân bổ persona chi phí (`cost/personas.yaml`). |
| Từ đâu | - **Phỏng vấn trực tiếp:** 4 người dùng ngoài nhóm (`evidence/interviews/P1.md`–`P4.md`).<br>- **Khảo sát Google Form:** 26 phản hồi của người dùng ngoài nhóm (`evidence/survey/responses.csv`). |
| Xử lý những bước gì | Ẩn danh toàn bộ họ tên, email, số điện thoại trước khi đưa vào repo; giữ lại câu trả lời hành vi thực tế và trích dẫn phục vụ phân tích pain. |
| Số dòng / số đoạn | - Phỏng vấn: **4** biên bản (`P1`–`P4`)<br>- Khảo sát: **26** phản hồi (`evidence/survey/responses.csv`, chưa tính dòng tiêu đề; file có 29 dòng vì một số ô trả lời viết nhiều dòng) |
| Phiên bản / ngày lấy | `2026-11-27` |
| Nhãn | `thật` (đã ẩn danh). |
| Giới hạn | Mẫu phỏng vấn (n=4) và khảo sát (n=26) còn nhỏ, thiên về nhóm bạn trẻ/gia đình trẻ, chưa phủ đều nhóm có trẻ nhỏ dưới 6 tuổi và người cao tuổi. |
