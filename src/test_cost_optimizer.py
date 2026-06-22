import unittest
from src.cost_optimizer import CostOptimizer

class TestCostOptimizer(unittest.TestCase):
    def test_optimize(self):
        optimizer = CostOptimizer()
        costs = [10.0, 20.0, 30.0]
        optimized_cost = optimizer.optimize(costs)
        self.assertAlmostEqual(optimized_cost, 20.0)

if __name__ == "__main__":
    unittest.main()
