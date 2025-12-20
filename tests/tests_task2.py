
class TestTask2:
  """Test Suite for HumanEval/6 - parse_nested_parens"""

  def test_basic_cases(self, parse_nested_parens):
    assert parse_nested_parens('(()) ((()))') == [2, 3]
    assert parse_nested_parens('(()()) ((()))') == [2, 3]

  def test_positive(self, parse_nested_parens):
    assert parse_nested_parens('() ((())) (()(()))') == [1, 3, 3]

  def test_empty_string(self, parse_nested_parens):
    assert parse_nested_parens('') == []

  def test_random_string(self, parse_nested_parens):
    try:
      parse_nested_parens('non a parenthesis')
    except ValueError:
      pass 
  
  def test_wrong_parenthesis(self, parse_nested_parens):
    try:
      parse_nested_parens('(()')
    except ValueError:
      pass