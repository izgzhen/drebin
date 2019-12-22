import glob
import sys
import os
from msbase.utils import load_json

source_root_dir = sys.argv[1]
dirname = sys.argv[2]
drebin_outputs_dir = sys.argv[3]

metadata = None
if len(sys.argv) > 4:
    metadata = load_json(sys.argv[4])

assert dirname in ["maldir", "gooddir"]

os.makedirs(dirname, exist_ok=True)

existing_drebin_outputs = [os.path.basename(f).replace(".data", ".apk") for f in glob.glob(drebin_outputs_dir + "/*.data") ]

if metadata is not None:
    apks = [ source_root_dir + "/" + sample["apk"] for sample in metadata ]
else:
    apks = glob.glob(source_root_dir + "/*.apk")

for apk in apks:
    apk_name = os.path.basename(apk)
    if apk_name in existing_drebin_outputs:
        print("Skip existing " + apk_name)
        continue
    os.symlink(apk, dirname + "/" + apk_name)
