print("Hi, im Seble Bedassa, this program takes the input of two coordinates of a linear function and outputs the slope.")
#An Example is, (4,2);(6,4)[inputs] 1 [output]

print("Enter the four values of the two coordinates of your linear function")
Coordinate_x1 = int(input())
Coordinate_y1 = int(input())
Coordinate_x2 = int(input())
Coordinate_y2 = int(input())

#This code uses rise/run formula to find the slope
Change_y = Coordinate_y2 - Coordinate_y1 
Change_x = Coordinate_x2 - Coordinate_x1
Slope = Change_y // Change_x

print(Slope)