import os
import tempfile

class TestTask10:
  """Test Suite for the complex graph task (FES + DAG Longest Path)"""

  def _create_temp_graph(self, content):
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    temp_file.write(content)
    temp_file.close()
    return temp_file.name

  def test_basic_cycle(self, func):
      """A->B->C->A, removig C->A (20)."""
      content = "3\nA\nB\nC\nA B 10\nB C 5\nC A 20"
      file_path = self._create_temp_graph(content)
      
      try:
          dag, distances = func(file_path)
          
          if 'C' in dag:
              neighbors = [n for n, w in dag['C']]
              assert 'A' not in neighbors, "L'arco C->A non è stato rimosso"
          
          # Verifica distanze nel DAG risultante (A->B->C)
          assert distances['A']['C'] == 15 # 10 (A-B) + 5 (B-C)
          assert distances['B']['C'] == 5
      finally:
          os.remove(file_path)

  def test_no_cycle(self, func):
      content = "2\nX\nY\nX Y 50"
      file_path = self._create_temp_graph(content)
      
      try:
          dag, distances = func(file_path)
          assert distances['X']['Y'] == 50
          assert len(dag['X']) == 1
      finally:
          os.remove(file_path)

  def test_empty_graph(self, func):
      content = "0"
      file_path = self._create_temp_graph(content)
      
      try:
          dag, distances = func(file_path)
          assert dag == {}
          assert distances == {}
      finally:
          os.remove(file_path)

  def test_minimum_cardinality_fes(self, func):
      content = "3\nA\nB\nC\nA B 10\nB C 10\nC A 10"
      file_path = self._create_temp_graph(content)
      
      try:
          dag, distances = func(file_path)
          total_edges = sum(len(neighbors) for neighbors in dag.values())
          assert total_edges == 2
      finally:
          os.remove(file_path)