# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu — đi ít (46%), đi vừa (33%), đi nhiều (21%); số lượt hỏi/phiên lần lượt 1, 2, 3. Nguồn: khảo sát câu 1 (n=26, 24 người có đi); số lượt hỏi/phiên là ước tính.
- **Số người dùng** 3 kịch bản: thấp 1.371 · cơ sở 4.113 · cao 6.855 nhóm/tháng. Nguồn: 1%, 3%, 5% (tự ước tính) của 137.100 nhóm/tháng theo `spec.md` §2.
- **Giá** (USD/1M token, giá Standard): `gpt-4o-mini` $0.15 vào / $0.60 ra · `gpt-6.1-terra` $1.00 vào / $5.00 ra. Nguồn: [OpenAI API pricing](https://developers.openai.com/api/docs/pricing), xem 2026-11-28; giá đã ghi trong `personas.yaml`.
- **Tỉ lệ đạt** dùng để tính: 22/30 (73%) — lượt 2 `run-2@20261128-081300` (`--rate-from eval/run-2.csv`), đúng bản agent của lượt 2 (commit `90a3f01`)
- Đo token trên model `gpt-4o-mini`, tính giá model `gpt-4o-mini` và `gpt-6.1-terra`.

Tỷ giá quy đổi: 1 USD = 26.030 VND theo giá bán USD của Vietcombank lúc 09:45 ngày 2026-11-28. Nguồn và mốc lấy tỷ giá được ghi trong `personas.yaml`.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-2.csv` · run ID `simulate-2@20261128-124011` · 50 phiên (0 phiên lỗi) · seed 42 · chạy thật qua bản agent lượt 2 (commit `90a3f01`; code trên `main` hiện là bản lượt 3)

| Persona | Số phiên | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| di_it | 23 | 1 | 2306 | 221 | 1.4 | 24.6 |
| di_vua | 16 | 2 | 5330 | 493 | 3.2 | 61.8 |
| di_nhieu | 11 | 3 | 9311 | 891 | 5.1 | 107.5 |

| Model | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | / tháng — thấp (1.371) | / tháng — cơ sở (4.113) | / tháng — cao (6.855) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `gpt-4o-mini` | $0.00100 (≈ 26 ₫) | **$0.0014 (≈ 35 ₫)** | $0.00077 (≈ 20 ₫) | $0.41 (≈ 10.574 ₫) | $1.22 (≈ 31.721 ₫) | $2.03 (≈ 52.868 ₫) | $0.00030 (≈ 8 ₫) |
| `gpt-6.1-terra` | $0.0071 (≈ 185 ₫) | **$0.0097 (≈ 252 ₫)** | $0.0055 (≈ 143 ₫) | $2.89 (≈ 75.339 ₫) | $8.68 (≈ 226.016 ₫) | $14.47 (≈ 376.693 ₫) | $0.0021 (≈ 55 ₫) |

Số chép từ `cost/simulate-2-summary.md`. *`cost/simulate-1` (11:57) chạy trên bản agent lượt 3 (bản code hiện trên `main`) và lấy tỉ lệ đạt 100% từ lượt `run-3` → không dùng cho bảng này (guide 4.2: không lấy tỉ lệ đạt 100%); giữ file làm hồ sơ.*

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ 1,8 lượt hỏi trung bình mỗi phiên ÷ tỉ lệ đạt. Tỉ lệ đạt đo theo từng câu thử.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): khoảng 1–6 phút thời gian có thể tiết kiệm (0,1–0,3 chuyến/tháng × 65,4% gặp vấn đề × 15–30 phút/lần).
- Chi phí / người / tháng (cơ sở): khoảng 8 ₫ với `gpt-4o-mini`; 55 ₫ với `gpt-6.1-terra`. Chi phí / task thành công: 35 ₫ (`gpt-4o-mini`) — tức khoảng 1 nghìn ₫ cho mỗi ~30 lịch đạt.
- **Kết luận một dòng — đáng làm không:** Chi phí model ước tính rất thấp so với thời gian có thể tiết kiệm; đáng tiếp tục thử nghiệm. Chưa tính hosting, kiểm chứng dữ liệu và duyệt thủ công; impact thực tế chưa được chứng minh vì catalog còn synthetic.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
