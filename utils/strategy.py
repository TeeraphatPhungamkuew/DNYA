
class DeltaNeutralStrategy:
    def __init__(self, pendle, gmx, aave):
        self.pendle = pendle
        self.gmx = gmx
        self.aave = aave

    def execute(self, asset, amount):
        pt, yt = self.pendle.deposit_and_split(asset, amount)
        usdc_received = self.pendle.sell_yt(yt)
        print(f"[Strategy] Sold YT for {usdc_received} USDC")
        self.gmx.open_short(asset, pt.amount)

    def rebalance_if_needed(self):
        delta = self.gmx.get_delta_exposure()
        if abs(delta) > 0.05:
            print(f"[Strategy] Rebalancing... delta={delta}")
            self.gmx.rebalance_position(delta)
