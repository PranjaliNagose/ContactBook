from contact import Contact
class ContactBook:
    def __init__(self):
        self.contact = []
    def add_contact(self,contact):
        self.contact.append(contact)
    def display_all_contacts(self):
        for contact in self.contact:
            contact.display_contact()
            print("------------------")
    def search_contact(self,name):
        for contact in self.contact:
            if contact.name.lower() == name.lower():
                return contact
            return None
    def update_contact(self,name,new_name=None,new_phone=None,new_email=None):
        contact = self.search_contact(name)
        if contact:
            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
            print(f"Contact'{name}' has been updated.")
        else:
            print(f"Contact'{name}' not found.")

    def delete_contact(self,name):
        contact = self.search_contact(name)
        if contact:
            self.contact.remove(contact)
            print(f"Contact '{name}' has been deleted.")
        else:
            print(f"Contact '{name}' not found.")