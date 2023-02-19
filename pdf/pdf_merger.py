from PyPDF2 import PdfMerger

# 定义要合并的PDF文件列表
pdf_files = ["test.pdf", "test.pdf"]

# 创建PdfFileMerger对象
pdf_merger = PdfMerger()

# 逐个打开PDF文件，并将其添加到pdf_merger对象中
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as file:
        pdf_merger.append(file)

# 示例
if __name__ == "__main__":
    # 将所有PDF文件合并为一个文件
    with open("merged_file.pdf", 'wb') as file:
        pdf_merger.write(file)
