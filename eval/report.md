# Báo cáo đánh giá — lượt 1 → lượt 2 → lượt 3

> Điền ở guide bước 4.1. Các lượt dùng cùng bộ câu thử và cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-N.csv` sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-235116` | 6/30 | 20% | 0/8 | 3/17 | 3/5 | chưa |
| 2 | `run-2@20261128-081300` | 22/30 | 73% | 8/8 | 12/17 | 2/5 | chưa |
| 3 | `run-3@20261128-113915` | 30/30 | 100% | 8/8 | 17/17 | 5/5 | đạt |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`, `eval/run-3.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`, `traces/run-3.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Hỏi ngược tên khu vui chơi (không mặc định Khu vui chơi Mẫu) | 20 | `K02`, `K03`, `K04`, `K05`, `K06`, `K09`, `K10`, `K11`, `K12`, `K13`, `K14`, `K17`, `K18`, `K19`, `K20`, `K21`, `K22`, `K23`, `K29`, `K30` |
| AI tự tính giờ sai dẫn đến vi phạm giờ đóng cửa / thời gian di chuyển | 1 | `K01` |
| Phân loại nhầm câu hỏi mơ hồ thành ngoài phạm vi | 2 | `K26`, `K28` |
| Nhận nhầm tên điểm trong khu thành khu vui chơi khác | 1 | `K24` |

**≥3 lỗi cụ thể (từ `eval/run-1.csv`):**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| `K01` | "Gia đình 2 người lớn + 1 bé 5 tuổi cao 110cm, đi Khu vui chơi Mẫu ngày 29/11, từ 9h đến 17h, ngân sách 4 triệu, bé thích động vật và trò nước" | "Không thể đưa lịch này như một phương án hợp lệ. Ràng buộc chưa đạt: P10 mở cửa 09:00–15:00, không khớp giờ xếp 15:30–16:15..." | Model tự chọn giờ cho từng điểm và sai giờ đóng cửa `P10` (15:00) + thiếu đệm di chuyển `P06 -> P10` (chỉ chừa 10 phút thay vì 15 phút), sửa 1 vòng vẫn không hết lỗi. |
| `K02` | "Nhà mình 2 người lớn, 1 bé 5 tuổi cao 110cm, đi ngày 01/12 (thứ Ba) từ 9h đến 17h, ngân sách 3,5 triệu, cả nhà thích xem show" | "Vui lòng cung cấp khu vui chơi. Chưa tra cứu hoặc lập lịch; vui lòng bổ sung rồi gửi lại." | Người dùng không gõ chữ "Khu vui chơi Mẫu" nên hệ thống dừng hỏi lại thay vì mặc định khu duy nhất của bản demo; kéo theo 20/30 câu trượt ngay ở bước tách input. |
| `K05` | "Gia đình 2 người lớn, bé 5 tuổi cao 110cm, đi ngày 28/11 từ 9h đến 18h, ngân sách 4 triệu..." | "Vui lòng cung cấp khu vui chơi. Mỗi thành viên cần có tuổi 0–100 và chiều cao_cm 50–220... Giá trị đã hiểu: thành viên 1: tuổi 30, chiều cao 0 cm..." | Ngoài thiếu tên khu, người lớn không ghi chiều cao bị tách thành `0 cm` rồi bị validator chặn vì `< 50 cm`. |
| `K26` | "tìm nơi nào phù hợp với chi phí trong ngân sách" | "Bản demo chỉ hỗ trợ lập lịch một ngày trong Khu vui chơi Mẫu; mình không thể hỗ trợ yêu cầu này." | Bị phân loại nhầm là `ngoai_pham_vi` và từ chối luôn thay vì hỏi lại ngân sách bằng số và các mục bắt buộc còn thiếu. |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: **Hỏi ngược tên khu/người lớn & AI tự xếp giờ sai (`code xếp giờ`)** — vì sao là nhóm **đau nhất với người dùng**: 20/30 câu ở lượt 1 bị chặn ngay trước khi xếp lịch dù người dùng đã nhập đủ ngày/giờ/ngân sách; còn khi vào được bước xếp lịch (`K01`) thì AI tự bịa giờ nên trượt `kiem_lich_trinh`.
- Đã sửa gì (trong `codebase/agent.py`):
  - Dùng **code xếp giờ** (`_build_schedule_by_code` / ghép khung giờ dựa trên ma trận di chuyển + đệm, giờ mở cửa, giờ show và tránh khung mưa) thay vì để model tự chọn giờ; model chỉ trích xuất ý và viết lý do/chọn ưu tiên.
  - Mặc định `khu = "Khu vui chơi Mẫu"` (và nêu rõ trong output) khi người dùng không nêu tên khu khác; mặc định người lớn 18–59 tuổi đủ chiều cao khi không nêu tuổi/chiều cao; cải thiện tách intent để câu thiếu thông tin (`K26`, `K28`) quay lại hỏi đúng mục thiếu.
- Kết quả: nhóm lỗi hỏi ngược khu & sai giờ `21/21` → `1/21` (chỉ còn `K24` nhầm tên quán thành khu khác; riêng `K01`–`K05`, `K12`, `K17`–`K22`, `K29`, `K30` đều qua `lich_hop_le`) · tổng `20%` (6/30) → `73%` (22/30) · `thuong`: `0/8` → `8/8` (100%).
- Câu nào **tệ đi** sau khi sửa: `K16` (lượt 1 hỏi lại mục thiếu và trùng hợp đạt `tu_choi_dung`; lượt 2 nhận đúng là khu ngoài data nhưng câu từ chối thiếu từ khóa phạm vi theo bộ chấm tự động) và `K13`, `K14` (lượt 2 vẫn tạo lịch hợp lệ cho các điểm còn lại thay vì chỉ từ chối không trả lịch như `metric_spec.yaml` quy định cho `tu_choi`).

## 4. Lỗi lượt 2

- Các câu chưa đạt ở lượt 2: `K06`, `K10`, `K11`, `K13`, `K14`, `K16`, `K23`, `K24`.
- Kết luận lượt 2: `22/30` (73%), chưa đạt ngưỡng tổng và các ngưỡng metric đã chốt trong `spec.md` §7.

## 5. Kết quả lượt 3

- Các lỗi còn lại ở lượt 2 đều đạt ở lượt 3 theo `pass_criterion`; auto-grader báo 25 PASS, 0 FAIL và 5 câu cần chấm tay.
- Chấm tay `hoi_lai_dung_luc`: `K07`, `K08`, `K25`, `K26`, `K28` đều đạt (5/5). Với `K08`, yêu cầu tuổi/chiều cao của từng người được tính là đủ để làm rõ số lượng nhóm.
- Kết luận lượt 3: `30/30` (100%), đạt ngưỡng tổng và các ngưỡng metric đã chốt trong `spec.md` §7.
