class TestTask5:
  """Test Suite for MBPP/13 - count_common"""

  def __init__(self, count_common):
    self.fun = count_common

  def get_benchmark_input(self):
    return (['apple', 'banana', 'orange', 'apple', 'apple', 'banana', 'grapes', 'kiwi', 'pear', 'apple'],)

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
        print(f"[DEBUG]: Task 5 - {method_name} failed.")
    
    return tests_passed, total_tests

  def test_01_basic_cases(self):
    assert self.fun(['red','green','black','pink','black','white','black','eyes','white','black','orange','pink','pink','red','red','white','orange','white',"black",'pink','green','green','pink','green','pink','white','orange',"orange",'red']) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
    assert self.fun(['one', 'two', 'three', 'four', 'five', 'one', 'two', 'one', 'three', 'one']) == [('one', 4), ('two', 2), ('three', 2), ('four', 1)]
    assert self.fun(['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google', 'Apple', 'Netflix', 'Amazon']) == [('Apple', 2), ('Amazon', 2), ('Netflix', 2), ('Facebook', 1)]

  def test_02_empty_list(self):
    assert self.fun([]) == []

  def test_03_less_than_four(self):
    result = self.fun(['apple', 'apple', 'banana'])
    assert len(result) <= 4

  def test_04_tie_frequency(self):
    result = self.fun(['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'])
    for item in result:
      assert item[1] == 2