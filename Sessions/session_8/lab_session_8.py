"""
Week 9 Lab Session - Data Structures and Abstract Classes
COMP11124 Interactive Software Design / Object Oriented Programming
"""

from abc import ABC, abstractmethod
from random import randint


# ============================================================================
# SECTION 1: DATA STRUCTURES
# ============================================================================

# ============================================================================
# TASK 1: TUPLES - Swap values without temporary variable
# ============================================================================

def swap_with_tuple() -> None:
    """Swap two variables using tuple packing and unpacking."""
    a = 5
    b = 10
    
    print("Task 1: Swapping values with tuples")
    print(f"Before swap: a = {a}, b = {b}")
    
    # Swap using tuple unpacking
    a, b = b, a
    
    print(f"After swap: a = {a}, b = {b}")
    print()


# ============================================================================
# TASK 2: SETS - Find common names in two sets
# ============================================================================

def find_common_names() -> None:
    """Compare two sets and find names that appear in both."""
    set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
    set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}
    
    print("Task 2: Finding common names in sets")
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    
    # Find intersection using set intersection method
    common_names = set1.intersection(set2)
    
    print(f"Common names: {common_names}")
    print()


# ============================================================================
# TASK 3: DICTIONARIES - Create histogram from list
# ============================================================================

def histogram(my_list: list) -> dict:
    """
    Create a histogram (dictionary) where keys are elements and values
    are the count of occurrences in the list.
    
    Args:
        my_list: A list of elements to count
        
    Returns:
        A dictionary with elements as keys and counts as values
    """
    result = {}
    for element in my_list:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result


def test_histogram() -> None:
    """Test the histogram function."""
    print("Task 3: Creating histogram from list")
    my_list = [1, 2, 3, 1, 2, 3, 4]
    
    result = histogram(my_list)
    expected = {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(f"Input list: {my_list}")
    print(f"Histogram: {result}")
    
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ Test passed!")
    print()


# ============================================================================
# SECTION 2: ABSTRACT CLASSES
# ============================================================================

# ============================================================================
# Abstract Base Class - Dice
# ============================================================================

class Dice(ABC):
    """Abstract base class representing a generic dice."""
    
    def __init__(self) -> None:
        """Initialize the dice with face set to None."""
        self.face = None
    
    @abstractmethod
    def roll(self) -> int:
        """
        Abstract method to roll the dice.
        Must be implemented by child classes.
        
        Returns:
            The face value of the dice after rolling
        """
        pass


# ============================================================================
# Concrete Class - SixSidedDice
# ============================================================================

class SixSidedDice(Dice):
    """Represents a standard six-sided dice."""
    
    def roll(self) -> int:
        """
        Roll the dice and return a random number between 1 and 6.
        
        Returns:
            A random number between 1 and 6
        """
        self.face = randint(1, 6)
        return self.face


# ============================================================================
# Concrete Class - TenSidedDice
# ============================================================================

class TenSidedDice(Dice):
    """Represents a ten-sided dice."""
    
    def roll(self) -> int:
        """
        Roll the dice and return a random number between 1 and 10.
        
        Returns:
            A random number between 1 and 10
        """
        self.face = randint(1, 10)
        return self.face


# ============================================================================
# TASK 1: Test SixSidedDice with histogram
# ============================================================================

def test_six_sided_dice() -> None:
    """Roll a six-sided dice 1000 times and show distribution."""
    print("Abstract Classes - Task 1: SixSidedDice")
    print("-" * 50)
    
    dice = SixSidedDice()
    results = []
    
    # Roll the dice 1000 times
    for _ in range(1000):
        results.append(dice.roll())
    
    # Create histogram
    dist = histogram(results)
    
    print(f"Rolled 6-sided dice 1000 times")
    print(f"Distribution: {dist}")
    print(f"Expected approximately: {{1: ~167, 2: ~167, 3: ~167, 4: ~167, 5: ~167, 6: ~167}}")
    print()


# ============================================================================
# TASK 2: Test TenSidedDice with histogram
# ============================================================================

def test_ten_sided_dice() -> None:
    """Roll a ten-sided dice 1000 times and show distribution."""
    print("Abstract Classes - Task 2: TenSidedDice")
    print("-" * 50)
    
    dice = TenSidedDice()
    results = []
    
    # Roll the dice 1000 times
    for _ in range(1000):
        results.append(dice.roll())
    
    # Create histogram
    dist = histogram(results)
    
    print(f"Rolled 10-sided dice 1000 times")
    print(f"Distribution: {dist}")
    print(f"Expected approximately: {{1: ~100, 2: ~100, 3: ~100, ..., 10: ~100}}")
    print()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("WEEK 9: DATA STRUCTURES AND ABSTRACT CLASSES")
    print("=" * 70)
    print()
    
    # Section 1: Data Structures
    print("SECTION 1: DATA STRUCTURES")
    print("=" * 70)
    swap_with_tuple()
    find_common_names()
    test_histogram()
    
    # Section 2: Abstract Classes
    print("SECTION 2: ABSTRACT CLASSES")
    print("=" * 70)
    test_six_sided_dice()
    test_ten_sided_dice()
    
    print("=" * 70)
    print("All tasks completed successfully!")
    print("=" * 70)
