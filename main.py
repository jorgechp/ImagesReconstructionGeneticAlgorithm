from genetic_algorithm.Image_manager import Image_manager
from genetic_algorithm.Image_type import Image_type
from genetic_algorithm.Genetic_algorithm import Genetic_algorithm

image_manager = Image_manager()

img = image_manager.load_image("test_image.png")
number_of_colors = img.shape[2]
type_image = None
if number_of_colors == 1:
    type_image = Image_type.BLACK_WHITE
elif number_of_colors == 2:
    type_image = Image_type.GRAYSCALE
else:
    type_image = Image_type.RGB

ga_algorithm = Genetic_algorithm(
    goal = 1000,
    goal_score = 1000,
    max_number_of_children = 10,
    population_limit = 400,
    crossover_chromosoma_probability = 0.6,
    tournament_size= 40,
    mutation_probability = 0.15,
    mutation_chromosoma_probability = 0.10,
    max_pixel_value = 255,
    strongest_rate=0.2
)

ga_algorithm.run_algorithm()