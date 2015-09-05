from SimpleCV import *
winsize = (640,480)
display = Display(winsize)
video = VirtualCamera('stefan_eye.mp4', 'video')
while display.isNotDone():
    image = video.getImage().rotate(90).crop(850,50,400,400)
    image2 = image.colorDistance(Color.RED)
    blobs = image2.findBlobs()
    image3 = image2.grayscale()
    if blobs:
        for b in blobs:
            if b.isCircle(0.7) and b.radius() > 3:
                image.drawCircle((b.x,b.y),b.radius(),Color.YELLOW,2)
    image.show()
