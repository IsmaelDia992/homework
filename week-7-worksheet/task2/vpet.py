# Define a class called VirtualPet with the following attributes:
# (1) name - the name of the pet
# (2) energy - the energy points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed, as a minimum, for the __init__ method





# This class has the following methods:
# (1) play() - If energy<2, report in the format "{name} is too tired to play!".
#     Otherwise simulate playing by reducing the energy by 2 and increase the hunger by 2.
# (2) feed() - Simulate feeding the pet and reducing hunger by 3.
#     If hunger is less than 0, report in the format "{name} is overfed!" and reset hunger to 0.
# (3) sleep() - let the pet sleep and increase the energy by 10.
# (4) __str__() - returns the details of the pet in the format "{name} has {energy} energy points and hunger level {hunger}", 
#     e.g., "Timmy has 100 energy points and hunger level 0"
# (5) __eq__() - returns True if all attributes are identical, False otherwise

# You should test each method in your code before submission.
# Check that attributes are modified as expected
# For example:

''' Tests
Pet = VirtualPet("Timmy",4,3)
print(Pet)
Pet.play()
print(Pet)
Pet.feed()
print(Pet)
Pet.sleep()
print(Pet)
'''