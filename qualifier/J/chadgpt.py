from fractions import Fraction

def is_in_menger_sponge(x, y, z, degree):
    """
    Check if the point (x, y, z) is inside the n-degree Menger Sponge.
    
    Args:
    x, y, z: Rational coordinates of the point.
    degree: The degree of the Menger Sponge.
    
    Returns:
    True if the point is in the Menger Sponge, False otherwise.
    """
    # Function to convert a rational number to its base-3 representation as a string
    def to_base_3(numerator, denominator, degree):
        base_3_digits = []
        for _ in range(degree):
            numerator *= 3
            base_3_digits.append(numerator // denominator)
            numerator = numerator % denominator
        return base_3_digits

    # Convert each of the coordinates to base-3 representation
    x_base_3 = to_base_3(x.numerator, x.denominator, degree)
    y_base_3 = to_base_3(y.numerator, y.denominator, degree)
    z_base_3 = to_base_3(z.numerator, z.denominator, degree)

    # Check if any digit in base-3 is 1, which means the point is in a hole
    for i in range(degree):
        if x_base_3[i] == 1 or y_base_3[i] == 1 or z_base_3[i] == 1:
            return False  # Point lies in a removed section
    
    return True  # Point is inside the Menger Sponge

# Example point: (2/3, 1/3, 4/9)
x = Fraction(2, 3)
y = Fraction(1, 3)
z = Fraction(4, 9)

# Check if the point is in a 2-degree Menger Sponge
is_in_menger_sponge(x, y, z, 2)
