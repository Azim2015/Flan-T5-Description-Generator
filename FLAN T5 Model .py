from transformers import pipeline



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






qa_model = pipeline("text2text-generation", model="google/flan-t5-xl", device=0)  # Use device=0 for the first GPU


def serialize_checklist(checklist):
    serialized_text = ""
    for category, details in checklist.items():
        if isinstance(details, dict):
            serialized_text += f"{category}:\n"
            for subcategory, description in details.items():
                serialized_text += f"  - {subcategory}: {description}\n"
        else:
            serialized_text += f"{category}: {details}\n"
    return serialized_text
    
    


scene_description = serialize_checklist(checklist)

prompt = "Describe the scene."
prompt = "What objects are in the scene?"
prompt = "Explain weather condition?"
prompt = "Explain privacy features in the scene? such as people or gender etc"
prompt = "Explain anything about privacy?"
prompt = "Any phone handling?"

input_text = f"Scene details:\n{scene_description}\n\nQuestion: {prompt}"

response = qa_model(input_text, max_length=250, num_return_sequences=1, temperature=0.7)[0]["generated_text"]
print("Detailed Scene Description:", response)
