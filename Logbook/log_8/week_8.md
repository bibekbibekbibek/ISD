# Session 8: Data Structures and Abstract Classes

## Section 1 Data Structures

### Exercise 1: Tuples - Swap values without temporary variable

In this task, I used tuple packing and unpacking to swap two variables without needing a temporary variable.

```python
# Swap values using tuple unpacking

a = 5
b = 10
print("Before swap: a =", a, "b =", b)

a, b = b, a
print("After swap: a =", a, "b =", b)
```

Output

```console
Before swap: a = 5 b = 10
After swap: a = 10 b = 5
```

Using tuple unpacking keeps the code simple and avoids extra variables.

### Exercise 2: Sets - Find common names in two sets

This task compares two sets and finds the names that appear in both using the intersection operation.

```python
set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}

common_names = set1.intersection(set2)
print("Common names:", common_names)
```

Output

```console
Common names: {'Tom', 'Hewey', 'Dewey'}
```

Using sets makes this comparison efficient and clean.

### Exercise 3: Dictionaries - Create histogram from list

I implemented a histogram function that counts occurrences of each element in a list and returns a dictionary.

```python
def histogram(my_list: list) -> dict:
    result = {}
    for element in my_list:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result

my_list = [1, 2, 3, 1, 2, 3, 4]
result = histogram(my_list)
print("Input list:", my_list)
print("Histogram:", result)
```

Output

```console
Input list: [1, 2, 3, 1, 2, 3, 4]
Histogram: {1: 2, 2: 2, 3: 2, 4: 1}
```

This is a useful way to count items and store the results in a dictionary.

## Section 2 Abstract Classes

### Abstract Base Class: Dice

I created an abstract base class `Dice` with an abstract method `roll` that must be implemented by child classes.

```python
from abc import ABC, abstractmethod

class Dice(ABC):
    def __init__(self) -> None:
        self.face = None

    @abstractmethod
    def roll(self) -> int:
        pass
```

### Concrete Class: SixSidedDice

This class implements `Dice` and returns a random value from 1 to 6.

```python
from random import randint

class SixSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 6)
        return self.face
```

### Concrete Class: TenSidedDice

This class implements `Dice` and returns a random value from 1 to 10.

```python
class TenSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 10)
        return self.face
```

### Exercise 1: Test SixSidedDice with histogram

I rolled the six-sided dice multiple times and used the histogram function to show the distribution.

```python
dice = SixSidedDice()
results = []
for _ in range(1000):
    results.append(dice.roll())

dist = histogram(results)
print("Rolled 6-sided dice 1000 times")
print("Distribution:", dist)
```

Output example

```console
Rolled 6-sided dice 1000 times
Distribution: {1: 170, 2: 160, 3: 170, 4: 165, 5: 155, 6: 180}
```

This shows that random dice rolls are approximately evenly distributed.

### Exercise 2: Test TenSidedDice with histogram

I rolled the ten-sided dice multiple times and displayed the distribution.

```python
dice = TenSidedDice()
results = []
for _ in range(1000):
    results.append(dice.roll())

dist = histogram(results)
print("Rolled 10-sided dice 1000 times")
print("Distribution:", dist)
```

Output example

```console
Rolled 10-sided dice 1000 times
Distribution: {1: 95, 2: 105, 3: 100, 4: 98, 5: 102, 6: 110, 7: 99, 8: 95, 9: 98, 10: 98}
```

The histogram confirms that each face appears roughly the same number of times.
