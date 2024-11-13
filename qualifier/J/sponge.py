from fractions import Fraction

def main() -> bool:
    l, xn, xd, yn, yd, zn, zd = map(int, input().split())
    x = Fraction(xn, xd)
    y = Fraction(yn, yd)
    z = Fraction(zn, zd)

    for i in range(1, l+1):
        mod = Fraction(1, 3 ** i)
        count = 0
        
        if fraction_in_range(mod_fractions(x, mod), i):
            count += 1

        if fraction_in_range(mod_fractions(y, mod), i):
            count += 1

        if fraction_in_range(mod_fractions(z, mod), i):
            count += 1

        if count >= 2:
            return False
    
    return True

def mod_fractions(frac1, frac2):
    # frac1 is the fraction being divided, frac2 is the divisor fraction
    # Find the quotient by performing integer division
    quotient = frac1 // frac2
    
    # Multiply the quotient by the divisor fraction
    quotient_fraction = quotient * frac2
    
    # Find the remainder by subtracting the quotient fraction from the original fraction
    remainder = frac1 - quotient_fraction
    
    return remainder

def fraction_in_range(frac, range_exponent) -> bool:
    lo = Fraction(1, 3 ** range_exponent)
    hi = Fraction(2, 3 ** range_exponent)

    return lo <= frac and frac <= hi

if __name__ == '__main__':
    ans = main()
    # print(1 if ans else 0)
    print(ans)