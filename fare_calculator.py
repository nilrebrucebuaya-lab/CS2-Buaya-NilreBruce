# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ").strip()

# 1. Passenger name -- Must not be empty
while name == "":
    print("Invalid Name.")
    name = input("Enter passenger name: ").strip()
    
distance = float(input("Enter distance (km): "))

# 2. Distance -- Number greater than 0
while distance <= 0:
    print("Distance should not be negative or zero.")
    distance = float(input("Enter distance (km): "))
    
passengers = int(input("Enter number of passengers: "))

# 3. Passengers -- Positive whole number
while passengers <= 0:
    print("Passengers should not be negative or zero.")
    passengers = int(input("Enter number of passengers: "))
    
total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
