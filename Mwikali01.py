import time
import os

class AttributeSet:
    def __init__(self, categoryName, traits):
        self.categoryName = categoryName
        self.traits = traits

def clearScreen():
    print("\033c", end="")

def redact(text):
    return "".join("█" if c.isalnum() else c for c in text)

def displayProtected(setObj):
    print("----------------------------------------")
    print(f"   PROTECTED SECTOR: {setObj.categoryName}")
    print("----------------------------------------")
    for trait in setObj.traits:
        print(" >", redact(trait))
    print("\n[Status] Data masked for privacy.\n")

def main():
    roommateData = [
        AttributeSet(
            "IDENTIFICATION",
            [
                "Subject ID: 'The Roommate'",
                "Name: 'Maya'",
                "Age: 24",
                "Occupation: Architecture Student / Barista"
            ]
        ),
        AttributeSet(
            "PHYSICAL METRICS",
            [
                "Height: 5'7\" (170 cm)",
                "Build: Slender, poor posture from drafting tables",
                "Skin Tone: Warm Olive",
                "Hair: Dark brown, perpetually in a messy bun",
                "Eyes: Hazel, usually squinting at a screen"
            ]
        ),
        AttributeSet(
            "APPAREL & AESTHETIC",
            [
                "Top: Oversized vintage university sweatshirt (stolen)",
                "Bottoms: Black leggings (covered in cat hair)",
                "Footwear: Fuzzy socks inside Crocs",
                "Accessories: Blue light glasses, silver nose ring"
            ]
        ),
        AttributeSet(
            "BEHAVIORAL QUIRKS",
            [
                "Diet: 80% Iced Coffee, 20% Instant Ramen",
                "Sleep Cycle: Nocturnal (Active 11 PM - 4 AM)",
                "Volume Level: Hums lo-fi beats unconsciously",
                "Hazard Level: Leaves dishes in sink for 3-5 business days"
            ]
        )
    ]

    clearScreen()
    print("=== PRIVACY SAFEGUARD PROTOCOL ACTIVE ===")
    time.sleep(1)

    for s in roommateData:
        displayProtected(s)
        time.sleep(1)

    print("SUMMARY: Sensitive data has been protected.")
    print("Program exiting to maintain confidentiality.")

if __name__ == "__main__":
    main()
