# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tools for Wanderlust Travel Concierge Agent."""

from typing import Any, Dict, List, Optional

# Curated destination database
DESTINATIONS = {
    "tokyo": {
        "id": "tokyo",
        "name": "Tokyo, Japan",
        "continent": "Asia",
        "country": "Japan",
        "vibe": ["futuristic", "culinary", "cultural", "shopping"],
        "budget_tier": "$$$",
        "currency": "JPY (Yen)",
        "best_season": "March to May (Cherry Blossom) & September to November",
        "avg_daily_cost_usd": 150,
        "est_flight_usd": 900,
        "highlights": [
            "Shibuya Crossing & Harajuku street style",
            "Tsukiji Outer Market sashimi breakfast",
            "Senso-ji temple in historic Asakusa",
            "Shinjuku Gyoen National Garden",
            "TeamLab Planets digital art museum"
        ],
        "hotels": [
            {"name": "Park Hyatt Tokyo", "tier": "luxury", "price_per_night": 650},
            {"name": "Hotel Gracery Shinjuku", "tier": "midscale", "price_per_night": 180},
            {"name": "Khaosan Tokyo Origami", "tier": "budget", "price_per_night": 55},
        ],
        "top_eats": ["Ramen at Ichiran", "Sushi Dai", "Monjayaki in Tsukishima"]
    },
    "paris": {
        "id": "paris",
        "name": "Paris, France",
        "continent": "Europe",
        "country": "France",
        "vibe": ["romantic", "art", "architecture", "culinary"],
        "budget_tier": "$$$",
        "currency": "EUR (Euro)",
        "best_season": "April to June & September to October",
        "avg_daily_cost_usd": 180,
        "est_flight_usd": 850,
        "highlights": [
            "Eiffel Tower and Champ de Mars picnic",
            "Louvre Museum & Musée d'Orsay",
            "Montmartre and Sacré-Cœur sunset",
            "Seine river sunset cruise",
            "Saint-Germain-des-Prés café hopping"
        ],
        "hotels": [
            {"name": "Le Bristol Paris", "tier": "luxury", "price_per_night": 1100},
            {"name": "Hotel Malte - Astotel", "tier": "midscale", "price_per_night": 220},
            {"name": "Generator Paris", "tier": "budget", "price_per_night": 65},
        ],
        "top_eats": ["Fresh croissants at Du Pain et des Idées", "Duck Confit at Le Petit Châtelet", "Macarons at Pierre Hermé"]
    },
    "bali": {
        "id": "bali",
        "name": "Bali, Indonesia",
        "continent": "Asia",
        "country": "Indonesia",
        "vibe": ["relaxation", "beaches", "wellness", "nature", "adventure"],
        "budget_tier": "$",
        "currency": "IDR (Indonesian Rupiah)",
        "best_season": "April to October (Dry Season)",
        "avg_daily_cost_usd": 60,
        "est_flight_usd": 950,
        "highlights": [
            "Tegallalang Rice Terraces in Ubud",
            "Sunset at Uluwatu Temple with Kecak Fire Dance",
            "Surfing in Canggu and Seminyak",
            "Sunrise hike at Mount Batur",
            "Nusa Penida island day trip"
        ],
        "hotels": [
            {"name": "Four Seasons Resort Bali at Sayan", "tier": "luxury", "price_per_night": 800},
            {"name": "Ubud Village Hotel", "tier": "midscale", "price_per_night": 95},
            {"name": "Puri Garden Hotel & Hostel", "tier": "budget", "price_per_night": 35},
        ],
        "top_eats": ["Nasi Campur", "Babi Guling", "Açaí bowls in Canggu"]
    },
    "costa_rica": {
        "id": "costa_rica",
        "name": "Arenal & Manuel Antonio, Costa Rica",
        "continent": "Americas",
        "country": "Costa Rica",
        "vibe": ["wildlife", "eco-adventure", "rainforest", "beaches"],
        "budget_tier": "$$",
        "currency": "CRC (Colón) / USD",
        "best_season": "December to April",
        "avg_daily_cost_usd": 110,
        "est_flight_usd": 550,
        "highlights": [
            "Arenal Volcano thermal hot springs",
            "Ziplining through Monteverde Cloud Forest",
            "Sloth and toucan spotting in Manuel Antonio National Park",
            "Whitewater rafting on the Pacuare River",
            "Hanging bridges canopy walk"
        ],
        "hotels": [
            {"name": "Nayara Tented Camp", "tier": "luxury", "price_per_night": 950},
            {"name": "Arenal Springs Resort & Spa", "tier": "midscale", "price_per_night": 210},
            {"name": "Selina Manuel Antonio", "tier": "budget", "price_per_night": 45},
        ],
        "top_eats": ["Gallo Pinto with fried plantains", "Casado with fresh catch", "Artisanal Tarrazú coffee"]
    },
    "rome": {
        "id": "rome",
        "name": "Rome, Italy",
        "continent": "Europe",
        "country": "Italy",
        "vibe": ["history", "culinary", "architecture", "cultural"],
        "budget_tier": "$$",
        "currency": "EUR (Euro)",
        "best_season": "April to May & September to October",
        "avg_daily_cost_usd": 140,
        "est_flight_usd": 800,
        "highlights": [
            "Colosseum & Roman Forum underground tour",
            "Vatican Museums and Sistine Chapel",
            "Pantheon and Trevi Fountain coin toss",
            "Trastevere evening food walking tour",
            "Villa Borghese gardens bike ride"
        ],
        "hotels": [
            {"name": "Hotel de Russie", "tier": "luxury", "price_per_night": 850},
            {"name": "Hotel Artemide", "tier": "midscale", "price_per_night": 190},
            {"name": "The YellowSquare Rome", "tier": "budget", "price_per_night": 40},
        ],
        "top_eats": ["Cacio e Pepe at Da Enzo", "Pizza al Taglio at Bonci Pizzarium", "Gelato at Frigidarium"]
    },
    "banff": {
        "id": "banff",
        "name": "Banff National Park, Canada",
        "continent": "Americas",
        "country": "Canada",
        "vibe": ["mountains", "nature", "hiking", "scenic"],
        "budget_tier": "$$$",
        "currency": "CAD (Canadian Dollar)",
        "best_season": "June to August (hiking) & December to March (skiing)",
        "avg_daily_cost_usd": 170,
        "est_flight_usd": 450,
        "highlights": [
            "Canoeing on turquoise Lake Louise",
            "Moraine Lake sunrise viewpoint",
            "Icefields Parkway scenic drive",
            "Banff Upper Hot Springs soak",
            "Johnston Canyon waterfall hike"
        ],
        "hotels": [
            {"name": "Fairmont Banff Springs", "tier": "luxury", "price_per_night": 750},
            {"name": "Moose Hotel and Suites", "tier": "midscale", "price_per_night": 230},
            {"name": "HI Banff Alpine Centre", "tier": "budget", "price_per_night": 50},
        ],
        "top_eats": ["Alberta Bison Steak", "BeaverTails pastry in Banff Town", "Fondue at Grizzly House"]
    }
}


def search_destinations(query: str = "", continent: str = "", budget_tier: str = "", travel_style: str = "") -> List[Dict[str, Any]]:
    """Search and filter the curated catalog of travel destinations.

    Args:
        query: Optional search keyword (e.g. 'temple', 'hiking', 'beach', 'tokyo', 'europe').
        continent: Optional continent filter ('Asia', 'Europe', 'Americas').
        budget_tier: Optional budget tier filter ('$' for budget, '$$' for moderate, '$$$' for premium).
        travel_style: Optional vibe or style ('adventure', 'relaxation', 'culinary', 'cultural', 'nature').

    Returns:
        A list of matching destination summaries.
    """
    results = []
    q = query.lower().strip()
    c_filter = continent.lower().strip()
    b_filter = budget_tier.strip()
    s_filter = travel_style.lower().strip()

    for dest_id, dest in DESTINATIONS.items():
        # Query match
        if q:
            text_pool = f"{dest['name']} {dest['country']} {dest['continent']} {' '.join(dest['vibe'])} {' '.join(dest['highlights'])}".lower()
            if q not in text_pool:
                continue

        # Continent filter
        if c_filter and c_filter not in dest["continent"].lower():
            continue

        # Budget filter
        if b_filter and dest["budget_tier"] != b_filter:
            continue

        # Style filter
        if s_filter and not any(s_filter in v.lower() for v in dest["vibe"]):
            continue

        results.append({
            "id": dest["id"],
            "name": dest["name"],
            "continent": dest["continent"],
            "vibe": dest["vibe"],
            "budget_tier": dest["budget_tier"],
            "avg_daily_cost_usd": dest["avg_daily_cost_usd"],
            "best_season": dest["best_season"],
            "highlights_summary": dest["highlights"][:3]
        })

    return results if results else list(DESTINATIONS.values())[:3]


def get_destination_details(destination_id: str) -> Dict[str, Any]:
    """Retrieve comprehensive details, attractions, hotels, and food for a specific destination.

    Args:
        destination_id: Identifier of the destination (e.g. 'tokyo', 'paris', 'bali', 'costa_rica', 'rome', 'banff').

    Returns:
        Full destination details dictionary or error note.
    """
    key = destination_id.lower().replace(" ", "_").replace(",", "")
    for k, v in DESTINATIONS.items():
        if k in key or key in k:
            return v
    return {"error": f"Destination '{destination_id}' not found in catalog. Available: {list(DESTINATIONS.keys())}"}


def calculate_trip_budget(destination_id: str, days: int = 5, num_travelers: int = 1, accommodation_tier: str = "midscale", include_flights: bool = True) -> Dict[str, Any]:
    """Calculate an estimated trip budget breakdown for a destination.

    Args:
        destination_id: Target destination id (e.g. 'tokyo', 'paris', 'bali', 'costa_rica', 'rome', 'banff').
        days: Duration of the trip in days (default: 5).
        num_travelers: Number of people traveling (default: 1).
        accommodation_tier: Tier of lodging ('budget', 'midscale', 'luxury').
        include_flights: Whether to calculate estimated round-trip airfare.

    Returns:
        A detailed cost breakdown including lodging, daily expenses, flights, and total budget.
    """
    dest = get_destination_details(destination_id)
    if "error" in dest:
        return dest

    # Find hotel rate
    hotel_rate = dest["avg_daily_cost_usd"]
    for h in dest.get("hotels", []):
        if h["tier"] == accommodation_tier.lower():
            hotel_rate = h["price_per_night"]
            break

    # Calculate costs
    rooms_needed = max(1, (num_travelers + 1) // 2)
    lodging_total = hotel_rate * days * rooms_needed
    daily_spend_per_person = dest["avg_daily_cost_usd"]
    food_activities_total = daily_spend_per_person * days * num_travelers
    flight_total = (dest["est_flight_usd"] * num_travelers) if include_flights else 0
    grand_total = lodging_total + food_activities_total + flight_total

    return {
        "destination": dest["name"],
        "trip_length_days": days,
        "travelers": num_travelers,
        "accommodation_tier": accommodation_tier,
        "breakdown_usd": {
            "estimated_flights": flight_total,
            "lodging_total": lodging_total,
            f"daily_spend_food_activities ({days} days)": food_activities_total,
            "grand_total_usd": grand_total,
            "estimated_per_person_usd": round(grand_total / max(1, num_travelers), 2)
        },
        "currency_info": dest["currency"]
    }


def get_weather_and_packing_tips(destination: str, season: str = "summer") -> Dict[str, Any]:
    """Get climate information, seasonal weather, and packing checklist recommendations.

    Args:
        destination: Destination name or id.
        season: Target travel season ('spring', 'summer', 'fall', 'winter').

    Returns:
        A dictionary containing weather expectation and recommended packing essentials.
    """
    dest = get_destination_details(destination)
    dest_name = dest.get("name", destination)

    packing_essentials = [
        "Universal power adapter & portable power bank",
        "Comfortable walking / hiking shoes",
        "Passport & travel insurance docs",
        "Reusable water bottle"
    ]

    weather_desc = f"Moderate temperatures typical for {season.title()} season."
    if "bali" in destination.lower() or "costa_rica" in destination.lower():
        weather_desc = "Tropical climate: warm (80-88°F / 27-31°C), humid with occasional showers."
        packing_essentials.extend(["Light breathable linen clothing", "Waterproof rain jacket", "Reef-safe sunscreen & bug repellent", "Swimwear"])
    elif "banff" in destination.lower():
        weather_desc = "Alpine climate: cool evenings, crisp mountain breeze (50-70°F in summer, sub-freezing in winter)."
        packing_essentials.extend(["Warm layers / fleece jacket", "Thermal base layers", "Sturdy trail hiking boots", "UV sunglasses"])
    elif "tokyo" in destination.lower() or "paris" in destination.lower() or "rome" in destination.lower():
        weather_desc = "Urban temperate climate with seasonal variations."
        packing_essentials.extend(["Smart casual city attire", "Light layers", "Cross-body anti-theft bag", "Compact umbrella"])

    return {
        "destination": dest_name,
        "season": season,
        "weather_summary": weather_desc,
        "packing_checklist": packing_essentials
    }
