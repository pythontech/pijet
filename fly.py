#=======================================================================
#       Fly-through controller
#=======================================================================
import pi3d
import math

DEGREE = math.pi / 180

class FlyThrough:
    def __init__(self, ox=0.0, oy=0.0, oz=0.0, speed=1.0):
        self.keys = pi3d.key()
        self.x = self.ox = ox
        self.y = self.oy = oy
        self.z = self.oz = oz
        self.speed = speed
        self.rot = 0
        self.tilt = 0

    def set_view(self):
        '''Set up camera transformation before drawing'''
        pi3d.identity()
        pi3d.rotate(self.tilt, 0, 0)
        pi3d.rotate(0, self.rot, 0)
        pi3d.position(self.x, self.y, self.z)

    def update(self):
        '''Check for any key press controls'''
        k = self.keys.read()
        if k < 0:
            return
        if k==119:              # W - forward
            self.x -= self.speed * math.sin(self.rot * DEGREE)
            self.z += self.speed * math.cos(self.rot * DEGREE)
        elif k==115:            # S - backward
            self.x += self.speed * math.sin(self.rot * DEGREE)
            self.z -= self.speed * math.cos(self.rot * DEGREE)
        elif k==39:             # ' - look up
            self.tilt -= 2.0
        elif k==47:             # / - look down
            self.tilt += 2.0
        elif k==97:             # A - turn left
            self.rot -= 2.0
        elif k==100:            # D - turn right
            self.rot += 2.0
        elif k==112:            # P - screenshot
            pass
        elif k==111:            # O - return to origin
            self.x, self.y, self.z = self.ox, self.oy, self.oz
            self.rot = 0.0
            self.tilt = 0.0
        elif k in (27,113):     # ESC, Q - quit
            raise KeyboardInterrupt

            
