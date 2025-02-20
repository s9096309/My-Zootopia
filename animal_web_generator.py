import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_html(data):
    """Generates HTML for animal information."""
    output = ""
    for animal in data:
        output += '<li class="cards__item">\n'  # Start of list item
        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}<br/>\n"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += '</li>\n'  # End of list item
    return output

def create_animals_html(input_json, template_file, output_file):
    """Creates the final HTML file."""
    try:
        animals_data = load_data(input_json)
        animal_html = generate_animal_html(animals_data)  # Use the new function

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