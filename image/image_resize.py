from PIL import Image

# 示例
if __name__ == "__main__":
    # 打开图像文件
    image = Image.open("image.jpg")

    # 设置缩放比例
    scale_percent = 200 # 缩放比例,100为不变

    # 计算新的图像大小
    width = int(image.width * scale_percent / 100)
    height = int(image.height * scale_percent / 100)
    dim = (width, height)

    # 修改图像分辨率
    resized_image = image.resize(dim)

    # 保存修改后的图像
    resized_image.save("resized_image.jpg")