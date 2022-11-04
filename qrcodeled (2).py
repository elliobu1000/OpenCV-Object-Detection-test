import cv2
from pyzbar import pyzbar
#from gpiozero import LED

from time import sleep

#led1 = LED(17)
#led2 = LED(18)


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        print(barcode_text)
        if barcode_text == "2":
            #            led2.off()
        #           led1.on()
            print(2)
        elif barcode_text == "3":
            #           led1.off()
        #          led2.on()
            print(3)

            
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame

def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
