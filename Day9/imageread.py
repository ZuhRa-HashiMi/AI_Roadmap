import cv2

image = cv2.imread("pic.png", cv2.IMREAD_GRAYSCALE)

print(image.shape)

print(image[:5, :5])