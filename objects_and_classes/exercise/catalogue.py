class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, letter: str):
        self.products = [p for p in self.products if p.startswith(letter)]
        return self.products

    def __repr__(self):
        self.products = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{self.products}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
