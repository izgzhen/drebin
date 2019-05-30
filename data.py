import glob
import os

for apk in glob.glob("/data/datasets/gapps/*/*.apk")[:14]:
    if "benign" in apk: continue
    os.system("cp %s maldir" % apk)

for apk in glob.glob("/data/datasets/gapps/*/*.apk")[14:20]:
    if "benign" in apk: continue
    os.system("cp %s testmaldir" % apk)


for apk in glob.glob("/data/datasets/gooddroid/*.apk")[:14]:
    os.system("cp %s gooddir" % apk)

for apk in glob.glob("/data/datasets/gooddroid/*.apk")[14:20]:
    os.system("cp %s testgooddir" % apk)


