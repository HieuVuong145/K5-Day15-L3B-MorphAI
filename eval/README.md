# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

Dữ liệu chạy thử là bộ catalog `synthetic` của **Khu vui chơi Mẫu** đặt trong `data/` (chi tiết tại `data/DATA_CARD.md`):
- `park.json`, `shows.json`, `tickets.json`, `travel_times.csv`, `weather.json`: mô phỏng điểm chơi, show theo thứ, giá vé lẻ/combo/sau 16:00, ma trận thời gian di chuyển giữa các phân khu (+ đệm 5 phút) và dự báo thời tiết theo khung giờ; có cài sẵn điểm đóng cửa sớm, giới hạn tuổi/chiều cao và dữ liệu cũ > 30 ngày để kiểm thử.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: **30 câu** (`thuong` 8 · `kho` 17 · `tu_choi` 5, gồm 2 câu tấn công `K13`, `K14`).
- Nguồn: `nguoi_dung` 11 · `data_that` 0 · `tu_viet` 19 · `sinh_seed` 0 → từ người dùng / data thật **11/30** (36,7%, đạt ngưỡng ≥ 1/3).
- Độ phủ — lưới input 5 chiều: nhóm đi (gia đình có trẻ 3–5 tuổi, nhóm bạn, người lớn tuổi) · ngân sách (dư, sát, không đủ 500k–2tr) · khung giờ (cả ngày, chiều tối, quá giờ đóng cửa) · thời tiết (nắng, mưa chiều, mưa cả ngày, chưa có dự báo) · thông tin & tính khả thi (đủ, thiếu, ngoài phạm vi).
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5): lớp 1 (nguồn sự thật): `K11`, `K12` · lớp 2 (mơ hồ/thiếu tin): `K07`, `K08` · lớp 3 (ngoài phạm vi): `K15`, `K16` · lớp 4 (đặc thù lĩnh vực): `K05`, `K06`, `K09`, `K10` (+ tấn công `K13`, `K14`).

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| `lich_hop_le` | code (`eval/auto_grade.py` gọi `kiem_lich_trinh`) | 100% câu có lịch |
| `so_lieu_khop_cong_cu` | code (`eval/auto_grade.py` đối chiếu trace + `tinh_tong_tien`) | 100% câu |
| `khong_bia_lich` | code (`eval/auto_grade.py`) | 100% câu không xếp được / hỏi lại / từ chối |
| `tu_choi_dung` | code (`eval/auto_grade.py`) | 100% câu `tu_choi` |
| `hoi_lai_dung_luc` | người chấm | ≥ 80% câu `hoi_lai` |
| `dung_so_thich` | code (`eval/auto_grade.py` kiểm tag trong `park.json`/`shows.json`) | ≥ 80% câu có sở thích |

- **Người thứ hai chấm thử:** Thanh (không phải người viết spec) chấm độc lập 5 output → khớp __/5 *(sẽ điền sau khi chạy lượt 1 sáng Thứ Bảy; cần ≥ 4/5)*
- LLM chấm (nếu có): không dùng LLM chấm
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ 75% câu qua toàn bộ `pass_criterion`, **và** `lich_hop_le`, `so_lieu_khop_cong_cu`, `khong_bia_lich`, `tu_choi_dung` đều đạt 100%, **và** `hoi_lai_dung_luc`, `dung_so_thich` ≥ 80%."

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · `python eval/auto_grade.py eval/run-N.csv --write` (và chấm tay câu `hoi_lai`) · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-235116` | `gpt-4o-mini` | Bản nối model đầu (bắt buộc nêu tên khu; sửa tối đa 1 vòng) | 6/30 | 20% | Chưa (`thuong` 0/8 · `kho` 3/17 · `tu_choi` 3/5) |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
