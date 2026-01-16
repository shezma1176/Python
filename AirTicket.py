class AirTicket:
    def __init__(self):
        self.bookings = []
        self.routes = {
            ("Dhaka", "Chittagong"): 4500,
            ("Dhaka", "Sylhet"): 5000,
            ("Dhaka", "Coxbazar"): 8000,
            ("Chittagong", "Sylhet"): 5500
        }
    def get_cost(self, src, dest):
        if(src, dest) in self.routes:
            return self.routes[(src, dest)]
        elif(dest, src) in self.routes:
            return self.routes[(dest, src)]
        else:
            return None
    def book_ticket(self):
        Name = input("Passenger Name: ")
        src = input("From: ")
        dest = input("To: ")
        cost = self.get_cost(src, dest)

        if cost is None:
            print("❌ Route Not Availabe\n")
            return
        
        ticket = {
            "name": Name,
            "From": src,
            "To": dest,
            "Cost": cost
        }

        self.bookings.append(ticket)
        print(f"✅ Ticket Booked 🎫 Cost: {cost} BDT\n")

    def view_tickets(self):
        if not self.bookings:
            print("❌No Bookings Found\n")
            return
        
        for i, t in enumerate(self.bookings, 1):
            print(f"{i}. {t['name']} | {t['From']} ➡️ {t['To']} | Cost: {t['Cost']} BDT")
            print()

    def compare_cost(self):
        src = input("From: ")
        dest = input("To: ")

        cost = self.get_cost(src, dest)
        if cost:
            print(f"💰Ticket cost from {src} to {dest}: {cost} BDT\n")
        else:
            print("❌Route Not Availabe\n")

    def menu(self):
        while True:
            print("✈️ Air Ticket Booking System")
            print("1. Book Ticket")
            print("2. View Tickets")
            print("3. Compare Ticket Cost")
            print("4. Exit")
            Choice = input("Choose one: ")
            
            if Choice == "1":
                self.book_ticket()
            elif Choice == "2":
                self.view_tickets()
            elif Choice == "3":
                self.compare_cost()
            elif Choice == "4":
                print("Thank you. Bye 👋")
                break
            else:
                print("Invalid Choice\n")

system = AirTicket()
system.menu()