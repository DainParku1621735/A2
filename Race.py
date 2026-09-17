# Assignment 2 - A horse race
# Name: Dain Park
# uID: u1621735

import graphics
import Dice

class Horse:
    def __init__(self, speed, y, image, window):
        self.x_pos=0
        self.y_pos=y
        self.image=image
        self.dice=Dice.Dice(speed)
        self.window=window

    def move(self):
        self.x_pos +=self.dice.roll()

    def draw(self):
        self.image.draw_at_pos(self.window, self.x_pos, self.y_pos)

    def crossed_finish_line(self, x):
        return self.x_pos >= x

def main():
    window = graphics.GraphWin("Horse Race", 700, 350)
    finish_x=650

    image1 = graphics.Image(graphics.Point(50,75), "Knight.gif")
    image2 = graphics.Image(graphics.Point(50, 175), "Wizard.gif")
    image3 = graphics.Image(graphics.Point(50,275), "fomfom.gif")

    horse1 = Horse(10, 75, image1, window)
    horse2 = Horse(12, 175, image2, window)
    horse3 = Horse(14, 275, image3, window)

    finish_line = graphics.Line(
        graphics.Point(finish_x,0),
        graphics.Point(finish_x, 350)
    )

    horse1.draw()
    horse2.draw()
    horse3.draw()
    finish_line.draw(window)
    window.getMouse()

    while not (horse1.crossed_finish_line(finish_x) or horse2.crossed_finish_line(finish_x) or horse3.crossed_finish_line(finish_x)):
        horse1.move()
        horse2.move()
        horse3.move()
        window.clear_win()
        horse1.draw()
        horse2.draw()
        horse3.draw()
        finish_line.draw(window)
        window.update()

    horse1_finished = horse1.crossed_finish_line(finish_x)
    horse2_finished = horse2.crossed_finish_line(finish_x)
    horse3_finished = horse3.crossed_finish_line(finish_x)

    if horse1_finished and horse2_finished:
        print("Tie Horse 1 with Horse 2")
    elif horse1_finished and horse3_finished:
        print("Tie Horse 1 with Horse 3")
    elif horse2_finished and horse3_finished:
        print("Tie Horse 2 with Horse 3")
    elif horse1_finished:
        print("Horse 1 is the winner")
    elif horse2_finished:
        print("Horse 2 is the winner")
    else:
        print("Horse 3 is the winner")

    window.getMouse()
    window.close()

if __name__ =="__main__":
    main()


