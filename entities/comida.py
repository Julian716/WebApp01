class Comida:
    def __init__(self, platillo, precio):
        self.platillo = platillo
        self.precio = precio

    @classmethod
    def get_list(cls):
        platillos = [
            cls("Tacos", "20"),
            cls("Chilaquiles", "50"),
            cls("Quesadillas", "25"),
            cls("Enchiladas", "45"),
            cls("Gorditas", "45"),
            cls("Tacos dorados", "30"),
            cls("Tortas", "35"),
            cls("Tamales", "40"),
            cls("Pizza", "100"),
        ]
        return platillos