import json
from cost_optimizer import CostOptimizer, AI_Solution

def test_add_solution():
    optimizer = CostOptimizer()
    solution = AI_Solution('Test Solution', 100.0, 0.9)
    optimizer.add_solution(solution)
    assert len(optimizer.get_solutions()) == 1

def test_compare_solutions():
    optimizer = CostOptimizer()
    solution1 = AI_Solution('Solution 1', 100.0, 0.9)
    solution2 = AI_Solution('Solution 2', 200.0, 0.95)
    optimizer.add_solution(solution1)
    optimizer.add_solution(solution2)
    needs = {'budget': 150.0}
    best_solution = optimizer.compare_solutions(needs)
    assert best_solution.name == 'Solution 1'

def test_integrate_solution():
    optimizer = CostOptimizer()
    solution = AI_Solution('Test Solution', 100.0, 0.9)
    assert optimizer.integrate_solution(solution) == True

def test_get_catalog():
    optimizer = CostOptimizer()
    solution1 = AI_Solution('Solution 1', 100.0, 0.9)
    solution2 = AI_Solution('Solution 2', 200.0, 0.95)
    optimizer.add_solution(solution1)
    optimizer.add_solution(solution2)
    catalog = optimizer.get_catalog()
    assert len(json.loads(catalog)) == 2
