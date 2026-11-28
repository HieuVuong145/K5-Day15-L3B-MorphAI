# Tóm tắt mô phỏng simulate-2@20261128-124011

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| di_it | 23 | 1 | 2306 | 221 | 1.4 | 24.6 |
| di_vua | 16 | 2 | 5330 | 493 | 3.2 | 61.8 |
| di_nhieu | 11 | 3 | 9311 | 891 | 5.1 | 107.5 |

Tỉ lệ đạt dùng để tính: 22/30 (73%) — lượt run-2@20261128-081300

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (1.371 người) | Chi phí / tháng — cơ sở (4.113 người) | Chi phí / tháng — cao (6.855 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.00100 (≈ 26 ₫) | $0.0014 (≈ 35 ₫) | $0.00077 (≈ 20 ₫) | $0.4062 (≈ 10.574 ₫) | $1.22 (≈ 31.721 ₫) | $2.03 (≈ 52.868 ₫) | $0.00030 (≈ 8 ₫) |
| gpt-6.1-terra (vào 1.0 · ra 5.0 $/1M) | $0.0071 (≈ 185 ₫) | $0.0097 (≈ 252 ₫) | $0.0055 (≈ 143 ₫) | $2.89 (≈ 75.339 ₫) | $8.68 (≈ 226.016 ₫) | $14.47 (≈ 376.693 ₫) | $0.0021 (≈ 55 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-4o-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 26.030 ₫ (Vietcombank bán USD 26.030 VND/USD lúc 09:45 ngày 2026-11-28; bảng tỷ giá chính thức: https://www.vietcombank.com.vn/vi-VN/KHCN/Cong-cu-Tien-ich/Ty-gia; snapshot ngày 2026-11-28: https://ndh.vn/ty-gia-vietcombank/).
