import cv2
 
img = cv2.imread('/home/iza/Área de Trabalho/Image_process/LapiscoTraining/Questions/1/image.jpg')
new_img = cv2.imwrite('/home/iza/Área de Trabalho/Image_process/LapiscoTraining/Questions/1/new_image.jpg', img)

cv2.imshow('new_image.jpg',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()