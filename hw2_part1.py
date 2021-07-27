""" Author: Christina Elmore
    Purpose: Calculate amount of oxygen needed for astronaughts to survive on mars.
"""

import math

def volume_cone(radius, height):                   #returns volume of a cone
    return float(math.pi * (radius ** 2) * (height/3))
def volume_cylinder(radius, height):               #returns volume of a cylinder
    return float(math.pi * (radius ** 2) * height)

RadiusC = float(raw_input("Radius of capsule (m) ==> "))
print RadiusC
HeightC = float(raw_input("Height of capsule (m) ==> "))
print HeightC
RadiusOR = float(raw_input("Radius of oxygen reservoir (m) ==> "))
print RadiusOR
HeightOR = float(raw_input("Height of oxygen reservoir (m) ==> "))
print HeightOR
VolumeC = volume_cone(RadiusC, HeightC)
oxygen_needed = VolumeC * .21 * .41 * 300
VolumeCy = volume_cylinder(RadiusOR, HeightOR)
oxygen_held = VolumeCy * 210
tanks_needed = math.ceil(oxygen_needed/oxygen_held)

print "Oxygen needed for the trip is %.3fm^3\nEach cylinder holds %.3fm^3 at 3000 psi\nThe trip will require %d reservoir tanks." %( oxygen_needed, oxygen_held, tanks_needed)