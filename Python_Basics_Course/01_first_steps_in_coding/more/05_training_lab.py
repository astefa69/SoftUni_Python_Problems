#Write a program that reads auditorium's dimensions
# and calculates the number of workstations in it at the described configuration (see figure).

w = float(input())
h = float(input())

w = w * 100
h = h * 100 
#Constraints: 3 ≤ h ≤ w ≤ 100.

#One workstation occupies 70 by 120 cm
# (table size 70 by 40 cm + chair and passage space size 70 by 80 cm).
# The corridor is at least 100 cm wide.
# It is calculated that exactly 1 workstation is wasted because of the entrance door (which has an opening of 160 cm),
# and exactly 2 workstations are wasted because of the chair (which is 160 cm by 120 cm).
area_workstation = 70 * 120 #in cm
workstation_h = 70 # width
workstation_w = 120 # height
hallway_length = 100 #КThe corridor is at least 100 cm wide.
door_area = 1 * area_workstation #because of the entrance door (which has an opening of 160 cm) exactly 1 workplace is wasted
podium_area = 2 * area_workstation

####

remaining_h = h - hallway_length
workstations_h_number = remaining_h // workstation_h


workstations_w_number = w // workstation_w


number_of_workstations = workstations_h_number * workstations_w_number - 3 # 3 is the number of workstations that are lost because of the podium and the door
number_of_workstations = int(number_of_workstations)

#Print an integer on the console: the number of seats in the auditorium.
print(number_of_workstations)

