import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "eval"))

import auto_grade  # noqa: E402  # type: ignore[reportMissingImports]


class TestPreferenceGrader(unittest.TestCase):
    def test_unavailable_outdoor_preference_passes_with_weather_reason(self):
        output = (
            "Sở thích hoạt động cảm giác mạnh chưa đáp ứng được: "
            "các điểm phù hợp đều ngoài trời và bị loại do mưa. "
            'JSON lịch: {"lich":[]}'
        )

        self.assertEqual(auto_grade.grade_dung_so_thich("K10", output), (True, ""))

    def test_unavailable_water_preference_passes_with_closed_hours_reason(self):
        output = (
            "Sở thích trò nước chưa đáp ứng được: "
            "các điểm phù hợp đã đóng trước khung giờ bạn chọn. "
            'JSON lịch: {"lich":[{"id":"P27","start":"15:00","end":"15:45"}]}'
        )

        self.assertEqual(auto_grade.grade_dung_so_thich("K23", output), (True, ""))

    def test_unavailable_preference_without_explanation_fails(self):
        output = 'JSON lịch: {"lich":[{"id":"P27","start":"15:00","end":"15:45"}]}'

        passed, reason = auto_grade.grade_dung_so_thich("K23", output)

        self.assertFalse(passed)
        self.assertIn("nuoc", reason)

    def test_feasible_preference_must_appear_in_schedule(self):
        output = (
            "Lịch không có hoạt động cảm giác mạnh nhưng không giải thích lý do. "
            'JSON lịch: {"lich":[{"id":"P27","start":"09:00","end":"09:45"}]}'
        )

        passed, reason = auto_grade.grade_dung_so_thich("K19", output)

        self.assertFalse(passed)
        self.assertIn("cam_giac_manh", reason)


if __name__ == "__main__":
    unittest.main()
