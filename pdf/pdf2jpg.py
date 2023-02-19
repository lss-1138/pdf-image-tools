import fitz
import os

# 将PDF转换为JPG
def convert_pdf_to_jpg(pdf_file_path, jpg_dir_path, dpi=300):
    # 打开PDF文件
    with fitz.open(pdf_file_path) as pdf:
        # 逐页转换PDF为JPG
        for page_idx, page in enumerate(pdf):
            # 将当前页转换为JPG图像
            pix = page.get_pixmap(alpha=False, matrix=fitz.Matrix(dpi/72,dpi/72))
            # 构建JPG文件路径
            jpg_file_name = f"page{page_idx+1}.jpg"
            jpg_file_path = os.path.join(jpg_dir_path, jpg_file_name)
            # 保存JPG文件
            pix.save(jpg_file_path)

# 示例
if __name__ == "__main__":
    pdf_file_path = "test.pdf"
    jpg_dir_path = "output_dir"
    # 创建JPG目录
    os.makedirs(jpg_dir_path, exist_ok=True)
    # 将PDF转换为JPG
    convert_pdf_to_jpg(pdf_file_path, jpg_dir_path, dpi=300)
