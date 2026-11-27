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
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): Một gia đình (2 người lớn, 1 bé 5 tuổi) nhập ngân sách, sở thích và khung giờ cho một ngày ở một khu vui chơi; AI chọn và sắp xếp hoạt động, code kiểm các ràng buộc cứng, và gia đình nhận lịch trình từng giờ kèm tổng tiền, lý do và nguồn, hoặc lý do không xếp được cùng gợi ý nới ràng buộc.
- Không làm: đặt vé hoặc thanh toán · lập lịch nhiều ngày · theo dõi thời tiết/sự kiện theo thời gian thực hoặc tự đổi lịch sau khi đã xuất · cam kết đây là phương án tối ưu tuyệt đối.
- **Dữ liệu bắt buộc:** khu vui chơi, ngày đi, ngân sách, khung giờ, nhóm đi (tuổi và chiều cao từng người). Thiếu một mục thì hỏi lại, không đoán.
- **Ràng buộc:** *cứng* (vi phạm thì không xuất lịch): giờ mở/giờ show, thời gian di chuyển (+ đệm), tuổi/chiều cao/yêu cầu đi cùng người lớn, ngân sách, khung giờ, nguồn điểm/show cập nhật trong 30 ngày. *Mềm* (chỉ ảnh hưởng độ phù hợp): sở thích, giờ ăn/nghỉ cho bé. Dự báo thời tiết chỉ được dùng khi có dữ liệu cho ngày đã chọn.
- **Sơ đồ** (workflow CP2; catalog hiện dùng cho chạy thử phải được đánh dấu synthetic):

  ```mermaid
  flowchart TD
      U["Nhập khu vui chơi, ngày đi, ngân sách, sở thích, khung giờ, nhóm đi (2 người lớn + bé 5 tuổi, chiều cao bé)"] --> V{"Đủ dữ liệu bắt buộc?"}
      V -->|Chưa đủ| Q["Hỏi lại dữ liệu thiếu; không đoán"]
      Q --> U
      V -->|Đủ| T["Tra điểm chơi, show, thời tiết theo ngày và thời gian di chuyển"]
      T --> A["AI chọn hoạt động và thứ tự; chỉ dùng ID có trong dữ liệu"]
      A --> C["Code kiểm: ID, giờ mở/show, di chuyển + đệm, tuổi/chiều cao, mưa, ngân sách, độ mới nguồn"]
      C -->|Hợp lệ| O["Trả lịch theo giờ, tổng tiền từ code, lý do và nguồn"]
      C -->|Có lỗi, lần đầu| R["AI sửa theo danh sách vi phạm do code trả"]
      R --> C
      C -->|Vẫn lỗi hoặc thiếu căn cứ| N["Không đưa lịch; code nêu ràng buộc chưa đạt và mức cần nới"]
      O --> E["Người dùng xem, đổi ngân sách/khung giờ/hoạt động hoặc áp dụng"]
      N --> E
      E -->|Đổi ràng buộc| U
  ```

- **Hình dạng:** [x] workflow cố định · [ ] một agent · [ ] nhiều agent — các bước tra cứu, đề xuất, kiểm tra và sửa có thứ tự cố định. Workflow dễ kiểm soát ràng buộc và đo hơn; một agent tự chọn công cụ hay nhiều agent không cần thiết cho một lịch trình.
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `tra_diem_choi(khu, nhom_di)` | Khu/phân khu và nhóm đi (`[{tuoi, chieu_cao_cm}]`) | Các điểm chơi từ `data/park.json`, giờ, thời lượng, phụ phí, điều kiện phù hợp/không phù hợp và nguồn; `synthetic: true` | Không |
  | `tra_lich_show(ngay)` | Ngày dạng `YYYY-MM-DD` | Các show hoạt động theo thứ trong tuần từ `data/shows.json`, giờ, thời lượng, nguồn; `synthetic: true` | Không |
  | `tra_thoi_tiet(ngay)` | Ngày dạng `YYYY-MM-DD` | Dự báo theo khung giờ từ `data/weather.json`, hoặc `co_du_lieu: false`; `synthetic: true` | Không |
  | `uoc_thoi_gian_di(a, b)` | ID điểm/show hoặc tên hai khu vực | Khu đi/đến, phút di chuyển, đệm 5 phút nếu có di chuyển; ma trận `data/travel_times.csv` synthetic | Không |
  | `tinh_tong_tien(lich, nhom_di, khung_gio=None)` | Lịch có ID, nhóm đi, khung giờ tùy chọn | So sánh vé lẻ/combo, vé sau 16:00, phụ phí và `tong_cong_vnd` từ `data/tickets.json`; được validator gọi nội bộ | Không |
  | `kiem_lich_trinh(lich, nhom_di, khung_gio, ngan_sach, ngay=None, today=None, so_thich=None)` | Điểm có `id/start/end`, nhóm tuổi/chiều cao, khung giờ, ngân sách; ngày, ngày tham chiếu và sở thích tùy chọn | `hop_le`, vi phạm cứng/mềm, chi tiết tổng tiền, gợi ý nới; kiểm nguồn điểm/show ≤30 ngày, giờ, show, phù hợp nhóm, mưa (nếu có dữ liệu), di chuyển + đệm, ngân sách, nghỉ và sở thích | Không |

  `search_example(query)` hiện vẫn có trong `tools.py` để tương thích với agent mẫu; đây không phải công cụ của workflow C1 và cần được thay bằng các công cụ trên khi nối agent. Hiện `agent.py` vẫn chỉ gọi công cụ mẫu này.

- **Mức tự động:** [x] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — AI tạo bản nháp, code kiểm; gia đình quyết định có đi theo lịch hay không. Không có hành động đặt chỗ hay thanh toán.
- **Chỗ chặn rủi ro**: model không tự tính giá hoặc tự xác nhận giờ; `kiem_lich_trinh` kiểm ID, giờ, ngày diễn show, điều kiện nhóm, mưa khi có dữ liệu, di chuyển + đệm và ngân sách; tổng tiền do `tinh_tong_tien` tính. Nguồn điểm/show cũ hơn 30 ngày bị đánh dấu vi phạm cứng (không tự lọc khỏi danh sách); tuổi dữ liệu của vé, thời tiết và ma trận di chuyển hiện chưa được validator kiểm tra. Nếu thiếu dự báo, validator hiện bỏ qua kiểm tra mưa, nên workflow phải nói rõ chưa xác minh thời tiết. Có vi phạm sau tối đa một lần sửa thì không xuất lịch như phương án hợp lệ; nêu lỗi và gợi ý nới do code trả. Mọi dữ liệu hiện có đều `synthetic`, không phải căn cứ cho khu vui chơi thật.
- **Chỗ người duyệt** (việc AI không được tự làm): Người dùng tự quyết có áp dụng lịch; AI không đặt vé, trả tiền, hoặc khẳng định thông tin synthetic là thông tin thật.
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | Nút V: thiếu dữ liệu bắt buộc thì hỏi lại; nút N: không có dữ liệu/không xếp được thì dừng và nêu ràng buộc |
  | G1/G2 — nói rõ làm được gì, làm tốt đến đâu | Nhãn synthetic/nguồn thật và ngày cập nhật trên kết quả; không gọi phương án là tối ưu tuyệt đối |
  | G8/G9 — dễ bỏ qua, dễ sửa | Nút E: người dùng đổi ngân sách, khung giờ hoặc hoạt động, quay về U để tạo và kiểm lại |
  | G11 — giải thích vì sao | Nút O: mỗi hoạt động có lý do gắn với sở thích/ràng buộc và nguồn; tổng tiền do code tính |

- **Kịch bản chạy thử tối thiểu:** (a) lịch hợp lệ ngay; (b) bản nháp vi phạm, sửa được trong 1 lần; (c) ngân sách hoặc chiều cao khiến không xếp được: hệ thống dừng và gợi ý nới. Ba kịch bản phủ cả ba nhánh của sơ đồ.
- Phần còn giả ở CP2: catalog giờ mở, show, giá, thời lượng và thời gian di chuyển nếu nhóm tự dựng; ghi `synthetic` trong data card và trên kết quả. Model ở chế độ giả (đầu ra có kịch bản sẵn để chạy được cả ba kịch bản trên) cho đến khi nối model thật; không demo dữ liệu giả như thông tin của một khu vui chơi thật.
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
