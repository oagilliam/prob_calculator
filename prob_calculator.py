# Free Code Camp
#Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. 
#What is the probability that a random draw of 4 balls will contain at least 1 red 
#ball and 2 green balls? While it would be possible to calculate the probability 
#using advanced mathematics, an easier way is to write a program to perform a large 
#number of experiments to estimate an approximate probability.

#For this project, you will write a program to determine the approximate probability 
#of drawing certain balls randomly from a hat.

class Hat:
    def __init__(self, **contents):
        ball_list = []
        for key, value in contents.items():
            if value > 0:
                ball_list += ([key] * value)
        print(ball_list)

hat1 = Hat(yellow=5, blue=4, green=3)
