import os
from datetime import datetime

class PathMaker:
	def __init__(self):
		pass
	def get_parts(self, totalPath):
		if(totalPath==None):
			return []
		return totalPath.strip("/").split("/")

	def get_paths(self, totalPath):
		parts = self.get_parts(totalPath)
		paths =[]
		path = "/"
		for p in parts:
			path = os.path.join(path,p)
			paths.append(path)
    		return paths

        def try_to_mkdir(self, path):
            if os.path.exists(path) == False:
                os.makedirs(path)

        def prepare_dir(self, base, now):
            path = str(now.year)
            self.try_to_mkdir(base + "/" +path)

            path = str(now.year)  + "/"  + str(now.month)
            self.try_to_mkdir(base + "/" +path)

            path = str( datetime.now().year)  + "/"  + str( datetime.now().month)+"/"+ str( datetime.now().day)
            self.try_to_mkdir(base + "/" +path)

            path =  str( datetime.now().year)  + "/"  + str( datetime.now().month)+"/"+ str( datetime.now().day)+"/"+ str( datetime.now().hour)
            self.try_to_mkdir(base + "/" +path)

            return path


