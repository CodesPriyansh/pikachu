def cuboid_volume(length, width, height):
    volume = length * width * height
    return volume 

l = int(input("enter the length: "))
w = int(input("enter the width: "))
h = int(input("enter the height: ")) 

v = cuboid_volume(l, w, h)
print("the volume of cuboid is", v) 
