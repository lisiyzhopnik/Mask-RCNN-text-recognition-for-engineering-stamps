import subprocess
proc = subprocess.Popen("cmd.exe /c start python.exe -i C:\\Users\\kuanyshov.a\\Anaconda3\\envs\\project1\\Mask_RCNN-master\\mrcnn\\print_output.py".split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)