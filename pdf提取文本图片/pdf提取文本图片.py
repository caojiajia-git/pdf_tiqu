# -*- coding: utf-8 -*-
########################### 提取文本方法1 ##############################################
# from pdfminer.pdfparser import PDFParser, PDFDocument, PDFPage
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, PDFTextExtractionNotAllowed
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LTTextBoxHorizontal, LAParams
#
# '''
# PDFParser     从文件中获取数据
# PDFDocument   存储文档数据结构到内存中
# PDFPageInterpreter 解析page内容
# PDFDevice    把解析到的内容转化为你需要的东西
# PDFResourceManager存储共享资源，例如字体或图片
# '''
# text_path = 'C:/Users/lenovo/Desktop/2020年食品7月133-147发片_发片.pdf'
# def parse():
#     '''解析PDF文本，并保存到TXT文件中'''
#     fp = open(text_path, 'rb')
#     # 用文件对象创建一个PDF文档分析器
#     parser = PDFParser(fp)
#     # 创建一个PDF文档
#     doc = PDFDocument()
#     # 连接分析器，与文档对象
#     parser.set_document(doc)
#     doc.set_parser(parser)
#     # 提供初始化密码，如果没有密码，就创建一个空的字符串
#     doc.initialize()
#     # 检测文档是否提供txt转换，不提供就忽略
#     if not doc.is_extractable:
#         raise PDFTextExtractionNotAllowed
#     else:
#         # 创建PDF，资源管理器，来共享资源
#         rsrcmgr = PDFResourceManager()
#         # 创建一个PDF设备对象
#         laparams = LAParams()
#         device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#         # 创建一个PDF解释其对象
#         interpreter = PDFPageInterpreter(rsrcmgr, device)
#
#         # 循环遍历列表，每次处理一个page内容
#         # doc.get_pages() 获取page列表
#         for page in doc.get_pages():
#             interpreter.process_page(page)
#             # 接受该页面的LTPage对象
#             layout = device.get_result()
#             # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
#             # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
#             # 想要获取文本就获得对象的text属性，
#             for x in layout:
#                 if (isinstance(x, LTTextBoxHorizontal)):
#                     with open(r'2.txt', 'a') as f:
#                         results = x.get_text()
#                         # results = x.get_text().encode('utf-8')
#                         print(results)
#                         f.write(results)
#
# if __name__ == '__main__':
#     parse()
# ########################## 提取文本方法2-方法3 ##############################################

import fitz
from operator import itemgetter
import time

#
# # 方法2：将pdf转换为txt文字
# def pdf_to_text(pdfPath, textPath):
#     doc = fitz.open(pdfPath)
#     for page in doc:
#         text = page.getText()
#         print(text)
#         with open(textPath, 'a') as f:
#             f.write(text + '\n')

# 方法3：将pdf转换为txt文字块
def pdf_to_TextBlocks(pdfPath, textPath):
    doc = fitz.open(pdfPath)
    for page in doc:
        blocks = page.getTextBlocks()
        sb = sorted(blocks, key=itemgetter(1, 0))
        for b in sb:
            print(b[4])
            with open(textPath, 'a') as f:
                f.write(b[4] + '\n')
def main():
    sTime = time.time()
    # pdf_to_text('C:/Users/lenovo/Desktop/2020年食品7月133-147发片_发片.pdf', 'C:/Users/lenovo/Desktop/pdftxt.txt')
    pdf_to_TextBlocks('C:/Users/lenovo/Desktop/2020年食品7月133-147发片_发片.pdf', 'C:/Users/lenovo/Desktop/pdftxt.txt')
    eTime = time.time()
    s = eTime - sTime
    print('花费的时间为：%.2f秒' % (s))
if __name__ == '__main__':
    main()
############################## 提取图片 ###########################################

# import time
# import re
# import os
# import fitz
# def pdf2pic(path, pic_path):
#     t0 = time.clock()  # 生成图片初始时间
#     checkXO = r"/Type(?= */XObject)"  # 使用正则表达式来查找图片
#     checkIM = r"/Subtype(?= */Image)"
#     doc = fitz.open(path)  # 打开pdf文件
#     imgcount = 0  # 图片计数
#     lenXREF = doc._getXrefLength()  # 获取对象数量长度
#     # 打印PDF的信息
#     print("文件名:{}, 页数: {}, 对象: {}".format(path, len(doc), lenXREF - 1))
#     # 遍历每一个对象
#     for i in range(1, lenXREF):
#         text = doc._getXrefString(i)  # 定义对象字符串
#         isXObject = re.search(checkXO, text)  # 使用正则表达式查看是否是对象
#         isImage = re.search(checkIM, text)  # 使用正则表达式查看是否是图片
#         if not isXObject or not isImage:  # 如果不是对象也不是图片，则continue
#             continue
#         imgcount += 1
#         pix = fitz.Pixmap(doc, i)  # 生成图像对象
#         new_name = "图片{}.png".format(imgcount)  # 生成图片的名称
#
#         # new_name = path.replace('\\', '_') + "_img{}.png".format(imgcount)
#         # new_name = new_name.replace(':', '')     # 生成图片的名称
#
#         # if pix.n < 5:  # 如果pix.n<5,可以直接存为PNG
#         #     pix.writePNG(os.path.join(pic_path, new_name))
#         # else:  # 否则先转换CMYK
#         #     pix0 = fitz.Pixmap(fitz.csRGB, pix)
#         #     pix0.writePNG(os.path.join(pic_path, new_name))
#         #     # pix0 = None
#         #pix = None  # 释放资源
#
#         #转换CMYK
#         pix0 = fitz.Pixmap(fitz.csRGB, pix)
#         pix0.writePNG(os.path.join(pic_path, new_name))
#
#         t1 = time.clock()  # 图片完成时间
#         print("运行时间:{}s".format(t1 - t0))
#         print("提取了{}张图片".format(imgcount))
#
# if __name__ == '__main__':
#     path = r"C:\Users\lenovo\Desktop\2020年食品7月133-147发片_发片.pdf"
#     pic_path = r"C:/Users/lenovo/Desktop/tu"
#     # 创建保存图片的文件夹
#     if os.path.exists(pic_path):
#         print("文件夹已存在，不必重新创建！")
#         pass
#     else:
#         os.mkdir(pic_path)
#     pdf2pic(path, pic_path)
