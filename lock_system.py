import ctypes
from datetime import datetime

flg=1
while flg:
    if '12:21' in str(datetime.time(datetime.now()))[:5]:
        ctypes.windll.user32.LockWorkStation()
    print str(datetime.time(datetime.now())),"sasa"
    if '12:22' in str(datetime.time(datetime.now()))[:5]:
        flg=0
    
