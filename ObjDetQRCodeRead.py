import cv2
import cv2
from pyzbar import pyzbar
#from gpiozero import LED

from time import sleep

#led1 = LED(17)
#led2 = LED(18)


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    a = 0
    b = 0
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        print(barcode_text)

        if barcode_text:
            print("QRCode Present")
            b = 1

        if barcode_text == "2":
  #          led2.off()
 #           led1.on()
            print("c 2 ")
            a = 2

        if barcode_text == "3":
 #           led1.off()
 #           led2.on()
            print("c 3 ")
            a = 3

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame, a, b


classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img,thres,nms,draw=True,objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId-1]
            if className in objects:
                objectInfo.append([box, className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,className.upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    return img,objectInfo

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    # cap.set(10,70)





while True:
    success, img = cap.read()
    result,objectInfo = getObjects(img,0.45,0.2,objects=[])
    #printing()
    if objectInfo[0][1]=="person":
        print("**PERSON**")

    qrvalue = 0
    stopqrValue = 0
    frame = read_barcodes(img)


    cv2.imshow("Output", img)
    cv2.waitKey(1)




