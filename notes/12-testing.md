# 12: Testing with pytest

## Why this matters

Testing ensures your code works correctly and prevents bugs. Good tests:
- Catch errors before users do
- Document how code should work
- Enable safe refactoring
- Build confidence in your code

---

## 1) Introduction to pytest

### What is pytest?
- Popular Python testing framework
- Simple syntax, powerful features
- Automatically discovers and runs tests
- Provides detailed failure messages

### Installing pytest
```bash
pip install pytest
```

### Basic test structure
```python
# test_maths.py
from maths import add
import pytest

def test_adding_two_numbers_gives_correct_answer():
    # Arrange - Set up test data
    number1 = 4
    number2 = 5
    expected = 9
    
    # Act - Execute the code being tested
    result = add(number1, number2)
    
    # Assert - Verify the result
    assert result == expected
```

### Test naming conventions
- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Descriptive names explain what's being tested

---

## 2) Writing Basic Tests

### Simple assertions
```python
def test_adding_two_negative_numbers_gives_correct_answer():
    assert add(-2, -2) == -4
```

### Testing multiple scenarios
```python
def test_shipping_with_low_cost_comes_back_with_standard_rate():
    assert calculate_shipping(5) == 3.99

def test_shipping_with_low_cost_and_express_comes_back_right():
    assert calculate_shipping(5, "express") == 7.99

def test_shipping_above_50_should_give_0():
    assert calculate_shipping(100) == 0
```

### Key points:
- Each test should test one thing
- Use descriptive test names
- Tests should be independent (can run in any order)

---

## 3) Parameterized Tests

### Why parameterize?
- Test multiple scenarios with one function
- Reduce code duplication
- Easy to add new test cases

### Basic parameterization
```python
@pytest.mark.parametrize("num1, num2, expected", [
    (1_000_000, 1_000_000, 2_000_000),
    (1, 1, 2),
    (-10, 5, -5),
    (10, -5, 5)
])
def test_adding_various_numbers_gives_correct_answer(num1, num2, expected):
    assert add(num1, num2) == expected
```

### How it works:
- `@pytest.mark.parametrize` decorator goes before function
- First argument: comma-separated parameter names as string
- Second argument: list of tuples with test data
- pytest runs the test once for each tuple

### Multiple parameterized tests
```python
@pytest.mark.parametrize("num1, num2, expected", [
    (0.1, 0.1, 0.2),
    (-0.1, -0.1, -0.2),
    (-1_000_000.4, -1_000_000.4, -2_000_000.8)
])
def test_adding_float_numbers_gives_correct_answer(num1, num2, expected):
    assert pytest.approx(add(num1, num2)) == expected
```

---

## 4) Testing Floating-Point Numbers

### The problem with floats
```python
# This might fail due to floating-point precision
assert 0.1 + 0.2 == 0.3  # False! (0.30000000000000004)
```

### Solution: `pytest.approx()`
```python
# Use pytest.approx() for floating-point comparisons
assert pytest.approx(0.1 + 0.2) == 0.3  # True!

# With tolerance
assert pytest.approx(add(0.1, 0.1), abs=0.01) == 0.2
```

### Why it matters:
- Floating-point arithmetic has precision limits
- `pytest.approx()` handles small rounding errors
- `abs=0.01` sets absolute tolerance (difference allowed)

---

## 5) Testing Exceptions

### Testing that errors are raised
```python
def test_raises_error_when_trying_to_add_two_strings():
    with pytest.raises(TypeError):
        add("1", "1")
```

### How `pytest.raises()` works:
- Context manager that expects an exception
- Test passes if exception is raised
- Test fails if no exception (or wrong exception)

### Parameterized exception tests
```python
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
```

### Checking error messages
```python
def test_raises_error_with_specific_message():
    with pytest.raises(ValueError, match="Customer ID is required"):
        create_order("", items)
```

- `match` parameter checks error message contains text
- Useful for verifying descriptive error messages

---

## 6) Testing Functions with Default Parameters

### Testing default values
```python
def test_shipping_with_low_cost_comes_back_with_standard_rate():
    # Uses default shipping_method="standard"
    assert calculate_shipping(5) == 3.99
```

### Testing explicit parameters
```python
def test_shipping_with_low_cost_and_express_comes_back_right():
    assert calculate_shipping(5, "express") == 7.99

def test_shipping_with_low_cost_and_overnight_comes_back_right():
    assert calculate_shipping(5, "overnight") == 12.99
```

### Testing keyword arguments
```python
def test_shipping_above_set_max_should_give_0():
    assert calculate_shipping(10, free_shipping_threshold=5) == 0
```

---

## 7) Testing Edge Cases

### Boundary conditions
```python
# Test at the threshold
def test_shipping_above_50_should_give_0():
    assert calculate_shipping(100) == 0

# Test exactly at threshold
def test_shipping_at_threshold():
    assert calculate_shipping(50) == 0  # or 3.99 depending on >= vs >
```

### Common edge cases to test:
- Zero values
- Negative values
- Very large numbers
- Empty lists/strings
- Boundary conditions (>= vs >)
- Default parameter values

---

## 8) Test-Driven Development (TDD)

### What is TDD?
Test-Driven Development is a development approach where you:
1. **Write tests first** (before the code)
2. **Write code** to make tests pass
3. **Refactor** to improve code quality

### The TDD Cycle: Red → Green → Refactor

```
┌─────────┐
│   RED   │  Write a failing test
└────┬────┘
     │
     ▼
┌─────────┐
│  GREEN  │  Write minimal code to pass
└────┬────┘
     │
     ▼
┌──────────┐
│ REFACTOR │  Improve code (tests still pass)
└──────────┘
```

### Example: Building `calculate_shipping()` with TDD

#### Step 1: Write the test first (RED)
```python
# function_test.py
from function import calculate_shipping

# We know what we want: calculate_shipping(5) -> 3.99
def test_shipping_with_low_cost_comes_back_with_standard_rate():
    assert calculate_shipping(5) == 3.99
```

**Run the test** - it fails because `calculate_shipping()` doesn't exist yet!

#### Step 2: Write minimal code to pass (GREEN)
```python
# function.py
def calculate_shipping(subtotal, shipping_method="standard", free_shipping_threshold=50):
    return 3.99  # Minimal code to make test pass
```

**Run the test** - it passes! ✅

#### Step 3: Add more tests, then implement
```python
# Add more test cases
def test_shipping_with_low_cost_and_express_comes_back_right():
    assert calculate_shipping(5, "express") == 7.99

def test_shipping_with_low_cost_and_overnight_comes_back_right():
    assert calculate_shipping(5, "overnight") == 12.99

def test_shipping_above_50_should_give_0():
    assert calculate_shipping(100) == 0
```

**Run tests** - they fail! Now implement the full function:

```python
# function.py
def calculate_shipping(subtotal, shipping_method="standard", free_shipping_threshold=50):
    if subtotal > free_shipping_threshold:
        return 0
    
    if shipping_method == "express":
        return 7.99
    elif shipping_method == "overnight":
        return 12.99
    return 3.99
```

**Run tests** - all pass! ✅

#### Step 4: Refactor (if needed)
- Improve code structure
- Add comments
- Optimize logic
- Tests ensure nothing breaks!

### Benefits of TDD

1. **Clear requirements** - Tests document what code should do
2. **Better design** - Writing tests first helps think about the interface
3. **Confidence** - Know immediately if changes break things
4. **Documentation** - Tests show how code should be used
5. **Fewer bugs** - Catch issues early

### TDD Workflow Example

```python
# 1. Start with a comment describing what you want
# calculate_shipping(5) -> 3.99

# 2. Write the test
def test_shipping_with_low_cost_comes_back_with_standard_rate():
    assert calculate_shipping(5) == 3.99

# 3. Run test (fails - function doesn't exist)
# 4. Write function stub
def calculate_shipping(subtotal, shipping_method="standard", free_shipping_threshold=50):
    pass  # Will fail, but now function exists

# 5. Write minimal implementation
def calculate_shipping(subtotal, shipping_method="standard", free_shipping_threshold=50):
    return 3.99  # Simplest thing that works

# 6. Test passes! Add more tests...
# 7. Implement full functionality
# 8. All tests pass!
```

### Key TDD Principles

- **Write tests first** - Before implementation
- **Make it work, then make it right** - Get tests passing, then refactor
- **Small steps** - One test at a time
- **Run tests frequently** - After each small change
- **Keep tests passing** - Don't break existing tests

### When to use TDD

- ✅ New features
- ✅ Bug fixes (write test that reproduces bug first)
- ✅ Refactoring (tests ensure you don't break things)
- ✅ Complex logic (helps think through edge cases)

---

## 9) Running Tests

### Command line
```bash
# Run all tests in current directory
pytest

# Run specific test file
pytest test_maths.py

# Verbose output (shows test names)
pytest -v

# Stop on first failure
pytest -x

# Show print statements
pytest -s
```

### Programmatic execution
```python
# run_tests.py
import pytest

if __name__ == "__main__":
    pytest.main(["-v", "test_maths.py"])
```

---

## 10) Test Organization

### Arrange-Act-Assert pattern
```python
def test_adding_two_numbers_gives_correct_answer():
    # Arrange - Set up test data (Given)
    number1 = 4
    number2 = 5
    expected = 9
    
    # Act - Execute the code (When)
    result = add(number1, number2)
    
    # Assert - Verify the result (Then)
    assert result == expected
```

### Benefits:
- Clear structure
- Easy to understand
- Separates setup, execution, verification

### One assertion per test (when possible)
```python
# Good - tests one thing
def test_shipping_standard():
    assert calculate_shipping(5) == 3.99

def test_shipping_express():
    assert calculate_shipping(5, "express") == 7.99

# Also acceptable - related assertions
def test_shipping_methods():
    assert calculate_shipping(5) == 3.99
    assert calculate_shipping(5, "express") == 7.99
    assert calculate_shipping(5, "overnight") == 12.99
```

---

## 11) Common Testing Patterns

### Testing return values
```python
def test_function_returns_correct_value():
    result = calculate_shipping(5)
    assert result == 3.99
```

### Testing exceptions
```python
def test_function_raises_error():
    with pytest.raises(TypeError):
        add("1", "2")
```

### Testing multiple conditions
```python
def test_shipping_all_methods():
    assert calculate_shipping(5, "standard") == 3.99
    assert calculate_shipping(5, "express") == 7.99
    assert calculate_shipping(5, "overnight") == 12.99
```

### Testing with different inputs
```python
@pytest.mark.parametrize("subtotal, method, expected", [
    (5, "standard", 3.99),
    (5, "express", 7.99),
    (5, "overnight", 12.99),
    (100, "standard", 0),
])
def test_shipping_calculations(subtotal, method, expected):
    assert calculate_shipping(subtotal, method) == expected
```

---

## 12) What We Covered

### Core concepts:
- ✅ Test-Driven Development (TDD) workflow
- ✅ Writing basic tests with `assert`
- ✅ Using `pytest.raises()` for exception testing
- ✅ Parameterized tests with `@pytest.mark.parametrize`
- ✅ Floating-point testing with `pytest.approx()`
- ✅ Testing functions with default parameters
- ✅ Testing edge cases and boundary conditions
- ✅ Running tests from command line

### What we didn't cover (for future learning):
- ❌ Fixtures (`@pytest.fixture`) - reusable test setup
- ❌ Mocking and patching
- ❌ Test coverage tools
- ❌ Integration tests
- ❌ Performance testing

---

## 13) Best Practices

### Test naming
- Use descriptive names: `test_adding_two_numbers_gives_correct_answer`
- Start with `test_`
- Describe what is being tested

### Test independence
- Each test should work independently
- Don't rely on test execution order
- Create fresh data for each test

### Test one thing
- Each test should verify one behavior
- If a test fails, you should know exactly what's wrong

### Keep tests simple
- Tests should be easy to read and understand
- Complex setup belongs in helper functions or fixtures (future topic)

### Test both success and failure
- Test normal operation
- Test error cases
- Test edge cases

---

## 14) Example: Complete Test File

```python
"""Tests for maths module."""

from maths import add
import pytest

# Basic tests
def test_adding_two_numbers_gives_correct_answer():
    number1 = 4
    number2 = 5
    expected = 9
    result = add(number1, number2)
    assert result == expected

def test_adding_two_negative_numbers_gives_correct_answer():
    assert add(-2, -2) == -4

# Parameterized tests
@pytest.mark.parametrize("num1, num2, expected", [
    (1_000_000, 1_000_000, 2_000_000),
    (1, 1, 2),
    (-10, 5, -5),
    (10, -5, 5)
])
def test_adding_various_numbers_gives_correct_answer(num1, num2, expected):
    assert add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (0.1, 0.1, 0.2),
    (-0.1, -0.1, -0.2),
])
def test_adding_float_numbers_gives_correct_answer(num1, num2, expected):
    assert pytest.approx(add(num1, num2)) == expected

# Exception tests
def test_raises_error_when_trying_to_add_two_strings():
    with pytest.raises(TypeError):
        add("1", "1")

@pytest.mark.parametrize("arg1, arg2", [
    ([], []),
    ({}, {}),
    (True, True),
])
def test_raises_error_when_trying_to_add_two_non_numbers(arg1, arg2):
    with pytest.raises(TypeError):
        add(arg1, arg2)
```

---

## 15) Key Takeaways

1. **TDD helps design better code**
   - Write tests first
   - Red → Green → Refactor cycle
   - Tests document requirements

2. **Tests verify code works correctly**
   - Catch bugs early
   - Document expected behavior
   - Enable safe changes

3. **pytest makes testing easy**
   - Simple syntax
   - Powerful features
   - Good error messages

4. **Write good tests**
   - Descriptive names
   - Test one thing
   - Test success and failure
   - Use parameterization for multiple cases

5. **Common patterns**
   - `assert` for return values
   - `pytest.raises()` for exceptions
   - `@pytest.mark.parametrize` for multiple inputs
   - `pytest.approx()` for floats

6. **Test organization**
   - Arrange-Act-Assert pattern
   - Independent tests
   - Clear structure

---

## 16) Practice Exercises

1. Write tests for a `subtract()` function
2. Test a function that validates email addresses
3. Use parameterization to test multiple email formats
4. Test that invalid emails raise appropriate exceptions
5. Write tests for a function that calculates discounts

---

## Summary

Testing is essential for reliable code. TDD helps you design better code by writing tests first. pytest provides a simple yet powerful framework for writing tests. Focus on:
- **TDD workflow**: Red → Green → Refactor
- Clear test names
- Testing one thing at a time
- Using parameterization for multiple cases
- Testing both success and failure paths
- Using `pytest.approx()` for floating-point comparisons

Remember: Good tests are like documentation that never gets out of date!

---

## 60-Second Recap

- **Testing catches bugs early** - Find issues before users do
- **pytest is the standard** - Simple syntax, powerful features
- **Write tests first (TDD)** - Red → Green → Refactor cycle
- **Test files start with `test_`** - pytest auto-discovers them
- **Use `assert` for checks** - Simple and readable
- **Parameterize for multiple cases** - `@pytest.mark.parametrize` saves code
- **Test exceptions with `pytest.raises()`** - Verify error handling
- **Use `pytest.approx()` for floats** - Handles rounding errors
- **Test both success and failure** - Cover all code paths
- **Keep tests independent** - Each test should work alone

---

## Mini Q&A

**Q: Why write tests first (TDD)?**  
A: Tests document requirements, help design better interfaces, and catch bugs immediately. Red → Green → Refactor cycle ensures code works correctly.

**Q: Do test files need a specific name?**  
A: Yes - files should start with `test_` or end with `_test.py`. pytest automatically discovers and runs them.

**Q: What's the difference between `assert` and `pytest.raises()`?**  
A: `assert` checks return values. `pytest.raises()` checks that exceptions are raised correctly.

**Q: When should I use `@pytest.mark.parametrize`?**  
A: When testing the same function with multiple different inputs. It reduces code duplication and makes adding test cases easy.

**Q: Why use `pytest.approx()` for floating-point comparisons?**  
A: Floating-point arithmetic has precision limits. `pytest.approx()` handles small rounding errors that would cause tests to fail incorrectly.

**Q: Should each test test one thing?**  
A: Yes - if a test fails, you should know exactly what's wrong. One test = one behavior.

**Q: Do I need to create fresh data in each test?**  
A: Yes - tests should be independent. Create new data structures (like empty dictionaries) in each test to avoid side effects.

**Q: What's the Arrange-Act-Assert pattern?**  
A: A structure for tests: Arrange (set up), Act (execute), Assert (verify). Makes tests clear and easy to understand.

**Q: Can I test functions that don't return anything?**  
A: Yes - test side effects (like changes to a dictionary) or use `pytest.raises()` if they raise exceptions.

**Q: How do I run specific tests?**  
A: `pytest test_file.py::test_function_name` runs one test, or `pytest -k "keyword"` runs tests matching a pattern.
