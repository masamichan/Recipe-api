"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_number(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

    def test_subtract_numbers(self):
        """Test substructing numbers."""
        res = calc.substract(10, 5)

        self.assertEqual(res, 5)
