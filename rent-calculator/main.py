def calculate_rent():
    print("--- College Roommate Rent Splitter ---")
    
    total_rent = float(input("Enter total monthly rent: $"))
    utilities = float(input("Enter total utilities (WiFi, Electricity, etc): $"))
    num_roommates = int(input("Enter number of roommates: "))
    
    # Simple split for utilities
    utility_per_person = utilities / num_roommates
    
    print("\nHow would you like to split the base rent?")
    print("1. Equally")
    print("2. By Room Size (Square Footage)")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        individual_rent = total_rent / num_roommates
        total_due = individual_rent + utility_per_person
        print(f"\nEach person owes: ${total_due:.2f} (${individual_rent:.2f} rent + ${utility_per_person:.2f} utilities)")
    
    elif choice == '2':
        total_sqft = float(input("Enter total square footage of all bedrooms combined: "))
        for i in range(num_roommates):
            name = input(f"Enter name for roommate {i+1}: ")
            room_sqft = float(input(f"Enter square footage for {name}'s room: "))
            
            # Rent is proportional to room size
            share = (room_sqft / total_sqft) * total_rent
            total_due = share + utility_per_person
            
            print(f"---> {name} owes: ${total_due:.2f} (${share:.2f} rent + ${utility_per_person:.2f} utilities)\n")

if __name__ == "__main__":
    calculate_rent()
