import json
from dataclasses import dataclass
from typing import List

@dataclass
class AI_Solution:
    name: str
    cost: float
    performance: float

class CostOptimizer:
    def __init__(self):
        self.solutions = []

    def add_solution(self, solution: AI_Solution):
        self.solutions.append(solution)

    def get_solutions(self) -> List[AI_Solution]:
        return self.solutions

    def compare_solutions(self, needs: dict) -> AI_Solution:
        best_solution = None
        best_score = 0
        for solution in self.solutions:
            score = solution.performance / solution.cost
            if score > best_score and solution.cost <= needs['budget']:
                best_solution = solution
                best_score = score
        return best_solution

    def integrate_solution(self, solution: AI_Solution) -> bool:
        # Simulate integration process
        return True

    def get_catalog(self) -> str:
        catalog = []
        for solution in self.solutions:
            catalog.append({
                'name': solution.name,
                'cost': solution.cost,
                'performance': solution.performance
            })
        return json.dumps(catalog)
