class TestTask2:
  """Test Suite for HumanEval/6 - parse_nested_parens"""

  def __init__(self, parse_nested_parens):
    self.fun = parse_nested_parens

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
        print(f"[DEBUG]: Task 2 - {method_name} failed.")
    
    return tests_passed, total_tests

  def test_01_basic_cases(self):
    assert self.fun('(()) ((()))') == [2, 3]
    assert self.fun('(()()) ((()))') == [2, 3]

  def test_02_positive(self):
    assert self.fun('() ((())) (()(()))') == [1, 3, 3]

  def test_03_empty_string(self):
    assert self.fun('') == []

  def test_04_random_string(self):
    try:
      self.fun('non a parenthesis')
    except (ValueError, Exception):
      pass 

  def test_05_wrong_parenthesis(self):
    try:
      self.fun('(()')
    except (ValueError, Exception):
      pass

  def test_06_single_group(self):
    assert self.fun('((((()))))') == [5]