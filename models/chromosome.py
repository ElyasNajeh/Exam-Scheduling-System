class Chromosome:

    def __init__(self, genes=None):

        if genes is None:
            genes = []

        self.genes = genes
        self.fitness = 0
