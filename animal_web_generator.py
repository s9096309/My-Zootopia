import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animal_info(data):
    """Prints animal information."""
    for animal in data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal and animal["locations"]:  # Check if locations list is not empty
            print(f"Location: {animal['locations'][0]}")  # Print the first location
        if "characteristics" in animal and "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")
        print()  # Add an empty line between animals


# File path
input_json = "animals_data.json"

# Load data
try:
    animals_data = load_data(input_json)
    print_animal_info(animals_data)
except FileNotFoundError:
    print(f"Error: File '{input_json}' not found.")
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in '{input_json}'.")
except Exception as e: # Catching other potential errors for more robust code
    print(f"An error occurred: {e}")