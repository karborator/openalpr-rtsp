# openalpr-rtsp
LPR detection via openalpr project consuming rtsp stream

Installation
 - pip install -r requirements
 - add openalpr to your system by following one of the compilation guides: https://github.com/openalpr/openalpr


Start
 - cd openalpr-rtsp
 - python lpr.py -c cam1 -r rtsp://user:pass@ip:port/channel ( example rtsp channel: ch01.264 )
