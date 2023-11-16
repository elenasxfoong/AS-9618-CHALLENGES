import turtle

class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()

def read_txtfile():
    count = 0
    try: 
        with open (r"/Users/Elena/Downloads/patterns.txt") as f:
            for line in f:
                count += 1
                if count % 2 != 0: #odd numbers 
                    clean = line.strip("\n")
                    angle_list.append(clean)
                else:
                    clean  = line.strip("\n")
                    times_list.append(clean)

            print (angle_list)
            print(times_list)

    except OSError:
        print ("Sorry could not find file")

def selection():
    x = int(input("Pick a nunber from 0-4: "))
    return x 


angle_list = []
times_list = []

read_txtfile()
x = selection()

mypattern = pattern(int(angle_list[x]), int(times_list[x]))  
mypattern.draw_pattern()
