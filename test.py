import cv2
imgname = input("::")
img = cv2.imread(imgname,1)
if img is None:
    print("can not open image!")
else:
    #img = cv2.Canny(img,100,200)
    cv2.imshow(imgname,img)
    cv2.waitKey()
    