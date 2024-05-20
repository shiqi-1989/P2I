# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal, QThread, QMutex
import fitz
import glob
import os
from PyPDF2 import PdfReader, PdfWriter


class PdfThead(QThread):
    signal = pyqtSignal(str)

    def __init__(self, param, path, *args, **kwargs):
        super().__init__()
        self.param = param
        self.path = path
        self.num = args

    def run(self):
        print('----开始线程----')
        if self.param == 1:
            btn = self.num[2]
            self.pdf2img()
            btn.setText("开始转换")
            btn.setEnabled(True)
        elif self.param == 2:
            btn = self.num[0]
            self.img2pdf()
            btn.setText("开始转换")
            btn.setEnabled(True)
        elif self.param == 3:
            print(self.num)
            btn = self.num[2]
            self.pdf_split()
            btn.setText("开始拆分")
            btn.setEnabled(True)
        else:
            self.signal.emit('请选择文件！')
            return

    def pdf2img(self):
        file_name = os.path.splitext(self.path)[0]
        if self.num[0] == '':
            home_page = 0
        else:
            home_page = int(self.num[0]) - 1
        doc = fitz.open(self.path)
        if self.num[1] == '':
            back_page = doc.page_count
        else:
            back_page = int(self.num[1])
        if back_page > doc.page_count:
            self.signal.emit('结束页超出最大页数')
            return
        if home_page + 1 > back_page:
            self.signal.emit('起始页不能大于结束页')
            return
        self.signal.emit(f"PDF共：{doc.page_count}页")
        # print(f"PDF共：{doc.page_count}页")
        # print(home_page, back_page)
        for pg in range(home_page, back_page):
            text = f"转为图片: {pg + 1}/{doc.page_count}"
            self.signal.emit(text)
            # if pg == doc.page_count - 1:
            #     print(f"\r转为图片: {pg + 1}/{doc.page_count}")
            # else:
            #
            #     print(f"\r转为图片: {pg + 1}/{doc.page_count}", end="")
            page = doc[pg]
            rotate = int(0)
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            img_path = f'{file_name}-{pg + 1:03}.png'
            # print(img_path)
            pm = page.get_pixmap(matrix=trans, alpha=False)
            pm.save(img_path)
        # print('转换完成！')
        self.signal.emit('转换完成！')

    def img2pdf(self):
        doc = fitz.open()
        self.signal.emit('检测图片...')
        # print('检测图片...')
        self.path = self.path.replace('/', '\\')
        # img_list = glob.glob(self.path + '/*.png')
        try:
            img_list = self.get_png()
        except:
            self.signal.emit('获取图片异常，请正确命名图片！')
            return
        if img_list:
            # for img in sorted(img_list, key=os.path.getatime):  # 读取图片，确保按文件名排序
            for img in img_list:
                img = self.path + '\\' + img
                self.signal.emit(img)
                # print(img)
                img_doc = fitz.open(img)  # 打开图片
                pdf_bytes = img_doc.convert_to_pdf()  # 使用图片创建单页的 PDF
                img_pdf = fitz.open("pdf", pdf_bytes)
                doc.insert_pdf(img_pdf)  # 将当前页插入文档
        else:
            self.signal.emit('没有可转换的图片')
            return
        pdf_path = os.path.join(self.path, "result.pdf")
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        doc.save(pdf_path)  # 保存pdf文件
        self.signal.emit('PDF转换成功！')
        # print('PDF转换成功！')
        doc.close()

    def pdf_split(self):
        print(self.path)
        file_name = os.path.splitext(self.path)[0]
        mode = self.num[0]
        pdf = PdfReader(self.path)
        pages = pdf.pages
        print(type(pages))
        page_len = len(pages)
        print(f"pages:{page_len}")
        if mode == 0:
            num = self.num[1]
            if num == '':
                x = 1
                y = 0
            else:
                num = int(num)
                x = page_len // num  # 分割页数
                y = page_len % num  # 剩余页数
            # print(f"分割页数:{x}")
            # print(f"剩余页数:{y}")
            if x > 0 and y == 0:
                for i in range(0, page_len, x):
                    pdf_writer = PdfWriter()
                    for page in range(i, i + x):
                        current_page = pages[page]
                        pdf_writer.add_page(current_page)
                        print(f"添加第{page}页")
                    out_put_file_name = f"{file_name}-{i + 1}-{i + x}.pdf"
                    with open(out_put_file_name, "wb") as f:
                        try:
                            pdf_writer.write(f)
                        except Exception as e:
                            self.signal.emit(str(e))
                    self.signal.emit(f"分割{i + 1}-{i + x}页")
                self.signal.emit('拆分完成！')
            else:
                self.signal.emit(f'无法平分为{num}份！')
                return
        if mode == 1:
            num = self.num[1].split(',')
            print(num)
            try:
                for i in num:
                    try:
                        i = int(i)
                        if i < 1:
                            self.signal.emit('请保证正确的分割格式！')
                            return
                        pdf_writer = PdfWriter()
                        current_page = pages[i - 1]
                        pdf_writer.add_page(current_page)
                        out_put_file_name = f"{file_name}-{i}.pdf"
                        with open(out_put_file_name, "wb") as f:
                            pdf_writer.write(f)
                        self.signal.emit(f"分割{i}页")
                    except:
                        num_list = i.strip().split('-')
                        print(num_list)
                        home_page = int(num_list[0])
                        back_page = int(num_list[1])
                        print(home_page, back_page)
                        if home_page >= back_page:
                            self.signal.emit('请保证正确的分割格式！')
                            return
                        pdf_writer = PdfWriter()
                        for page in range(home_page - 1, back_page):
                            current_page = pages[page]
                            pdf_writer.add_page(current_page)
                        out_put_file_name = f"{file_name}-{home_page}-{back_page}.pdf"
                        with open(out_put_file_name, "wb") as f:
                            pdf_writer.write(f)
                        self.signal.emit(f"分割{home_page}-{back_page}页")
                self.signal.emit('拆分完成！')
            except:
                self.signal.emit('请保证正确的分割格式！')
                return

    def get_png(self):  # 自定义按照数字名称排序
        all_file = os.listdir(self.path)
        png_list = []
        suffixes = ('.png', '.jpg', '.jpeg')
        for file in all_file:
            if file.endswith(suffixes):
                png_list.append(file)

        png_list.sort(key=lambda x: int(x[:-4]))
        return png_list
