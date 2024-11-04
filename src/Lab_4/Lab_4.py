class Perfume:
    def __init__(self, volume=0, price=0.0, manufacturer="",
                 public_numeric=0, public_string=""):
        self.__volume = volume
        self.__price = price
        self.__manufacturer = manufacturer
        self.public_numeric = public_numeric
        self.public_string = public_string

    def get_volume(self): 
        return self.__volume

    def set_volume(self, volume): 
        self.__volume = volume

    def get_price(self): 
        return self.__price

    def set_price(self, price): 
        self.__price = price

    def get_manufacturer(self): 
        return self.__manufacturer

    def set_manufacturer(self, manufacturer): 
        self.__manufacturer = manufacturer

    def __str__(self):
        return f"{self.__manufacturer}: {self.__volume}ml, {self.__price} UAH"

    def __repr__(self):
    return (
        f"Perfume({self.__volume}, {self.__price}, '{self.__manufacturer}', "
        f"{self.public_numeric}, '{self.public_string}')"
    )
    def __del__(self):
        print(f"Deleting Perfume: {self.__manufacturer}")

def main():
    perfumes = [
        Perfume(50, 500, "Chanel", 1, "Classic"),
        Perfume(100, 700, "Dior", 2, "Luxury"),
        Perfume(30, 300, "Gucci", 3, "Trendy")
    ]

    for perfume in perfumes:
        print(perfume)

if __name__ == "__main__":
    main()
