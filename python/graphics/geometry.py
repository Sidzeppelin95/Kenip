import math
def polar(cx,cy,r,a):
 t=math.radians(a);return cx+r*math.cos(t),cy+r*math.sin(t)
def points_on_circle(cx,cy,r,count,start=-90):return [polar(cx,cy,r,start+360*i/count) for i in range(count)] if count>0 else []