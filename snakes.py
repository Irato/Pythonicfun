class Snakes:
    def __init__(self) -> None:
        print("psssss")

#Subclass of snakes that is lurking around kkkk
class Python(Snakes):
    def __init__(self) -> None:
        Snakes.__init__(self)

yellow_snake = Python()
