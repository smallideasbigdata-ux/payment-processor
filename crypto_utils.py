#!/usr/bin/env python3
"""Utilities for cryptocurrency operations"""

import hashlib
import ecdsa
from typing import Optional

class CryptoValidator:
    """Validates cryptocurrency addresses and transactions"""
    
    @staticmethod
    def validate_btc_address(address: str) -> bool:
        """Validate Bitcoin address format"""
        if len(address) < 26 or len(address) > 35:
            return False
        return address.startswith(('1', '3', 'bc1'))
    
    @staticmethod
    def validate_eth_address(address: str) -> bool:
        """Validate Ethereum address format"""
        if not address.startswith('0x'):
            return False
        return len(address) == 42

class TransactionBuilder:
    """Build cryptocurrency transactions"""
    
    def __init__(self):
        self.fees = {"btc": 0.0001, "eth": 0.002}
        
    def estimate_fee(self, crypto_type: str) -> float:
        return self.fees.get(crypto_type, 0.001)
