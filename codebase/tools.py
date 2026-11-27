"""Công cụ của bài toán — Track C1: Lịch trình một ngày ở khu vui chơi.

Mỗi công cụ có @tool và docstring đủ 4 ý:
    tên · input · output · có tác động ra ngoài không.
Tất cả công cụ đều CHỈ ĐỌC dữ liệu từ data/, không có tác động ra ngoài.
"""
import csv
import datetime
import json
import os

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
DEFAULT_TODAY = "2026-11-27"
MAX_SOURCE_AGE_DAYS = 30
TRAVEL_BUFFER_MIN = 5


def _load_json(filename: str):
    with open(os.path.join(DATA_DIR, filename), encoding="utf-8") as f:
        return json.load(f)


def _load_travel_matrix() -> dict:
    matrix = {}
    with open(os.path.join(DATA_DIR, "travel_times.csv"), encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            z1 = row["zone"]
            matrix[z1] = {k: int(v) for k, v in row.items() if k != "zone"}
    return matrix


def _catalog_maps():
    park = _load_json("park.json")
    shows = _load_json("shows.json")
    by_id = {}
    for p in park:
        by_id[p["id"]] = ("park", p)
    for s in shows:
        by_id[s["id"]] = ("show", s)
    return park, shows, by_id


def _to_min(hhmm: str) -> int:
    h, m = hhmm.strip().split(":")
    return int(h) * 60 + int(m)


def _add_min(hhmm: str, minutes: int) -> str:
    total = _to_min(hhmm) + minutes
    return "%02d:%02d" % (total // 60, total % 60)


def _parse_date(date_str: str) -> datetime.date:
    return datetime.date.fromisoformat(date_str.strip())


def _weekday_short(date_str: str) -> str:
    names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return names[_parse_date(date_str).weekday()]


def _check_group_eligibility(item: dict, nhom_di: list) -> list:
    """Kiểm tra tuổi, chiều cao và yêu cầu người lớn đi cùng cho một điểm chơi."""
    reasons = []
    if not nhom_di:
        return reasons
    has_adult = any(int(m.get("tuoi", 0)) >= 18 for m in nhom_di)
    min_age = item.get("min_age", 0)
    min_h = item.get("min_height_cm", 0)
    adult_under_h = item.get("adult_required_under_cm")

    for idx, m in enumerate(nhom_di, start=1):
        age = int(m.get("tuoi", 0))
        height = int(m.get("chieu_cao_cm", 0))
        if age < min_age:
            reasons.append("Thành viên %d (%d tuổi) chưa đạt tuổi tối thiểu %d" % (idx, age, min_age))
        if height < min_h:
            reasons.append("Thành viên %d (%d cm) chưa đạt chiều cao tối thiểu %d cm" % (idx, height, min_h))
        if adult_under_h is not None and height < adult_under_h and not has_adult:
            reasons.append("Thành viên %d (%d cm < %d cm) cần có người lớn (≥18 tuổi) đi cùng"
                           % (idx, height, adult_under_h))
    return reasons


@tool
def tra_diem_choi(khu: str = "Khu vui chơi Mẫu", nhom_di: list = None) -> dict:
    """tra_diem_choi: Tra danh sách điểm chơi tại khu vui chơi mẫu và kiểm tra độ phù hợp với nhóm.
    Input: khu (str, tên khu vui chơi hoặc tên phân khu), nhom_di (list dict {tuoi, chieu_cao_cm}, tuỳ chọn).
    Output: dict gồm danh sách điểm chơi kèm giờ mở/đóng, thời lượng, phụ phí, nguồn, ngày cập nhật và trạng thái phù hợp.
    Không tác động ra ngoài."""
    park = _load_json("park.json")
    khu_clean = (khu or "").strip()
    if khu_clean and khu_clean.lower() not in ("khu vui chơi mẫu", "tat_ca", "all"):
        filtered = [p for p in park if p["zone"].lower() == khu_clean.lower() or khu_clean.lower() in p["park"].lower()]
        # Nếu khớp tên phân khu thì chỉ lấy phân khu đó, ngược lại giữ nguyên kết quả lọc
        zone_exact = [p for p in park if p["zone"].lower() == khu_clean.lower()]
        if zone_exact:
            filtered = zone_exact
    else:
        filtered = list(park)

    items = []
    for p in filtered:
        reasons = _check_group_eligibility(p, nhom_di or [])
        entry = dict(p)
        entry["phu_hop_nhom"] = len(reasons) == 0
        entry["ly_do_khong_phu_hop"] = reasons
        items.append(entry)

    return {
        "park": "Khu vui chơi Mẫu",
        "count": len(items),
        "items": items,
        "synthetic": True,
    }


@tool
def tra_lich_show(ngay: str) -> dict:
    """tra_lich_show: Tra danh sách các show biểu diễn hoạt động trong ngày được chọn.
    Input: ngay (str, định dạng YYYY-MM-DD).
    Output: dict gồm thứ trong tuần và danh sách show (id, name, zone, start, duration_min, cancel_on_rain, source, updated_at).
    Không tác động ra ngoài."""
    shows = _load_json("shows.json")
    wd = _weekday_short(ngay)
    active = [s for s in shows if wd in s.get("days", [])]
    return {
        "ngay": ngay,
        "weekday": wd,
        "count": len(active),
        "shows": active,
        "synthetic": True,
    }


@tool
def uoc_thoi_gian_di(a: str, b: str) -> dict:
    """uoc_thoi_gian_di: Ước lượng thời gian di chuyển (phút) giữa hai điểm chơi/show hoặc hai khu vực.
    Input: a (str, ID điểm/show hoặc tên khu vực), b (str, ID điểm/show hoặc tên khu vực).
    Output: dict gồm zone_from, zone_to, minutes (int), buffer_min (int), synthetic (bool).
    Không tác động ra ngoài."""
    _, _, by_id = _catalog_maps()
    matrix = _load_travel_matrix()

    def _resolve_zone(ref: str) -> str:
        ref_clean = ref.strip()
        if ref_clean in by_id:
            return by_id[ref_clean][1]["zone"]
        if ref_clean in matrix:
            return ref_clean
        raise ValueError("Không tìm thấy điểm hoặc khu vực: %s" % ref)

    z1 = _resolve_zone(a)
    z2 = _resolve_zone(b)
    minutes = matrix[z1][z2]
    buffer_min = TRAVEL_BUFFER_MIN if minutes > 0 else 0
    return {
        "from": a,
        "to": b,
        "zone_from": z1,
        "zone_to": z2,
        "minutes": minutes,
        "buffer_min": buffer_min,
        "synthetic": True,
        "source": "synthetic (ma trận thời gian di chuyển nội khu)",
    }


@tool
def tra_thoi_tiet(ngay: str) -> dict:
    """tra_thoi_tiet: Tra dự báo thời tiết theo từng khung giờ trong ngày.
    Input: ngay (str, định dạng YYYY-MM-DD).
    Output: dict gồm summary, danh sách slots ({start, end, status: nang|mua}), hoặc thông báo chưa có dữ liệu.
    Không tác động ra ngoài."""
    weather = _load_json("weather.json")
    day_info = weather.get("days", {}).get(ngay.strip())
    if not day_info:
        return {
            "ngay": ngay,
            "co_du_lieu": False,
            "slots": [],
            "message": "Chưa có dữ liệu thời tiết cho ngày %s" % ngay,
            "synthetic": True,
        }
    return {
        "ngay": ngay,
        "co_du_lieu": True,
        "weekday": day_info["weekday"],
        "summary": day_info["summary"],
        "slots": day_info["slots"],
        "source": weather["source"],
        "updated_at": weather["updated_at"],
        "synthetic": True,
    }


@tool
def tinh_tong_tien(lich: list, nhom_di: list, khung_gio: dict = None) -> dict:
    """tinh_tong_tien: Tính tổng tiền vé cổng (tự so sánh mua lẻ với combo) và phụ phí các điểm trong lịch.
    Input: lich (list dict có id), nhom_di (list dict {tuoi, chieu_cao_cm}), khung_gio (dict {start, end}, tuỳ chọn).
    Output: dict gồm tong_cong_vnd, tien_ve_vnd, phu_phi_vnd, ap_dung_combo, chi_tiet_nguoi, source.
    Không tác động ra ngoài."""
    tickets = _load_json("tickets.json")
    _, _, by_id = _catalog_maps()
    single = tickets["single_tickets"]
    cutoff = tickets.get("afternoon_cutoff", "16:00")

    after_16h = False
    if khung_gio and khung_gio.get("start"):
        after_16h = _to_min(khung_gio["start"]) >= _to_min(cutoff)

    counts = {"free": 0, "child_or_senior": 0, "adult": 0}
    chi_tiet_nguoi = []
    single_total = 0

    for idx, m in enumerate(nhom_di or [], start=1):
        age = int(m.get("tuoi", 0))
        height = int(m.get("chieu_cao_cm", 0))
        if height < single["free_under_cm"]:
            cat = "free"
            price = 0
        elif height < single["child_or_senior"]["height_max_exclusive_cm"] or age >= single["child_or_senior"]["senior_min_age"]:
            cat = "child_or_senior"
            price = single["child_or_senior"]["after_16h_vnd" if after_16h else "full_day_vnd"]
        else:
            cat = "adult"
            price = single["adult"]["after_16h_vnd" if after_16h else "full_day_vnd"]

        counts[cat] += 1
        single_total += price
        chi_tiet_nguoi.append({
            "thanh_vien": idx,
            "tuoi": age,
            "chieu_cao_cm": height,
            "loai_ve": cat,
            "gia_le_vnd": price,
        })

    # Tính phương án combo (chỉ áp dụng cho vé cả ngày)
    best_ticket_total = single_total
    applied_combos = []
    if not after_16h:
        rem_a = counts["adult"]
        rem_cs = counts["child_or_senior"]
        combo_cost = 0
        # Ưu tiên combo khớp và tiết kiệm nhiều nhất
        combos_sorted = sorted(tickets.get("combos", []), key=lambda c: c["price_vnd"])
        # Thử áp dụng combo lặp lại khi đủ người và rẻ hơn giá lẻ tương ứng
        changed = True
        while changed:
            changed = False
            best_choice = None
            best_saving = 0
            for c in combos_sorted:
                req_a = c["requires"].get("adult", 0)
                req_cs = c["requires"].get("child_or_senior", 0)
                if rem_a >= req_a and rem_cs >= req_cs:
                    retail_eq = (
                        req_a * single["adult"]["full_day_vnd"]
                        + req_cs * single["child_or_senior"]["full_day_vnd"]
                    )
                    saving = retail_eq - c["price_vnd"]
                    if saving > best_saving:
                        best_saving = saving
                        best_choice = c
            if best_choice is not None:
                rem_a -= best_choice["requires"].get("adult", 0)
                rem_cs -= best_choice["requires"].get("child_or_senior", 0)
                combo_cost += best_choice["price_vnd"]
                applied_combos.append(best_choice["name"])
                changed = True

        leftover_cost = (
            rem_a * single["adult"]["full_day_vnd"]
            + rem_cs * single["child_or_senior"]["full_day_vnd"]
        )
        if applied_combos and (combo_cost + leftover_cost) < best_ticket_total:
            best_ticket_total = combo_cost + leftover_cost
        else:
            applied_combos = []

    # Tính phụ phí các điểm trong lịch
    phu_phi = 0
    phu_phi_chi_tiet = []
    n_people = len(nhom_di or [])
    for item in lich or []:
        item_id = item.get("id")
        if item_id in by_id:
            kind, meta = by_id[item_id]
            if kind == "park" and meta.get("extra_fee_vnd", 0) > 0:
                part_count = len(item["participants"]) if "participants" in item else n_people
                cost = meta["extra_fee_vnd"] * part_count
                phu_phi += cost
                phu_phi_chi_tiet.append({"id": item_id, "name": meta["name"], "so_nguoi": part_count, "tien_vnd": cost})

    return {
        "tien_ve_vnd": best_ticket_total,
        "tien_ve_mua_le_vnd": single_total,
        "phu_phi_vnd": phu_phi,
        "tong_cong_vnd": best_ticket_total + phu_phi,
        "ap_dung_combo": applied_combos,
        "ve_chieu_toi": after_16h,
        "chi_tiet_nguoi": chi_tiet_nguoi,
        "phu_phi_chi_tiet": phu_phi_chi_tiet,
        "source": tickets["source"],
        "updated_at": tickets["updated_at"],
        "synthetic": True,
    }


@tool
def kiem_lich_trinh(
    lich: list,
    nhom_di: list,
    khung_gio: dict,
    ngan_sach: int,
    ngay: str = None,
    today: str = None,
    so_thich: list = None,
) -> dict:
    """kiem_lich_trinh: Kiểm tra toàn bộ ràng buộc cứng/mềm của lịch trình và tính tổng tiền, mức cần nới bằng code.
    Input: lich (list dict {id, start, end}), nhom_di (list dict {tuoi, chieu_cao_cm}), khung_gio ({start, end}), ngan_sach (int), ngay (str, tuỳ chọn), today (str, tuỳ chọn), so_thich (list str, tuỳ chọn).
    Output: dict gồm hop_le (bool), vi_pham_cung (list), vi_pham_mem (list), tong_tien (dict), goi_y_noi (list).
    Không tác động ra ngoài."""
    _, _, by_id = _catalog_maps()
    matrix = _load_travel_matrix()
    weather = _load_json("weather.json")

    hard_errors = []
    soft_warnings = []
    suggestions = []

    ref_today = _parse_date(today or DEFAULT_TODAY)
    win_start = _to_min(khung_gio["start"])
    win_end = _to_min(khung_gio["end"])

    day_slots = []
    wd = None
    if ngay:
        wd = _weekday_short(ngay)
        day_info = weather.get("days", {}).get(ngay.strip())
        if day_info:
            day_slots = day_info.get("slots", [])

    # Chuẩn bị danh sách mục hợp lệ để kiểm tra thứ tự thời gian
    valid_entries = []
    matched_tags = set()

    for idx, item in enumerate(lich or []):
        item_id = item.get("id", "")
        if item_id not in by_id:
            hard_errors.append({
                "loai": "id_khong_ton_tai",
                "id": item_id,
                "chi_tiet": "Mục #%d có ID '%s' không tồn tại trong dữ liệu." % (idx + 1, item_id),
            })
            suggestions.append("Bỏ ID không hợp lệ '%s' và chọn từ danh sách tra_diem_choi/tra_lich_show." % item_id)
            continue

        kind, meta = by_id[item_id]
        matched_tags.update(meta.get("tags", []))

        # 1. Kiểm tra nguồn còn mới (<= 30 ngày)
        upd_date = _parse_date(meta["updated_at"])
        age_days = (ref_today - upd_date).days
        if age_days > MAX_SOURCE_AGE_DAYS:
            hard_errors.append({
                "loai": "nguon_qua_cu",
                "id": item_id,
                "chi_tiet": "%s (%s) có ngày cập nhật %s (cũ %d ngày > %d ngày)."
                            % (item_id, meta["name"], meta["updated_at"], age_days, MAX_SOURCE_AGE_DAYS),
            })
            suggestions.append("Không dùng %s (%s) vì dữ liệu đã cũ quá %d ngày." % (item_id, meta["name"], MAX_SOURCE_AGE_DAYS))

        # 2. Kiểm tra khung giờ người dùng
        s_min = _to_min(item["start"])
        e_min = _to_min(item["end"])
        if e_min <= s_min:
            hard_errors.append({
                "loai": "khung_gio",
                "id": item_id,
                "chi_tiet": "%s có giờ kết thúc (%s) <= giờ bắt đầu (%s)." % (item_id, item["end"], item["start"]),
            })
        elif s_min < win_start or e_min > win_end:
            hard_errors.append({
                "loai": "khung_gio",
                "id": item_id,
                "chi_tiet": "%s (%s–%s) nằm ngoài khung giờ của nhóm (%s–%s)."
                            % (item_id, item["start"], item["end"], khung_gio["start"], khung_gio["end"]),
            })
            suggestions.append("Điều chỉnh %s vào trong khung %s–%s hoặc nới khung giờ."
                               % (item_id, khung_gio["start"], khung_gio["end"]))

        # 3. Kiểm tra giờ mở cửa hoặc lịch show
        if kind == "park":
            op_min = _to_min(meta["open"])
            cl_min = _to_min(meta["close"])
            if s_min < op_min or e_min > cl_min:
                hard_errors.append({
                    "loai": "gio_mo_cua",
                    "id": item_id,
                    "chi_tiet": "%s (%s) mở cửa %s–%s, không khớp giờ xếp %s–%s."
                                % (item_id, meta["name"], meta["open"], meta["close"], item["start"], item["end"]),
                })
                suggestions.append("Đẩy %s lên trước %s hoặc thay bằng điểm mở muộn hơn." % (item_id, meta["close"]))
        else:
            show_start = _to_min(meta["start"])
            show_end = show_start + meta["duration_min"]
            if wd and wd not in meta.get("days", []):
                hard_errors.append({
                    "loai": "gio_show",
                    "id": item_id,
                    "chi_tiet": "Show %s (%s) chỉ diễn vào %s, không diễn ngày %s (%s)."
                                % (item_id, meta["name"], ", ".join(meta["days"]), ngay, wd),
                })
                suggestions.append("Bỏ show %s vào ngày %s hoặc đổi sang ngày cuối tuần." % (item_id, ngay))
            if s_min != show_start or e_min < show_end:
                hard_errors.append({
                    "loai": "gio_show",
                    "id": item_id,
                    "chi_tiet": "Show %s diễn đúng %s–%s, không khớp %s–%s."
                                % (item_id, meta["start"], _add_min(meta["start"], meta["duration_min"]), item["start"], item["end"]),
                })

        # 4. Kiểm tra tuổi / chiều cao / người lớn đi cùng
        if kind == "park":
            elig_reasons = _check_group_eligibility(meta, nhom_di)
            for r in elig_reasons:
                hard_errors.append({
                    "loai": "tuoi_chieu_cao",
                    "id": item_id,
                    "chi_tiet": "%s (%s): %s." % (item_id, meta["name"], r),
                })
            if elig_reasons:
                suggestions.append("Bỏ %s (%s) vì không phù hợp tuổi/chiều cao trong nhóm." % (item_id, meta["name"]))

        # 5. Kiểm tra thời tiết mưa
        if day_slots:
            is_outdoor = (not meta["indoor"]) if kind == "park" else meta.get("cancel_on_rain", False)
            if is_outdoor:
                for slot in day_slots:
                    if slot["status"] == "mua":
                        sl_s = _to_min(slot["start"])
                        sl_e = _to_min(slot["end"])
                        if max(s_min, sl_s) < min(e_min, sl_e):
                            hard_errors.append({
                                "loai": "thoi_tiet_mua",
                                "id": item_id,
                                "chi_tiet": "%s (%s) ở ngoài trời/huỷ khi mưa nhưng khung %s–%s ngày %s có mưa."
                                            % (item_id, meta["name"], slot["start"], slot["end"], ngay),
                            })
                            suggestions.append("Đổi %s sang điểm trong nhà (như Thủy Cung hoặc Rạp Phim 4D) trong khung mưa %s–%s."
                                               % (item_id, slot["start"], slot["end"]))
                            break

        valid_entries.append((s_min, e_min, item_id, meta, item))

    # 6. Kiểm tra chồng giờ & thời gian di chuyển + đệm
    valid_entries.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(valid_entries) - 1):
        s1, e1, id1, meta1, raw1 = valid_entries[i]
        s2, e2, id2, meta2, raw2 = valid_entries[i + 1]
        if s2 < e1:
            hard_errors.append({
                "loai": "chong_gio",
                "id": "%s->%s" % (id1, id2),
                "chi_tiet": "%s (%s–%s) bị chồng giờ với %s (%s–%s)."
                            % (id1, raw1["start"], raw1["end"], id2, raw2["start"], raw2["end"]),
            })
            suggestions.append("Tách giờ giữa %s và %s để không bị trùng." % (id1, id2))
            continue

        travel = matrix[meta1["zone"]][meta2["zone"]]
        buffer_min = TRAVEL_BUFFER_MIN if travel > 0 else 0
        needed = travel + buffer_min
        gap = s2 - e1
        if gap < needed:
            hard_errors.append({
                "loai": "thoi_gian_di_chuyen",
                "id": "%s->%s" % (id1, id2),
                "chi_tiet": "Từ %s (%s) sang %s (%s) cần %d phút đi + %d phút đệm = %d phút, nhưng chỉ chừa %d phút."
                            % (id1, meta1["zone"], id2, meta2["zone"], travel, buffer_min, needed, gap),
            })
            suggestions.append("Dời %s muộn thêm ít nhất %d phút (từ %s trở đi)."
                               % (id2, needed - gap, _add_min(raw1["end"], needed)))

    # 7. Kiểm tra ngân sách bằng code (tinh_tong_tien)
    cost_info = tinh_tong_tien(lich, nhom_di, khung_gio)
    tong_tien = cost_info["tong_cong_vnd"]
    if tong_tien > ngan_sach:
        thieu = tong_tien - ngan_sach
        hard_errors.append({
            "loai": "ngan_sach",
            "id": "BUDGET",
            "chi_tiet": "Tổng chi phí %s VNĐ vượt ngân sách %s VNĐ (thiếu %s VNĐ)."
                        % ("{:,}".format(tong_tien), "{:,}".format(ngan_sach), "{:,}".format(thieu)),
        })
        suggestions.append("Cần nới ngân sách thêm ít nhất %s VNĐ (tổng tối thiểu %s VNĐ) hoặc bỏ điểm có phụ phí/chọn vé chiều tối sau 16:00."
                           % ("{:,}".format(thieu), "{:,}".format(tong_tien)))

    # 8. Ràng buộc mềm: nghỉ cho trẻ <= 6 tuổi khi đi > 4 tiếng, và sở thích
    has_young_child = any(int(m.get("tuoi", 99)) <= 6 for m in (nhom_di or []))
    if has_young_child and (win_end - win_start) > 240:
        has_rest = any(
            ("nghi_ngoi" in meta.get("tags", []) or "an_uong" in meta.get("tags", [])) and (e - s) >= 45
            for s, e, _, meta, _ in valid_entries
        )
        if not has_rest:
            soft_warnings.append("Nhóm có trẻ ≤ 6 tuổi đi hơn 4 tiếng nhưng chưa có khoảng ăn/nghỉ ≥ 45 phút.")

    if so_thich:
        missing_pref = [pref for pref in so_thich if pref not in matched_tags]
        if missing_pref:
            soft_warnings.append("Lịch chưa có điểm nào khớp sở thích: %s." % ", ".join(missing_pref))

    # Loại trùng gợi ý nhưng giữ nguyên thứ tự
    unique_suggestions = list(dict.fromkeys(suggestions))

    return {
        "hop_le": len(hard_errors) == 0,
        "vi_pham_cung": hard_errors,
        "vi_pham_mem": soft_warnings,
        "tong_tien": cost_info,
        "goi_y_noi": unique_suggestions,
    }


@tool
def search_example(query: str) -> list:
    """search_example: (tạm giữ để tương thích với agent.py hiện tại) Tìm nhanh điểm chơi mẫu theo từ khoá.
    Input: query (str). Output: danh sách dict {code, text}. Không tác động ra ngoài."""
    park = _load_json("park.json")
    q = (query or "").lower()
    matched = [p for p in park if q in p["name"].lower() or any(t in q for t in p.get("tags", []))]
    sample = (matched or park)[:5]
    return [
        {
            "code": p["id"],
            "text": "%s (%s, %s–%s, ≥%d cm, phụ phí %dđ)" % (p["name"], p["zone"], p["open"], p["close"], p["min_height_cm"], p["extra_fee_vnd"]),
        }
        for p in sample
    ]
