
class TestTask5:
  """Test Suite for MBPP/13 - count_common"""

  def test_basic_cases(self, count_common):
    assert count_common(['red','green','black','pink','black','white','black','eyes','white','black','orange','pink','pink','red','red','white','orange','white',"black",'pink','green','green','pink','green','pink','white','orange',"orange",'red']) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
    assert count_common(['one', 'two', 'three', 'four', 'five', 'one', 'two', 'one', 'three', 'one']) == [('one', 4), ('two', 2), ('three', 2), ('four', 1)]
    assert count_common(['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google', 'Apple', 'Netflix', 'Amazon']) == [('Apple', 2), ('Amazon', 2), ('Netflix', 2), ('Facebook', 1)]

  def test_empty_list(self, count_common):
    assert count_common([]) == []

  def test_less_than_four_elements(self, count_common):
    result = count_common(['apple', 'apple', 'banana'])
    assert len(result) <= 4
    assert ('apple', 2) in result
    assert ('banana', 1) in result

  def test_tie_frequency(self, count_common):
    result = count_common(['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e'])
    assert len(result) == 4
    for item in result:
      assert item[1] == 2

  def test_single_element_repeated(self, count_common):
    assert count_common(['test', 'test', 'test']) == [('test', 3)]

  def test_non_string_elements(self, count_common):
    assert count_common([1, 1, 2, 2, 2, 3]) == [(2, 3), (1, 2), (3, 1)]