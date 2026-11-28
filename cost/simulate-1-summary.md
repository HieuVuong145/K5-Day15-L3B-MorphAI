# Tóm tắt mô phỏng simulate-1@20261128-115737

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| di_it | 23 | 1 | 2740 | 250 | 1.5 | 30.8 |
| di_vua | 16 | 2 | 5525 | 526 | 3.2 | 65.1 |
| di_nhieu | 11 | 3 | 10166 | 879 | 5.4 | 121.2 |

Tỉ lệ đạt dùng để tính: 22/30 (73%) — lượt run-2@20261128-081300

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (1.371 người) | Chi phí / tháng — cơ sở (4.113 người) | Chi phí / tháng — cao (6.855 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.0011 (≈ 28 ₫) | $0.0015 (≈ 38 ₫) | $0.00083 (≈ 22 ₫) | $0.4325 (≈ 11.258 ₫) | $1.30 (≈ 33.773 ₫) | $2.16 (≈ 56.289 ₫) | $0.00032 (≈ 8 ₫) |
| gpt-6.1-terra (vào 1.0 · ra 5.0 $/1M) | $0.0076 (≈ 199 ₫) | $0.0104 (≈ 271 ₫) | $0.0058 (≈ 151 ₫) | $3.07 (≈ 79.976 ₫) | $9.22 (≈ 239.927 ₫) | $15.36 (≈ 399.878 ₫) | $0.0022 (≈ 58 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử, tính theo 22/30.
- Token đo trên model: gpt-4o-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 26.030 ₫ (Vietcombank bán USD 26.030 VND/USD lúc 09:45 ngày 2026-11-28; bảng tỷ giá chính thức: https://www.vietcombank.com.vn/vi-VN/KHCN/Cong-cu-Tien-ich/Ty-gia; snapshot ngày 2026-11-28: https://ndh.vn/ty-gia-vietcombank/).
