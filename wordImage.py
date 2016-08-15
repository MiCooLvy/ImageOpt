# coding:utf-8
import cv2, threading
import numpy as np


def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)

    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color)

    return histImg


def average(*num):
    sum = 0
    for i in num:
        sum += i
    return int(sum / len(num))


def avgthread(image, w, startH, endH, binImg):
    for i in range(startH, endH):
        for j in range(w):
            avgPx = average(image[i, j, 0], image[i, j, 1], image[i, j, 2])
            binImg[i, j] = avgPx


def binImage(image):
    imgW = image.shape[0]
    imgH = image.shape[1]
    binImg = np.zeros([imgW, imgH], np.uint8)
    for h in range(imgH):
        for w in range(imgW):
            avgPx = average(image[w, h, 0], image[w, h, 1], image[w, h, 2])
            binImg[w, h] = avgPx
    return binImg

def main():
    p0 = 'E:/dev/opencv/pyCV/dog.jpg'
    p1 = 'E:/dev/opencv/pyCV/girl01.jpg'
    p2 = 'E:/dev/opencv/pyCV/blank.jpg'
    p3 = 'E:/dev/opencv/pyCV/g02.jpg'

    img = cv2.imread(p0)
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    b, g, r = cv2.split(img)

    # imgH = img.shape[0]
    # imgW = img.shape[1]
    # binImg = np.zeros([imgH, imgW], np.uint8)
    #
    # t = threading.Thread(target=avgthread, args=(img, imgW, 0, imgH / 2, binImg))
    # t1 = threading.Thread(target=avgthread, args=(img, imgW, imgH / 2, imgH, binImg))
    #
    # t.start()
    # t1.start()
    #
    # t.join()
    # t1.join()


    cv2.imshow("binImage", binImage(img))

#    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
