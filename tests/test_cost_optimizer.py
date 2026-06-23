from cost_optimizer import AISolution, CostOptimizer, load_solutions_from_json

def test_load_solutions_from_json():
    json_data = '[{"name": "Solution 1", "cost": 100.0, "quality": 0.8}, {"name": "Solution 2", "cost": 80.0, "quality": 0.7}]'
    solutions = load_solutions_from_json(json_data)
    assert len(solutions) == 2
    assert solutions[0].name == "Solution 1"
    assert solutions[0].cost == 100.0
    assert solutions[0].quality == 0.8

def test_get_alternative_solutions():
    solutions = [AISolution("Solution 1", 100.0, 0.8), AISolution("Solution 2", 80.0, 0.7)]
    optimizer = CostOptimizer(solutions)
    alternative_solutions = optimizer.get_alternative_solutions()
    assert len(alternative_solutions) == 2
    assert alternative_solutions[0].name == "Solution 1"
    assert alternative_solutions[0].cost == 100.0
    assert alternative_solutions[0].quality == 0.8

def test_compare_solutions():
    solutions = [AISolution("Solution 1", 100.0, 0.8), AISolution("Solution 2", 80.0, 0.7)]
    optimizer = CostOptimizer(solutions)
    compared_solutions = optimizer.compare_solutions()
    assert len(compared_solutions) == 2
    assert compared_solutions[0].name == "Solution 2"
    assert compared_solutions[0].cost == 80.0
    assert compared_solutions[0].quality == 0.7

def test_recommend_solution():
    solutions = [AISolution("Solution 1", 100.0, 0.8), AISolution("Solution 2", 80.0, 0.7)]
    optimizer = CostOptimizer(solutions)
    recommended_solution = optimizer.recommend_solution(90.0, 0.7)
    assert recommended_solution.name == "Solution 2"
    assert recommended_solution.cost == 80.0
    assert recommended_solution.quality == 0.7

def test_recommend_solution_no_suitable():
    solutions = [AISolution("Solution 1", 100.0, 0.8), AISolution("Solution 2", 80.0, 0.7)]
    optimizer = CostOptimizer(solutions)
    try:
        optimizer.recommend_solution(50.0, 0.9)
        assert False
    except ValueError as e:
        assert str(e) == "No suitable solution found"
