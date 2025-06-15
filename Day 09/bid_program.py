bid_details = {}

bidding_continue = True

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}.")

while bidding_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bid_details[name] = bid
    next_bid = input("Are there any other bidders? Yes or no").lower()
    if next_bid == "no":
        bidding_continue = False
        find_highest_bidder(bid_details)
    elif bidding_continue == "yes":
        print("\n" * 20)




