import time
import cv2 as cv2



# пункт 1
def viewImage():
    img = cv2.imread(cv2.samples.findFile("variant-8.jpg"))
    width = int(img.shape[1])//2
    height = int(img.shape[0])//2
    cropped = img[height-200:height+200, width-200:width+200] # вырезал прямоугольник в середине размером 400х400
    cv2.imshow('Cat', cropped)



# пункт 2, 3, и муха


def video_processing():
    cap = cv2.VideoCapture(0)
    img = cv2.imread('fly64.png')
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            x0 = x + (w // 2)
            y0 = y + (h // 2)

            cv2.line(frame, (0, y0), (640, y0), (0, 255, 0), 2)
            cv2.line(frame, (x0, 0), (x0, 480), (0, 255, 0), 2)


            img_w = w // 4 if (w // 4) % 2 == 0 else w // 4 + 1
            img_h = h // 4 if (h // 4) % 2 == 0 else h // 4 + 1
            img = cv2.resize(img, (img_w, img_h), interpolation=cv2.INTER_LINEAR)
            frame[y0 - img_h // 2:y0 + img_h // 2, x0 - img_w // 2:x0 + img_w // 2] = img

            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                print(a, b)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()


if __name__ == '__main__':
    # viewImage()
    # video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()

