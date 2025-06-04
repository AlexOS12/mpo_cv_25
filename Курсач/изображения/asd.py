import cv2
import numpy as np

src = cv2.imread("1.png", cv2.IMREAD_COLOR)

size = src.shape
w, h = size[:2]
w *= 3
h *= 3

src = cv2.resize(src, (h, w), interpolation=cv2.INTER_NEAREST)
src = cv2.GaussianBlur(src, (3,3), 0)

# dst = cv2.Laplacian(src, cv2.CV_8U, ksize=3)

# res = cv2.addWeighted(src, 1, dst, 0.5, 0)

# cv2.imwrite("out.png", res)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(src, -1, kernel)

cv2.imwrite("out.png", sharpened)