from PIL import Image


# 示例
if __name__ == "__main__":
    # 打开图片
    img = Image.open('example.jpg')

    # 转为黑白
    bw_img = img.convert('L')

    # 保存黑白图片
    bw_img.save('example_bw.jpg')
