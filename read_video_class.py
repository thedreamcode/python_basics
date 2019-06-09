import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import sys

class ReadVideo:
    def __init__(self):
        self.lenArgs = len(sys.argv)
        self.listKnwnArgs = ["-videoPath", "-width", "-height"]
        self.videoPath = "/home/dream/Videos/4K Video Downloader/Around_world.mp4"
        self.width = 720
        self.height = 480
        self.cap = None
        print ("Len of arguments are: " + str(self.lenArgs))
        print ("Arguments are: " + str(sys.argv))

    def getVideoSource(self):
        self.cap = cv2.VideoCapture(self.videoPath)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def video_loop(self):
        self.updating_aguments()
        self.getVideoSource()
        player = MediaPlayer(self.videoPath)

        while True:
            ret, frame = self.cap.read()
            audio_frame, val = player.get_frame()

            if (ret == 0):
                print("End of video")
                break

            frame = cv2.resize(frame, (self.width, self.height))
            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if val != 'eof' and audio_frame is not None:
                frame, t = audio_frame
                print("Frame:" + str(frame) + " T: " + str(t))

        self.cap.release()
        cv2.destroyAllWindows()

    def updating_aguments(self):
        if (self.lenArgs > 1):
            for i in range(1, self.lenArgs):
                getArg = sys.argv[i].split("=")
                for j in range(len(self.listKnwnArgs)):
                    if len(getArg) == 2:
                        if (self.listKnwnArgs[j] == getArg[0]):
                            if (j == 0):
                                self.videoPath = getArg[1]
                            elif (j == 1):
                                self.width = int(getArg[1])
                            elif (j == 2):
                                self.height = int(getArg[1])
                            
    
if __name__ == "__main__":
    readvideo = ReadVideo()
    readvideo.video_loop()