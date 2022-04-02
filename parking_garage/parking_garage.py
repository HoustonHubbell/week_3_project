class Parking_Garage():

    def __init__(self):
        self.tickets = [10,9,8,7,6,5,4,3,2,1]
        self.spaces_available = 10
        self.current_tickets = {}

    def take_ticket(self):
        if self.spaces_available <= 0:
            print("This lot is full.")
        else:
            new_ticket = self.tickets.pop()
            self.current_tickets[new_ticket] = "unpaid"
            self.spaces_available -= 1
            print("Your ticket number is: " + str(new_ticket))

    def pay(self):
        if self.spaces_available < 10:
            ticket_number = int(input("What is your ticket number? "))
            while ticket_number < 0 or ticket_number > 10:
                print("That is not a valid ticket number. Try again:")
                ticket_number = int(input("What is your ticket number?"))
            if self.current_tickets[ticket_number] == "unpaid":
                pay_ticket = input("You need to pay $3. Pay now? y/n ")
                if pay_ticket.lower() == 'y':
                    self.current_tickets[ticket_number] = "paid"
                else:
                    print("You need to pay for your parking.")
            else:
                print("You have already paid")
            print("Receipt: ")
            print(self.current_tickets)
            print("You have 15 minutes to leave. Thanks for your payment.")
        else:
            print("You cannot pay for a ticket that has not been taken.")

        
    def leave_garage(self):
        if self.spaces_available < 10:
            ticket_number = int(input("What is your ticket number? "))
            while ticket_number < 0 or ticket_number > 10:
                print("That is not a valid ticket number. Try again:")
                ticket_number = int(input("What is your ticket number?"))
            if self.current_tickets[ticket_number] == "unpaid":
                pay_ticket = input("You need to pay $3. Pay now? y/n ")
                if pay_ticket.lower() == 'y':
                    self.current_tickets[ticket_number] = "paid"
                    self.spaces_available += 1
                    self.tickets.append(ticket_number)
                    del self.current_tickets[ticket_number]
                    print("Thank you; have a nice day!")
                else:
                    print("You need to pay for your parking.")
            
            else:
                self.spaces_available += 1
                self.tickets.append(ticket_number)
                del self.current_tickets[ticket_number]
                print("Thank you; come again.")
            print(self.current_tickets)
        else:
            print("You cannot leave an empty garage!")

car = Parking_Garage()

def run():
    while True:
        response = input("What would you like to do? Options: park, pay, leave, quit  ")
        if response.lower() == "park":
            car.take_ticket()
        elif response.lower() == "pay":
            car.pay()
        elif response.lower() == "leave":
            car.leave_garage()
        elif response.lower() == "quit":
            break
        else:
            "This is not a valid response."
run()
