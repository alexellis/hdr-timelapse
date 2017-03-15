from picamera import PiCamera
from config import config
from pathMaker import PathMaker
from datetime import datetime

import os
import time
import glob

class Capture:
    def __init__(self, config, path_maker):
        self.camera = PiCamera()
        self.camera.resolution = (int(config["width"]), int(config["height"]))
        self.config = config
        self.path_maker = path_maker

    def take(self):
        names = []
        start = time.time()
        self.camera.start_preview()

        now = datetime.now()
        folder = self.path_maker.prepare_dir("/var/image", now)

        base_name = str(time.time()).replace(".", "_")
        evs = [-25,-10,0,10,25]
        for ev in evs:
            name = "slice_"+base_name + "_" + str(ev)+ ".jpg"
            self.camera.capture(name)
            names.append(name)
        self.camera.stop_preview()

        now = datetime.now()
#        path = self.path_maker.prepare_dir(base, now)

        cmd = "enfuse -o /var/image/" + folder + "/" + base_name+".jpg " + " ".join(names)
        os.system(cmd)

        map(os.remove, glob.glob("slice*.jpg"))

        end = time.time()
        return (names, (end-start))

if __name__ == "__main__":
    capture = Capture(config, PathMaker())
    files = capture.take()
    print("Duration: " + str(files[1]) + "s")
