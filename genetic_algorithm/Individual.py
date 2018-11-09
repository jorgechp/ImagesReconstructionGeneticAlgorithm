
class Individual(object):
    """
    An Individual consists in a DNA and a score.
    """
    def __init__(self, dna, score = 0 ):
        """
        Public constructro

        PARAMS
        -dna The DNA of the individual
        -score The score of the individual

        :return: numpy array DNA
        """
        self._dna = dna
        self._score = score

    def get_dna(self):
        """
        Get the DNA of the Individual instance

        :return: numpy array DNA
        """
        return self._dna

    def get_score(self):
        """
        Get the score of the Individual instance

        :return: int The score
        """
        return self._score

    def set_score(self, score_to_set):
        self._score = score_to_set

    def __gt__(self, other: object):
        if not isinstance(other, Individual):
            raise Exception("Individual are only comparable to Individual, not to {0}".format(type(other)))
        else:
            return self._score.__gt__(other._score)

    def __lt__(self, other: object):
        if not isinstance(other, Individual):
            raise Exception("Individual are only comparable to Individual, not to {0}".format(type(other)))
        else:
            return self._score.__lt__(other._score)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Individual):
            raise Exception("Individual are only comparable to Individual, not to {0}".format(type(other)))
        else:
            return self._score.__eq__(other._score)

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Individual):
            raise Exception("Individual are only comparable to Individual, not to {0}".format(type(other)))
        else:
            return self._score.__eq__(other._score)

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Individual):
            raise Exception("Individual are only comparable to Individual, not to {0}".format(type(other)))
        else:
            return self._score.__le__(other._score)

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Individual):
            raise Exception("Individual are only comparable to Individual, not to {0}".format(type(other)))
        else:
            return self._score.__ge__(other._score)

    def __repr__(self):
        return "<Individual({0})>".format(self._score)

