import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_obj):
    """Serializes a single animal object into HTML."""
    output = '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f'<p class="card__text"><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal_obj and animal_obj["locations"]:
        output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>\n' # Close the <p> tag
    output += '</li>\n'
    return output

def generate_animal_html(data):
    """Generates HTML for all animal information."""
    output = ""
    for animal in data:
        output += serialize_animal(animal)  # Use the new function
    return output

def create_animals_html(input_json, template_file, output_file):
    """Creates the final HTML file."""
    try:
        animals_data = load_data(input_json)
        animal_html = generate_animal_html(animals_data)

        with open(template_file, "r") as file:
            template_content = file.read()

        updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_html)

        with open(output_file, "w") as file:
            file.write(updated_content)

        print(f"HTML file '{output_file}' created successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_json}' or '{template_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_json}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# File paths
input_json = "animals_data.json"
template_file = "animals_template.html"
output_file = "animals.html"

# Create the HTML
create_animals_html(input_json, template_file, output_file)