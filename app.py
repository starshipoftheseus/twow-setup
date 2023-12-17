from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Image paths for monsters
def add_image_paths(monster_allocations, level):
    for monster, info in monster_allocations.items():
        # Construct the image path based on the monster's name and level
        info['image_path'] = url_for('static', filename=f'monsters/level{level}Monsters/{monster.lower()}.png')

# Function to add image paths for terrain tokens
location_images = {
    1: 'static/tokens/terrainTokens/1.png',
    2: 'static/tokens/terrainTokens/2.png',
    3: 'static/tokens/terrainTokens/3.png',
    4: 'static/tokens/terrainTokens/4.png',
    5: 'static/tokens/terrainTokens/5.png',
    6: 'static/tokens/terrainTokens/6.png',
    7: 'static/tokens/terrainTokens/7.png',
    8: 'static/tokens/terrainTokens/8.png',
    9: 'static/tokens/terrainTokens/9.png',
    10: 'static/tokens/terrainTokens/10.png',
    11: 'static/tokens/terrainTokens/11.png',
    12: 'static/tokens/terrainTokens/12.png',
    13: 'static/tokens/terrainTokens/13.png',
    14: 'static/tokens/terrainTokens/14.png',
    15: 'static/tokens/terrainTokens/15.png',
    16: 'static/tokens/terrainTokens/16.png',
    17: 'static/tokens/terrainTokens/17.png',
    18: 'static/tokens/terrainTokens/18.png',
    19: 'static/tokens/terrainTokens/19.png',
    20: 'static/tokens/terrainTokens/20.png',
    21: 'static/tokens/terrainTokens/21.png'

}

def get_location_image_path(location):
    return url_for('static', filename=f'tokens/terrainTokens/{location}.png')

# Function to get the image path for a player board
def get_board_image_path(board_name):
    return url_for('static', filename=f'boards/{board_name}.jpg')

def assign_monster_and_weakness_locations(level_1_monsters, level_2_monsters, level_3_monsters, terrain_locations):
    # First, reserve one location in each terrain for weakness tokens
    weakness_allocations = {}
    reserved_locations = {}
    for terrain in terrain_locations:
        location = random.choice(terrain_locations[terrain])
        weakness_allocations[terrain] = location
        reserved_locations[terrain] = location

    # Function to randomly assign monsters to unique terrains and locations
    def assign(monsters, available_locations, reserved_locs):
        allocations = {}
        terrains = list(available_locations.keys())

        for monster in random.sample(monsters, len(terrains)):
            terrain = random.choice(terrains)
            locations = [loc for loc in available_locations[terrain] if loc != reserved_locs[terrain]]
            location = random.choice(locations) if locations else None

            if location:
                allocations[monster] = {
                    "Terrain": terrain, 
                    "Location": location,
                    "LocationImage": url_for('static', filename=f'tokens/terrainTokens/{location}.png')
                }
                available_locations[terrain].remove(location)
            terrains.remove(terrain)  # Remove terrain to ensure uniqueness

        return allocations

    # Assign monsters for each level
    level_1_allocations = assign(level_1_monsters, terrain_locations.copy(), reserved_locations)
    level_2_allocations = assign(level_2_monsters, terrain_locations.copy(), reserved_locations)
    level_3_allocations = assign(level_3_monsters, terrain_locations.copy(), reserved_locations)

    # Add terrain token image paths
    for terrain, locations in terrain_locations.items():
        for i, location in enumerate(locations):
            image_path = url_for('static', filename=f'tokens/terrainTokens/{location}.png')
            locations[i] = {"location": location, "image_path": image_path}

    return level_1_allocations, level_2_allocations, level_3_allocations, weakness_allocations


@app.route('/', methods=['GET', 'POST'])  # This decorator should handle both GET and POST


# Main function to start the game setup
def setup_game():
    if request.method == 'POST':
        # When the button is pressed, reload the page which will re-run the setup
        return redirect(url_for('setup_game'))
    
    # Monster names for each level
    level_1_monsters = ["Arachas", "Archespore", "Barghest", "Drowners Nest", 
                        "Ekimmara", "Foglet", "Ghouls Nest", "Harpy", 
                        "Nekkers Nest", "Rotfiend"]
    level_2_monsters = ["Noonwraith", "Fiend", "Werewolf", "Wyvern", "Griffin",
                        "Nightwraith", "Water Hag", "Whispess", "Weavess", 
                        "Penitent", "Grave hag", "Manticore"]
    level_3_monsters = ["Striga", "Brewess", "Bruxa", "Glustyworp", "Yghern", 
                        "Leshen", "Troll"]

    # Terrain types and their corresponding locations
    terrain_locations = {
        "Forest": [6, 7, 8, 10, 16, 17, 21],
        "Mountain": [2, 3, 9, 13, 18, 19],
        "Water": [1, 4, 5, 12, 14, 15, 20]
    }

    # Allocate monsters and weakness tokens
    # Call functions to assign locations and add image paths
    level_1_locs, level_2_locs, level_3_locs, weakness_locs = assign_monster_and_weakness_locations(
        level_1_monsters, level_2_monsters, level_3_monsters, terrain_locations)
     
    # Select player boards
    player_boards = ["Wolf", "Cat", "Bear", "Viper", "Griffin", "Manticore", "Swallow", "Alzur", "Philippa", "Gekhira", "Ardea", "Othar"]
    selected_boards = random.sample(player_boards, 2)

    # Select ship token locations
    ship_locations = [1, 5, 6, 9, 12, 13]
    selected_ship_locations = random.sample(ship_locations, 3)

    # Add image paths for selected player boards
    player_board_images = {board: get_board_image_path(board) for board in selected_boards}
   
    # Add image paths to monster allocations
    add_image_paths(level_1_locs, 1)
    add_image_paths(level_2_locs, 2)
    add_image_paths(level_3_locs, 3)

    # Add image paths for weakness token locations
    weakness_location_images = {terrain: get_location_image_path(location) for terrain, location in weakness_locs.items()}

    def add_terrain_token_image_paths(terrain_locations):
        for terrain, locations in terrain_locations.items():
            for i, location in enumerate(locations):
            # Ensure the correct path is constructed here
                image_path = url_for('static', filename=f'tokens/terrainTokens/{location}.png')
                terrain_locations[terrain][i] = {"location": location, "image_path": image_path}
    # Add image paths for locations
    ship_location_images = {loc: get_location_image_path(loc) for loc in selected_ship_locations}

    results = {
        # ... [existing results]
        "ship_location_images": ship_location_images
    }

    # Call the function and get updated terrain locations
    updated_terrain_locations = add_terrain_token_image_paths(terrain_locations)


    # Store the results in a dictionary, including weakness_location_images
    results = {
        "level_1_monsters": level_1_locs,
        "level_2_monsters": level_2_locs,
        "level_3_monsters": level_3_locs,
        "weakness_tokens": weakness_locs,
        "weakness_location_images": weakness_location_images,  # Add this line
        "player_boards": selected_boards,
        "player_board_images": player_board_images,
        "ship_locations": selected_ship_locations,
        "ship_location_images": ship_location_images
    }


    # Render these results in an HTML template
    return render_template('game_setup.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
