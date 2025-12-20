
class TestTask6:
  """Test Suite for MBPP/775 - odd_position"""

  def test_basic_cases(self, odd_position):
    assert odd_position([2, 1, 4, 3, 6, 7, 6, 3]) == True
    assert odd_position([4, 1, 2]) == True
    assert odd_position([1, 2, 3]) == False

  def test_empty_list(self, odd_position):
    assert odd_position([]) == True

  def test_single_element_even(self, odd_position):
    assert odd_position([2]) == True

  def test_single_element_odd(self, odd_position):
    assert odd_position([1]) == True

  def test_fail_at_first_odd_index(self, odd_position):
    assert odd_position([0, 2, 0]) == False

  def test_large_list(self, odd_position):
    nums = [0, 1] * 50
    assert odd_position(nums) == True

  def test_non_integer_input(self, odd_position):
    try:
      odd_position([2, "1", 4])
    except (TypeError, Exception):
      pass