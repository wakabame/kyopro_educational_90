from math import sin, cos, pi, atan2

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

def theta_to_place(theta):
   rad = L/2
   center = (0, L/2)

   return (0, center[0] - rad * cos(theta), center[1] + rad * sin(theta))


def horizontal_length(pt1, pt2):
    x_diff = pt1[0] - pt2[0]
    y_diff = pt1[1] - pt2[1]
    return (x_diff ** 2 + y_diff ** 2)**0.5

for _ in range(Q):
    E = int(input())
    theta = E * 2*pi/T - pi/2
    h = horizontal_length((X,Y,0), theta_to_place(theta))
    z = theta_to_place(theta)[2]
    print(atan2(z, h) * 360 / 2/ pi)
