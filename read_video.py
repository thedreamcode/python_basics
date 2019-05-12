import cv2


def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def main():
    sourcePath = "/home/dream/Videos/4K Video Downloader/Around the World in 80 Clips.mp4"
    camera = getVideoSource(sourcePath, 720, 480)

    while True:
            
        ret, frame = camera.read()
        frame = cv2.resize(frame, (720, 480))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()