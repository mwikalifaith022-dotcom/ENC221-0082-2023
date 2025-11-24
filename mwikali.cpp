#include <iostream>
#include <vector>
#include <string>
#include <thread>
#include <chrono>

struct AttributeSet {
    std::string categoryName;
    std::vector<std::string> traits;
};

void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void displaySet(const AttributeSet& set) {
    std::cout << "----------------------------------------" << std::endl;
    std::cout << "   SCANNING SECTOR: " << set.categoryName << std::endl;
    std::cout << "----------------------------------------" << std::endl;

    for (const auto& trait : set.traits) {
        std::cout << " > " << trait << std::endl;
    }
    std::cout << "\n[Status] Processing next data packet...\n" << std::endl;
}

int main() {
    std::vector<AttributeSet> roommateData = {
        {
            "IDENTIFICATION",
            {
                "Subject ID: 'The Roommate'",
                "Name: 'Maya'",
                "Age: 24",
                "Occupation: Architecture Student / Barista"
            }
        },
        {
            "PHYSICAL METRICS",
            {
                "Height: 5'7\" (170 cm)",
                "Build: Slender, poor posture from drafting tables",
                "Skin Tone: Warm Olive",
                "Hair: Dark brown, perpetually in a messy bun",
                "Eyes: Hazel, usually squinting at a screen"
            }
        },
        {
            "APPAREL & AESTHETIC",
            {
                "Top: Oversized vintage university sweatshirt (stolen)",
                "Bottoms: Black leggings (covered in cat hair)",
                "Footwear: Fuzzy socks inside Crocs",
                "Accessories: Blue light glasses, silver nose ring"
            }
        },
        {
            "BEHAVIORAL QUIRKS",
            {
                "Diet: 80% Iced Coffee, 20% Instant Ramen",
                "Sleep Cycle: Nocturnal (Active 11 PM - 4 AM)",
                "Volume Level: Hums lo-fi beats unconsciously",
                "Hazard Level: Leaves dishes in sink for 3-5 business days"
            }
        }
    };

    std::cout << "INITIALIZING ROOMMATE SURVEILLANCE PROTOCOL..." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));

    int cycleCount = 1;
    while (true) {
        clearScreen();
        std::cout << "=== CYCLE " << cycleCount << " IN PROGRESS ===" << std::endl;
        std::cout << "Target acquired.\n" << std::endl;

        for (const auto& set : roommateData) {
            displaySet(set);
            std::this_thread::sleep_for(std::chrono::seconds(5));
        }

        std::cout << "Cycle complete. Rebooting scan sequence..." << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(2));
        cycleCount++;
    }

    return 0;
}
