import os
import time

class AttributeSet:
    def __init__(self, category_name, traits):
        self.category_name = category_name
        self.traits = traits

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_set(attribute_set):
    print("----------------------------------------")
    print(f"   SCANNING SECTOR: {attribute_set.category_name}")
    print("----------------------------------------")
    for trait in attribute_set.traits:
        print(" > " + trait)
    print("\n[Status] Processing next data packet...\n")

def main():
    roommate_data = [
        AttributeSet(
            "IDENTIFICATION",
            [
                "Name: Your Roommate",
                "Nationality: Kenyan",
                "Student Status: Third-year student at Majimoto University",
                "General Impression: Intelligent, focused, quietly observant"
            ]
        ),
        AttributeSet(
            "PHYSICAL PROFILE",
            [
                "Height: Short",
                "Build: Slim",
                "Hair: Short and neat",
                "Facial Expression: Calm but sharp-eyed"
            ]
        ),
        AttributeSet(
            "ACADEMIC & SKILL SET",
            [
                "Strength: Quick thinker with fast comprehension",
                "Study Habits: Prefers quiet environments",
                "Performance: Consistently above average",
                "Talent: Strong memory for fine details"
            ]
        ),
        AttributeSet(
            "BEHAVIORAL TRAITS",
            [
                "Daily Rhythm: Early riser",
                "Personality: Reserved but witty when comfortable",
                "Organization Level: Keeps space tidy and minimalistic",
                "Focus Trait: Soft muttering while concentrating"
            ]
        ),
        AttributeSet(
            "MISCELLANEOUS OBSERVATIONS",
            [
                "Favorite Drink: Strong Kenyan chai",
                "Preferred Clothing: Hoodies and jeans",
                "Hobby: Sketching geometric patterns",
                "Overall Vibe: Quiet storm of discipline and intelligence"
            ]
        )
    ]

    print("INITIALIZING ROOMMATE ANALYSIS PROTOCOL...")
    time.sleep(2)

    cycle = 1
    while True:
        clear_screen()
        print(f"=== SCAN CYCLE {cycle} START ===\n")

        for data in roommate_data:
            display_set(data)
            time.sleep(3)

        print("Cycle complete. Preparing next analysis sequence...")
        time.sleep(2)
        cycle += 1

if __name__ == "__main__":
    main()
