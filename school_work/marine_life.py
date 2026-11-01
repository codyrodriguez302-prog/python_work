# Assignment: Inheritance vs Polymorphism - Marine Life Classification System
# 
# OBJECTIVE: Understand the difference between inheritance and polymorphism
# 
# INHERITANCE: Child classes get (inherit) methods and variables from parent classes
# POLYMORPHISM: Same method name behaves differently in different classes
#
# CLASS HIERARCHY:
# MarineAnimal (parent)
# ├── Predator (child of MarineAnimal)
# │   ├── Shark (child of Predator)  
# │   └── Octopus (child of Predator)
# └── FilterFeeder (child of MarineAnimal)

# =============================================================================
# PART 1: COMPLETE THE CLASS DEFINITIONS
# =============================================================================

class MarineAnimal:
    """
    Parent class for all marine animals
    Variables: species_name, habitat_depth, body_length, ocean_zone
    Methods: get_description(), calculate_food_needs(), swim()
    """
    
    def __init__(self, species_name, habitat_depth, body_length, ocean_zone):
        # TODO: Initialize the four instance variables
        pass
    
    def get_description(self):
        """Returns basic marine animal information"""
        # TODO: Return a formatted string with species info
        pass
    
    def calculate_food_needs(self):
        """Base food calculation - 3% of body length in kg per day"""
        # TODO: Calculate base food needs
        pass
    
    def swim(self):
        """Describes how the animal swims - THIS WILL BE OVERRIDDEN (POLYMORPHISM!)"""
        # TODO: Return swimming description for generic marine animal
        pass


class Predator(MarineAnimal):
    """
    Predator class - inherits from MarineAnimal
    Additional variable: hunting_range
    Overrides: calculate_food_needs() and swim()
    """
    
    def __init__(self, species_name, habitat_depth, body_length, ocean_zone, hunting_range):
        # TODO: Call parent constructor and initialize hunting_range
        pass
    
    def calculate_food_needs(self):
        """Predators need 8% of body length + 0.5kg per km of hunting range"""
        # TODO: Calculate food needs for predators
        pass
    
    def swim(self):
        """Override parent's swim method - POLYMORPHISM!"""
        # TODO: Return predator-specific swimming description
        pass


class Shark(Predator):
    """
    Shark - inherits from Predator
    Additional variable: bite_force
    Overrides: swim()
    """
    
    def __init__(self, species_name, habitat_depth, body_length, ocean_zone, hunting_range, bite_force):
        # TODO: Call parent constructor and initialize bite_force
        pass
    
    def swim(self):
        """Sharks have specific swimming description"""
        # TODO: Return shark-specific swimming behavior including bite_force
        pass


class Octopus(Predator):
    """
    Octopus - inherits from Predator  
    Additional variable: tentacle_count
    Overrides: swim()
    """
    
    def __init__(self, species_name, habitat_depth, body_length, ocean_zone, hunting_range, tentacle_count):
        # TODO: Call parent constructor and initialize tentacle_count
        pass
    
    def swim(self):
        """Octopus have specific swimming description"""
        # TODO: Return octopus-specific swimming behavior including tentacle_count
        pass


class FilterFeeder(MarineAnimal):
    """
    FilterFeeder class - inherits from MarineAnimal
    Additional variable: filter_capacity
    Overrides: calculate_food_needs() and swim()
    """
    
    def __init__(self, species_name, habitat_depth, body_length, ocean_zone, filter_capacity):
        # TODO: Call parent constructor and initialize filter_capacity
        pass
    
    def calculate_food_needs(self):
        """Filter feeders need 1% of body length plus filter efficiency bonus"""
        # TODO: Calculate filter feeder food needs
        pass
    
    def swim(self):
        """Override parent's swim method - POLYMORPHISM!"""
        # TODO: Return filter feeder-specific swimming description
        pass


# =============================================================================
# PART 2: TEST CASES - RUN TO VERIFY YOUR IMPLEMENTATION
# =============================================================================

def test_inheritance_vs_polymorphism():
    """
    Test cases to demonstrate inheritance vs polymorphism
    """
    print("=" * 60)
    print("TESTING INHERITANCE VS POLYMORPHISM")
    print("=" * 60)
    
    # Create marine animal objects
    marine_animals = [
        MarineAnimal("Generic Fish", 50, 0.3, "Coastal"),
        FilterFeeder("Blue Whale", 200, 25.0, "Open Ocean", 2000),
        Predator("Barracuda", 30, 1.5, "Reef", 5),
        Shark("Great White", 100, 4.5, "Open Ocean", 50, 1800),
        Octopus("Giant Pacific", 150, 3.0, "Deep Sea", 8, 8)
    ]
    
    print("\n1. INHERITANCE DEMONSTRATION")
    print("-" * 40)
    print("All classes inherit get_description() from MarineAnimal:")
    
    for animal in marine_animals:
        print(f"  {animal.get_description()}")
    
    print("\n2. POLYMORPHISM DEMONSTRATION")  
    print("-" * 40)
    print("Same method name (swim), different behaviors:")
    
    for animal in marine_animals:
        print(f"  {animal.swim()}")
    
    print("\n3. METHOD OVERRIDING (Part of Polymorphism)")
    print("-" * 40)
    print("calculate_food_needs() behaves differently for each type:")
    
    for animal in marine_animals:
        food_needs = animal.calculate_food_needs()
        print(f"  {animal.species_name}: {food_needs:.2f} kg/day")
    
    print("\n4. INHERITANCE CHAIN DEMONSTRATION")
    print("-" * 40)
    print("Checking what each object inherited:")
    
    shark = marine_animals[3]  # Great White
    print(f"Shark inherits from Predator:")
    print(f"  - Has hunting_range: {shark.hunting_range} km (from Predator)")
    print(f"  - Has habitat_depth: {shark.habitat_depth} m (from MarineAnimal)")
    print(f"  - Has bite_force: {shark.bite_force} PSI (own attribute)")


def test_specific_cases():
    """
    Additional test cases for edge cases and verification
    """
    print("\n" + "=" * 60)
    print("ADDITIONAL TEST CASES")
    print("=" * 60)
    
    # Test 1: Verify inheritance chain
    octopus = Octopus("Common Octopus", 80, 1.2, "Rocky Bottom", 3, 8)
    
    print(f"\n1. Octopus Inheritance Test:")
    print(f"   Species (from MarineAnimal): {octopus.species_name}")
    print(f"   Hunting Range (from Predator): {octopus.hunting_range} km")
    print(f"   Tentacles (own): {octopus.tentacle_count}")
    
    # Test 2: Polymorphism with isinstance
    print(f"\n2. Type Checking:")
    print(f"   Octopus is MarineAnimal: {isinstance(octopus, MarineAnimal)}")
    print(f"   Octopus is Predator: {isinstance(octopus, Predator)}")
    print(f"   Octopus is Octopus: {isinstance(octopus, Octopus)}")
    
    # Test 3: Method Resolution Order
    print(f"\n3. Method Resolution:")
    print(f"   swim() method: {octopus.swim()}")
    print(f"   calculate_food_needs() method: {octopus.calculate_food_needs():.2f} kg/day")


# =============================================================================
# PART 3: ANALYSIS QUESTIONS (ANSWER THESE)
# =============================================================================

def analysis_questions():
    """
    Answer these questions after completing the assignment
    """
    print("\n" + "=" * 60)
    print("ANALYSIS QUESTIONS - ANSWER THESE:")
    print("=" * 60)
    
    questions = [
        "1. What is the difference between inheritance and polymorphism?",
        "2. Which methods demonstrate inheritance? (Hint: used without overriding)",
        "3. Which methods demonstrate polymorphism? (Hint: same name, different behavior)",
        "4. Why can we call swim() on all marine animal objects even though they're different classes?",
        "5. What would happen if we didn't override calculate_food_needs() in Predator class?",
        "6. How does the Shark class benefit from both Predator and MarineAnimal classes?"
    ]
    
    for question in questions:
        print(f"\n{question}")
        print("   Your answer: _______________________________________________")


# =============================================================================
# PART 4: RUN ALL TESTS
# =============================================================================

if __name__ == "__main__":
    # Run the tests
    test_inheritance_vs_polymorphism()
    test_specific_cases()
    analysis_questions()
    
    print("\n" + "=" * 60)
    print("ASSIGNMENT COMPLETE!")
    print("=" * 60)
    print("KEY CONCEPTS DEMONSTRATED:")
    print("✓ Inheritance: Child classes get parent methods/variables")
    print("✓ Polymorphism: Same method name, different behaviors")
    print("✓ Method Overriding: Child classes can change parent methods")
    print("✓ Super(): Calling parent class constructors")
    print("✓ Multi-level Inheritance: Shark -> Predator -> MarineAnimal")


# =============================================================================
# EXPECTED OUTPUT SUMMARY:
# =============================================================================
"""
INHERITANCE Examples:
- All classes use get_description() from MarineAnimal (inherited, not overridden)
- Predator gets species_name, habitat_depth, body_length, ocean_zone from MarineAnimal
- Shark gets everything from Predator AND MarineAnimal

POLYMORPHISM Examples:
- swim() method exists in all classes but behaves differently
- calculate_food_needs() method behaves differently in MarineAnimal, Predator, FilterFeeder
- Same method call (animal.swim()) produces different results

This demonstrates that:
- INHERITANCE = "getting stuff from parent"  
- POLYMORPHISM = "same interface, different behavior"
"""