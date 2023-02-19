import pdf2docx

# 将PDF文件转换为docx格式的Word文档
def convert_pdf_to_docx(pdf_file_path, docx_file_path, password=None):
    pdf2docx.parse(pdf_file_path, docx_file_path, password=password)

# 示例
if __name__ == "__main__":
    pdf_file_path = "TLT20230202.pdf"
    docx_file_path = "TLT20230202.docx"
    password = "TLT20230202"
    convert_pdf_to_docx(pdf_file_path, docx_file_path, password=password)
