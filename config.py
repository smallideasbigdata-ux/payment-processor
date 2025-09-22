"""Configuration management"""

import os
from dataclasses import dataclass

@dataclass
class NetworkConfig:
    """Network configuration settings"""
    rpc_url: str
    network_id: int
    explorer_url: str

# Network configurations
NETWORKS = {
    "mainnet": NetworkConfig(
        rpc_url="https://mainnet.infura.io",
        network_id=1,
        explorer_url="https://etherscan.io"
    ),
    "testnet": NetworkConfig(
        rpc_url="https://ropsten.infura.io",
        network_id=3,
        explorer_url="https://ropsten.etherscan.io"
    )
}

def get_network_config(network: str) -> NetworkConfig:
    """Get configuration for specified network"""
    return NETWORKS.get(network, NETWORKS["testnet"])
