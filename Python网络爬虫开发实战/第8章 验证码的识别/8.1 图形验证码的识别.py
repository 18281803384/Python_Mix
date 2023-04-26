import pytesseract
from PIL import Image

image = Image.open('file/8.1_Code.jpg')


image = image.convert('L')  # 将图片转化为灰度图像
# image.show()
threshold = 127 # 二值化阈值
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')  # 将图片进行二值化处理
# image.show()
result = pytesseract.image_to_string(image)
print("验证码识别结果为:",result)


