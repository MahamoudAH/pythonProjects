auction = {}

game = "yes"

while game != "no":
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    auction[name] = bid
    game = input("Are there any other bidders? Type 'yes or 'no': ")
