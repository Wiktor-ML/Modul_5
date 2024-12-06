class BaseContact:
    def __init__(self, first_name, last_name, phone_privat, email_privat):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_privat = phone_privat
        self.email_privat = email_privat
    
    def contact(self):
        return f"Wybieram numer {self.phone_privat} i dzwonię do {self.first_name} {self.last_name}"
    
    @property
    def label_length(self):
        return (len(self.first_name) + len(self.last_name))
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_privat} {self.email_privat}"
    
class BusinessContact(BaseContact):
    def __init__(self, job_title, company, phone_work, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job_title = job_title
        self.phone_work = phone_work
        
    def contact(self):
        return f"Wybieram numer {self.phone_work} i dzwonię do {self.first_name} {self.last_name}"
       
    @property
    def label_length(self):
        return (len(self.first_name) + len(self.last_name))
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_work} {self.job_title} {self.company}"
    
from faker import Faker
fake = Faker("pl_PL")

def create_contacts(number_of_cards,card_type):
    contacts = []
    for _ in range(number_of_cards):
        if card_type == "base":
            contacts.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_privat=fake.phone_number(), email_privat=fake.email()))
        elif card_type == "business":
            contacts.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_privat=fake.phone_number(), email_privat=fake.email(), job_title=fake.job(), company=fake.company(), phone_work=fake.phone_number()))
    return contacts


for card in create_contacts(5,"base"):
    print(card)
    print(card.contact())
    print(f"Dlugosc imienia i nazwiska: {card.label_length}")
    print("-"*20)

