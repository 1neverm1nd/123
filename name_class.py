
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."

# Usage example
a1 = Name('john', 'SMITH')
print(a1.first_name)  # 'John'
print(a1.last_name)   # 'Smith'
print(a1.full_name)   # 'John Smith'
print(a1.initials)    # 'J.S.'
