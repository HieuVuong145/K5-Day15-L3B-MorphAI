# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu — đi ít (46%), đi vừa (33%), đi nhiều (21%); số lượt hỏi/phiên lần lượt 1, 2, 3. Nguồn: khảo sát câu 1 (n=26, 24 người có đi); số lượt hỏi/phiên là ước tính.
- **Số người dùng** 3 kịch bản: thấp 1.371 · cơ sở 4.113 · cao 6.855 nhóm/tháng. Nguồn: 1%, 3%, 5% (tự ước tính) của 137.100 nhóm/tháng theo `spec.md` §2.
- **Giá** (USD/1M token, giá Standard): `gpt-4o-mini` $0.15 vào / $0.60 ra · `gpt-6.1-terra` $1.00 vào / $5.00 ra. Nguồn: [OpenAI API pricing](https://developers.openai.com/api/docs/pricing), xem 2026-11-28; giá đã ghi trong `personas.yaml`.
- **Tỉ lệ đạt** dùng để tính: 30/30 (100%) — lượt `run-2` (kết quả mới nhất)
- Đo token trên model `gpt-4o-mini`, tính giá model `gpt-4o-mini` và `gpt-6.1-terra`.

Tỷ giá quy đổi: 1 USD = 26.030 VND theo giá bán USD của Vietcombank lúc 09:45 ngày 2026-11-28. Nguồn và mốc lấy tỷ giá được ghi trong `personas.yaml`.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-115737` · 50 phiên · seed 42

Tỉ lệ đạt 100% nên chi phí / task thành công bằng chi phí / phiên.

| Model | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|---|
| `gpt-4o-mini` | $0.0011 (≈ 28 ₫) | $0.0011 (≈ 28 ₫) | $0.00061 (≈ 16 ₫) | $0.4325 (≈ 11.258 ₫) | $1.30 (≈ 33.773 ₫) | $2.16 (≈ 56.289 ₫) | $0.00032 (≈ 8 ₫) |
| `gpt-6.1-terra` | $0.0076 (≈ 199 ₫) | $0.0076 (≈ 199 ₫) | $0.0043 (≈ 113 ₫) | $3.07 (≈ 79.976 ₫) | $9.22 (≈ 239.927 ₫) | $15.36 (≈ 399.878 ₫) | $0.0022 (≈ 58 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ 1,8 lượt hỏi trung bình mỗi phiên ÷ tỉ lệ đạt. Tỉ lệ đạt đo theo từng câu thử; phép tính dùng chính xác `22/30`, không dùng số 73,3% đã làm tròn.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): khoảng 1–6 phút thời gian có thể tiết kiệm (0,1–0,3 chuyến/tháng × 65,4% gặp vấn đề × 15–30 phút/lần).
- Chi phí / người / tháng (cơ sở): khoảng 8 ₫ với `gpt-4o-mini`; 55 ₫ với `gpt-6.1-terra`. Chi phí / task thành công: 35 ₫ (`gpt-4o-mini`) — tức khoảng 1 nghìn ₫ cho mỗi ~30 lịch đạt.
- **Kết luận một dòng — đáng làm không:** Chi phí model ước tính rất thấp so với thời gian có thể tiết kiệm; đáng tiếp tục thử nghiệm. Chưa tính hosting, kiểm chứng dữ liệu và duyệt thủ công; impact thực tế chưa được chứng minh vì catalog còn synthetic.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
