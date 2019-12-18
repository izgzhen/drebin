import glob
import sys
import os
from msbase.utils import load_json

metadata = load_json(sys.argv[1])
dirname = sys.argv[2]
metadata_root_dir = sys.argv[3]
drebin_outputs_dir = sys.argv[4]

assert dirname in ["maldir", "gooddir"]

os.makedirs(dirname, exist_ok=True)

existing_drebin_outputs = [os.path.basename(f).replace(".data", ".apk") for f in glob.glob(drebin_outputs_dir + "/*.data") ]

for sample in metadata:
    apk_name = os.path.basename(sample['apk'])
    if apk_name in existing_drebin_outputs:
        print("Skip existing " + apk_name)
        continue
    os.symlink(metadata_root_dir + "/" + sample['apk'], dirname + "/" + apk_name)
