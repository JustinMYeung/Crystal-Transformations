import numpy as np
import math
#import matplotlib.pyplot as plt


def calculateAreaRatio(lattice1, lattice2):
	""" 
	STEP 1
	Calculates the ratio between the areas of the 2 selected crystals
	Equation 2.1 of Lattice Match: An Application to heteroepitaxy
	Example shown in equation 3.1
	"""

	# Lattice 1 area calculations
	#np.linalg.det() - google this to figure out how to get area and take abs of it
	area1 = np.linalg.norm(np.cross(lattice1[0], lattice1[1]))

	# Lattice 2 area calculations 
	area2 = np.linalg.norm(np.cross(lattice2[0], lattice2[1]))

	# n calculation
	ratio = area2 / area1

	return ratio

# -------------------------------------------------------------------------------

def rationalizeRatio(ratio, N):
	"""
	STEP 2
	Calculates a set of numbers that form a rational number with a ratio
	Equation 2.2 of Lattice Match: An Application to heteroepitaxy
	Example shown in equation 3.1
	Taken from # https://www.johndcook.com/blog/2010/10/20/best-rational-approximation/

	Intakes number 0 < x < 1
	Maximum denominator = N

	
	"""

	# Flip ratio if it is greater than 1 to fit rationalizeRatio
	if(ratio > 1):
		ratio = 1 /ratio

    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
        mediant = float(a+c)/(b+d)

        # checks if it is within the 1% accepted error
        if (abs(ratio - mediant)/ratio <= 0.01):
            if b + d <= N:
                return a+c, b+d
            elif d > b:
                return c, d
            else:
                return a, b
        elif ratio > mediant:
            a, b = a+c, b+d
        else:
            c, d = a+c, b+d

    if (b > N):
        return c, d
    else:
        return a, b

# -------------------------------------------------------------------------------

# def calculateM():

	"""
	STEP 3
	Calculates the M matrix that represents the transformations 
	to get from L1 to L2
	Equation 2.3 of Lattice Match: An Application to heteroepitaxy
	Example shown in  3.2 and 3.3

	Intakes number 0 < x < 1
	Maximum denominator = N
	"""

# 	for n in nVals:
# 		for x1 in range(0,n):
# 			for x2 in range(0,n):
# 				for x3 in ramge(0,n):
# 					if (x1 * x3 == n) and (j <= m - 1):
# 						m[0,0] = x1
# 						m[1,0] = x2
# 						m[1,1] = x3
# 						if np.dot(transformations,lattice1) == lattice2:
# 							xVals.append((x1,x2,x3)

# 	return xVals


# -------------------------------------------------------------------------------

def lattice_transformations(lattice1, lattice2):

	"""

	Calculates the transformations and re-orientations required to transform from a1, b1 to a2, b2

	a(i) and b(i) are vectors that form 2d lattice of a single crystal
	| ai[1] ai[2] |
	| bi[1] bi[2] |

	Intended formula:
	  L2    =    M      *   L1 - is a square matrix so might be able to take inverse
	| a2 | = | i j | * | a1 |
	| b2 |   | 0 m |   | b1 |

	Where: 
	i * m = n
	i, m > 0
	0 <= j <= m - 1

	The n value above comes from:
	n = r1/r2 = area1/area2
	r1 = int, number of cells in supercell lattice1
	r2 = int, number of cells in supercell lattice2

	Output:
	M =
	| x1 x2 |
	| 0  x3 |

	"""

	# Define the initial and final lattices

	# Primative lattice transformations
	transformations = np.zeros((2,2))

	# List of sets of n values that create the area ratios
	nVals = []

	# List of values [x1, x2, x3] that compose the M transformation matrix
	xVals = []

	# STEP 1
	# Calculates the area ratio between lattice 1 and lattice 2
	ratio = calculateAreaRatio(lattice1, lattice2)

	# STEP 2
	# Calculates the integer ratio with 
	for i in range(1,50):
		nVals.append(rationalizeRatio(ratio, i))

	print("N vals: " + nVals)

	# STEP 3
	# Calculate the possible M matrices
	
	
	# TODO: Figure out which set of the x1 x2 and x3 is the best transformation

#lattice_transformations(np.array([[5.653,0], [0,5.653]]), [6.481,0], [0,6.481])

# TODO: test each component as a tiny function (getRational and other mini functions)




# -------------------------------------------------------------------------------

# Unit tests for calculateAreaRatio()

# Unit tests for rationalizeRatio()

# Unit tests for calculateM()



