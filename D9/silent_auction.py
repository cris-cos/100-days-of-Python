from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids = {}
winner = ""
max_bid = 0

def register_new_bid():
    key = input("Please input your name: ")
    bid_value = int(input("what is your bid? "))
    bids[key] = bid_value
    flow_control()

def compare_bids(bids, winner, max_bid):
    for bidder in bids:
        if bids[bidder] > max_bid:
            max_bid = bids[bidder]
            winner = bidder
    print(f"The winner is {winner}, with a bid of {max_bid}")
    print(f"Here is a list of all the bids: {bids}")

def flow_control():
    flow = input("Are there any other bids? Type yes or no:")
    if flow == "yes":
        clear()
        register_new_bid()
    elif flow == "no":
        clear()
        compare_bids(bids, winner, max_bid)
    else:
        print("That was not a valid option, try again:\n")
        flow_control()

print(logo)
register_new_bid()