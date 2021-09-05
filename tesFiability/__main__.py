from decimal import *

SENSITIVITY = Decimal(100/100)
SPECIFICITY = Decimal(95/100)

BASE_RATE = Decimal(1/1000)

P_positiveTest = (BASE_RATE*SENSITIVITY + (1-BASE_RATE)*(1-SPECIFICITY))


print('A : Be ill')
print('B : positive test')
print()
print('P_positiveTest :',P_positiveTest)
print()

# if test is positive, the probaility of being ill
# P (ill | positiveTest)

P_ill_knowing_positiveTest = (SENSITIVITY * BASE_RATE) / P_positiveTest

print('-------------------------------------------------------')
print('P(A|B) =', P_ill_knowing_positiveTest)


# if test is negative, the probability of not being ill
# P (not ill | not positiveTest)

print('-------------------------------------------------------')
# print('if test is negative, the probability of not being ill')
numerator = (SPECIFICITY * (1-BASE_RATE))
den = (1-P_positiveTest)
P_notIll_knowing_negativeTest = numerator / den

print('P(¬A|¬B) =', P_notIll_knowing_negativeTest)
