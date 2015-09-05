from SimpleCV import *
winsize = (640,480)
display = Display(winsize)

video = VirtualCamera('stefan_eye.mp4', 'video')
while display.isNotDone():
    a = video.getImage()
    a.rotate(90).invert().toGray().binarize().save(display)

