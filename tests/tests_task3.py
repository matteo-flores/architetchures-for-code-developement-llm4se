
class TestTask3:
  """Test Suite for HumanEval/19 - sort_numbers"""

  def test_basic_cases(self, sort_numbers):
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('five zero four seven nine') == 'zero four five seven nine'
    assert sort_numbers('six five four three two one') == 'one two three four five six'

  def test_positive_case(self, sort_numbers):
    assert sort_numbers('nine zero eight') == 'zero eight nine'

  def test_single_number(self, sort_numbers):
    assert sort_numbers('five') == 'five'

  def test_repeated_numbers(self, sort_numbers):
    assert sort_numbers('zero zero three one three') == 'zero zero one three three'
  
  def test_empty_string(self, sort_numbers):
    assert sort_numbers('') == ''
  
  def test_wrong_input(self, sort_numbers):
    try:
      sort_numbers('invalid input')
    except ValueError:
      pass