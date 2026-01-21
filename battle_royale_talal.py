import random
import time

def battle_royale_talal_edition():
    # --- STEP 1: INITIALIZATION ---
    # Why? We define the starting state so the game has a "memory" of your stats.
    creator_name = "Muhammad Talal"
    batch_year = "UET 2026"
    
    health = 100
    players_left = 50
    inventory = ["Bandage"]
    weapon_power = 40 
    day_count = 1
    
    print(f"{'='*40}")
    print(f"🚀 BATTLE ROYALE: {batch_year} EDITION")
    print(f"Developed by: {creator_name}")
    print(f"{'='*40}")
    time.sleep(1) # Why? Adds a pause so the user can read the intro.
    print(f"\n🛩️ Landed in UET Sector! {players_left} Players remain.")
    
    # --- STEP 2: GAME LOOP ---
    # Why? 'while' keeps the game running as long as the conditions are met.
    while health > 0 and players_left > 1:
        print(f"\n[DAY {day_count}] --- HP: {health} | Players: {players_left} | Gear: {inventory} ---")
        
        # --- STEP 3: INPUT HANDLING ---
        # Why? Allows the player to drive the logic of the program.
        action = input("Action -> (1: Scout 🔍, 2: Loot 📦, 3: Heal 🩹, 4: Quit 🏃): ")
        
        if action == "1": # FIGHTING LOGIC
            enemy_power = random.randint(20, 90)
            print(f"🔍 Scouting UET Library... Spotted an enemy (Power: {enemy_power})!")
            
            choice = input("Engage in combat? (y/n): ").lower()
            if choice == 'y':
                if weapon_power >= enemy_power:
                    eliminated = random.randint(2, 6)
                    players_left -= eliminated
                    print(f"🎯 Clean shot! You eliminated the threat. {players_left} remain.")
                else:
                    damage = (enemy_power - weapon_power) + 10
                    health -= damage
                    print(f"💥 Outgunned! You took {damage} damage.")
            
        elif action == "2": # UPGRADE LOGIC
            # Why? choice() picks a random string from our list to keep the game fresh.
            item = random.choice(["AKM", "AWM Sniper", "Level 3 Vest", "Medkit", "Energy Drink"])
            print(f"📦 Found a crate: {item}!")
            
            if item in ["AKM", "AWM Sniper"]:
                weapon_power += 25
                print("⬆️ Attack Power Upgraded!")
            
            inventory.append(item)

        elif action == "3": # RECOVERY LOGIC
            # Why? We check if the item exists in the list before using it to prevent errors.
            if "Bandage" in inventory or "Medkit" in inventory:
                healing_item = "Medkit" if "Medkit" in inventory else "Bandage"
                health = min(100, health + 40)
                inventory.remove(healing_item)
                print(f"🩹 Used {healing_item}. HP restored to {health}.")
            else:
                print("❌ No healing items found!")

        elif action == "4": # EXIT LOGIC
            print("Coward! You fled the UET Sector.")
            break

        # --- STEP 4: WORLD EVENT LOGIC ---
        # Why? random.random() returns a number between 0 and 1. 
        # 0.3 means there is a 30% chance of the circle shrinking every turn.
        if random.random() < 0.3 and players_left > 5:
            shrink = random.randint(3, 8)
            players_left -= shrink
            print(f"⭕ CIRCLE SHRINKING! {shrink} players caught in the blue zone.")

        day_count += 1
        time.sleep(0.5)

    # --- STEP 5: END GAME HANDLER ---
    if health > 0 and action != "4":
        print(f"\n🏆 WINNER WINNER CHICKEN DINNER, {creator_name}!")
        print(f"UET 2026 Champion status achieved.")
    elif health <= 0:
        print("\n💀 WASTED. Better luck next time, Talal.")

if __name__ == "__main__":
    battle_royale_talal_edition()
