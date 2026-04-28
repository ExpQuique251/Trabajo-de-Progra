class GymManagement:
    def __init__(self):
        self.clients = []  # List to store client information
        self.routines = []  # List to store training routines

    def register_client(self):
        name = input("Enter client name: ")
        age = int(input("Enter client age: "))
        self.clients.append({'name': name, 'age': age, 'routines': [], 'ratings': []})
        print(f"Client {name} registered successfully.")

    def register_routine(self):
        routine_name = input("Enter routine name: ")
        description = input("Enter routine description: ")
        self.routines.append({'name': routine_name, 'description': description, 'ratings': []})
        print(f"Routine {routine_name} registered successfully.")

    def assign_routine_to_client(self):
        client_name = input("Enter client name: ")
        routine_name = input("Enter routine name: ")
        rating = int(input("Enter routine rating (1-5): "))
        for client in self.clients:
            if client['name'] == client_name:
                client['routines'].append(routine_name)
                client['ratings'].append(rating)
                print(f"Routine {routine_name} assigned to {client_name} with rating {rating}.")
                return
        print("Client not found.")

    def generate_reports(self):
        print("Client Reports:")
        for client in self.clients:
            average_rating = sum(client['ratings']) / len(client['ratings']) if client['ratings'] else 0
            print(f"Client: {client['name']}, Average Rating: {average_rating:.2f}, Routines: {client['routines']}")

        print("Routine Reports:")
        for routine in self.routines:
            routine_ratings = [clients['ratings'][index] for client in self.clients for index in range(len(client['routines'])) if client['routines'][index] == routine['name']]
            average_routine_rating = sum(routine_ratings) / len(routine_ratings) if routine_ratings else 0
            print(f"Routine: {routine['name']}, Average Rating: {average_routine_rating:.2f}")

    def interactive_menu(self):
        while True:
            print("\n--- Gym Management System ---")
            print("1. Register Client")
            print("2. Register Routine")
            print("3. Assign Routine to Client")
            print("4. Generate Reports")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.register_client()
            elif choice == '2':
                self.register_routine()
            elif choice == '3':
                self.assign_routine_to_client()
            elif choice == '4':
                self.generate_reports()
            elif choice == '5':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice, please choose again.")

# Create an instance of GymManagement and run the menu
if __name__ == '__main__':
    gym_management = GymManagement()
    gym_management.interactive_menu()