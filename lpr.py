import cv2
import os
import sys
import getopt
import subprocess
import json
from io import StringIO

def alpr(cam_id):
    alpr = 'alpr -c eu rtsp-stream{}.jpg'.format(cam_id)
    os.system(alpr)
#     batcmd=alpr
#     result = subprocess.check_output(batcmd, shell=True)
#     res = json.loads(result)
#     print(res["results"])



def get_arguments():
    try:
        rtsp_stream_url = None
        cam_id = None
        opts, args = getopt.getopt(sys.argv[1:], "r:c:", ["rtsp_stream_url=",'cam_id='])
        for opt, arg in opts:
            if opt == '-r':
                rtsp_stream_url = arg
            if opt == '-c':
                cam_id = arg

        if not rtsp_stream_url:
            print('Required argument -r "Rtsp stream" is missing.Example "lpr.py -r rtsp://0.0.0.0:554/v2"')
            exit()
        if not cam_id:
            print('Required argument -c "Camera id" is missing.Example "lpr.py -c 1 -r rtsp://0.0.0.0:554/v2"')
            exit()

        return rtsp_stream_url, cam_id
    except Exception as e:
        print(e)
        exit()

"""
Arguments:
    sys.argv[1] is Rtsp Stream "rtsp://0.0.0.0:554/v2"
"""
def main():
    rtsp_url,cam_id = get_arguments()
    counter=0
    print('Starting LPR Engine')

    video = cv2.VideoCapture(rtsp_url)
    while True:
        _,frame = video.read()
        cv2.imwrite('rtsp-stream{}.jpg'.format(cam_id), frame)
        if counter == 20:
            alpr(cam_id)
            counter = 0
        counter += 1


    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
