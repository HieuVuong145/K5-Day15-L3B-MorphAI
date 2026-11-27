# AI SPEC — Lịch trình một ngày ở khu vui chơi · Nhóm MorphAI · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [x] C · [ ] D · [ ] E — bài toán: C1 · Lịch trình một ngày ở khu vui chơi (đề gợi ý trong file track C)
Data BTC cấp đã dùng (nếu có — không commit nguyên file): không dùng (track C không có data BTC cấp)

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này, trong khoá hoặc trên app thật (3–5 bước; ảnh chụp từ tài khoản của mình, đã che thông tin): 
  - Người lập kế hoạch tìm danh sách các hoạt động vui chơi, trò chơi kèm theo bản đồ và giá vé cho mỗi hoạt động ở trên website hoặc app của khu vui chơi.
  - Người lập kế hoạch chưa biết nhiều thông tin nên tìm thêm các bài review/lịch trình mẫu trên các nền tảng mạng xã hội để xem thứ tự trải nghiệm các hoạt động hợp lý theo tuần tự.
  - Người lập kế hoạch tự kiểm tra hoạt động vui chơi nào trẻ con chơi được (xét theo tuổi và chiều cao,...), các show biểu diễn lúc mấy giờ.
  - Người lập kế hoạch sau đó tự lập một lịch trình dự kiến; Nếu gặp điều kiện thời thiết xấu hoặc đi muộn giờ thì tự thích nghi.
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn. Không kiểm được thì ghi "chưa kiểm": Một số người hỏi Chatbot AI chung chung như "lên lịch đi VinWonders 1 ngày", nhưng Chatbot thường bịa giờ show/giá vé hoặc không kiểm được trùng giờ — chưa kiểm chứng tỉ lệ dùng thực tế (sẽ hỏi trong khảo sát/phỏng vấn ở bước 1.2).

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): Người lập kế hoạch cho lịch trình hoạt động vui chơi
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): Lập kế hoạch các hoạt động tại khu vui chơi cho gia đình có trẻ nhỏ sao cho khớp giờ mở cửa, giờ show, phù hợp lứa tuổi và nằm trong ngân sách.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: Đọc bản đồ khu vui chơi kèm các review rồi họ tự note lại. Kế hoạch thường không như dự kiến khi show đổi theo ngày, thiếu thông tin giới hạn chiều cao/tuổi của bé, hoặc cộng nhầm tiền vé/thời gian di chuyển. Chưa bỏ được vì lịch trình gợi ý không cá nhân hoá theo khung giờ và ngân sách của từng nhà.
- Pain (KHÔNG chữ AI): Người lập kế hoạch lịch trình ở khu vui chơi cho gia đình có con nhỏ — đang tự ghép lịch đi khu vui chơi từ nhiều nguồn rời rạc — vướng ở chỗ thông tin giờ mở, giờ show, quy định lứa tuổi và giá vé không đồng nhất — hậu quả là mất nhiều thời gian chuẩn bị nhưng đến nơi vẫn bị lỡ show, đi lòng vòng làm trẻ mệt hoặc vượt ngân sách.
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): __

## §2. Impact & quyết định chọn *(guide 1.3)*

> Bản 27/11 16:40 — mới có 4 phỏng vấn (n nhỏ, ghi x/n, không ghi %). Ô *(chờ số)* điền khi có đếm review (`evidence/data-mining.md`) và khảo sát (`evidence/survey/`). Cập nhật đến CP3.

| Hướng (không có chữ AI) | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| ① Người lên lịch cho gia đình / nhóm bạn tự ghép giờ mở, giờ show, giá vé, giới hạn tuổi trước ngày đi khu vui chơi | 3/4 phỏng vấn kể mất thời gian chuẩn bị (P2, P3, P4) · review: *(chờ số)* | 1–3 lần (P2: 1, P3: 3, P4: 1) | 180 phút chuẩn bị (P2) · "1 buổi tối" (P4) · vẫn phải cắt bớt hoạt động vì thiếu ngân sách (P2) | *(chờ số: số nhóm khách/tháng × tỉ lệ gặp vấn đề × phút)* | Có | *(chốt 17:00)* |
| ② Nhóm đang ở khu vui chơi gặp mưa, lạnh hoặc show bị huỷ, phải tự xoay phần còn lại của ngày | 2/4 phỏng vấn (P3, P4) · review nhãn `thoi_tiet`: *(chờ số)* | 1–3 lần (P3: 3, P4: 1) | Bỏ lỡ hoạt động đã định (P4: huỷ tắm) · chi thêm tiền ngoài dự kiến (P3: áo ấm, áo mưa, ô) | *(chờ số)* | Có (dùng chung data và bộ kiểm với ①) | *(chốt 17:00)* |
| ③ Chọn hoạt động cho vừa ngân sách | 1/4 (P2) · review nhãn `chi_phi`: *(chờ số)* | 1 lần (P2) | Phải bỏ hoạt động, "tiếc vì không được trải nghiệm hết" (P2) | *(chờ số)* | Có | Gộp vào ① (ngân sách là một ràng buộc của lịch) |
| ④ Xếp hàng chờ lâu ở trò đông | 0/4 phỏng vấn nhắc · review nhãn `xep_hang`: *(chờ số)* | — | Phút chờ | — | Không: không có data thời gian chờ thật | Loại |

- **Impact / tháng** của hướng chọn = __ nhóm khách × __ lần × __ phút = __ — nguồn từng thừa số:
  - Số nhóm khách / tháng: số lượt khách công bố công khai của một khu vui chơi *(chờ nguồn — phải mở trang)* ÷ số người mỗi nhóm (khảo sát câu 2)
  - Tỉ lệ gặp vấn đề: x/N review (`evidence/data-mining.md`) + khảo sát câu 5 *(chờ số)*
  - Phút mỗi lần: 180 phút (P2) — n = 1, thay bằng trung vị khảo sát câu 4 + 8 *(chờ số)*
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
  - ④ Xếp hàng: không có data thời gian chờ thật, lát cắt không giải được.
  - C3 (khách bị huỷ chuyến bay) và C2 (lễ tân đổi phòng): nhóm chọn C1; C2 khó gặp đủ lễ tân trong 2 ngày.
  - Điều phỏng vấn cho thấy ngược giả thuyết: 0/4 người đi cùng trẻ nhỏ; P1 không đúng vai (concert, lịch BTC sắp sẵn — không có pain xếp lịch).
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8): đi 1 lần / tháng (P2, P4) · đi 3 lần / tháng (P3) — *(tự ước tính từ n = 3, thay bằng khảo sát câu 1)*

## §3. Giải pháp tương tự *(guide 2.1)*
- Google Maps / Apple Maps: đáng học ở ước lượng thời gian di chuyển giữa các điểm chính xác · đáng né là chỉ xem từng điểm rời rạc, không tự ghép lịch theo giờ mở cửa, giờ show hay tổng ngân sách · mình khác ở chỗ tự ghép trọn lịch 1 ngày thoả đồng thời mọi ràng buộc.
- ChatGPT / Chatbot AI chung (P3, P4 đã dùng): đáng học ở giao diện hỏi tự nhiên, ra gợi ý nhanh · đáng né là hay bịa giờ mở/giá vé, không kiểm trùng giờ hay vượt ngân sách bằng code và không tự đổi sang điểm trong nhà khi trời mưa/lạnh · mình khác ở chỗ mọi giờ và giá lấy từ công cụ và có code kiểm tra chéo.
- App / Website của khu vui chơi (VinWonders, Sun World): đáng học ở thông tin giờ mở, bản đồ nội khu chính xác · đáng né là thông tin nằm rải rác nhiều mục, chỉ liệt kê điểm chơi chứ không tối ưu lịch theo khung giờ và túi tiền riêng · mình khác ở chỗ lọc và sắp xếp cá nhân hoá theo đúng ràng buộc của nhóm đi.

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
