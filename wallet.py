from hathor.wallet import Wallet
from hathor.wallet.base_wallet import WalletOutputInfo
from hathor.wallet.util import generate_private_key
import json
import os
from typing import Dict, List, Optional

class LearnAndEarnWallet:
    def __init__(self, wallet_path: str = "wallet_data"):
        self.wallet_path = wallet_path
        self.wallet = None
        self.initialize_wallet()

    def initialize_wallet(self):
        """Initialize or load the wallet"""
        if not os.path.exists(self.wallet_path):
            os.makedirs(self.wallet_path)
            self.wallet = Wallet(generate_private_key())
            self.save_wallet()
        else:
            self.load_wallet()

    def save_wallet(self):
        """Save wallet data to file"""
        if self.wallet:
            wallet_data = {
                "private_key": self.wallet.private_key.hex(),
                "address": self.wallet.get_address()
            }
            with open(os.path.join(self.wallet_path, "wallet.json"), "w") as f:
                json.dump(wallet_data, f)

    def load_wallet(self):
        """Load wallet data from file"""
        try:
            with open(os.path.join(self.wallet_path, "wallet.json"), "r") as f:
                wallet_data = json.load(f)
                self.wallet = Wallet(bytes.fromhex(wallet_data["private_key"]))
        except FileNotFoundError:
            self.initialize_wallet()

    def get_balance(self) -> float:
        """Get the current token balance"""
        # This is a simplified version. In a real implementation,
        # you would query the Hathor network for the actual balance
        return 100.0  # Placeholder balance

    def send_tokens(self, to_address: str, amount: float) -> bool:
        """Send tokens to another address"""
        try:
            # In a real implementation, you would create and broadcast
            # a transaction to the Hathor network
            return True
        except Exception as e:
            print(f"Error sending tokens: {e}")
            return False

    def get_transaction_history(self) -> List[Dict]:
        """Get transaction history"""
        # This is a placeholder. In a real implementation,
        # you would query the Hathor network for actual transactions
        return [
            {
                "type": "reward",
                "description": "Quiz completion reward",
                "amount": 10.0,
                "date": "2024-03-20"
            }
        ]

    def export_address(self) -> str:
        """Export the wallet address"""
        return self.wallet.get_address()

# Create a singleton instance
wallet = LearnAndEarnWallet() 