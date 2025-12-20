
class TestTask1:
  """Test Suite for HumanEval/0 - has_close_elements"""

  def test_basic_cases(self, has_close_elements):
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
  
  def test_positive_threshold(self, has_close_elements):
    assert has_close_elements([1.0, 2.0, 3.0], 5) == True
  
  def test_empty_list(self, has_close_elements):
    
    assert has_close_elements([], 1) == False
  
  def test_one_element_list(self, has_close_elements):
    assert has_close_elements([1.0], 1) == False
  
  def test_0_distance(self, has_close_elements):
    assert has_close_elements([1.0, 2.0, 3.0], 0) == False

  def test_negative_distance(self, has_close_elements):
    try:
      result = has_close_elements([1.0, 2.0], -1)
      assert result == False
    except ValueError:
      pass