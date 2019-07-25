import cv2
import numpy as np

def nearest(img,rate):
    img_new = np.zeros((img.shape[0] * rate, img.shape[1] * rate, img.shape[2]),int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for m in range(rate):
                for n in range(rate):
                    img_new[rate*i + m][rate*j + n]= img[i][j]
    return img_new
def show_image(img,img_nearest,img_linear,img_nearest_self):
    cv2.namedWindow('original', cv2.WINDOW_NORMAL)
    cv2.imshow('original', img)
    cv2.namedWindow('nearest_function', cv2.WINDOW_NORMAL)
    cv2.imshow('nearest_function', img_nearest)
    cv2.namedWindow('linear_function', cv2.WINDOW_NORMAL)
    cv2.imshow('linear_function', img_linear)
    cv2.namedWindow('linear_self', cv2.WINDOW_NORMAL)
    cv2.imshow('linear_self', img_nearest_self)
    cv2.waitKey(0)

if __name__ == '__main__':
    # rate = increase rate
    img = cv2.imread('lena.jpg')
    rate = 2
    img_linear_x = int(img.shape[1] * rate)
    img_linear_y = int(img.shape[0] * rate)
    img_nearest = cv2.resize(img, (img_linear_x, img_linear_x), cv2.INTER_NEAREST)
    img_linear = cv2.resize(img, (img_linear_x, img_linear_x), cv2.INTER_LINEAR)
    print('original =',img.shape)
    print('nearest_function =',img_nearest.shape)
    print('linear_function =',img_linear .shape)
    a = nearest(img,rate)
    img_nearest_self = a.astype('uint8')
    show_image(img,img_nearest,img_linear,img_nearest_self)

