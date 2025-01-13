from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = randint(10000,60000)


    def book(self, fro ,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(200, 2000)}")


t = train(randint) 
t.book("Rampur", "Delhi")
t.getstatus()
t.getFare("Rampur", "Delhi")