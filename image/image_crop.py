from PIL import Image
# 示例
if __name__ == "__main__":
    # 打开图片
    img = Image.open('example.jpg')

    # 定义裁切区域 前两位表示左上角的坐标，后两位表示右下角的坐标
    box = (100, 0, 950, 1205)

    # 裁切图片
    crop_img = img.crop(box)

    # 保存裁切后的图片
    crop_img.save('example_crop.jpg')
