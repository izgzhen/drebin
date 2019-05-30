import glob
import os

home = os.getenv("HOME")

for DIR in glob.glob(home + "/projects/seguard-research/samples/misc/*"):
    if "good" in DIR:
        dest = 'gooddir'
    else:
        dest = 'maldir'
    for f in glob.glob(DIR + "/*.apk"):
        os.symlink(f, dest + "/" + os.path.basename(f))

for DIR in glob.glob(home + '/projects/seguard-research/samples/gapps/*'):
    if "benign" in DIR:
        dest = 'gooddir'
    else:
        dest = 'maldir'
    for f in glob.glob(DIR + "/*.apk"):
        os.symlink(f, dest + "/" + os.path.basename(f))
