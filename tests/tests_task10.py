import os
import tempfile

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
      except Exception as e:
        print(f"[DEBUG]: Task 10 - {method_name} failed.")
    
    return tests_passed, total_tests

  def _create_temp_graph(self, content):
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    temp_file.write(content)
    temp_file.close()
    return temp_file.name

  def test_01_basic_cycle(self):
    content = "3\nA\nB\nC\nA B 10\nB C 5\nC A 20"
    file_path = self._create_temp_graph(content)
    try:
      dag, distances = self.fun(file_path)
      if 'C' in dag:
        neighbors = [n for n, w in dag['C']]
        assert 'A' not in neighbors
      assert distances['A']['C'] == 15
      assert distances['B']['C'] == 5
    finally:
      os.remove(file_path)

  def test_02_no_cycle(self):
    content = "2\nX\nY\nX Y 50"
    file_path = self._create_temp_graph(content)
    try:
      dag, distances = self.fun(file_path)
      assert distances['X']['Y'] == 50
      assert len(dag['X']) == 1
    finally:
      os.remove(file_path)

  def test_03_empty_graph(self):
    content = "0"
    file_path = self._create_temp_graph(content)
    try:
      dag, distances = self.fun(file_path)
      assert dag == {}
      assert distances == {}
    finally:
      os.remove(file_path)

  def test_04_minimum_cardinality_fes(self):
    content = "3\nA\nB\nC\nA B 10\nB C 10\nC A 10"
    file_path = self._create_temp_graph(content)
    try:
      dag, distances = self.fun(file_path)
      total_edges = sum(len(neighbors) for neighbors in dag.values())
      assert total_edges == 2
    finally:
      os.remove(file_path)

  def test_05_source_nodes_identification(self):
    content = "3\nA\nB\nC\nA B 10\nB C 5"
    file_path = self._create_temp_graph(content)
    try:
      dag, distances = self.fun(file_path)
      assert 'A' in distances
      assert distances['A']['B'] == 10
      assert distances['A']['C'] == 15
    finally:
      os.remove(file_path)