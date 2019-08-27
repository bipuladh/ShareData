from security import encryptfile, decryptfile

from consts import HOME_DIR_PATH
import os

src_file = os.path.join(HOME_DIR_PATH, "mct.txt.aes")
decryptfile(src_file, "hijklop")