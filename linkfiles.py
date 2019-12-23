import glob
import sys
import os
from msbase.utils import load_json

source_root_dir = sys.argv[1]
drebin_outputs_dir = sys.argv[2]

# Drebin will fail on those
blacklist = set(open("blacklist.txt", "r").read().strip().split("\n"))

metadata = None
if len(sys.argv) > 3:
    if sys.argv[3].endswith("*.json"):
        metadata = load_json(sys.argv[3])
    elif os.path.isdir(sys.argv[3]):
        metadata = [ s for m in glob.glob(sys.argv[3] + "/**/*.json", recursive=True) for s in load_json(m) ]

for dirname in ["maldir", "gooddir"]:
    os.makedirs(dirname, exist_ok=True)

existing_drebin_outputs = [os.path.basename(f).replace(".data", ".apk") for f in glob.glob(drebin_outputs_dir + "/*.data") ]

if metadata is not None:
    benign_apks = [ source_root_dir + "/" + sample["apk"] for sample in metadata if sample["label"] == "benign" ]
    mal_apks = [ source_root_dir + "/" + sample["apk"] for sample in metadata if sample["label"] != "benign" ]
else:
    benign_apks = []
    mal_apks = glob.glob(source_root_dir + "/*.apk")

for dirname, apks in [("maldir", mal_apks), ("gooddir", benign_apks)]:
    for apk in apks:
        apk_name = os.path.basename(apk)
        if apk_name in existing_drebin_outputs:
            print("Skip existing " + apk_name)
            continue
        dest = dirname + "/" + apk_name
        if dest not in blacklist:
            os.symlink(os.path.realpath(apk), dest)
