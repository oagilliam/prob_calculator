# Free Code Camp
#Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. 
#What is the probability that a random draw of 4 balls will contain at least 1 red 
#ball and 2 green balls? While it would be possible to calculate the probability 
#using advanced mathematics, an easier way is to write a program to perform a large 
#number of experiments to estimate an approximate probability.

#For this project, you will write a program to determine the approximate probability 
#of drawing certain balls randomly from a hat.
import random 

class Hat:
    def __init__(self,**balls):
        self.contents = []
        for key, value in balls.items():
            if value > 0:
                self.contents += ([key] * value)
        print(self.contents) #[yellow, yellow, yellow, blue, green, greem]

    def draw(self, num):
        balls_removed = []

        if self.num > len(self.contents):
            return self.contents
        for i in range(num):
            balls_selected = self.contents.pop(int(random() * len(self.contents)))
            balls_removed.append(balls_selected)
        return balls_removed


hat1 = Hat(yellow=5, blue=4, green=3)
