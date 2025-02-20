import json


# Load the JSON data
def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


# Generate HTML for the animals
def generate_animals_html(data):
    animals_html = ""
    for animal in data:
        name = animal.get("name", "Unknown")
        diet = animal.get("characteristics", {}).get("diet", "Unknown")
        locations = ", ".join(animal.get("locations", []))
        type_ = animal.get("characteristics", {}).get("type", "Unknown")

        animals_html += f"""
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <p class="card__text">
                <strong>Diet:</strong> {diet}<br/>
                <strong>Location:</strong> {locations}<br/>
                <strong>Type:</strong> {type_}<br/>
            </p>
        </li>
        """
    return animals_html


# Update the template and save the final HTML
def create_animals_html(input_json, template_file, output_file):
    # Load data
    animals_data = load_data(input_json)

    # Generate animals' HTML
    animals_html = generate_animals_html(animals_data)

    # Read the template
    with open(template_file, "r") as file:
        template_content = file.read()

    # Replace the placeholder
    updated_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write to a new HTML file
    with open(output_file, "w") as file:
        file.write(updated_content)


# File paths
input_json = "animals_data.json"
template_file = "animals_template.html"
output_file = "animals.html"

# Create the HTML
create_animals_html(input_json, template_file, output_file)
