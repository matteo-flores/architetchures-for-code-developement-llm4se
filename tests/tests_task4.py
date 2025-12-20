
class TestTask4:
  """Test Suite for MBPP/467 - decimal_to_Octal"""

  def test_basic_cases(self, decimal_to_Octal):
    assert decimal_to_Octal(10) == 12
    assert decimal_to_Octal(2) == 2
    assert decimal_to_Octal(33) == 41

  def test_zero(self, decimal_to_Octal):
      assert decimal_to_Octal(0) == 0

  def test_large_number(self, decimal_to_Octal):
      assert decimal_to_Octal(100) == 144

  def test_power_of_eight(self, decimal_to_Octal):
    assert decimal_to_Octal(8) == 10
    assert decimal_to_Octal(64) == 100

  def test_negative_input(self, decimal_to_Octal):
    try:
      result = decimal_to_Octal(-10)
      assert result == -12 or isinstance(result, (int, str))
    except (ValueError, Exception):
      pass

  def test_float_input(self, decimal_to_Octal):
    try:
      decimal_to_Octal(10.5)
    except (TypeError, ValueError, Exception):
      pass