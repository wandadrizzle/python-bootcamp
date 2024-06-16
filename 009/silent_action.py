import extra_deets as s, os

print(s.gavel)
print("Welcome to the secret auction program.")

def auction():
    log = {}
    while True:
        name = input("What is your name? ")
        bid = int(input("What's your bid? R"))
        log.update({name:bid})
        #print(log)
        guest = input("Are there other bidders? Type 'yes' or 'no'.\n").lower()
        if guest == "no":
            os.system('cls')
            bid = max(log.values())

            for k, v in log.items():
                if v == bid:
                    name = k
            print(f"The winner was {name} with a bid of R{bid}.")
            break
        elif guest == "yes":
            os.system('cls')
            continue
        else:
            print("You have entered an invalid input. The action has ended.")
            exit()
            
auction()