
import matplotlib.pyplot as plt
import cv2
image = cv2.imread("C:/Users/21620/Desktop/maldives.jpg")
if image is None:
    print("Error: Unable to load image")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)  
    plt.show()
    cv2.imwrite('C:/Users/21620/Desktop/cv/image_rgb.jpg', image_rgb)    
    cv2.imshow('image_rgb');
    cv2.waitKey(0)
    cv2.destroyAllWindows()
