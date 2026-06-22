import json
import builtins
from dataclasses import dataclass
from typing import List

@dataclass
class CostOptimizer:
    def optimize(self, costs: List[float]) -> float:
        return sum(costs) / len(costs)

def main():
    optimizer = CostOptimizer()
    costs = [10.0, 20.0, 30.0]
    optimized_cost = optimizer.optimize(costs)
    print(f"Optimized cost: {optimized_cost}")

if __name__ == "__main__":
    main()
