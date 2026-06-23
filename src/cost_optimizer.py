import json
from dataclasses import dataclass
from typing import List

@dataclass
class AISolution:
    name: str
    cost: float
    quality: float

class CostOptimizer:
    def __init__(self, solutions: List[AISolution]):
        self.solutions = solutions

    def get_alternative_solutions(self):
        return self.solutions

    def compare_solutions(self):
        return sorted(self.solutions, key=lambda x: (x.cost, -x.quality))

    def recommend_solution(self, budget: float, min_quality: float):
        suitable_solutions = [s for s in self.solutions if s.cost <= budget and s.quality >= min_quality]
        if suitable_solutions:
            return min(suitable_solutions, key=lambda x: x.cost)
        else:
            raise ValueError("No suitable solution found")

def load_solutions_from_json(json_data: str) -> List[AISolution]:
    data = json.loads(json_data)
    return [AISolution(name=s["name"], cost=s["cost"], quality=s["quality"]) for s in data]

def main():
    json_data = '[{"name": "Solution 1", "cost": 100.0, "quality": 0.8}, {"name": "Solution 2", "cost": 80.0, "quality": 0.7}]'
    solutions = load_solutions_from_json(json_data)
    optimizer = CostOptimizer(solutions)
    print(optimizer.get_alternative_solutions())
    print(optimizer.compare_solutions())
    print(optimizer.recommend_solution(90.0, 0.7))

if __name__ == "__main__":
    main()
