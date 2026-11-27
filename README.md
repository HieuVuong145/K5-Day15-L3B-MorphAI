# Mini Hackathon AI — AI20K khoá 5 · L3

> **[README]** → [01-challenge-brief](01-challenge-brief.md) → [tracks/](tracks/README.md) → [02-guide](02-guide.md) → [03-rubric](03-rubric.md)

**Tìm một chỗ đau thật của người dùng, thiết kế một giải pháp AI cho nó, rồi chứng minh bằng số.**

> **Trang hackathon:** https://ai20k-hackathon.pages.dev — đăng ký nhóm, tìm đồng đội, nộp checkpoint, đồng hồ đếm giờ, side quest.

Bài của nhóm phải cân bằng hai nửa: **tư duy sản phẩm** (đúng người dùng, đúng chỗ đau, đáng làm) và **giải pháp AI** (thiết kế công nghệ ra sao, AI dựa vào dữ liệu và công cụ nào, chạy thật được). Ba câu phải trả lời, mỗi câu bằng số:

1. **Pain & impact:** ai đang đau, đau thế nào, bao nhiêu người, mỗi tháng mất bao nhiêu?
2. **Giải pháp AI:** AI quyết định gì, dựa trên dữ liệu và công cụ nào, chọn workflow hay agent và vì sao, chặn rủi ro ở đâu, người duyệt ở đâu? Bản chạy thử phải gọi AI thật.
3. **Đánh giá & chi phí:** giải pháp đúng được bao nhiêu trên bộ câu thử? Dùng thật ở quy mô thật của sản phẩm thì tốn bao nhiêu mỗi tháng?

- Nhóm **3–5 người**, tự ghép, bầu một đội trưởng. Chưa có nhóm: mục **Đồng đội** trên trang hackathon.
- Khoảng **10 giờ làm thật**: chiều tối Thứ Sáu 27/11 và sáng Thứ Bảy 28/11.
- **6 track:** A EdTech (chính khoá AI20K) · B Y tế · C Du lịch · D Thương mại điện tử · E Tài chính · F Làn khác (lĩnh vực bất kỳ, có insight từ người dùng thật).
- BTC **không cấp API key** cho mọi nhóm. Nhóm dùng gói miễn phí hoặc tài khoản của nhóm (một số credit API là quà của side quest trên trang hackathon).
- Mọi kỹ thuật cần dùng, nhóm đã học trong 15 ngày giai đoạn 1. [02-guide.md](02-guide.md) chỉ rõ bước nào ôn lại ngày nào.

---

## Đọc theo thứ tự này

| # | File | Đọc khi nào | Trong đó có gì |
|---|---|---|---|
| 1 | **README.md** *(file này)* | Đầu buổi Zoom | Tổng quan · checkpoint · chấm điểm · luật |
| 2 | [01-challenge-brief.md](01-challenge-brief.md) | Lúc chọn track | Đề bài: bối cảnh, 6 track, 7 hạng mục bắt buộc, dữ liệu |
| 3 | [tracks/](tracks/README.md): **file của track nhóm chọn** | Ngay sau file 2 | Bối cảnh · người dùng · định hướng ý tưởng · data · công cụ gợi ý |
| 4 | [**02-guide.md**](02-guide.md) | **Mở suốt hai ngày** | Làm từng bước: câu hỏi phải trả lời → làm gì → ra file nào → nộp mốc nào |
| 5 | [03-rubric.md](03-rubric.md) | Trước mỗi checkpoint | Chấm từng phần thế nào |

Đi kèm:
- [starter-repo/](starter-repo/README.md): khung repo nộp bài. Có sẵn thư mục, file mẫu, và lệnh `run.py` chạy bộ câu thử và mô phỏng chi phí.
- [data/](01-challenge-brief.md#data): dữ liệu BTC cấp cho track A (EdTech). Track B–F nhóm tự tìm data.
- [further-reading/](further-reading/README.md): JTBD, phỏng vấn người dùng, HAX, PAIR, bảng giá model.

---

<a id="checkpoint"></a>
## CHECKPOINT

**Mỗi checkpoint nộp trên [trang hackathon](https://ai20k-hackathon.pages.dev), thay cả nhóm.** Đội trưởng đăng ký nhóm một lần (tên nhóm + PIN + mã học viên đội trưởng); ai trong nhóm có PIN cũng nộp thay được. Trang ghi giờ nộp và commit của repo lúc nộp, agent tự kiểm đủ phần trong vài phút.
- Đúng hạn và đủ phần → đủ điểm mốc. Muộn hoặc thiếu → 0 điểm mốc đó.
- Vẫn nộp phần đã có và khai thật phần còn thiếu.
- Tự soát trước khi nộp: bước guide ghi ở từng mốc.

### CP1 · 17:00 Thứ Sáu 27/11 · 3 điểm

- `TEAMS.md` điền đủ thành viên + mã học viên, **đúng format** (đội trưởng ở dòng 1).
- Track (A–F) + bài toán của nhóm trong 1–2 câu: ai, đang làm gì, vướng ở đâu. Không viết chữ AI. Track F kèm thẻ đề.
- Lát cắt dự kiến (1 câu).
- Canvas 7 dòng (`canvas.md`).
- Link repo GitHub công khai, mở được bằng cửa sổ ẩn danh.

Tự soát: [guide 1.4](02-guide.md#b1-4) · **Nộp CP1:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### CP2 · 19:30 Thứ Sáu 27/11 · 4 điểm

- Canvas cập nhật + 1–3 dòng "đã đổi gì so với CP1".
- Nguồn bằng chứng đang làm (đào data / phỏng vấn / khảo sát) và đã làm đến đâu.
- Link `spec.md`, trong §4 có sơ đồ kiến trúc giải pháp.
- Link `eval/benchmark.csv`, ≥10 câu thử. Đã có `eval/metric_spec.yaml` và `data/DATA_CARD.md` bản đầu.
- **Chuẩn "đạt" bằng số**, chép từ `spec.md` §7. **Chốt tại mốc này, không sửa về sau.**
- Bản chạy thử dạng khung: `python run.py` đi hết luồng với AI giả.

Tự soát: [guide 2.5](02-guide.md#b2-5) · **Nộp CP2:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### CP3 · 10:00 Thứ Bảy 28/11 · 4 điểm

- Bằng chứng pain đạt ngưỡng ở ≥1 nguồn + ≥5 trích dẫn / ví dụ nguyên văn. Link `evidence/summary.md`.
- Bộ câu thử 20–30 câu: ≥5 câu `kho`, ≥2 câu `tu_choi`.
- **Video 30 giây:** bản chạy thử gọi AI thật. YouTube để "Không công khai", hoặc Google Drive để "Bất kỳ ai có đường liên kết". Mở thử bằng cửa sổ ẩn danh.
- Kết quả lượt 1 (x/N câu đạt) + run ID.
- Link `spec.md` đã có §0–§7.
- Phần chưa xong, nếu có.

Tự soát: [guide 3.4](02-guide.md#b3-4) · **Nộp CP3:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### CP4 · 14:30 Thứ Bảy 28/11 · 4 điểm

- Phòng demo + link repo.
- Tích 7 hạng mục bắt buộc đã có ([01-challenge-brief](01-challenge-brief.md#7-hang-muc)).
- Kết quả lượt 1 → lượt 2 (ví dụ 14/24 → 18/24).
- Chi phí / task thành công ở kịch bản cơ sở, kèm tên model.
- Slide, định dạng nào cũng được (PDF, PPTX, HTML, Keynote…): file trong repo **hoặc** link slide nộp ở form CP4 (Drive, Canva, Google Slides…, ai có link cũng xem được) · link video demo dự phòng.
- Phần chưa xong, nếu có.

Tự soát: [guide 4.4](02-guide.md#b4-4) · **Nộp CP4:** [trang hackathon → Nộp checkpoint](https://ai20k-hackathon.pages.dev/#submit)

### Hạn chót · 23:59 Thứ Bảy 28/11 · không nộp form

Khoá repo bản cuối:
- Sửa theo góp ý ở buổi demo, mọi thay đổi sau 14:30 ghi vào `spec.md` §10.
- Mỗi người 1 file `reflection/`.

Hướng dẫn: [guide 5.3](02-guide.md#b5-3).

---

## Lịch hai ngày

| Khi nào | Ở đâu | Việc |
|---|---|---|
| Kiểm Python | `python --version` (không được thì `py --version`) | `python3 --version` |
| Chạy bản chạy thử (chế độ giả, chưa gọi model) | `python run.py` | `python3 run.py` |
| Kiểm bộ câu thử | `python run.py check` | `python3 run.py check` |
| Tạo file `.env` để nối model | `copy .env.example .env` | `cp .env.example .env` |

- Windows: gõ `python` mà mở Microsoft Store hoặc báo không có lệnh → dùng `py`. Chưa có Python: cài từ python.org, **tick "Add python.exe to PATH"**, mở lại PowerShell.
- macOS: báo `command not found: python` là bình thường → dùng `python3`.
- `python run.py` in ra "[câu trả lời giả — chưa nối model] …" là khung chạy đúng. Nối model thật: [docs/connect-model.md](docs/connect-model.md).

Trong README này lệnh viết là `python …`; máy nhóm cần `python3` hay `py` thì gõ thay.

## Lệnh

| Lệnh | Làm gì |
|---|---|
| `python run.py` | Chạy bản chạy thử (gõ đầu vào, nhận kết quả, kèm số lần gọi model / token) |
| `python run.py check` | Kiểm `eval/benchmark.csv` (6 cột, số câu, `kho` / `tu_choi`, mã `source`, ô trống, dòng mẫu) `eval/metric_spec.yaml` (≥3 metric điền đủ) và `TEAMS.md` (đúng format để BTC quét). Chỉ cảnh báo, không sửa file |
| `python run.py eval --try` | **Thử nối model:** chạy 3 câu đầu (`--try 5` = 5 câu) → `eval/run-try.csv`. Thấy "Nối model được" là xong. Không tính là một lượt |
| `python run.py eval` | Chạy cả bộ qua `codebase/agent.py` → `eval/run-1.csv` (lần sau `run-2.csv`…) + `traces/run-1.jsonl`. Mỗi dòng có run ID, model, số lần gọi model / công cụ, token. Model còn giả → chỉ ghi `run-mock.csv`; mọi câu lỗi → `run-error.csv`; Ctrl+C → `run-stopped.csv` — đều **không** được đánh số |
| `python run.py eval --fake` | Thử riêng bộ chạy, không gọi agent → `eval/run-fake.csv` |
| `python run.py score eval/run-1.csv` | Sau khi điền cột `pass` (1 / 0): in % đạt tổng và theo `type`. Còn ô trống → "CHƯA CHẤM XONG", không in % |
| `python run.py simulate --try` | Thử mô phỏng chi phí 10 phiên (làm trước CP3) → `cost/simulate-try.csv` |
| `python run.py simulate` | Mô phỏng chi phí khi dùng thật theo `cost/personas.yaml` (≥50 phiên) → `cost/simulate-N.csv` + `cost/simulate-N-summary.md` |
| `python run.py simulate --rate-from eval/run-2.csv` | Như trên, lấy tỉ lệ đạt từ đúng lượt chỉ định. Không ghi thì khung lấy lượt `run-N` mới nhất đã chấm, cùng model, và ghi rõ đã lấy lượt nào trong bản tóm tắt |

Gói miễn phí báo hết lượt: thêm `--wait 4` sau `eval` hoặc `simulate` (nghỉ 4 giây giữa hai lượt gọi). Sửa CSV bằng Excel: *File → Save As → CSV UTF-8*; Google Sheets: *Tệp → Tải xuống → CSV*.

**Lượt có lỗi kỹ thuật** (cột `error` có chữ): không sửa tay file đó, chạy lại thành lượt mới và ghi vào bảng các lượt ở `eval/README.md`. Không xoá file lượt nào.

Nhóm dùng stack khác (Node, Streamlit, notebook…): sửa hàm `run_app()` trong `run.py` để `python run.py` vẫn chạy được bản chạy thử, và giữ `answer()` trong `codebase/agent.py` để `eval`, `simulate` chạy được.

## Bản chạy thử — viết ở đâu

| File | Viết gì | Bước guide |
|---|---|---|
| `codebase/agent.py` | `answer(text)` — luồng chính, đúng hình dạng ở `spec.md` §4. Khung có sẵn một workflow 2 bước *ví dụ* | 3.2 |
| `codebase/tools.py` | Công cụ của bài toán, mỗi công cụ một hàm có `@tool` | 2.2, 3.2 |
| `codebase/ai.py` | `call_model(system, user)` — chỗ duy nhất gọi model. Chưa điền `.env` thì chạy **chế độ giả** | 3.3 |

- **Trước CP2:** để chế độ giả, công cụ trả dữ liệu giả — `python run.py` đi hết luồng là đủ.
- **Trước CP3:** nối model thật theo [docs/connect-model.md](docs/connect-model.md), `eval --try` thấy token > 0 rồi mới `eval`.
- Bộ chạy gửi **nguyên ô `input`** của câu thử vào `answer(text)`. Dữ liệu nền (bài học, thông báo, lịch…) để trong `data/`, đọc qua công cụ.

## Phần nào thật, phần nào giả

| Thành phần | Thật / Giả | Ghi chú |
|---|---|---|
| Lời gọi AI ở quyết định trung tâm | **Thật** (bắt buộc từ CP3) | Model: ____ |
|  |  |  |

## Dùng AI vào việc gì

2–3 dòng (bắt buộc): nhóm dùng công cụ AI nào để làm gì, người kiểm lại phần nào. Chi tiết: [docs/ai-usage.md](docs/ai-usage.md). Coding agent đọc [AGENTS.md](AGENTS.md).

____

## File mẫu — điền ở bước nào

| File | Điền ở bước guide | Mốc |
|---|---|---|
| `TEAMS.md` | 1.0 | CP1 · **đúng format**, BTC quét khi chấm |
| `canvas.md` | 1.4 | CP1, cập nhật CP2 |
| `evidence/hypothesis.md` | 1.1 | trước khi tìm bằng chứng |
| `evidence/data-mining.md` · `evidence/interviews/TEMPLATE.md` → `P1.md`… · `evidence/survey/TEMPLATE.md` | 1.2 | bắt đầu sau Zoom, xong CP3 |
| `evidence/summary.md` | 1.2 | CP3 |
| `spec.md` | §0–§2: 1.1–1.3 · §3–§5: 2.1–2.3 · §7: 2.4 · §8: 4.2 · §10: suốt | §7 chốt CP2 · §0–§7 CP3 · đủ CP4 |
| `data/DATA_CARD.md` | 2.4 | bản đầu CP2 |
| `eval/benchmark.csv` · `eval/metric_spec.yaml` | 2.4 | ≥10 câu + metric chốt CP2 · 20–30 câu CP3 |
| `codebase/` | 3.2, 3.3 | khung CP2 · AI thật CP3 |
| `eval/report.md` · `eval/README.md` | 4.1 (README mục 1–4 từ 2.4) | CP4 |
| `cost/personas.yaml` · `cost/cost-estimate.md` | 4.2 | thử 10 phiên CP3 · đủ CP4 |
| `validation/log.md` *(bonus)* | 4.3 | CP4 |
| `slides/outline.md` → `demo-slides.pdf` | 5.1 | CP4 |
| `reflection/TEMPLATE.md` → `reflection/<ten>.md` | 5.3 | 23:59 Thứ Bảy 28/11 |
| `AGENTS.md` · `docs/ai-usage.md` | khi dùng coding agent / AI | suốt |

## Bảy hạng mục bắt buộc — nằm ở file nào

| # | Hạng mục | File |
|---|---|---|
| 1 | Bằng chứng pain | `evidence/` (tổng hợp ở `evidence/summary.md`) |
| 2 | Impact có số | `spec.md` §2 |
| 3 | Thiết kế giải pháp | `spec.md` §4 |
| 4 | Bản chạy thử làm trọn lát cắt | `codebase/` · lệnh ở mục "Lệnh" |
| 5 | Định nghĩa "tốt" + bộ câu thử | `data/DATA_CARD.md` · `eval/` |
| 6 | Mô phỏng chi phí khi dùng thật | `cost/` |
| 7 | Slide + demo + video dự phòng | slide trong repo (PDF, PPTX, HTML…) hoặc link slide ở form CP4 · link video: ____ |
| + | *Bonus:* người dùng thử | `validation/log.md` |
