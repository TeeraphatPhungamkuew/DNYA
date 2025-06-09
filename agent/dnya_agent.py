
from vibekit.agent import BaseAgent
from vibekit.interfaces import PendleInterface, GMXInterface, AaveInterface
from utils.strategy import DeltaNeutralStrategy

class DNYAAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        self.pendle = PendleInterface()
        self.gmx = GMXInterface()
        self.aave = AaveInterface()
        self.strategy = DeltaNeutralStrategy(self.pendle, self.gmx, self.aave)

    def on_asset_deposit(self, asset, amount):
        print(f"[Agent] Deposit detected: {amount} {asset}")
        self.strategy.execute(asset, amount)

    def on_interval(self):
        print("[Agent] Running delta check...")
        self.strategy.rebalance_if_needed()
