from utils import parity ,crc ,checksum


if __name__ == "__main__":

    while True:
        print("Enter the message you want to send")
        message = input("> ")

        print("Select the strategy")
        print("1. Parity.")
        print("2. Cyclic Redundancy Check.")
        print("3. Checksum.")
        print("4. Exit")

        try:
            choice = int(input("> "))
        except ValueError:
            print("Invalid Input.. retry")
            continue

        match choice:
            case 1:
                method = "parity"
            case 2:
                method = "crc"
            case 3:
                method = "checksum"
            case 4:
                print("Exiting..")
                break
            case _:
                print("Invalid choice..")
                continue
        
        print("-" * 50)
    