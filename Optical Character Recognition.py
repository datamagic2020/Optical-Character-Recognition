import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
config = 'digits'

image = cv2.imread("images\ocrs2.jpg")
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img_RGB))

results = pytesseract.image_to_boxes(img_RGB)
ih, iw, ic = image.shape
for box in results.splitlines():
    box = box.split(' ')
    print(box)

    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(image, (x, ih-y), (w, ih-h), (0, 255, 0), 2)
    cv2.putText(image, box[0], (x, ih-h), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

# results = pytesseract.image_to_data(img_RGB)
# for id, line in enumerate(results.splitlines()):
#
#     if id != 0:
#         line = line.split()
#         if len(line) == 12:
#             x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
#             cv2.rectangle(image, (x, y), (w+x, h+y), (0, 255, 0), 2)
#             cv2.putText(image, line[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Input", image)
cv2.waitKey(0)