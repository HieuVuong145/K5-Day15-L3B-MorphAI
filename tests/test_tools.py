"""Unit test cho bộ công cụ Track C1 trong codebase/tools.py."""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "codebase"))

import tools  # noqa: E402


class TestTools(unittest.TestCase):
    def setUp(self):
        self.family = [
            {"tuoi": 34, "chieu_cao_cm": 170},
            {"tuoi": 32, "chieu_cao_cm": 158},
            {"tuoi": 5, "chieu_cao_cm": 110},
        ]
        self.adults_2 = [
            {"tuoi": 25, "chieu_cao_cm": 172},
            {"tuoi": 24, "chieu_cao_cm": 162},
        ]

    def test_valid_family_schedule_with_combo(self):
        lich = [
            {"id": "P09", "start": "09:15", "end": "10:00"},
            {"id": "P26", "start": "11:00", "end": "12:00"},
            {"id": "P13", "start": "13:00", "end": "13:50"},
            {"id": "S05", "start": "15:30", "end": "15:55"},
        ]
        res = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.family,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-11-29",
            today="2026-11-27",
            so_thich=["nuoc"],
        )
        self.assertTrue(res["hop_le"], res["vi_pham_cung"])
        self.assertEqual(res["vi_pham_mem"], [])
        self.assertEqual(res["tong_tien"]["tong_cong_vnd"], 2_650_000)
        self.assertEqual(res["tong_tien"]["tien_ve_mua_le_vnd"], 2_900_000)

    def test_invalid_unknown_id(self):
        lich = [{"id": "P999", "start": "09:30", "end": "10:15"}]
        res = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.family,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-11-29",
        )
        self.assertFalse(res["hop_le"])
        loai = [e["loai"] for e in res["vi_pham_cung"]]
        self.assertIn("id_khong_ton_tai", loai)

    def test_invalid_early_closing_time(self):
        lich = [{"id": "P09", "start": "15:15", "end": "16:00"}]
        res = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.family,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-11-29",
        )
        self.assertFalse(res["hop_le"])
        loai = [e["loai"] for e in res["vi_pham_cung"]]
        self.assertIn("gio_mo_cua", loai)

    def test_invalid_height_limit(self):
        # P15 ("Vòng quay Bầu Trời") yêu cầu >= 120 cm, bé cao 110 cm
        lich = [{"id": "P15", "start": "10:00", "end": "10:30"}]
        res = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.family,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-11-29",
        )
        self.assertFalse(res["hop_le"])
        loai = [e["loai"] for e in res["vi_pham_cung"]]
        self.assertIn("tuoi_chieu_cao", loai)
        self.assertTrue(len(res["goi_y_noi"]) > 0)

    def test_invalid_travel_time_and_buffer(self):
        # Cong_Vien_Nuoc -> Doi_Cam_Giac_Manh mất 25p + 5p đệm = 30p, chừa 10p phải báo lỗi
        lich = [
            {"id": "P09", "start": "10:00", "end": "10:45"},
            {"id": "P17", "start": "10:55", "end": "11:30"},
        ]
        res = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.adults_2,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-11-29",
        )
        self.assertFalse(res["hop_le"])
        loai = [e["loai"] for e in res["vi_pham_cung"]]
        self.assertIn("thoi_gian_di_chuyen", loai)

    def test_invalid_budget_and_relaxation_suggestion(self):
        lich = [{"id": "P01", "start": "09:30", "end": "10:00"}]
        res = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.adults_2,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=500_000,
            ngay="2026-11-29",
        )
        self.assertFalse(res["hop_le"])
        loai = [e["loai"] for e in res["vi_pham_cung"]]
        self.assertIn("ngan_sach", loai)
        self.assertTrue(any("1,600,000" in g for g in res["goi_y_noi"]))

    def test_invalid_rain_and_weekend_show(self):
        # S04: 14:30-14:55, ngoài trời (huỷ khi mưa), chỉ diễn Sat/Sun
        lich = [{"id": "S04", "start": "14:30", "end": "14:55"}]
        # 2026-11-28 là Thứ Bảy nhưng mưa chiều 14:00-17:00
        res_rain = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.family,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-11-28",
        )
        self.assertFalse(res_rain["hop_le"])
        self.assertIn("thoi_tiet_mua", [e["loai"] for e in res_rain["vi_pham_cung"]])

        # 2026-12-02 là Thứ Tư nắng -> lỗi show chỉ diễn cuối tuần
        res_weekday = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.family,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-12-02",
        )
        self.assertFalse(res_weekday["hop_le"])
        self.assertIn("gio_show", [e["loai"] for e in res_weekday["vi_pham_cung"]])

    def test_invalid_stale_source(self):
        # P28 cố ý đặt updated_at = 2026-10-01 (> 30 ngày so với 2026-11-27)
        lich = [{"id": "P28", "start": "14:30", "end": "15:15"}]
        res = tools.kiem_lich_trinh(
            lich=lich,
            nhom_di=self.adults_2,
            khung_gio={"start": "09:00", "end": "17:00"},
            ngan_sach=3_000_000,
            ngay="2026-11-29",
            today="2026-11-27",
        )
        self.assertFalse(res["hop_le"])
        self.assertIn("nguon_qua_cu", [e["loai"] for e in res["vi_pham_cung"]])

    def test_ticket_height_boundary_99_vs_100(self):
        t99 = tools.tinh_tong_tien([], [{"tuoi": 4, "chieu_cao_cm": 99}])
        t100 = tools.tinh_tong_tien([], [{"tuoi": 4, "chieu_cao_cm": 100}])
        self.assertEqual(t99["tien_ve_vnd"], 0)
        self.assertEqual(t100["tien_ve_vnd"], 800_000)


if __name__ == "__main__":
    unittest.main()
