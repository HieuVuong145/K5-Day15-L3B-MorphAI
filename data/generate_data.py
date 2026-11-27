"""Script sinh dữ liệu chạy thử (synthetic) cho Khu vui chơi Mẫu — Track C1.

Chạy: python3 data/generate_data.py
Dùng SEED cố định để tái lập chính xác 5 file trong data/:
  - park.json (28 điểm chơi, 7 khu vực)
  - shows.json (8 show diễn)
  - tickets.json (bảng giá vé + combo tham chiếu VinWonders Nha Trang)
  - travel_times.csv (ma trận thời gian đi giữa 7 khu vực)
  - weather.json (dự báo thời tiết 5 ngày)
"""
import csv
import json
import os
import random

SEED = 20261127
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

PARK_NAME = "Khu vui chơi Mẫu"
SOURCE_TEXT = "synthetic (tham chiếu khung giờ/giá VinWonders Nha Trang, xem 2026-11-27)"
UPDATED_AT = "2026-11-27"

ZONES = [
    "Cong_Chinh",
    "Pho_Co_Tich",
    "Cong_Vien_Nuoc",
    "Thuy_Cung_Bien",
    "Doi_Cam_Giac_Manh",
    "Vuon_Thu_Sinh_Thai",
    "Khu_Am_Thuc_Nghi_Ngoi",
]


def build_park(rng: random.Random) -> list:
    """Tạo 28 điểm chơi thuộc 7 khu vực, cài sẵn các chỗ khó theo Phụ lục C và spec.md §4."""
    items = [
        # --- Cong_Chinh (4 điểm) ---
        ("P01", "Quảng trường Nhạc Nước Chào Đón", "Cong_Chinh", "08:30", "20:00", 30, 0, 0, None, False, 0, ["gia_dinh", "chup_anh", "nhe_nhang"]),
        ("P02", "Bảo tàng Ánh Sáng 3D", "Cong_Chinh", "09:00", "19:30", 45, 3, 0, 100, True, 0, ["trong_nha", "tre_em", "gia_dinh", "kham_pha"]),
        ("P03", "Rạp Phim Bay 4D", "Cong_Chinh", "09:30", "19:30", 30, 5, 105, 120, True, 0, ["trong_nha", "gia_dinh", "hieu_ung"]),
        ("P04", "Khu Vui Chơi Liên Hoàn Trong Nhà", "Cong_Chinh", "08:30", "20:00", 60, 2, 80, 110, True, 0, ["trong_nha", "tre_em", "van_dong"]),

        # --- Pho_Co_Tich (4 điểm) ---
        ("P05", "Đu Quay Ngựa Gỗ Hoàng Gia", "Pho_Co_Tich", "09:00", "19:30", 30, 2, 85, 110, False, 0, ["tre_em", "gia_dinh", "nhe_nhang"]),
        ("P06", "Tàu Hỏa Xuyên Rừng Cổ Tích", "Pho_Co_Tich", "09:00", "19:00", 35, 2, 80, 110, False, 0, ["tre_em", "gia_dinh", "ngam_canh"]),
        ("P07", "Ngôi Nhà Kẹo Ngọt & Workshop Tô Tượng", "Pho_Co_Tich", "09:00", "19:00", 45, 3, 0, 100, True, 0, ["trong_nha", "tre_em", "thu_cong"]),
        ("P08", "Lâu Đài Phép Thuật Tương Tác", "Pho_Co_Tich", "09:30", "19:30", 40, 4, 95, 115, True, 0, ["trong_nha", "tre_em", "gia_dinh"]),

        # --- Cong_Vien_Nuoc (4 điểm — đóng cửa sớm lúc 15:00) ---
        ("P09", "Đường Trượt Nước Nhí", "Cong_Vien_Nuoc", "09:00", "15:00", 45, 3, 90, 110, False, 0, ["nuoc", "tre_em", "gia_dinh"]),
        ("P10", "Sông Lười Nhiệt Đới", "Cong_Vien_Nuoc", "09:00", "15:00", 45, 3, 90, 120, False, 0, ["nuoc", "gia_dinh", "thu_gian"]),
        ("P11", "Hồ Tạo Sóng Biển Nhân Tạo", "Cong_Vien_Nuoc", "09:00", "15:00", 60, 4, 100, 125, False, 0, ["nuoc", "gia_dinh"]),
        ("P12", "Ống Trượt Xoáy Lốc Cảm Giác Mạnh", "Cong_Vien_Nuoc", "09:30", "15:00", 40, 10, 130, None, False, 100000, ["nuoc", "cam_giac_manh"]),

        # --- Thuy_Cung_Bien (4 điểm — trong nhà, hợp ngày mưa) ---
        ("P13", "Đường Hầm Đại Dương Thủy Cung", "Thuy_Cung_Bien", "09:00", "19:30", 50, 0, 0, None, True, 0, ["trong_nha", "kham_pha", "gia_dinh", "tre_em"]),
        ("P14", "Khu Vực Chim Cánh Cụt & Sứa Phát Sáng", "Thuy_Cung_Bien", "09:00", "19:30", 35, 0, 0, None, True, 0, ["trong_nha", "tre_em", "gia_dinh", "dong_vat"]),
        # Hai điểm tên gần giống nhau (cố ý)
        ("P15", "Vòng quay Bầu Trời", "Doi_Cam_Giac_Manh", "09:00", "19:30", 30, 8, 120, None, False, 0, ["ngam_canh", "cam_giac_manh"]),
        ("P16", "Vòng quay Mặt Trời", "Thuy_Cung_Bien", "09:00", "20:00", 30, 0, 0, 110, True, 0, ["trong_nha", "ngam_canh", "gia_dinh", "tre_em"]),

        # --- Doi_Cam_Giac_Manh (5 điểm — yêu cầu chiều cao, có phụ phí) ---
        ("P17", "Tàu Lượn Siêu Tốc Đỉnh Đồi", "Doi_Cam_Giac_Manh", "09:00", "19:00", 35, 12, 140, None, False, 0, ["cam_giac_manh", "toc_do"]),
        ("P18", "Tháp Rơi Tự Do 60m", "Doi_Cam_Giac_Manh", "09:30", "18:30", 30, 12, 140, None, False, 0, ["cam_giac_manh"]),
        ("P19", "Đĩa Bay Xoay Tròn", "Doi_Cam_Giac_Manh", "09:00", "19:00", 30, 8, 120, None, False, 0, ["cam_giac_manh"]),
        ("P20", "Đường Trượt Núi Alpine Coaster", "Doi_Cam_Giac_Manh", "09:00", "17:30", 40, 8, 120, 130, False, 150000, ["cam_giac_manh", "ngam_canh"]),
        ("P21", "Đường Trượt Zipline Xuyên Đảo", "Doi_Cam_Giac_Manh", "09:30", "17:00", 45, 14, 140, None, False, 250000, ["cam_giac_manh", "mao_hiem"]),

        # --- Vuon_Thu_Sinh_Thai (4 điểm — đóng cửa sớm 15:00, có 1 điểm phụ phí) ---
        ("P22", "Vườn Hươu Cao Cổ & Thú Hiền", "Vuon_Thu_Sinh_Thai", "08:30", "15:00", 45, 0, 0, 110, False, 0, ["dong_vat", "tre_em", "gia_dinh"]),
        ("P23", "Nhà Kính Bướm & Thực Vật Nhiệt Đới", "Vuon_Thu_Sinh_Thai", "08:30", "15:00", 35, 0, 0, None, True, 0, ["trong_nha", "thien_nhien", "tre_em"]),
        ("P24", "Khu Tương Tác Hải Cẩu", "Vuon_Thu_Sinh_Thai", "09:30", "15:00", 30, 4, 95, 120, False, 120000, ["dong_vat", "tre_em", "gia_dinh"]),
        ("P25", "Đồi Chim Nhiệt Đới", "Vuon_Thu_Sinh_Thai", "08:30", "15:00", 40, 0, 0, None, False, 0, ["dong_vat", "ngam_canh"]),

        # --- Khu_Am_Thuc_Nghi_Ngoi (3 điểm — ăn trưa/nghỉ ngơi, có 1 điểm nguồn cũ) ---
        ("P26", "Nhà Hàng Gia Đình Góc Biển", "Khu_Am_Thuc_Nghi_Ngoi", "10:00", "20:00", 60, 0, 0, None, True, 0, ["trong_nha", "an_uong", "nghi_ngoi", "gia_dinh"]),
        ("P27", "Phòng Nghỉ Điều Hòa Cho Gia Đình Có Bé", "Khu_Am_Thuc_Nghi_Ngoi", "09:00", "19:30", 45, 0, 0, None, True, 0, ["trong_nha", "nghi_ngoi", "tre_em"]),
        ("P28", "Quán Cà Phê Sân Vườn Hoàng Hôn", "Khu_Am_Thuc_Nghi_Ngoi", "14:00", "20:00", 45, 0, 0, None, False, 0, ["an_uong", "nghi_ngoi"]),
    ]

    result = []
    for row in items:
        pid, name, zone, op, cl, dur, min_age, min_h, adult_h, indoor, fee, tags = row
        # P28 cố ý đặt nguồn cũ > 30 ngày (2026-10-01) để test chặn rủi ro nguồn quá cũ
        upd = "2026-10-01" if pid == "P28" else UPDATED_AT
        result.append({
            "id": pid,
            "name": name,
            "park": PARK_NAME,
            "zone": zone,
            "open": op,
            "close": cl,
            "duration_min": dur,
            "min_age": min_age,
            "min_height_cm": min_h,
            "adult_required_under_cm": adult_h,
            "indoor": indoor,
            "extra_fee_vnd": fee,
            "tags": tags,
            "source": SOURCE_TEXT,
            "updated_at": upd,
            "synthetic": True,
        })
    # Dùng rng nhẹ cho metadata thứ tự tham chiếu (không làm thay đổi nội dung)
    _ = rng.random()
    return result


def build_shows() -> list:
    """Tạo 8 show diễn: có show cuối tuần, show ngoài trời huỷ khi mưa, show trong nhà."""
    all_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    weekend = ["Sat", "Sun"]
    items = [
        ("S01", "Diễu Hành Sắc Màu Cổ Tích", "Pho_Co_Tich", "10:30", 25, all_days, False, True),
        ("S02", "Show Biểu Diễn Cá Heo & Hải Cẩu", "Thuy_Cung_Bien", "11:00", 30, all_days, True, False),
        ("S03", "Rối Nước Kể Chuyện Dân Gian", "Cong_Chinh", "14:00", 30, all_days, True, False),
        ("S04", "Vũ Điệu Nhiệt Đới Bên Hồ Sóng", "Cong_Vien_Nuoc", "14:30", 25, weekend, False, True),
        ("S05", "Show Cho Cá Mập Ăn Dưới Thủy Cung", "Thuy_Cung_Bien", "15:30", 25, all_days, True, False),
        ("S06", "Xiếc Tạp Kỹ Trong Nhà Hát Lớn", "Cong_Chinh", "16:30", 35, all_days, True, False),
        ("S07", "Lễ Hội Ánh Sáng & Nhạc Nước Cuối Tuần", "Cong_Chinh", "18:30", 30, weekend, False, True),
        ("S08", "Tata Show Đa Phương Tiện", "Cong_Chinh", "19:30", 35, all_days, False, True),
    ]
    return [
        {
            "id": sid,
            "name": name,
            "park": PARK_NAME,
            "zone": zone,
            "start": start,
            "duration_min": dur,
            "days": days,
            "indoor": indoor,
            "cancel_on_rain": cancel_rain,
            "source": SOURCE_TEXT,
            "updated_at": UPDATED_AT,
            "synthetic": True,
        }
        for sid, name, zone, start, dur, days, indoor, cancel_rain in items
    ]


def build_tickets() -> dict:
    """Tạo bảng giá vé dựng theo khung VinWonders Nha Trang (có ngưỡng 100cm và combo)."""
    return {
        "park": PARK_NAME,
        "currency": "VND",
        "afternoon_cutoff": "16:00",
        "single_tickets": {
            "free_under_cm": 100,
            "child_or_senior": {
                "height_min_cm": 100,
                "height_max_exclusive_cm": 140,
                "senior_min_age": 60,
                "full_day_vnd": 800000,
                "after_16h_vnd": 550000,
            },
            "adult": {
                "height_min_cm": 140,
                "full_day_vnd": 1050000,
                "after_16h_vnd": 700000,
            },
        },
        "combos": [
            {
                "id": "C_FAMILY_2A1C",
                "name": "Combo Gia Đình (2 Người lớn + 1 Trẻ em, cả ngày)",
                "requires": {"adult": 2, "child_or_senior": 1},
                "full_day_only": True,
                "price_vnd": 2650000,
                "note": "Rẻ hơn mua lẻ 250.000đ (2x1.050.000 + 800.000 = 2.900.000đ)",
            },
            {
                "id": "C_GROUP_4A",
                "name": "Combo Nhóm Bạn (4 Người lớn, cả ngày)",
                "requires": {"adult": 4, "child_or_senior": 0},
                "full_day_only": True,
                "price_vnd": 3900000,
                "note": "Rẻ hơn mua lẻ 300.000đ (4x1.050.000 = 4.200.000đ)",
            },
        ],
        "source": SOURCE_TEXT,
        "updated_at": UPDATED_AT,
        "synthetic": True,
    }


def build_travel_times(rng: random.Random) -> list:
    """Tạo ma trận 7x7 thời gian đi (phút) giữa các khu vực; cặp xa nhất 25 phút."""
    base = {
        ("Cong_Chinh", "Pho_Co_Tich"): 6,
        ("Cong_Chinh", "Cong_Vien_Nuoc"): 12,
        ("Cong_Chinh", "Thuy_Cung_Bien"): 8,
        ("Cong_Chinh", "Doi_Cam_Giac_Manh"): 15,
        ("Cong_Chinh", "Vuon_Thu_Sinh_Thai"): 14,
        ("Cong_Chinh", "Khu_Am_Thuc_Nghi_Ngoi"): 5,
        ("Pho_Co_Tich", "Cong_Vien_Nuoc"): 10,
        ("Pho_Co_Tich", "Thuy_Cung_Bien"): 10,
        ("Pho_Co_Tich", "Doi_Cam_Giac_Manh"): 14,
        ("Pho_Co_Tich", "Vuon_Thu_Sinh_Thai"): 12,
        ("Pho_Co_Tich", "Khu_Am_Thuc_Nghi_Ngoi"): 6,
        # Chỗ khó cố ý: hai khu cách nhau 25 phút
        ("Cong_Vien_Nuoc", "Doi_Cam_Giac_Manh"): 25,
        ("Cong_Vien_Nuoc", "Thuy_Cung_Bien"): 15,
        ("Cong_Vien_Nuoc", "Vuon_Thu_Sinh_Thai"): 18,
        ("Cong_Vien_Nuoc", "Khu_Am_Thuc_Nghi_Ngoi"): 10,
        ("Thuy_Cung_Bien", "Doi_Cam_Giac_Manh"): 12,
        ("Thuy_Cung_Bien", "Vuon_Thu_Sinh_Thai"): 10,
        ("Thuy_Cung_Bien", "Khu_Am_Thuc_Nghi_Ngoi"): 7,
        ("Doi_Cam_Giac_Manh", "Vuon_Thu_Sinh_Thai"): 16,
        ("Doi_Cam_Giac_Manh", "Khu_Am_Thuc_Nghi_Ngoi"): 14,
        ("Vuon_Thu_Sinh_Thai", "Khu_Am_Thuc_Nghi_Ngoi"): 11,
    }
    _ = rng.random()
    rows = []
    for z1 in ZONES:
        row = {"zone": z1}
        for z2 in ZONES:
            if z1 == z2:
                row[z2] = 0
            else:
                row[z2] = base.get((z1, z2)) or base.get((z2, z1))
        rows.append(row)
    return rows


def build_weather() -> dict:
    """Tạo dự báo thời tiết 5 ngày, gồm ngày mưa chiều và ngày mưa cả ngày."""
    return {
        "park": PARK_NAME,
        "source": "synthetic (mẫu thời tiết chạy thử)",
        "updated_at": UPDATED_AT,
        "synthetic": True,
        "days": {
            "2026-11-28": {
                "weekday": "Sat",
                "summary": "Sáng nắng, chiều mưa vừa",
                "slots": [
                    {"start": "08:30", "end": "12:00", "status": "nang"},
                    {"start": "12:00", "end": "14:00", "status": "nang"},
                    {"start": "14:00", "end": "17:00", "status": "mua"},
                    {"start": "17:00", "end": "20:00", "status": "nang"},
                ],
            },
            "2026-11-29": {
                "weekday": "Sun",
                "summary": "Nắng đẹp cả ngày",
                "slots": [
                    {"start": "08:30", "end": "12:00", "status": "nang"},
                    {"start": "12:00", "end": "14:00", "status": "nang"},
                    {"start": "14:00", "end": "17:00", "status": "nang"},
                    {"start": "17:00", "end": "20:00", "status": "nang"},
                ],
            },
            "2026-11-30": {
                "weekday": "Mon",
                "summary": "Mưa lớn cả ngày",
                "slots": [
                    {"start": "08:30", "end": "12:00", "status": "mua"},
                    {"start": "12:00", "end": "14:00", "status": "mua"},
                    {"start": "14:00", "end": "17:00", "status": "mua"},
                    {"start": "17:00", "end": "20:00", "status": "mua"},
                ],
            },
            "2026-12-01": {
                "weekday": "Tue",
                "summary": "Nắng nhẹ cả ngày",
                "slots": [
                    {"start": "08:30", "end": "12:00", "status": "nang"},
                    {"start": "12:00", "end": "14:00", "status": "nang"},
                    {"start": "14:00", "end": "17:00", "status": "nang"},
                    {"start": "17:00", "end": "20:00", "status": "nang"},
                ],
            },
            "2026-12-02": {
                "weekday": "Wed",
                "summary": "Nắng đẹp cả ngày",
                "slots": [
                    {"start": "08:30", "end": "12:00", "status": "nang"},
                    {"start": "12:00", "end": "14:00", "status": "nang"},
                    {"start": "14:00", "end": "17:00", "status": "nang"},
                    {"start": "17:00", "end": "20:00", "status": "nang"},
                ],
            },
        },
    }


def main():
    rng = random.Random(SEED)

    park = build_park(rng)
    shows = build_shows()
    tickets = build_tickets()
    travel_rows = build_travel_times(rng)
    weather = build_weather()

    with open(os.path.join(DATA_DIR, "park.json"), "w", encoding="utf-8") as f:
        json.dump(park, f, ensure_ascii=False, indent=2)

    with open(os.path.join(DATA_DIR, "shows.json"), "w", encoding="utf-8") as f:
        json.dump(shows, f, ensure_ascii=False, indent=2)

    with open(os.path.join(DATA_DIR, "tickets.json"), "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=2)

    with open(os.path.join(DATA_DIR, "travel_times.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["zone"] + ZONES)
        writer.writeheader()
        writer.writerows(travel_rows)

    with open(os.path.join(DATA_DIR, "weather.json"), "w", encoding="utf-8") as f:
        json.dump(weather, f, ensure_ascii=False, indent=2)

    print("Đã sinh 5 file data (SEED=%d): %d điểm chơi, %d show, %d khu vực, %d ngày thời tiết."
          % (SEED, len(park), len(shows), len(ZONES), len(weather["days"])))


if __name__ == "__main__":
    main()
