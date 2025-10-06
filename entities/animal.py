class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @classmethod
    def get_list(cls):
        animals = [
            cls("Aguila", "blanca"),
            cls("Saltamontes", "amarillo"),
            cls("Cocodrilo", "verde"),
            cls("Leon", "naranja"),
            cls("Gorila", "gris"),
            cls("Tiburon", "azul"),
            cls("Loro", "rojo"),
            cls("Pez globo", "morado"),
            cls("Hipopotamo", "rosa"),
        ]
        return animals