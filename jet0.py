# JET version 1
# =============
# Based on pi3d/Shapes.py by Tim Skillman
#
# Need typically PYTHONPATH=$HOME/pi3d:$HOME/pi3d/include

import pi3d
import fly

# Setup display and initialise pi3d
display = pi3d.display()
display.create3D(100,100,1200,900)   	# x,y,width,height
display.setBackColour(1,1,0,1)    	# r,g,b,alpha

# Load textures
raspimg = pi3d.loadTextureAlpha("textures/Raspi256x256.png")   

##Create inbuilt shapes

#arialFont = pi3d.font("AR_CENA","#dd00aa")   #load AR_CENA font and set the font colour to 'raspberry'
#destineFont = pi3d.font("AR_Destine", "#0055ff")


# Fetch key presses
#mykeys = pi3d.key()

#create a light
mylight = pi3d.createLight(0,1,1,1,"",10,10,10)
mylight.on()

def Box(name, w,d,h, gx,gy,gz=0.0):
    return pi3d.createCuboid(w,d,h, name, gx+w*0.5, gz+h*0.5, -gy-d*0.5)

class JetWorld:
    def __init__(self):
        self.skytex = pi3d.loadTexture("textures/SkyBox.png")
        #self.greentex = pi3d.loadTexture("textures/green-grid.png")
        self.greentex = pi3d.loadTexture("textures/mountains3_256.jpg")
        self.walltex = pi3d.loadTexture('textures/grey-stripe.png')
        self.coffeetex = pi3d.loadTexture('textures/coffee.png')

        self.sky = pi3d.createEnvironmentCube(900.0,'CROSS')
        self.ground = pi3d.createCuboid(800,400,0.1,'ground',0,0,0)

        self.j1 = Box('J1', 10,4,2, -6, 15)
        self.j1l = Box('J1L', 2,2,1, -5, 16, 2)

        self.torus = pi3d.createTorus(2, 0.6, 12, 24, "Torus", -4,2,-17)
        self.rasp = pi3d.createTube(0.4, 0.1, 1.5, 24, "tube", 4,3,-15, 30,0,0)

    def draw(self):
        self.sky.draw(self.skytex, 0,0,0)
        self.ground.draw(self.greentex)
        self.j1.draw(self.walltex)
        self.j1l.draw(self.walltex)
        self.torus.draw(self.coffeetex)
        self.rasp.draw(raspimg)

    def update(self):
        self.torus.rotateIncX(0.2)
        self.torus.rotateIncY(3)
        self.torus.rotateIncZ(0.5)
        self.rasp.rotateIncY(3)
        self.rasp.rotateIncZ(2)

world = JetWorld()

viewer = fly.FlyThrough(0,-4,0)

# Display scene
try:
    while True:
        display.clear()
        viewer.set_view()
        world.draw()

    
#    pi3d.drawString(arialFont,"Raspberry Pi ROCKS!",-0.8,-0.7,-2.2, 10.0, 0.003,0.003)
    #pi3d.drawString(destineFont,"Some nice OpenGL bitmap fonts to play with",-1.3,-0.3,-2.2, 10.0, 0.002,0.002)
    
        viewer.update()
        world.update()

        display.swapBuffers()
finally:
    display.destroy()
    viewer.keys.close()
