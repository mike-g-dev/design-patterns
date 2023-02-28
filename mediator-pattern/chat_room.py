class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def send_message(self, message: str) -> None:
        ChatRoom.show_message(self, message)


class ChatRoom:
    @staticmethod
    def show_message(user: User, message: str) -> None:
        print(f"[{user.name}]: {message}")
