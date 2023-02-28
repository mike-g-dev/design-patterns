from chat_room import User

def client():
    mike = User("Mike")
    andrew = User("Andrew")

    mike.send_message("Hi...")
    andrew.send_message("Hello...")


if __name__ == "__main__":
    client()
