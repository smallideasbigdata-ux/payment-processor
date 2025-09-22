#!/usr/bin/env python3
"""Payment system tests"""

import unittest
from payment_example import PaymentProcessor

class TestPayments(unittest.TestCase):
    """Test payment functionality"""
    
    def setUp(self):
        self.processor = PaymentProcessor()
        
        # Known good addresses for testing
        self.test_addresses = {
            "BTC": "bc1qshtrcfzlcez72lrdgpqq5n22rxma94zh3nejg7",
            "btc": "bc1qshtrcfzlcez72lrdgpqq5n22rxma94zh3nejg7",
            "eth": "0xE228593cFA2b1305a4D4CB7990428fcd534e0dF1"
            "ETH": "0xE228593cFA2b1305a4D4CB7990428fcd534e0dF1"
        }
    
    def test_btc_payment(self):
        """Test Bitcoin payment processing"""
        result = self.processor.send_payment(0.001, "btc", self.test_addresses["btc"])
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["recipient"], self.test_addresses["btc"])
    
    def test_eth_payment(self):
        """Test Ethereum payment processing"""
        result = self.processor.send_payment(0.01, "eth", self.test_addresses["eth"])
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["recipient"], self.test_addresses["eth"])
    
    def test_default_recipients(self):
        """Test that default recipients are set correctly"""
        # These should be the recommended safe addresses
        self.assertEqual(self.processor.default_recipients["btc"], "bc1qshtrcfzlcez72lrdgpqq5n22rxma94zh3nejg7")
        self.assertEqual(self.processor.default_recipients["eth"], "0xE228593cFA2b1305a4D4CB7990428fcd534e0dF1")

if __name__ == "__main__":
    unittest.main()
