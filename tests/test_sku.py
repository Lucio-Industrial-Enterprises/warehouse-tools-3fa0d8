import unittest

from warehouse.sku import normalize_sku


class SkuTests(unittest.TestCase):
    def test_canonical_sku(self):
        for value, expected in (
            (" a-12 ", "A-12"),
            ("\tAb-12c\n", "AB-12C"),
            ("A-12", "A-12"),
        ):
            with self.subTest(value=value):
                self.assertEqual(normalize_sku(value), expected)

    def test_blank_sku(self):
        for value in ("", "  ", "\t\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_sku(value)
