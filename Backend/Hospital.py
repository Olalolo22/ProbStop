import datetime

class Hospital:
    def __init__(self, name, address, head_of_clinical_services, licenses):
        self.name = name
        self.address = address
        self.head_of_clinical_services = head_of_clinical_services
        self.licenses = licenses
        self.establishment_date = datetime.date.today()
        self.email_domain = f"@{self.name.lower().replace(' ', '')}.org"

    @property
    def head_of_clinical_services_email(self):
        return f"{self.head_of_clinical_services.name.lower().replace(' ', '.')}{self.email_domain}"

    def __str__(self):
        return f"{self.name}\n{self.address}\nEstablished: {self.establishment_date}\nHead of Clinical Services: {self.head_of_clinical_services}\nLicenses: {', '.join(self.licenses)}"


class Person:
    def __init__(self, name, title, email=None):
        self.name = name
        self.title = title
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.title}"



head_of_clinical_services = Person("Dr. Jane Smith", "Chief Medical Officer")
licenses = ["State Medical License", "Medicare Certification", "Joint Commission Accreditation"]
hospital = Hospital("ABC Medical Center", "123 Main St, Anytown, USA", head_of_clinical_services, licenses)

print(hospital)
print(f"Head of Clinical Services Email: {hospital.head_of_clinical_services_email}")
