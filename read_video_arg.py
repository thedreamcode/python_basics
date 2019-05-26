import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import sys

def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def main():
    lenArgs = len(sys.argv)
    listKnwnArgs = ["-videoPath", "-width", "-height"]
    videoPath = "/home/dream/Videos/4K Video Downloader/Around the World in 80 Clips.mp4"
    width = 720
    height = 480

    print ("Len of arguments are: " + str(lenArgs))
    print ("Arguments are: " + str(sys.argv))
    

    if (lenArgs > 1):
        for i in range(1, lenArgs):
            getArg = sys.argv[i].split("=")
            for j in range(len(listKnwnArgs)):
                if len(getArg) == 2:
                    if (listKnwnArgs[j] == getArg[0]):
                        if (j == 0):
                            videoPath = getArg[1]
                        elif (j == 1):
                            width = int(getArg[1])
                        elif (j == 2):
                            height = int(getArg[1])
                        

    camera = getVideoSource(videoPath, width, height)
    player = MediaPlayer(videoPath)

    while True:
            
        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            break

        frame = cv2.resize(frame, (width, height))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if val != 'eof' and audio_frame is not None:
            frame, t = audio_frame
            print("Frame:" + str(frame) + " T: " + str(t))

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()