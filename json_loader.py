import json

def load_settings(file_path='data/jsons/settings.json'):
    """Load game settings from the specified JSON file."""
    try:
        with open(file_path, 'r') as file:
            settings = json.load(file)
        return settings
    except FileNotFoundError:
        print(f"Settings file not found at {file_path}. Creating default settings.")
        create_default_settings(file_path)  # You can call a function to create default settings
        return load_settings(file_path)  # Retry loading settings after creating

def create_default_settings(file_path='data/jsons/settings.json'):
    """Create default settings if the settings file does not exist."""
    default_settings = {
        "slider_values": [50.0, 50.0]  # Default volume levels
    }
    with open(file_path, 'w') as file:  # Use 'w' mode to create or overwrite
        json.dump(default_settings, file, indent=4)
        print("Default settings created.")
        
def load_save(file_path='data/jsons/save_file.json'):
    """Load game save data from the specified JSON file."""
    try:
        with open(file_path, 'r') as file:
            save_data = json.load(file)
        return save_data
    except FileNotFoundError:
        return "No save file"

save_file = load_save()

game_state = {    
    
    "current_character": save_file.get('current_character', None),
    "current_bgm": save_file.get('current_bgm', None),
    "current_background": save_file.get('current_background', None),
    "current_dialogue": save_file.get('current_dialogue', None),
    "last_saved_text": save_file.get('last_saved_text', "Greeting, Trailblazer.")
}

# Load the settings from the JSON file
settings = load_settings()  # This will use the default file path
slider_values = settings.get('slider_values', [50.0, 50.0])  # Get slider values or use default

# Convert slider values to a 0.0 to 1.0 range
bgm_volume = slider_values[0] / 100  # BGM volume
sfx_volume = slider_values[1] / 100  # SFX volume

# Example of updating the slider values dynamically
# If the user adjusts the sliders in the settings menu, update the slider_values
# For demonstration, let's assume the user adjusted the sliders

# Update the volume values again
bgm_volume = slider_values[0] / 100
sfx_volume = slider_values[1] / 100
