import glob
import sys
import os
from msbase.utils import load_json

metadata = load_json(sys.argv[1])
dirname = sys.argv[2]
metadata_root_dir = sys.argv[3]

assert dirname in ["maldir", "gooddir"]

os.makedirs(dirname, exist_ok=True)

for sample in metadata:
    os.symlink(metadata_root_dir + "/" + sample['apk'], dirname + "/" + os.path.basename(sample['apk']))
