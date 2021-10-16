import cv2
import os
import time

people = ["Đức", "HĐức", "Hiếu", "Hùng", "Kiên", "Linh", "Quân", "Tân", "Thắng", 
"Trường", "Tuấn", "Vân", "Việt Đức", "Xuân Anh"]

count = 0

for person in people:
    time_start = time.time()
    cam = cv2.VideoCapture("./Video/" + person + ".mp4")
    video_length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))-1
    try:
        if not os.path.exists(person):
            os.makedirs(person)
    except OSError:
        print ('Error: Creating directory of data')
    currentframe = 0
    while(True):
        success, frame = cam.read()
        if success:
            # extract frame EVERY ONE SECOND
            cam.set(cv2.CAP_PROP_POS_MSEC,(currentframe*200))
            name = './' + person + '/frame' + str(currentframe) + '.png'
            cv2.imwrite(name, frame)
            currentframe += 1
            if (currentframe > (video_length-1)):
                time_end = time.time()
                cam.release()
                break
        else:
            break
    count += 1
    cam.release()
    
cv2.destroyAllWindows()