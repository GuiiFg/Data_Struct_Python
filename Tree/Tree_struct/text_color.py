from turtle import color


class PaintText():
    
    color = {
        "red" : '\033[1;31m',
        "white" : '\033[0;37m'
    }

    def ChangeTextConsoleColor(toColor : str, color = color):

        print(color[f"{toColor}"])
