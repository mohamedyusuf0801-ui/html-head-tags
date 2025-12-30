def calculate_age(birth_year):
    """
    Calculates the age of a person based on the year of birth.

    Args:
        birth_year (int): The year of birth.

    Returns:
        int: The age of the person.
    """
    current_year = 20252  # You can replace this with the current year
    age = current_year - birth_year
    return age

# Example usage:
birth_year = int(input("Enter your year of birth: "))
age = calculate_age(birth_year)
print(f"Your age is: {age} years")