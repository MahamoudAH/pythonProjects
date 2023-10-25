auction = {}

game = "yes"

while game != "no":
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    auction[name] = bid
    game = input("Are there any other bidders? Type 'yes or 'no': ")

winner_bid = 0
winner_name = ""
for key, value in auction.items():
    if value > winner_bid:
        winner_bid = value
        winner_name = key

print(f"The winner is {winner_name} a bid of ${winner_bid}")
