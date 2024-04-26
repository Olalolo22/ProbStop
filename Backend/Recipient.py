class Recipient:
    def __init__(self, name, age, height, weight, blood_group, hla_typing, nature_of_ailment):
        self.name = name
        self.age = age
        self.height = height 
        self.weight = weight  
        self.blood_group = blood_group
        self.hla_typing = hla_typing 
        self.nature_of_ailment = nature_of_ailment  

    def calculate_bmi(self):
        height_m = self.height / 100
        bmi = self.weight / (height_m ** 2)
        return bmi

    def get_hla_alleles(self):
        return [tuple(allele.split(':')) for allele in self.hla_typing.split(',')]
