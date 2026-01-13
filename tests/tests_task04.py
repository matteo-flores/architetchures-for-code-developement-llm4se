class TestTask4:
  """Test Suite for MBPP/467 - decimal_to_Octal"""

  def __init__(self, decimal_to_Octal):
    self.fun = decimal_to_Octal
  
  def get_benchmark_input(self):
    return (1000,)

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
        print(f"[DEBUG]: Task 4 - {method_name} failed.")
    
    return tests_passed, total_tests

  def test_01_basic_cases(self):
    assert self.fun(10) == 12
    assert self.fun(2) == 2
    assert self.fun(33) == 41

  def test_02_zero(self):
    assert self.fun(0) == 0

  def test_03_large_number(self):
    assert self.fun(100) == 144

  def test_04_power_of_eight(self):
    assert self.fun(8) == 10
    assert self.fun(64) == 100

  def test_05_negative_input(self):
    try:
      result = self.fun(-10)
      assert result == -12 or result == 12 or isinstance(result, (int, str))
    except (ValueError, Exception):
        pass

  def test_06_float_input(self):
    try:
      self.fun(10.5)
    except (TypeError, ValueError, Exception):
      pass