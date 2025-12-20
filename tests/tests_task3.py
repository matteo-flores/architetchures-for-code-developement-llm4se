class TestTask3:
  """Test Suite for HumanEval/19 - sort_numbers"""

  def __init__(self, sort_numbers):
    self.fun = sort_numbers
  
  def get_benchmark_input(self):
    return ('six five four three two one zero',)

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
        print(f"[DEBUG]: Task 3 - {method_name} failed.")
    
    return tests_passed, total_tests

  def test_01_basic_cases(self):
    assert self.fun('three one five') == 'one three five'
    assert self.fun('five zero four seven nine') == 'zero four five seven nine'
    assert self.fun('six five four three two one') == 'one two three four five six'

  def test_02_positive_case(self):
    assert self.fun('nine zero eight') == 'zero eight nine'

  def test_03_single_number(self):
    assert self.fun('five') == 'five'

  def test_04_repeated_numbers(self):
    assert self.fun('zero zero three one three') == 'zero zero one three three'

  def test_05_empty_string(self):
    assert self.fun('') == ''

  def test_06_wrong_input(self):
    try:
      self.fun('invalid input')
    except (ValueError, Exception):
      pass