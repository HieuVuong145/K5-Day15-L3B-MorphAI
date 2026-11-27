# Kế hoạch triển khai CP3

* **Hạn nộp:** 10:00 sáng mai (Thứ Bảy)
* **Phân chia cặp (Chặng 4):**
  * **Cặp X:** Trường + Cường *(Nối model và chặn rủi ro)*
  * **Cặp Y:** Hiếu + Thanh *(Bằng chứng và câu thử)*

---

## 1. Danh mục sản phẩm cần nộp (Deliverables)

- [ ] **Bằng chứng:** Đạt ngưỡng ở $\ge 1$ nguồn, có $\ge 5$ trích dẫn, kèm link `evidence/summary.md`.
- [ ] **Bộ câu thử:** 20–30 câu thử, trong đó có $\ge 5$ câu khó và $\ge 2$ câu từ chối *(hiện mới có 17 câu)*.
- [ ] **Video demo:** Video 30 giây quay bản chạy thử gọi AI thật.
- [ ] **Kết quả đánh giá:** Kết quả lượt 1 dạng `$x/N$`, kèm run ID.
- [ ] **Tài liệu đặc tả:** `spec.md` hoàn thiện đầy đủ từ §0–§7.

---

## 2. Công việc tối nay (Làm trước khi ngủ)

### Cặp X: Nối model và chặn rủi ro

#### 1. Trường — Nối model thật *(Việc dễ kẹt nhất, ưu tiên làm đầu tiên)*
- [ ] Lấy API key, lưu trong file `.env` *(tuyệt đối không commit file này)*. Làm theo hướng dẫn tại `docs/connect-model.md`. Chạy `python run.py eval --try` đảm bảo trả về token $> 0$.
- [ ] Cho phép nhập câu chữ tự do để model tách ý thành JSON. Thêm bước kiểm tra khoảng hợp lý:
  * Chiều cao: `50–220 cm`
  * Tuổi: `0–100` *(để K17 kiểm được)*
- [ ] Viết prompt xếp lịch và prompt sửa lịch: chỉ được dùng ID có trong data, sửa tối đa 1 lần.
- [ ] Chuẩn hóa output: bắt buộc kèm JSON `lich [{id, start, end}]` để các metric chấm bằng code chạy được. Nhánh *"không xếp được"* lấy gợi ý từ `goi_y_noi`.
- [ ] Xử lý an toàn prompt: tin nhắn của người dùng chỉ được coi là dữ liệu, không phải lệnh. Chặn được **K13** và **K14**.
- [ ] Viết `README.md` của nhóm: hướng dẫn cài đặt, lệnh chạy, ví dụ input *(Rubric R3 và điều kiện cứng số 1 yêu cầu file này)*.

#### 2. Cường — Code chấm điểm
- [ ] Viết code chấm 4 metric tự động, đọc dữ liệu từ `traces/run-N.jsonl`:
  * `lich_hop_le`: chạy lại `kiem_lich_trinh` trên lịch trong output.
  * `so_lieu_khop_cong_cu`: dùng regex, có tính các ngoại lệ như đã ghi.
  * `khong_bia_lich`
  * `tu_choi_dung`
- [ ] Điền `eval/README.md` mục 1–4: dataset, cách dựng bộ câu thử, metric, lệnh chạy.
- [ ] Ngồi cùng Trường chạy `eval --try`, kiểm tra code chấm có hoạt động trơn tru trên output thật hay không.

---

### Cặp Y: Bằng chứng và câu thử

#### 1. Hiếu — Bằng chứng và Impact
- [ ] Phỏng vấn thêm 2–3 phụ huynh từng dẫn trẻ đi khu vui chơi trong khoảng 1 tháng qua *(hiện mới có khoảng 1–2 người đúng vai)*.
- [ ] Xử lý vụ P2 và P3 bị sửa nội dung: ghi rõ lý do sửa vào file, hoặc trả về đúng nguyên văn lời người được phỏng vấn. Xác nhận phản hồi khảo sát #3 không phải do người trong nhóm điền.
- [ ] Bổ sung vào `evidence/summary.md`:
  * Bảng đếm theo từng vai: gia đình (6 người) và nhóm bạn (13 người).
  * Đối chiếu câu 3 với câu 5 của khảo sát: người không lên lịch có lỡ điểm nhiều hơn không? *(Đây là chỗ lệch so với giả thuyết, rubric R1 có 3 điểm cho phần này)*.
  * Ghi rõ giới hạn của mẫu khảo sát.
- [ ] Hoàn thiện `spec.md` §2: tìm và mở trang nguồn công bố số lượt khách của khu vui chơi. Thêm một thừa số quy ra tiền.

#### 2. Thanh — Thêm câu thử và chuẩn bị chi phí
- [ ] Thêm $\ge 7$ câu thử cho đủ 24 câu, lấp các trường hợp còn trống:
  * Bé cao đúng `100 cm`, bé cao đúng `140 cm`.
  * Ông bà $\ge 60$ tuổi.
  * Combo rẻ hơn mua lẻ.
  * Mua vé sau `16:00`.
  * Bé phải có người lớn đi kèm.
  * Khu nước đóng cửa lúc `15:00`.
  * Nguồn data cũ (P28).
  * 1–2 câu `data_that` lấy từ phản hồi khảo sát.
- [ ] Chạy thử các câu mới bằng `tools.py` để chắc chắn data cho ra đúng `expected` *(lưu ý: chỉ thêm câu mới, tuyệt đối không sửa câu cũ)*.
- [ ] Viết nháp `cost/personas.yaml` theo khảo sát câu 1 (đi 1 lần, 2–3 lần, $\ge 4$ lần/năm). Ghi giá của 2 model, kèm link và ngày xem.

---

## 3. Lịch trình sáng Thứ Bảy (Từ 8:30 — Cả nhóm cùng làm)

- [ ] **Chạy đánh giá:** Chạy `python run.py eval` để xuất ra file `eval/run-1.csv`.
- [ ] **Chấm điểm:** Chạy code chấm của Cường kết hợp chấm tay, điền cột `pass`, sau đó chạy `python run.py score eval/run-1.csv`.
- [ ] **Chấm chéo (Cross-check):** Người thứ hai chấm thử 5 output *(Thanh chấm phần Cường đã chấm)*, yêu cầu độ khớp $\ge 4/5$. Ghi kết quả đối chiếu vào `eval/README.md`.
- [ ] **Hoàn thiện spec:** Hiếu điền §7 dòng kết quả lượt 1 và rà soát hoàn thiện `spec.md` §0–§7.
- [ ] **Quay video:** Thanh quay video 30 giây gồm 1 ca thường và 1 ca không xếp được, đặt chế độ **Không công khai (Unlisted)**, kiểm tra lại bằng cửa sổ ẩn danh.
- [ ] **Kiểm tra & Nộp bài:** Chạy `python run.py check`, `commit`, `push`, và nộp CP3 trước **10:00**.

---

> **⚠️ LƯU Ý QUAN TRỌNG:**
> Lượt 1 có điểm thấp cũng không sao, vì số liệu thật vẫn được tính đủ điểm. **Tuyệt đối không** sửa `expected`, **không** bỏ câu trượt, và **không** sửa chuẩn *"đạt"*.