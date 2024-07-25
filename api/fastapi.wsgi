import sys
import os
DIR=os.path.dirname(__file__)
sys.path.append(DIR)
sys.path.insert(0, ’/home/s2322057/dbmap_app/’)
from myapp import app as application
