from SimpleCV import *
from sklearn import cluster
winsize = (640,480)
features = []
display = Display(winsize)
video = VirtualCamera('stefan_eye.mp4', 'video')
while display.isNotDone():
    image = video.getImage().rotate(90).crop(600,20,600,600)
    xmid = image.width/2
    ymid = image.height/2
    image2 = image.colorDistance(Color.RED)
    blobs = image.findBlobs()
    if blobs:
        for b in blobs:
            image3 = image.crop(b.x,b.y,100,100)
            blobs2 = image3.binarize(140).findBlobs()
            if blobs2:
                for c in blobs2:
                    if c.isCircle(0.7):
                        image.dl().circle((b.x + c.x,b.y + c.y),c.width(),Color.YELLOW)
                        features.append([b.x + c.x,b.y + c.y])
    if(features.__len__() > 200):
        Kmeans = cluster.KMeans(n_clusters=2)
        preds = Kmeans.fit_predict(features)
        axAvg=0
        bxAvg = 0
        ayAvg=0
        byAvg= 0
        asize=0
        bsize = 0
        for i,q in enumerate(preds):
            if q == 0:
                axAvg += features[i][0]
                ayAvg += features[i][1]
                asize +=1
            else:
                bxAvg += features[i][0]
                byAvg += features[i][1]
                bsize +=1

        axAvg /= asize
        ayAvg /= asize
        bxAvg /= bsize
        byAvg /= bsize
        adiff = 0
        bdiff = 0
        if axAvg > xmid:
            adiff += axAvg-xmid
        else:
            adiff += xmid-axAvg
        if ayAvg > ymid:
            adiff += ayAvg-ymid
        else:
            adiff += ymid-ayAvg
        if bxAvg > xmid:
            bdiff += bxAvg-xmid
        else:
            bdiff += xmid-bxAvg
        if byAvg > ymid:
            bdiff += byAvg-ymid
        else:
            bdiff += ymid-byAvg
        if adiff < bdiff:
            print axAvg - xmid -174
            print ayAvg - ymid +63
        else:
            print bxAvg - xmid -174
            print byAvg - ymid +63