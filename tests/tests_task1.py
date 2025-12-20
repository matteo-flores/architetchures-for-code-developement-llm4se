class TestTask1:
  """Test Suite for HumanEval/0 - has_close_elements"""

  def __init__(self, has_cloese_elements):
    self.fun = has_cloese_elements

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
          print(f"[DEBUG]: {method_name} failed: {e}")
    
    return tests_passed, total_tests

  def test_01_basic_cases(self):
    assert self.fun([1.0, 2.0, 3.0], 0.5) == False
    assert self.fun([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

  def test_02_positive_threshold(self):
    assert self.fun([1.0, 2.0, 3.0], 5) == True

  def test_03_empty_list(self):
    assert self.fun([], 1) == False

  def test_04_one_element_list(self):
    assert self.fun([1.0], 1) == False

  def test_05_zero_distance(self):
    assert self.fun([1.0, 2.0, 3.0], 0) == False

  def test_06_negative_distance(self):
    try:
      result = self.fun([1.0, 2.0], -1)
      assert result == False
    except ValueError:
        pass