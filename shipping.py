# Shipping price

weight = 1.5

# Ground Shipping

flat_charge_ground_shipping = 20.00

if weight <= 2:
  cost = weight * 1.50 + flat_charge_ground_shipping
elif weight >= 2 and weight <= 6:
  cost = weight * 3.00 + flat_charge_ground_shipping

elif weight >= 6 and weight <= 10:
  cost = weight * 4.00 + flat_charge_ground_shipping 
elif weight >= 10:
  cost = weight * 4.00 + flat_charge_ground_shipping 


print("Cost for Ground Shipping : $", cost)


# Ground Shipping Premium

flat_charge_ground_shipping = 125.00

print("Ground Shipping Premium $" , flat_charge_ground_shipping )

# Drone Shipping

flat_charge_drone_shipping = 0.00

if weight <= 2:
  cost = weight * 4.50 + flat_charge_drone_shipping
elif weight >= 2 and weight <= 6:
  cost = weight * 9.00 + flat_charge_drone_shipping
elif weight >= 6 and weight <= 10:
  cost = weight * 12.00 + flat_charge_drone_shipping
elif weight >= 10:
  cost = weight * 14.25 + flat_charge_drone_shipping

print("Dron Shipping : $", cost )