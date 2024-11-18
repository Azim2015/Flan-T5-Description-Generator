# Flan-T5-Description-Generator
A description would be generator from structure textual data. The data source is stored in the form of Dictionary in Python language.
In fact, in this project the code relies on images and more specifically the focus is on images of traffic, passengers, pedestrians etc.
Since generating a comprehensive description from an image is a different task, this part would be implemented in a different project instead and the textual feature-based data would be used to be fed into the main model. The structured data should convey much more features that we do not consider in this project.

A sample structured textual data is as follows:

checklist = {
    "Location/Setting": {
        "Urban areas with buildings": "Visible storefronts and advertisements, including 'GIFTS' shop and other storefront signs.",
        "City street": "Busy street filled with taxis and pedestrians.",
        "Highway, suburban, rural, mountainous": "N/A",
        "Vehicles in a parking lot, tollbooth, or on a highway ramp": "N/A",
        "Narrow streets or cobblestone roads": "N/A"
    },
    "Vehicle Information": {
        "Vehicle types": "Yellow taxis, police car, white van.",
        "Vehicle colors": "Yellow (taxis), white (van and police car).",
        "License plates": "License plates are visible on several vehicles.",
        "Electric bikes and scooters present": "N/A"
    },
    "Traffic and Road Elements": {
        "Traffic density": "High density with many taxis stopped in traffic.",
        "Road markings": "Pedestrian crosswalks visible on the road.",
        "Signage": "Store signs and advertisements, including 'GIFTS' sign and NYPD sign.",
        "Road conditions": "Dry road.",
        "Traffic lights": "N/A",
        "Pedestrian elements": "Crosswalk with pedestrians visible on the sidewalk.",
        "Road barriers": "Metal barriers set up along the sidewalk, possibly for crowd control.",
        "Bus stops or taxi stands": "N/A"
    },
    "Environmental and Weather Conditions": {
        "Time of day": "Daylight.",
        "Weather conditions": "Clear, no signs of rain or adverse weather.",
        "Seasons": "N/A",
        "Visibility impacted by fog, snow, or glare": "N/A"
    },
    "Safety Equipment and Measures": {
        "Seatbelts": "N/A",
        "Car seats": "N/A",
        "Helmets": "N/A",
        "Airbags": "N/A",
        "Car cameras": "N/A",
        "Steering controls": "N/A",
        "Other safety-related devices": "N/A"
    },
    "Driver and Passenger Behaviors": {
        "Driver distraction": "N/A",
        "Passenger activities": "N/A",
        "Emotional expressions": "N/A",
        "Body language": "N/A",
        "Hands on the wheel": "N/A",
        "Seat adjustments": "N/A",
        "Sunglasses": "N/A"
    },
    "Technology Inside the Vehicle": {
        "Mobile phones": "N/A",
        "Navigation screens": "N/A",
        "Car dashboard displays": "N/A",
        "Interior mirrors": "N/A"
    },
    "Exterior and Pedestrian Elements": {
        "Pedestrians walking on sidewalks, crossing streets": "Pedestrians visible on the sidewalk along the storefronts.",
        "Pedestrians using crosswalks, jaywalking, or standing on curbs": "Pedestrians standing on the sidewalk near crosswalks.",
        "Cyclists and bikers": "N/A",
        "Other drivers": "N/A",
        "Street vendors": "Possible vendors or shop displays along the sidewalk.",
        "Street furniture": "N/A"
    },
    "Miscellaneous Elements": {
        "Roadside advertisements": "Billboards and store signs visible, promoting various shops and items.",
        "Shops and storefronts": "Shops and storefronts visible along the street, including 'GIFTS' shop and souvenir stores.",
        "Parked vehicles": "N/A",
        "Construction zones": "N/A"
    },
    "Privacy Elements": {
        "License plate": "N/A",
        "Number of faces visible": "N/A",
        "Clarity of faces": "N/A",
        "Expressions": "N/A",
        "Phone visibility": "N/A"
    },
    "Distracted drivers": "N/A",
    "Passengers assisting with navigation": "N/A",
    "Child in car seat": "N/A",
    "Hands on mobile phones": "N/A",
    "Seatbelt buckling/unbuckling": "N/A",
    "Phone conversation while driving": "N/A",
    "Rear-view focus": "N/A",
    "Child safety seats": "N/A"
}
