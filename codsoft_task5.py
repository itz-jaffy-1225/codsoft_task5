class ContactDetails:
    def __init__(self, full_name, phone, email, location):
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.location = location

class ContactManager:
    def __init__(self):
        self.contacts_list = []

    def add_new_contact(self, contact):
        self.contacts_list.append(contact)
        print("Contact successfully added!")

    def display_contact_list(self):
        if not self.contacts_list:
            print("The contact list is currently empty.")
        else:
            print("\n--- Contact List ---")
            for contact in self.contacts_list:
                print(f"Name: {contact.full_name}, Phone: {contact.phone}")

    def search_for_contact(self, keyword):
        matching_contacts = [contact for contact in self.contacts_list if keyword.lower() in contact.full_name.lower() or keyword in contact.phone]
        if matching_contacts:
            print("\n--- Matching Contacts ---")
            for contact in matching_contacts:
                print(f"Name: {contact.full_name}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_existing_contact(self, old_name, new_contact_info):
        for contact in self.contacts_list:
            if contact.full_name.lower() == old_name.lower():
                contact.full_name = new_contact_info.full_name
                contact.phone = new_contact_info.phone
                contact.email = new_contact_info.email
                contact.location = new_contact_info.location
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact_entry(self, name):
        for contact in self.contacts_list:
            if contact.full_name.lower() == name.lower():
                self.contacts_list.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def run_contact_management_system():
    contact_manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add a New Contact")
        print("2. Display the Contact List")
        print("3. Search for a Contact")
        print("4. Update an Existing Contact")
        print("5. Delete a Contact Entry")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            full_name = input("Enter the full name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            location = input("Enter the location: ")
            new_contact = ContactDetails(full_name, phone, email, location)
            contact_manager.add_new_contact(new_contact)

        elif choice == '2':
            contact_manager.display_contact_list()

        elif choice == '3':
            keyword = input("Enter the name or phone number to search for: ")
            contact_manager.search_for_contact(keyword)

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            full_name = input("Enter the new full name: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            location = input("Enter the new location: ")
            new_contact_info = ContactDetails(full_name, phone, email, location)
            contact_manager.update_existing_contact(old_name, new_contact_info)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact_entry(name)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    run_contact_management_system()
