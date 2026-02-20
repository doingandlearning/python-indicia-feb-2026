from maths import add
import pytest

def test_adding_two_numbers_gives_correct_answer():
  # Arrange     Given
  number1 = 4
  number2 = 5
  expected = 9

  # Act         When
  result = add(number1, number2)

  # Assert      Then
  assert result == expected

def test_adding_two_negative_numbers_gives_correct_answer():
  assert add(-2, -2) == -4


# big numbers
# small numbers
# negative, positive
# positive, negative
# decimals 

# parameterized testing
# decorator
@pytest.mark.parametrize("num1, num2, expected", [
  (1_000_000, 1_000_000, 2_000_000),
  (1,1,2),
  (-10, 5, -5),
  (10, -5, 5)
])
def test_adding_various_numbers_gives_correct_answer(num1, num2, expected):
  assert add(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
  (0.1, 0.1, 0.2),
  (-0.1, -0.1, -0.2),
  (-1_000_000.4, -1_000_000.4, -2_000_000.8)
])
def test_adding_float_numbers_gives_correct_answer(num1, num2, expected):
  assert pytest.approx(add(num1, num2)) == expected

def test_raises_error_when_trying_to_add_two_strings():
  with pytest.raises(TypeError):
    add("1", "1")

@pytest.mark.parametrize("arg1, arg2", [
  ([], []),
  ({}, {}),
  ([], 2),
  (2, []),
  (True, True),
  ((), [])
])
def test_raises_error_when_trying_to_add_two_non_numbers(arg1, arg2):
  with pytest.raises(TypeError):
    add(arg1, arg2)
