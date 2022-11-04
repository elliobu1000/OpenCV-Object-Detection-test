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

# def bla(qr):
    # if qr == 1



def main():
    # global qrvalue
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    qrvalue = 0
    stopqrValue = 0
    while ret:
        frame, state, state2 = read_barcodes(frame)
        if state2 != 0:
            stopqrValue = state2
        if state != 0:
            qrvalue = state
            # stopmotor()
        print('qrvalue', qrvalue)
        print("****")
        print('stopqrval', stopqrValue)
        ret, frame = camera.read()
        cv2.imshow('Barcode reader', frame)
        if (qrvalue != 0):
            sleep(0.1)
            break
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()
    return qrvalue, stopqrValue


if __name__ == '__main__':
    main()




