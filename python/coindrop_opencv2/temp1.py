import glob

path = "D:/_GIT/cointoss/python/coindrop_opencv2/capture/reflective-test-set/*.jpg"
for fname in glob.glob(path):
    print(fname)