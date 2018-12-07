import sys
import time

# local version with improvments
sys.path.insert(1, "./sympy")

# load local
from sympy import *
from sympy.functions.elementary.trigonometric import TrigonometricFunction, InverseTrigonometricFunction

args = [
    (1*pi/2, 2),
    (2*pi/2, 2),
    (1*pi/3, 2),
    (2*pi/3, 2),
    (1*pi/4, 2),
    (2*pi/4, 2),
    (3*pi/4, 2),
    (1*pi/5, 2),
    (2*pi/5, 2),
    (3*pi/5, 2),
    (4*pi/5, 2),
    (1*pi/6, 2),
    (2*pi/6, 2),
    (3*pi/6, 2),
    (4*pi/6, 2),
    (5*pi/6, 2),
    (1*pi/7, 2),
    (2*pi/7, 2),
    (3*pi/7, 2),
    (4*pi/7, 2),
    (5*pi/7, 2),
    (6*pi/7, 2),
    (1*pi/8, 2),
    (2*pi/8, 2),
    (3*pi/8, 2),
    (4*pi/8, 2),
    (5*pi/8, 2),
    (6*pi/8, 2),
    (7*pi/8, 2),
    (1*pi/9, 2),
    (2*pi/9, 2),
    (3*pi/9, 2),
    (4*pi/9, 2),
    (5*pi/9, 2),
    (6*pi/9, 2),
    (7*pi/9, 2),
    (8*pi/9, 2),
    (10*pi/9, 2),
    (25*pi/9, 2),
    (1*pi/10, 2),
    (2*pi/10, 2),
    (3*pi/10, 2),
    (4*pi/10, 2),
    (5*pi/10, 2),
    (6*pi/10, 2),
    (7*pi/10, 2),
    (8*pi/10, 2),
    (9*pi/10, 2),
    (1*pi/11, 2),
    (2*pi/11, 2),
    (3*pi/11, 2),
    (4*pi/11, 2),
    (5*pi/11, 2),
    (6*pi/11, 2),
    (7*pi/11, 2),
    (8*pi/11, 2),
    (9*pi/11, 2),
    (10*pi/11, 2),
    (-23*pi/11, 2),
    (1*pi/12, 2),
    (2*pi/12, 2),
    (3*pi/12, 2),
    (4*pi/12, 2),
    (5*pi/12, 2),
    (6*pi/12, 2),
    (7*pi/12, 2),
    (8*pi/12, 2),
    (9*pi/12, 2),
    (10*pi/12, 2),
    (11*pi/12, 2),
]

args_inverse = [
    (Rational(1,2), 2),
    (Rational(1,3), 2),
    (Rational(2,3), 2),
    (Rational(1,4), 2),
    (Rational(2,4), 2),
    (Rational(3,4), 2),
    (Rational(1,5), 2),
    (Rational(2,5), 2),
    (Rational(3,5), 2),
    (Rational(4,5), 2),
    (Rational(1,6), 2),
    (Rational(2,6), 2),
    (Rational(3,6), 2),
    (Rational(4,6), 2),
    (Rational(5,6), 2),
    (Rational(1,7), 2),
    (Rational(2,7), 2),
    (Rational(3,7), 2),
    (Rational(4,7), 2),
    (Rational(5,7), 2),
    (Rational(6,7), 2),
    (Rational(1,8), 2),
    (Rational(2,8), 2),
    (Rational(3,8), 2),
    (Rational(4,8), 2),
    (Rational(5,8), 2),
    (Rational(6,8), 2),
    (Rational(7,8), 2),
    (Rational(1,9), 2),
    (Rational(2,9), 2),
    (Rational(3,9), 2),
    (Rational(4,9), 2),
    (Rational(5,9), 2),
    (Rational(6,9), 2),
    (Rational(7,9), 2),
    (Rational(8,9), 2),
    (Rational(1,10), 2),
    (Rational(2,10), 2),
    (Rational(3,10), 2),
    (Rational(4,10), 2),
    (Rational(5,10), 2),
    (Rational(6,10), 2),
    (Rational(7,10), 2),
    (Rational(8,10), 2),
    (Rational(9,10), 2),
    (Rational(1,11), 2),
    (Rational(2,11), 2),
    (Rational(3,11), 2),
    (Rational(4,11), 2),
    (Rational(5,11), 2),
    (Rational(6,11), 2),
    (Rational(7,11), 2),
    (Rational(8,11), 2),
    (Rational(9,11), 2),
    (Rational(10,11), 2),
    (Rational(1,12), 2),
    (Rational(2,12), 2),
    (Rational(3,12), 2),
    (Rational(4,12), 2),
    (Rational(5,12), 2),
    (Rational(6,12), 2),
    (Rational(7,12), 2),
    (Rational(8,12), 2),
    (Rational(9,12), 2),
    (Rational(10,12), 2),
    (Rational(11,12), 2),
    # atan extra
    (Rational(15,11), 2),
    (Rational(23,11), 2),
]

print('')
print('========== sin(arg) ============ ')
successCounter = 0
totalCounter = 0
t0 = time.time()
for arg, bla in args:

    q = Rational(arg/pi).q
    if 0 != q % 2:
        continue

    #
    result = sin(arg, evaluate=False)

    # fix on inverse function of itself
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        # fixes atan(tan(x)) etc
        result = trigsimp(result, method='old')

    # simplify
    result = simplify(result)

    # compare
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        print('sin(%s) = %s still has TrigonometricFunction' %(arg, result))
    else:
        successCounter = successCounter + 1

    totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of sin(arg) tests: %s/%s' %(successCounter, totalCounter))
print('========== END sin(arg). Duration = %s s ============ ' %(t1-t0))

print('')
print('========== cos(arg) ============ ')
successCounter = 0
totalCounter = 0
t0 = time.time()
for arg, bla in args:

    q = Rational(arg/pi).q
    if 0 != q % 2:
        continue

    #
    result = cos(arg, evaluate=False)

    # fix on inverse function of itself
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        # fixes atan(tan(x)) etc
        result = trigsimp(result, method='old')

    # simplify
    result = simplify(result)

    # compare
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        print('cos(%s) = %s still has TrigonometricFunction' %(arg, result))
    else:
        successCounter = successCounter + 1

    totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of cos(arg) tests: %s/%s' %(successCounter, totalCounter))
print('========== END cos(arg). Duration = %s s ============ ' %(t1-t0))

print('')
print('========== acos(cos(arg)) ============ ')
successCounter = 0
totalCounter = 0
t0 = time.time()
for arg, bla in args:
    result = acos(cos(arg, evaluate=False), evaluate=False)

    # fix on inverse function of itself
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        # fixes atan(tan(x)) etc
        result = trigsimp(result, method='old')

    # simplify
    result = simplify(result)

    # make sure arg is between 0 and pi
    ang = arg
    ang %= 2*pi # restrict to [0,2*pi)
    if ang > pi: # restrict to [0,pi]
        ang = 2*pi - ang

    # compare
    if result != ang:
        print('acos(cos(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()))
    else:
        successCounter = successCounter + 1

    totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of acos(cos(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END acos(cos(arg)). Duration = %s s ============ ' %(t1-t0))


print('')
print('========== asin(sin(arg)) ============ ')
successCounter = 0
totalCounter = 0
t0 = time.time()
for arg, bla in args:
    result = asin(sin(arg, evaluate=False), evaluate=False)

    # fix on inverse function of itself
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        # fixes atan(tan(x)) etc
        result = trigsimp(result, method='old')

    # simplify
    result = simplify(result)

    # get the resulting angle
    ang = arg
    ang %= 2*pi # restrict to [0,2*pi)
    if ang > pi: # restrict to (-pi,pi]
        ang = pi - ang

    # restrict to [-pi/2,pi/2]
    if ang > pi/2:
        ang = pi - ang
    if ang < -pi/2:
        ang = -pi - ang

    # compare
    if result != ang:
        print('asin(sin(%s)) = %s == %s' %(arg, result, ang))
    else:
        successCounter = successCounter + 1

    totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of asin(sin(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END asin(sin(arg)). Duration = %s s ============ ' %(t1-t0))

print('')
print('========== atan(tan(arg)) ============ ')
successCounter = 0
totalCounter = 0
t0 = time.time()
for arg, bla in args:

    # if on asymptote
    if abs((arg % pi)) == pi/2:
        continue

    # formula
    result = atan(tan(arg, evaluate=False), evaluate=False)

    # fix on inverse function of itself
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        # fixes atan(tan(x)) etc
        result = trigsimp(result, method='old')

    # simplify
    result = simplify(result)

    #
    ang = arg
    ang %= pi # restrict to [0,pi)
    if ang > pi/2: # restrict to [-pi/2,pi/2]
        ang -= pi

    # compare
    if result != ang:
        print('atan(tan(%s)) = %s == %s || tan(%s) = %s = %s' %(arg, result, ang, arg, tan(arg), tan(arg).evalf()))
    else:
        successCounter = successCounter + 1

    totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of atan(tan(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END atan(tan(arg)). Duration = %s s ============ ' %(t1-t0))

print('')
print('========== asin(cos(arg)) ============ ')
successCounter = 0
totalCounter = 0
t0 = time.time()
for arg, bla in args:
    result = asin(cos(arg, evaluate=False), evaluate=False)

    # fix on inverse function of itself
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        # fixes atan(tan(x)) etc
        result = trigsimp(result, method='old')

    # simplify
    result = simplify(result)

    #
    ang = simplify(pi/2 - acos(cos(arg)))

    # compare
    if result != ang:
        print('asin(cos(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()) )
    else:
        successCounter = successCounter + 1

    totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of asin(cos(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END asin(cos(arg)). Duration = %s s ============ ' %(t1-t0))

print('')
print('========== acos(sin(arg)) ============ ')
successCounter = 0
totalCounter = 0
t0 = time.time()
for arg, bla in args:
    result = acos(sin(arg, evaluate=False), evaluate=False)

    # fix on inverse function of itself
    if result.has(TrigonometricFunction, InverseTrigonometricFunction):
        # fixes atan(tan(x)) etc
        result = trigsimp(result, method='old')

    # simplify
    result = simplify(result)

    #
    ang = simplify(pi/2 - asin(sin(arg)))

    # compare
    if result != ang:
        print('acos(sin(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()) )
    else:
        successCounter = successCounter + 1

    totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of acos(sin(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END acos(sin(arg)). Duration = %s s ============ ' %(t1-t0))


print('')
print('========== tan(asin(arg)) ============ ')
successCounter = 0
totalCounter = 0
signs = [1,-1]
t0 = time.time()
for sign in signs:
    for arg, bla in args_inverse:
        # only take arguments smaller than 1
        if abs(arg) >= 1:
            continue

        arg = sign*arg

        result = tan(asin(arg, evaluate=False), evaluate=False)

        # fix on inverse function of itself
        if result.has(TrigonometricFunction, InverseTrigonometricFunction):
            # fixes atan(tan(x)) etc
            result = trigsimp(result, method='old')

        # simplify
        result = simplify(result)

        # angle
        ang = arg / sqrt(1 - arg**2)

        # compare
        if result != ang:
            print('tan(asin(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()) )
        else:
            successCounter = successCounter + 1

        totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of tan(asin(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END tan(asin(arg)). Duration = %s s ============ ' %(t1-t0))


print('')
print('========== sin(acos(arg)) ============ ')
successCounter = 0
totalCounter = 0
signs = [1,-1]
t0 = time.time()
for sign in signs:
    for arg, bla in args_inverse:
        # only take arguments smaller than 1
        if abs(arg) >= 1:
            continue

        arg = sign*arg

        # formula
        result = sin(acos(arg, evaluate=False), evaluate=False)

        # fix on inverse function of itself
        if result.has(TrigonometricFunction, InverseTrigonometricFunction):
            # fixes atan(tan(x)) etc
            result = trigsimp(result, method='old')

        # simplify
        result = simplify(result)

        # angle
        ang = sqrt(1 - arg**2)

        # compare
        if result != ang:
            print('sin(acos(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()) )
        else:
            successCounter = successCounter + 1

        totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of sin(acos(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END sin(acos(arg)). Duration = %s s ============ ' %(t1-t0))


print('')
print('========== cos(asin(arg)) ============ ')
successCounter = 0
totalCounter = 0
signs = [1,-1]
t0 = time.time()
for sign in signs:
    for arg, bla in args_inverse:
        # only take arguments smaller than 1
        if abs(arg) >= 1:
            continue

        arg = sign*arg

        # formula
        result = cos(asin(arg, evaluate=False), evaluate=False)

        # fix on inverse function of itself
        if result.has(TrigonometricFunction, InverseTrigonometricFunction):
            # fixes atan(tan(x)) etc
            result = trigsimp(result, method='old')

        # simplify
        result = simplify(result)

        # angle
        ang = sqrt(1 - arg**2)

        # compare
        if result != ang:
            print('cos(asin(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()) )
        else:
            successCounter = successCounter + 1

        totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of cos(asin(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END cos(asin(arg)). Duration = %s s ============ ' %(t1-t0))


print('')
print('========== sin(atan(arg)) ============ ')
successCounter = 0
totalCounter = 0
signs = [1,-1]
t0 = time.time()
for sign in signs:
    for arg, bla in args_inverse:
        arg = sign*arg

        # formula
        result = sin(atan(arg, evaluate=False), evaluate=False)

        # fix on inverse function of itself
        if result.has(TrigonometricFunction, InverseTrigonometricFunction):
            # fixes atan(tan(x)) etc
            result = trigsimp(result, method='old')

        # simplify
        result = simplify(result)

        # angle
        ang = arg / sqrt(1 + arg**2)

        # compare
        if result != ang:
            print('sin(atan(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()) )
        else:
            successCounter = successCounter + 1

        totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of sin(atan(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END sin(atan(arg)). Duration = %s s ============ ' %(t1-t0))


print('')
print('========== cos(atan(arg)) ============ ')
successCounter = 0
totalCounter = 0
signs = [1,-1]
t0 = time.time()
for sign in signs:
    for arg, bla in args_inverse:

        arg = sign*arg

        # formula
        result = cos(atan(arg, evaluate=False), evaluate=False)

        # fix on inverse function of itself
        if result.has(TrigonometricFunction, InverseTrigonometricFunction):
            # fixes atan(tan(x)) etc
            result = trigsimp(result, method='old')

        # simplify
        result = simplify(result)

        # angle
        ang = 1 / sqrt(1 + arg**2)

        # compare
        if result != ang:
            print('cos(atan(%s)) = %s == %s ==> %s = %s' %(arg, result, ang, result.evalf(), ang.evalf()) )
        else:
            successCounter = successCounter + 1

        totalCounter = totalCounter + 1

t1 = time.time()
print('success / total number of cos(atan(arg)) tests: %s/%s' %(successCounter, totalCounter))
print('========== END cos(atan(arg)). Duration = %s s ============ ' %(t1-t0))
