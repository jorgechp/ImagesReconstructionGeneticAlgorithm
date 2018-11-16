import queue


import numpy as np

class Image_Decomposer(object):


    def __init__(self, image_to_decompose):
        self.__original_shape = image_to_decompose.shape
        self.__flatted_image = image_to_decompose.flatten()
        self.__flatted_transformed_image = np.zeros(len(self.__flatted_image))


    def decompose(self, size_fragments = 150):


        return queue.deque(list(self.__split(self.__flatted_image, size_fragments)))


    def __split(self,image, size_of_parts):
        self.__len_of_parts = size_of_parts
        size_of_list = len(image)
        num_of_parts = int(size_of_list / size_of_parts) + 1
        splitted_list = list()
        for i in range(num_of_parts):
            bottom_index = i * size_of_parts
            top_index = bottom_index + size_of_parts - 1
            top_index = min(top_index,size_of_list)

            part = image[bottom_index:top_index]
            splitted_list.append(part)
        return splitted_list


    def add_fragment_to_compose(self, index, fragment):
        try:
            bottom_index = index * self.__len_of_parts
            top_max_limit = len(self.__flatted_transformed_image)
            top_index = bottom_index + len(fragment)
            self.__flatted_transformed_image[bottom_index:top_index] = fragment
        except ValueError:
            print("hola")


    def compose(self):
        return self.__flatted_transformed_image.reshape(self.__original_shape)
