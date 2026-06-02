import math


# EXERCICE 1

def segment (p1, p2, m): # p1 et p2 pas liste mais complexe
    div = (p2 - p1) / m
    points = [0] * (m + 1)
    for i in range(m + 1):
        points[i] = p1 + i * div
    return points
segment(complex(2, 3), complex(10, 4), 5)

# example

print(segment(1 + 1j, 2 - 3j, 10))


# EXERCICE 2

# (i)

points_chiffres = [0] * 10
points_chiffres[9] = [0, 1, 1+ 2j, 2j, 1j, 1 + 1j]
points_chiffres[8] = [0, 1, 1 + 2j, 2j, 0, 1j, 1 + 1j]
points_chiffres[7] = [2j, 1 + 2j, 1]
points_chiffres[6] = [1 + 2j, 2j, 0, 1, 1 + 1j, 1j]
points_chiffres[5] = [0, 1, 1 + 1j, 1j, 2j, 2j + 1]
points_chiffres[4] = [1, 2j + 1, 1j + 1, 1j, 2j]
points_chiffres[3] = [0, 1, 1 + 1j, 1j, 1 + 1j, 2j + 1, 2j]
points_chiffres[2] = [1, 0, 1j, 1j + 1, 2j + 1, 2j]
points_chiffres[1] = [1 + 2j, 1]
points_chiffres[0] = [0, 1, 1 + 2j, 2j, 0]

def digit_sample(d):
    return points_chiffres[d]

# (ii)

segments_nombres = [0] * 10

def sample_number(d):
	points = digit_sample(d)
	segments = [0] * (len(points_chiffres[d]) - 1)
for i in range(len(points) - 1):
		segments[i] = segment(points[i], points[i + 1], 5) # le chiffre 5 est à modifier selon le niveau de précision souhaité
	return segments

#example
print(sample_number(2))


# EXERCICE 3

def complex(points_coord): # points_coord est une liste de listes (ex: [[x point 1, y point 1], …, [x point n, y point n]])
	points_complex = [0] * len(points_coord)
	for i in range(len(points_coord)):
		reel = points_coord[i][0]
		im = points_coord[i][1]
		points_complex[i] = reel + im * 1j
	return points_complex

# example
print(complex([[1, 2], [3, -4]]))
