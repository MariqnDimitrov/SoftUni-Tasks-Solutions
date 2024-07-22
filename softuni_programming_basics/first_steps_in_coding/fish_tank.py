length=int(input())
width=int(input())
height=int(input())
percentage=float(input())/100
volume_liters=(length*width*height)/1000
needed_liters=volume_liters*(1-percentage)
print(needed_liters)