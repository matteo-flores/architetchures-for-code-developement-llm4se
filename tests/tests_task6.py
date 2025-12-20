class TestTask6:
  """Test Suite for MBPP/775 - odd_position"""

  def __init__(self, odd_position):
    self.fun = odd_position

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
        print(f"[DEBUG]: Task 6 - {method_name} failed.")
    
    return tests_passed, total_tests

  def test_01_basic_cases(self):
    assert self.fun([2, 1, 4, 3, 6, 7, 6, 3]) == True
    assert self.fun([4, 1, 2]) == True
    assert self.fun([1, 2, 3]) == False

  def test_02_empty_list(self):
    assert self.fun([]) == True

  def test_03_single_element(self):
    assert self.fun([2]) == True
    assert self.fun([1]) == True

  def test_04_large_list(self):
    nums = [0, 1] * 50
    assert self.fun(nums) == True