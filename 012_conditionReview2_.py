weight = 1.5
premium = 125.00

# ground shipping
if weight <= 2:
  cost = (weight * 1.50) + 20
elif weight <=6:
  cost = (weight * 3) + 20
elif weight <= 10:
  cost = (weight * 4) + 20
else:
  cost = (weight * 4.75) + 20

# drone shipping
if weight <= 2:
  drone = (weight * 4.50)
elif weight <=6:
  drone = (weight * 9.00)
elif weight <= 10:
  drone = (weight * 12.00)
else:
  drone = (weight * 14.25)


print("Ground Shipping: " + str(cost))
print("Ground Shipping Premium: " + str(premium))
print("Drone Shipping: " + str(drone))