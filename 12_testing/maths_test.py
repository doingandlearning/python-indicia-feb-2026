from maths import add

def test_adding_two_numbers_gives_correct_answer():
  # Arrange     Given
  number1 = 4
  number2 = 5
  expected = 9

  # Act         When
  result = add(number1, number2)

  # Assert      Then
  assert result == expected