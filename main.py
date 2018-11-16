import numpy as np

from genetic_algorithm.Image_Decomposer import Image_Decomposer
from genetic_algorithm.Image_manager import Image_manager
from genetic_algorithm.Image_type import Image_type
from genetic_algorithm.Genetic_algorithm import Genetic_algorithm

image_manager = Image_manager()


img = image_manager.load_image("test_image2.png")
number_of_colors = img.shape[2]
type_image = None
if number_of_colors == 1:
    type_image = Image_type.BLACK_WHITE
elif number_of_colors == 2:
    type_image = Image_type.GRAYSCALE
else:
    type_image = Image_type.RGB

img_decomposer = Image_Decomposer(img)
list_of_fragments = img_decomposer.decompose(85)

ga_algorithm = Genetic_algorithm(
    goal_score=350,
    max_number_of_children=15,
    population_limit=1500,
    crossover_chromosoma_probability=0.1,
    tournament_size=45,
    mutation_probability=0.10,
    mutation_chromosoma_probability=0.05,
    max_pixel_value=255,
    strongest_rate=0.23
)

for index,fragment in enumerate(list_of_fragments):
    fragment_numpy = np.array(fragment)
    ga_algorithm.reset()
    ga_algorithm.setGoal(fragment_numpy)
    best_fit, worst_fit = ga_algorithm.run_algorithm()
    img_decomposer.add_fragment_to_compose(index,best_fit.get_dna())

image_composed = img_decomposer.compose()
image_manager.save_image(image_composed,"test_image_transformed.png")





