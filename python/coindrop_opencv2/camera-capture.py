import time
import picamera

print "sleeping for 20mins"
time.sleep(1200)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    time.sleep(1)
    for i, filename in enumerate(filenames):
        print('Captured image %s' % filename)
        if i == 50:
            break
        time.sleep(5)
    camera.stop_preview()

#count=0
for idx, item in enumerate(list):
    print item
    #count +=1
    #if count % 10 == 0:
    if (idx+1) % 10 == 0:
        print 'did ten'