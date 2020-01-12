#weight the cost is being calculated for
weight_input = 1.5


#flat charge to be added to weight cost for ground
ground_flat = 20
#flat charge for premium, no weight cost
premium_flat = 125


#total cost for ground
def ground_cost_calc(weight):
  if weight <= 2:
    return weight * 1.5 + ground_flat
  elif weight <= 6:
    return weight * 3 + ground_flat
  elif weight <= 10:
    return weight * 4 + ground_flat
  elif weight > 10:
    return weight * 4.75 + ground_flat

#stores calculated cost for gound shipping
ground_cost = ground_cost_calc(weight_input)
print("Total cost for ground shipping is $" + str(ground_cost) + ".")

#total cost for drone
def drone_cost_calc(weight):
  if weight <= 2:
    return weight * 4.5
  elif weight <= 6:
    return weight * 9
  elif weight <= 10:
    return weight * 12
  elif weight > 10:
    return weight * 14.25

#stores calculated cost for drone shipping
drone_cost = drone_cost_calc(weight_input)
print("Total cost for drone shipping is $" + str(drone_cost) + ".")

print("Total cost for premium ground shipping is $125.")

#compares cost for different shipping methods
def method_suggestion(ground, drone, premium):
  if (ground < drone) and (ground < premium):
    return "Ground shipping is the cheapest option."
  elif (drone < premium) and (drone < ground):
    return "Drone shipping is the cheapest option."
  elif (premium < ground) and (premium < drone):
    return "Premium ground shipping is the cheapest option."

#prints cheapest method
print(method_suggestion(ground_cost, drone_cost, premium_flat))
    