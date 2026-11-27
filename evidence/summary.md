# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (nhóm bỏ crawl review Google Maps do hạn chế kỹ thuật, thay bằng khảo sát ≥20) | ☐ | — |
| Phỏng vấn (≥3 người ngoài nhóm: đã hỏi 6 người `P1–P6`, 5 người đúng bối cảnh đi khu vui chơi, trong đó 3 phụ huynh có con nhỏ `P3`, `P5`, `P6` — đúng vai người dùng chính) | ☑ | `evidence/interviews/P1.md`–`P6.md` |
| Khảo sát (≥20 người ngoài nhóm: `n = 26` phản hồi hợp lệ) | ☑ | `evidence/survey/questions.md` · `responses.csv` |

## 2. Số chính

- **Phỏng vấn:** **5/6 người** (`P2`–`P6`) gặp pain khi tự lên lịch/đi chơi; riêng vai chính (phụ huynh có con nhỏ) **3/3** (`P3`, `P5`, `P6`) *(n nhỏ không ghi %; `P1` đi concert một mình nên không đúng bối cảnh)* · số lần / tháng: `P1` 1, `P2` 1, `P3` 3, `P4` 1, `P5` 2, `P6` 1 · thời gian tìm hiểu/lên lịch: `P2` 180 phút (1 tối), `P4` 1 buổi tối, `P5` 1 ngày, `P6` 120–180 phút, `P3` tìm rải rác 1 tháng.
- **4/5 người đúng bối cảnh đã dùng ChatGPT/AI** (`P3`, `P4`, `P5`, `P6`) mà lịch vẫn vỡ tại chỗ: mưa (`P3`, `P4`, `P6`), trò giới hạn tuổi trẻ (`P6`), quá nhiều hoạt động so với thời gian (`P5`). Tức là AI chung giúp *gom thông tin* nhưng không *kiểm điều kiện* — đúng phần việc nhóm giao cho code (`spec.md` §4).
- **Khảo sát (`n = 26`):**
  - **17/26 (65.4%)** bị bỏ lỡ ít nhất 1 điểm/show định chơi (`13/26` lỡ 1–2 điểm, `3/26` lỡ 3–4 điểm, `1/26` lỡ ≥5 điểm).
  - **19/26 (73.1%)** lãng phí ≥15 phút đi lại lòng vòng/tìm đường/chờ đợi (`11/26` = 42.3% mất ≥30 phút).
  - **12/26 (46.2%)** tổng chi phí thực tế vượt dự tính ban đầu (`2/26` vượt >50%).
  - Lý do bỏ lỡ phổ biến (chọn nhiều): thiếu thời gian/đi lòng vòng (`13/26` = 50.0%), thời tiết mưa/nắng gắt (`8/26` = 30.8%), lỡ giờ show/đóng cửa sớm (`7/26` = 26.9%), xếp hàng quá lâu (`7/26` = 26.9%), không hợp tuổi/chiều cao trẻ (`5/26` = 19.2%), phát sinh chi phí (`3/26` = 11.5%).

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Người đi làm (đi concert 1 mình) | Không | 1 | 0 phút xếp lịch (5h+ xem concert) | Lịch BTC sắp sẵn |
| P2 | Sinh viên (lên lịch cho gia đình) | Có (một phần) | 1 (cuối tháng 10/2026) | 180 phút (1 tối) | Website, tự lên lịch thủ công |
| P3 | Phụ huynh (đi cùng gia đình) | Có | 3 | Rải rác 1 tháng + tiền mua đồ mưa lạnh | Google + hỏi ChatGPT |
| P4 | Sinh viên (đi cùng nhóm bạn) | Có | 1 | 1 buổi tối + huỷ hoạt động tắm | Google, Google Maps + ChatGPT |
| P5 | Phụ huynh có con nhỏ | Có | 2 | 1 ngày chuẩn bị · không kịp chơi hết | Google Maps + AI gợi ý |
| P6 | Phụ huynh có con nhỏ | Có | 1 | 120–180 phút chuẩn bị · tốn thêm thời gian đổi trò + tiền áo mưa, ô | Web + nhờ ChatGPT tổng hợp |

### Khảo sát tách theo vai (câu 2) và theo cách lên lịch (câu 3 × câu 5)

| Vai (câu 2) | n | Lỡ ≥1 điểm/show | Mất ≥15 phút lòng vòng | Vượt ngân sách | Lý do thời tiết | Lý do tuổi/chiều cao trẻ |
|---|---|---|---|---|---|---|
| Gia đình có trẻ nhỏ | 6 | 3/6 | 5/6 | 3/6 | 3/6 | 3/6 |
| Nhóm bạn (2–4 và 5+) | 13 | 10/13 | 10/13 | 8/13 | 4/13 | 2/13 |
| Khác (một mình, cặp đôi, khác) | 7 | 4/7 | 4/7 | 1/7 | 1/7 | 0/7 |

| Cách lên lịch (câu 3) | n | Lỡ ≥1 điểm/show (câu 5) |
|---|---|---|
| Tự tìm hiểu / hỏi bạn bè rồi tự ghép | 10 | **9/10** |
| Không lên lịch, tới nơi tính tiếp | 13 | 7/13 |
| Nhờ AI gợi ý | 1 | 1/1 |
| Theo tour / có người lo | 2 | 0/2 |

- **Đọc bảng:** người *có* bỏ công tự ghép lịch vẫn lỡ điểm nhiều nhất (9/10) → tự ghép từ nhiều nguồn không chặn được lỗi; chỉ 2 người có người khác lo hết thì không lỡ. Ủng hộ việc để code kiểm ràng buộc thay vì chỉ đưa thêm thông tin.
- **Điều ngược / chưa chắc:** nhóm gia đình có trẻ nhỏ lỡ điểm *ít hơn* nhóm bạn (3/6 so với 10/13), nhưng là nhóm duy nhất có pain tuổi/chiều cao và thời tiết ở mức một nửa. n = 6 quá nhỏ để kết luận — phỏng vấn `P3`, `P5`, `P6` bổ sung lý do. Cách tính: lọc theo chữ trong câu trả lời ở `responses.csv` ("gia đình", "Nhóm bạn"; câu 5 khác "0 điểm"; câu 8 khác "Gần như không mất").

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. *"Tôi mất 1 tối để quyết định, tôi không biết tiếng Thái nên gặp khó trong việc tìm kiếm website và đọc nội dung."* — `P2`
2. *"Ngân sách không đủ để trải nghiệm các hoạt động trò chơi. Buộc phải cắt bỏ 1 số hoạt động kém hấp dẫn hơn... tôi tiếc vì không được trải nghiệm hết."* — `P2`
3. *"Mưa và lạnh, nguy hiểm cho trẻ nhỏ nếu đi thuyền trên sông... Mua thêm quần áo ấm, áo mưa + ô nên mất thêm ngân sách."* — `P3`
4. *"Trời lạnh nên không thể tắm nên bỏ lỡ mất hoạt động... Huỷ bỏ lịch trình đó."* — `P4`
5. *"Sắp xếp theo vị trí các điểm chơi, sao cho đường đi hợp lý với thời gian đến địa điểm nhất"* — khảo sát `responses.csv`, phản hồi #5
6. *"Mất 1 ngày, chốt 1 tuần trước khi đi. Quá nhiều hoạt động để tải trong 1 ngày."* — `P5`
7. *"Trời mưa và có trò chơi không cho trẻ dưới 9 tuổi nên nhiều trò phải đổi, phải dành nhiều thời gian tìm chỗ khác để chơi."* — `P6`

## 4. Các nguồn có khớp nhau không

- **Khớp nhau rất rõ ở 4 điểm:** (1) Thời tiết xấu làm vỡ kế hoạch tại chỗ (`P3`, `P4`, `P6` gặp, khớp với `8/26` = 30.8% khảo sát và `3/6` ở nhóm gia đình); (2) Chi phí vượt dự tính/thiếu ngân sách (`P2`, `P3`, `P6` gặp, khớp với `12/26` = 46.2% khảo sát); (3) Không đủ thời gian cho số hoạt động định chơi (`P5`, khớp với `13/26` = 50.0% lý do "thiếu thời gian/đi lòng vòng"); (4) Tự tra Google/ChatGPT vẫn mất nhiều thời gian nhưng không kiểm được ràng buộc thực tế (`P3`–`P6`; khảo sát: người tự ghép lịch vẫn lỡ điểm 9/10).
- **Ngược một phần:** `P6` nói AI cung cấp thông tin "khá đầy đủ, nhiều hơn yêu cầu" — tức khâu *tìm* thông tin không phải chỗ vướng với người này; chỗ vướng là thông tin không được *kiểm* với điều kiện của bé và thời tiết ngày đi. Nhóm vì vậy đặt giá trị vào bước code kiểm, không vào việc tìm hộ thông tin.
- **Điểm bổ sung lẫn nhau:** Khảo sát chỉ ra thêm 2 pain lớn là **đi lòng vòng tốn thời gian (50.0%)** và **lỡ show/đóng cửa sớm (26.9%), không hợp tuổi/chiều cao trẻ (19.2%)** — giúp nhóm thiết kế đủ cả 6 công cụ kiểm tra cứng.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng phần lớn (có mở rộng)** — vì số liệu cả phỏng vấn (`5/6`, vai chính `3/3`) và khảo sát (`65.4%` lỡ điểm/show, `73.1%` mất ≥15 phút đi lòng vòng, `46.2%` vượt ngân sách) đều xác nhận người dùng gặp pain thật khi tự ghép lịch đi khu vui chơi. Tuy nhiên, khảo sát cho thấy `50.0%` người đi là nhóm bạn và `23.1%` là gia đình có trẻ nhỏ, nên thiết kế giữ lát cắt gia đình có trẻ nhỏ (bao phủ cả ràng buộc chiều cao/tuổi) nhưng áp dụng được cho cả nhóm bạn. Phần giả thuyết *"mất thời gian chuẩn bị"* chỉ đúng một phần: `P6` thấy AI tìm thông tin đủ, `13/26` người khảo sát không lên lịch trước — pain chính nằm ở chỗ lịch vỡ tại khu vui chơi hơn là ở khâu tìm thông tin. Điều vẫn chưa biết: thời gian xếp hàng thực tế tại từng trò theo khung giờ cao điểm (nằm ngoài phạm vi dữ liệu hiện có).
