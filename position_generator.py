import random

def generate_initial_positions(custom_map, num_students, num_shooters, num_police, seed=42):
    # Set the seed for reproducibility
    random.seed(seed)
    
    width, height = len(custom_map[0]), len(custom_map)
    student_positions = []
    shooter_positions = []
    police_positions = []

    # Get valid tiles for students
    valid_student_tiles = [(x, y) for x in range(width) for y in range(height) if custom_map[y][x] == 3]
    student_positions = random.sample(valid_student_tiles, num_students)

    # Get valid tiles for shooters
    valid_shooter_tiles = [(x, y) for x in range(width) for y in range(height) if custom_map[y][x] == 7]
    shooter_positions = random.sample(valid_shooter_tiles, num_shooters)
    
    # Get valid tiles for shooters
    valid_police_tiles = [(x, y) for x in range(width) for y in range(height) if custom_map[y][x] == 5]
    police_positions = random.sample(valid_police_tiles, num_police)

    return {'students': student_positions, 'shooter': shooter_positions, 'police': police_positions}
