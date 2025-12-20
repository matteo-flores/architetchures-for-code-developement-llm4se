
class TestTask10:
  """Test Suite for the complex graph task (FES + DAG Longest Path)"""

  def __init__(self, solve_graph):
    self.fun = solve_graph

  def execute_tests(self):
    tests_passed = 0
    test_methods = [method for method in dir(self) if method.startswith('test_')]
    total_tests = len(test_methods)
    
    for method_name in test_methods:
      method = getattr(self, method_name)
      try:
        method()
        tests_passed += 1
      except Exception:
        print(f"[DEBUG]: Task 10 - {method_name} failed.")
    
    return tests_passed, total_tests

  def get_benchmark_input(self):
    return ("3\nA\nB\nC\nA B 10\nB C 5\nC A 20",)

  def test_01_basic_cycle(self):
    content = "3\nA\nB\nC\nA B 10\nB C 5\nC A 20"
    dag, distances = self.fun(content)
    if 'C' in dag:
      neighbors = [n for n, w in dag['C']]
      assert 'A' not in neighbors
    assert distances['A']['C'] == 15

  def test_02_no_cycle(self):
    content = "2\nX\nY\nX Y 50"
    dag, distances = self.fun(content)
    assert distances['X']['Y'] == 50

  def test_03_minimum_cardinality(self):
    content = "3\nA\nB\nC\nA B 10\nB C 10\nC A 10"
    dag, distances = self.fun(content)
    total_edges = sum(len(neighbors) for neighbors in dag.values())
    assert total_edges == 2