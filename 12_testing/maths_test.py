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