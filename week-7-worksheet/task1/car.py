class Car:
    def __init__(model, year):
        self.model = model
        self.year = year

    def __str__(self):
        return f"Model {self.model} from year {self.year}"

