import console

class PYIAlert:

    @staticmethod
    def simple_alert(title: str, message: str, positive_button: str="Ok", negative_button: str="Cancel"):
        return console.alert(title,message,positive_button,negative_button)
    