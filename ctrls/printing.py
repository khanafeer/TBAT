# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import barcode
from  barcode import writer
from bidi.algorithm import get_display
import arabic_reshaper
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap
import os
import math
import glob
class print_doc():
    def __init__(self):
        self.printer = QPrinter()
        self.printer.setPaperSize(self.printer.paperSize())
        self.printer.setPageMargins(0,0,0,0,QPrinter.Millimeter)
        try:
            lines = [line.rstrip('\n') for line in open('data')]
            self.NAME = lines[0].split('=')[1]
            self.DETAILS = lines[1].split('=')[1]
        except:
            self.NAME = ""
            self.DETAILS = ""
    def pr_header(self):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><div dir="rtl">
                    <table dir="ltr" width="%s" border="0"><tr><td>''' % ('100%')
        txt += '''<img height='80' src="logo.png">'''
        txt += '''</td><td></td><td align="right">'''
        if self.NAME:
            txt += u"<h1>%s</h1>" % (self.NAME)
        if self.DETAILS:
            txt += u"<h3>%s</h3><br>" % (self.DETAILS)
        txt += '''</td></tr></table>'''


        return txt
    def pr_footer(self):
        #get these info from DB
        # get these info from DB
        txt = u"</div></body></html>"
        return txt
    def clear_dir(self):
        for the_file in os.listdir("thumb"):
            file_path = os.path.join("thumb", the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
    def print_logic(self,width,heihgt,num_copies,info,details,A4,h_num=5,v_num=13,position=1):
        width = width / float(h_num)
        heihgt = heihgt / float(v_num)
        try:os.mkdir("thumb")
        except:pass
        self.clear_dir()

        x = 1
        if A4:
            for i in info:
                for j in range(num_copies):
                    self.create_image(str(x)+"_"+str(j),i[0], i[1],details, width, heihgt)
                x += 1
            self.barcode_A4(h_num,v_num,width,heihgt,position)
        else:
            for i in info:
                nm = num_copies
                if v_num == 2:
                    nm = math.ceil(num_copies / 2.)
                for j in range(int(nm)):
                    self.create_image_full(str(x)+"_"+str(j),i[0], i[1], details, width, heihgt,h_num,v_num)
                x += 1
            self.barcode_printing(width*h_num ,heihgt*v_num)
    def create_image_full(self,img_name,bc,name,details,width,height,h_num,v_num):
        def mm2px(mm, dpi=300):
            return math.floor((mm * dpi) / 25.4)
        #bc.png
        bc_object = barcode.get('ean13', bc, writer=writer.ImageWriter(width, height / 3))
        svg = bc_object.save('bc')
        #top
        txt_size = int(mm2px(3))
        font = ImageFont.truetype('andlso.ttf', txt_size)
        img = Image.new("RGBA", (int(mm2px(width*h_num)), int(mm2px(height * v_num))), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        reshaped_text = get_display(arabic_reshaper.reshape(unicode(name)))
        # draw.text((80, 50), reshaped_text, (0, 0, 0), font=font)
        y_text = 0
        lines = textwrap.wrap(reshaped_text, width=30)
        for line in lines:
            ww, hh = font.getsize(line)
            draw.text((40, y_text), line, (0, 0, 0), font=font)
            y_text += hh
        #price part
        pf= ImageFont.truetype('andlso.ttf', int(mm2px(3)))
        # draw.text((375,175), price, (0, 0, 0), font=pf)
        txt_price = Image.new('RGBA', (500, int(mm2px(4))), (255, 255, 255))
        d = ImageDraw.Draw(txt_price)
        d.text((0, 0), bc, (0, 0, 0), font=pf)

        #details part
        details_text = get_display(arabic_reshaper.reshape(unicode(details)))


        #bc image
        im2 = Image.open(svg)
        #draw section
        if v_num == 2:
            img.paste(txt_price, box=(int(mm2px((width/2))), int(mm2px((height * 2) / 3))))
            draw.text((10, int(mm2px((height * 2) / 3))), details_text, (0, 0, 0), font=font)
        else:
            img.paste(txt_price, box=(40, int(mm2px((height * 2) / 3))))
            draw.text((40, int(mm2px((height * 2.5) / 3))), details_text, (0, 0, 0), font=font)
        img.paste(im2, box=(-40, int(mm2px(height /3))))
        img.save("thumb/%s.png" % (img_name))
        img.paste(img,box=(0, int(mm2px(height))))
        img.save("thumb/%s.png" % (img_name))

        #empty image
        img3 = Image.new("RGBA", (int(mm2px(width)), int(mm2px(height))), (255, 255, 255))
        img3.save('empty.png')
    def create_image(self,img_name,bc,name,details,width,height):
        def mm2px(mm, dpi=300):
            return math.floor((mm * dpi) / 25.4)
        #bc.png
        bc_object = barcode.get('ean13', bc, writer=writer.ImageWriter(width, 4))
        svg = bc_object.save('bc')
        #top
        txt_size = int(mm2px(3))
        font = ImageFont.truetype('andlso.ttf', txt_size)
        img = Image.new("RGBA", (int(mm2px(width)), int(mm2px(height))), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        reshaped_text = get_display(arabic_reshaper.reshape(unicode(name)))
        # draw.text((80, 50), reshaped_text, (0, 0, 0), font=font)

        y_text = 50
        lines = textwrap.wrap(reshaped_text, width=30)
        for line in lines:
            ww, hh = font.getsize(line)
            draw.text((80, y_text), line, (0, 0, 0), font=font)
            y_text += hh



        reshaped_text = get_display(arabic_reshaper.reshape(unicode(bc)))
        draw.text((80, int(mm2px((height * 2) / 3))), reshaped_text, (0, 0, 0), font=font)

        reshaped_text = get_display(arabic_reshaper.reshape(unicode(details)))
        draw.text((80, int(mm2px((height * 2.5) / 3))), reshaped_text, (0, 0, 0), font=font)

        im2 = Image.open(svg)
        img.paste(im2, box=(0, 135))

        img.save("thumb/%s.png"%(img_name))


        img3 = Image.new("RGBA", (int(mm2px(width)), int(mm2px(height))), (255, 255, 255))
        img3.save("thumb/empty.png")
    def barcode_A4(self,h_num,v_num,width,height,position):
        html = '''<html><head><meta charset="UTF-8">
        <style>body{padding : 0;margin : 0}table{height:100%;
    width:100%;table-layout:fixed;}p {display: block;}
     </style></head><body><table cellspacing="0">'''
        t = 1
        c = 0
        imgs = glob.glob("thumb/*.png")
        v_num = int(math.ceil(len(imgs) / float(h_num)))
        for i in range(v_num):
            html += "<tr width='"+str(width*h_num)+"'>"
            for j in range(h_num):
                if t == position:
                    position = t+1
                    try:
                        html += "<td  align='center'><img height='"+str(height)+"' width='"+str(width)+"' src='"+imgs[c]+"'></td>"
                    except:
                        html += "<td  align='center'><img height='" + str(height) + "' width='" + str(
                            width) + "' src='thumb/empty.png'></td>"
                    c += 1
                else:
                    html += "<td  align='center'><img height='"+str(height)+"' width='"+str(width)+"' src='thumb/empty.png'></td>"
                t += 1
            html += "</tr>"
        html += "</table></body></html>"
        self.printer.setResolution(300)
        self.printer.setPageMargins(0,0,0,0,QPrinter.Millimeter)
        self.printer.setPageSize(QPrinter.A4)
        doc = QTextDocument()
        doc.setHtml(html)
        doc.setPageSize(QSizeF(210,300))
        doc.setDocumentMargin(0)
        doc.print_(self.printer)
    def barcode_printing(self,width,height):
        for i in glob.glob("thumb/*.png"):
            html = '''<html><head><meta charset="UTF-8">
                    <style>body{padding : 0;margin : 0}</style></head><body>'''
            html += "<img height='"+str(height)+"' width='"+str(width)+"' src='"+i+"'>"
            html += "</body></html>"
            self.printer.setResolution(300)
            self.printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
            self.printer.setPaperSize(QSizeF(width,height),QPrinter.Millimeter)
            doc = QTextDocument()
            doc.setPageSize(QSizeF(width,height))
            doc.setDocumentMargin(0)
            doc.setHtml(html)
            doc.print_(self.printer)

    def print_attend(self,table,course,day):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><center><h1>تقرير الحضور والغياب</h1></center><hr>
        <div dir="rtl">'''
        txt += u'''<table width='%s' border="0">
        <col with="%s"><col with="%s">
         <tr><td><center>%s</center></td><td><center>اسم المجموعة</center></td></tr>
         <tr><td><center>%s</center></td><td><center>اليوم</center></td></tr>
        </table>''' % (
        "100%", "50%", "50%", course,day)
        txt += self.get_table(table)
        txt += u'''</div></body></html>'''
        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        doc.print_(self.printer)
    def print_mony_st(self,table,course,name,phone,fphone):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><center><h1>تقرير المعاملات المادية للطالب</h1></center><hr>
        <div dir="rtl">'''
        txt += u'''<table width='%s' border="0">
        <col with="%s"><col with="%s">
         <tr><td><center>%s</center></td><td><center>اسم الطالب</center></td></tr>
         <tr><td><center>%s</center></td><td><center>هاتف الطالب</center></td></tr>
         <tr><td><center>%s</center></td><td><center>هاتف ولى الامر</center></td></tr>
         <tr><td><center>%s</center></td><td><center>اسم المجموعة</center></td></tr>
        </table>''' % (
        "100%", "50%", "50%",name,phone,fphone,course)
        txt += self.get_table(table)
        txt += u'''</div></body></html>'''
        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        doc.print_(self.printer)
    def print_attend_st(self,table,course,day,name,phone,fphone):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><center><h1>تقرير حضور وغياب الطالب</h1></center><hr>
        <div dir="rtl">'''
        txt += u'''<table width='%s' border="0">
        <col with="%s"><col with="%s">
         <tr><td><center>%s</center></td><td><center>اسم الطالب</center></td></tr>
         <tr><td><center>%s</center></td><td><center>هاتف الطالب</center></td></tr>
         <tr><td><center>%s</center></td><td><center>هاتف ولى الامر</center></td></tr>
         <tr><td><center>%s</center></td><td><center>اسم المجموعة</center></td></tr>

        </table>''' % (
        "100%", "50%", "50%",name,phone,fphone,course)
        txt += self.get_table(table)
        txt += u'''</div></body></html>'''
        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        doc.print_(self.printer)
    def print_mony(self,table,course,day,tottal,baid,rest):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><center><h1>تقرير المعاملات المالية</h1></center><hr>
        <div dir="rtl">'''
        txt += u'''<table width='%s' border="0">
        <col with="%s"><col with="%s">
         <tr><td><center>%s</center></td><td><center>اسم المجموعة</center></td></tr>
                 <tr><td><center>%s</center></td><td><center>طريقة الدفع</center></td></tr>
                </table>''' % (
            "100%", "50%", "50%", course, day)
        txt += self.get_table(table)
        txt += u'''<table width='%s' border="0">
                        <col with="%s"><col with="%s">
                         <tr><td><center>%s</center></td><td><center>المقرر دفعة</center></td></tr>
                         <tr><td><center>%s</center></td><td><center>المدفوع</center></td></tr>
                         <tr><td><center>%s</center></td><td><center>الباقى</center></td></tr>
                        </table>''' % (
            "100%", "50%", "50%", tottal,baid,rest)
        txt += u'''</div></body></html>'''
        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        doc.print_(self.printer)
    def get_table(self,tb):
        txt = u"""<table width="100%" border="1">"""
        for i in range(len(tb)):
            if i == 0:
                txt += u"""<tr align="center">"""
                for x in range(len(tb[i])):
                    txt += u"<th>"+tb[i][x]+u"</th>"
                txt += u"</center></td></tr>"
            else:
                txt += u"""<tr align="center">"""
                for x in range(len(tb[i])):
                    txt += u"<td><center>" + unicode(tb[i][x]) + u"</center></td>"
                txt += u"</tr>"
        txt =txt + u"</table><br>"
        return txt
    def print_tottal(self,d1,d2,tottal,baid,rest):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><center><h1>تقرير اجمالى المالية</h1></center><hr>
                        <div dir="rtl">'''
        txt += u'''<table width='%s' border="0">
                        <col with="%s"><col with="%s">
                         <tr><td><center>%s</center></td><td><center>من</center></td></tr>
                         <tr><td><center>%s</center></td><td><center>الى</center></td></tr>
                        </table>''' % (
            "100%", "50%", "50%", d1, d2)
        txt += u'''<table width='%s' border="2">
                                <col with="%s"><col with="%s">
                                 <tr><td><center>%s</center></td><td><center>المقرر دفعة</center></td></tr>
                                 <tr><td><center>%s</center></td><td><center>المدفوع</center></td></tr>
                                 <tr><td><center>%s</center></td><td><center>الباقى</center></td></tr>
                                </table>''' % (
            "100%", "50%", "50%", tottal, baid, rest)
        txt += u'''</div></body></html>'''

        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        doc.print_(self.printer)
    def print_tottal_log(self, table,d1, d2, tottal, baid, rest):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><center><h1>تقرير اجمالى المالية</h1></center><hr>
                <div dir="rtl">'''
        txt += u'''<table width='%s' border="0">
                <col with="%s"><col with="%s">
                <tr><td><center>%s</center></td><td><center>من</center></td></tr>
                <tr><td><center>%s</center></td><td><center>الى</center></td></tr>
                </table>''' % (
            "100%", "50%", "50%",d1, d2)
        txt += self.get_table(table)
        txt += u'''<table width='%s' border="2">
                        <col with="%s"><col with="%s">
                        <tr><td><center>%s</center></td><td><center>المقرر دفعة</center></td></center></td></tr>
                        <tr><td><center>%s</center></td><td><center>المدفوع</center></td></center></td></tr>
                        <tr><td><center>%s</center></td><td><center>الباقى</center></td></center></td></tr>
                        </table>''' % (
            "100%", "50%", "50%", tottal, baid, rest)
        txt += u'''</div></body></html>'''

        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        doc.print_(self.printer)
    def print_st_report(self,table,d1,d2,bc,nm,school,add,ph,fph,mail,det,rtio):
        txt = u'''<html><head><meta charset="UTF-8"></head><body><center><h1>تقرير الطلاب المفصل</h1></center><hr>
                        <div dir="rtl">'''
        txt += u'''<table width='%s' border="0">
                        <col with="%s"><col with="%s">
                        <tr><td><center>%s</center></td><td><center>من</center></td></tr>
                        <tr><td><center>%s</center></td><td><center>الى</center></td></tr>
                        </table>''' % (
            "100%", "50%", "50%", d1, d2)
        txt += u'''<center><h3>بيانات الطالب</h3></center>'''
        txt += u'''<table width='%s' border="2">
                                        <col with="%s"><col with="%s">
                                        <tr><td><center>%s</center></td><td><center>هاتف الطالب</center></td><td><center>%s</center></td><td><center>كود الطالب</center></td></center></td></tr>
                                        <tr><td><center>%s</center></td><td><center>هاتف ولى الامر</center></td><td><center>%s</center></td><td><center>الاسم</center></td></center></td></tr>
                                        <tr><td><center>%s</center></td><td><center>البريد الالكترونى</center></td><td><center>%s</center></td><td><center>المدرسة</center></td></center></td></tr>                                       
                                        <tr><td><center>%s</center></td><td><center>التفاصيل</center></td><td><center>%s</center></td><td><center>العنوان</center></td></center></td></tr>
                                        </table>''' % (
            "100%", "50%", "50%", ph,bc,fph,nm,mail,school,det, add)
        txt += u'''<center><h3>تقرير الطالب</h3></center>'''
        txt += self.get_table(table)
        txt += u'''<br><center><h1>%s</h1></center>''' %(rtio)
        txt += u'''</div></body></html>'''
        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        print txt
        doc.print_(self.printer)


    def print_info(self,list,title):
        txt = self.pr_header()
        txt += u'<center><h1>%s</h1></center><br>'%(title)
        txt += self.get_table(list)
        txt += self.pr_footer()
        doc = QTextDocument()
        op = QTextOption()
        op.setTextDirection(Qt.RightToLeft)
        doc.setDefaultTextOption(op)
        doc.setHtml(txt)
        doc.print_(self.printer)