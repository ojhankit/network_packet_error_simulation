# tests/test_parity.py

import unittest
from utils.parity import apply_parity, verify_parity

class TestParity(unittest.TestCase):

    def test_apply_parity_even(self):
        # Test that applies parity to even number of ones
        message = "101010"
        result = apply_parity(message)
        self.assertEqual(result, "1010101")  # Parity bit should be added as 1 (even parity)

    def test_apply_parity_odd(self):
        # Test that applies parity to odd number of ones
        message = "101011"
        result = apply_parity(message)
        self.assertEqual(result, "1010110")  # Parity bit should be added as 0 (even parity)

    def test_verify_parity_valid(self):
        # Test verifying parity for a valid message
        message = "1010101"  # even number of 1s, parity bit 1
        result = verify_parity(message)
        self.assertTrue(result)  # Should return True as it's a valid message

    def test_verify_parity_invalid(self):
        # Test verifying parity for an invalid (corrupted) message
        message = "1010110"  # even number of 1s, parity bit 0 (corrupted)
        result = verify_parity(message)
        self.assertFalse(result)  # Should return False as the message is corrupted

if __name__ == '__main__':
    unittest.main()
