"""Offline parser tests only; fixtures below are synthetic software-test input."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from download_audit import audit_csv


def fixture(*rows):
    head = "LocationID,StateAbbr,MeasureID,Data_Value_Type,Data_Value\n"
    return (head + "".join(rows)).encode("utf-8")


class CDCAuditTests(unittest.TestCase):
    def test_valid_synthetic_rows(self):
        x = fixture(
            "01001,AL,DIABETES,Crude prevalence,13.0\n",
            "01003,AL,DIABETES,Crude prevalence,\n",
            "01001,AL,OBESITY,Crude prevalence,31.5\n",
        )
        result = audit_csv(x)
        self.assertEqual(result["observed_rows"], 3)
        self.assertEqual(result["unique_county_ids"], 2)
        self.assertEqual(result["unique_measure_codes"], 2)
        self.assertEqual(result["missing_data_value_rows"], 1)

    def test_duplicate_key_rejected(self):
        x = fixture(
            "01001,AL,DIABETES,Crude prevalence,13\n",
            "01001,AL,DIABETES,Crude prevalence,14\n",
        )
        with self.assertRaisesRegex(ValueError, "Duplicated"):
            audit_csv(x)

    def test_out_of_range_rejected(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            audit_csv(fixture("01001,AL,DIABETES,Crude prevalence,101\n"))

    def test_no_rows_rejected(self):
        with self.assertRaisesRegex(ValueError, "no rows"):
            audit_csv(fixture())


if __name__ == "__main__":
    unittest.main()
