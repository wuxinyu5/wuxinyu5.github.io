import cv2

# 灰度处理
img = cv2.imread("pic.png",cv2.IMREAD_GRAYSCALE)
# 打印矩阵形状
print(type(img))
print(img.shape)
cv2.imshow('image',img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
else:
    cv2.imshow('image', img)
# 保存图片
# cv2.imwrite("img_gray.jpg",img)
# cv2.imwrite("img_gray.bmp",img)