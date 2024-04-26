class Donor:
    def __init__(self, name, age, height, weight, blood_group, hla_typing, nature_of_ailment , deceased , organs_available , location  ):
        self.name = nam
        self.age = age
        self.height = height  # in centimeters
        self.weight = weight  # in kilograms
        self.blood_group = blood_group
        self.hla_typing = hla_typing  # comma-separated string of HLA alleles
        self.nature_of_ailment = nature_of_ailment
        self.deceased = deceased
        self.organs_available = organs_available
        self.location = location
        

    def calculate_bmi(self):
        height_m = self.height / 100
        bmi = self.weight / (height_m ** 2)
        return bmi

    def get_hla_alleles(self):
        return [tuple(allele.split(':')) for allele in self.hla_typing.split(',')]
