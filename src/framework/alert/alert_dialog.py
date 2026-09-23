import console

class PYIAlert:

    @staticmethod
    def simple_alert(title: str, message: str, positive_button: str):
        return console.alert(title,message,positive_button)
    