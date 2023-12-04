import numpy as np
import cv2

def correct_file(name: str) -> None:
    with open(name, "r") as file:
        tekst = file.read()
    tekst = tekst.replace("]", "")
    tekst = tekst.replace("[", "")
    with open(f"corrected_{name}", "w") as file:
        print(tekst, file=file)

# read files
correct_file("mtx.txt")
mtx = np.loadtxt("corrected_mtx.txt")
print(mtx)

correct_file("dist.txt")
dist = np.loadtxt("corrected_dist.txt")
print(dist)

# poprawka zdjęcia
img = cv2.imread('zdj11.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png', dst)