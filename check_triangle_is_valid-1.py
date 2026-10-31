# A python program Checks whether a triangle is valid when its three angles
angle1= float(input("enter first angle"))
angle2= float(input("enter second angle"))
angle3= float(input("enter third angle"))
if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 +angle3 == 180):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")