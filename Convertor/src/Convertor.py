#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'guipengliang'

#print('In MainWindow.py')
#import logging
#from Util.Setting import Settings

#a=Settings()
#logging.info('a=Settings()')

import sys
#logging.info('import sys')
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *\
#print('import sys')
from PyQt4 import QtCore,QtGui
#logging.info('from PyQt4 import QtCore,QtGui')
#print('import PyQt4')
from UIMainWindow import Ui_MainWindow
#logging.info('from UIMainWindow import Ui_MainWindow')
#print('import UIMainWindow')
import urllib
#logging.info('import urllib')
#print('import urllib')
import base64
#logging.info('import base64')
#print('import base64')
import hashlib
#logging.info('import hashlib')
#print('import hashlib')
import Resource_rc
#logging.info('import Resource_rc')
#print('import Resource')
#import codecs
#logging.info('import codecs')
from Util.HtmlEntities import HtmlEntities
#logging.info('from Util.HtmlEntities import HtmlEntities')

class MyWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Convertor')
        self.setWindowIcon(QtGui.QIcon(':/img/icon.png'))
        self.ui.m_printLabel.setText('')
        pass

    def __del__(self):
        pass

    def onUpperBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            str=str.upper()
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
            print(e)
        pass

    def onLowerBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            str=str.lower()
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
            print(e)
        pass

    def onSwapcaseBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            str=str.swapcase()
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
            print(e)
        pass

    def onCapitalizeBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            str=str.capitalize()
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
           print(e)
        pass

    def onAsciiEncodeBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            strRt=''
            #for c in str:
               # strRt+=str(ord(c))
            for item in map(ord,strSrc):
                #tmpStr='%d'%item
                tmpStr=str(item)
                strRt+=tmpStr+' '
            strRt=strRt.strip()
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def onAsciiDecodeBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            strSrc=strSrc.split()
            strRt=''
            try:
                for item in strSrc:
                    strRt+=chr(int(item))
            except Exception as e:
                pass
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def onHexEncodeBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            strStrs=strSrc.split()

            strRt=''
            for item in strStrs:
                if not item.strip():
                    continue
                for c in item:
                    strRt+=hex(ord(c))+' '
            strRt=strRt.strip()
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def onGBKToCodeBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            qstrTmp=strSrc
            #qstrTmp=qstrTmp.toLocal8Bit()
            qstrTmp=qstrTmp.encode('gbk')
            strRt = ''
            for item in qstrTmp:
                strRt+='\\x%x'%item
            # for c in qstrTmp:
            #     strRt+=hex(ord(c))+' '
            strRt=strRt.strip()
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def onCodeToGBKBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            strRt = self.codeToGbk(strSrc)
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
           print(e)
        pass

    def gbkCodeToChinese(self,strStrs):
        bStrs=strStrs.encode('latin-1')
        uStrs=bStrs.decode('unicode_escape')
        bTrueStrs=uStrs.encode('latin-1')
        strStrs=bTrueStrs.decode('gbk')
        return strStrs
        pass

    def codeToGbk(self, str):
        try:
            strSrc = str
            strStrs = strSrc.replace('0x','\\x').replace(' ','')
            # strStrs=bytes(strStrs,'gbk').decode('unicode_escape')
            strStrs=self.gbkCodeToChinese(strStrs)

            return strStrs
            # strStrs = strSrc.replace('0x',' ').split()
            # strRt = ''
            # for c in strStrs:
            #     if not c.strip():
            #         continue
            #     #a = r'\x' + c.strip().decode()
            #     c=bytes(c,'utf-8')
            #     # b=c.decode('string-escape')
            #     a = hex(ord(c.strip()))
            #     strRt += a.decode('string-escape')
            # for item in strRt:
            #     a = hex(ord(item))
            #     print(a)
            # print(strRt)
            # strRt = strRt.strip().decode('gb2312')
            # return strRt
        except Exception as e:
            print(e)

    def onUtf8ToCodeBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            strRt = self.utf8ToCode(strSrc)
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def utf8ToCode(self, str):
        try:
            strSrc =str
            qstrTmp = strSrc
            # qstrTmp = qstrTmp.toUtf8()
            qstrTmp=qstrTmp.encode('utf-8')
            strRt = ''
            for item in qstrTmp:
                strRt+='\\x%x'%item
            # for c in qstrTmp:
            #     strRt += hex(ord(c)) + ' '

            strRt = strRt.strip()
            return strRt
        except Exception as e:
            print(e)

    def onCodeToUtf8BtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            strRt = self.codeToUtf8(strSrc)
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def utf8CodeToChinese(self,strStrs):
        bStrs=strStrs.encode('latin-1')
        uStrs=bStrs.decode('unicode_escape')
        bTrueStrs=uStrs.encode('latin-1')
        strStrs=bTrueStrs.decode('utf-8')
        return strStrs
        pass

    def codeToUtf8(self, str):
        try:
            strSrc = str
            strStrs = strSrc.replace('0x','\\x').replace(' ','')
            # strStrs=bytes(strStrs,'utf-8').decode('unicode_escape')
            strStrs=self.utf8CodeToChinese(strStrs)
            return strStrs
            # strSrc =str
            # strStrs = strSrc.replace('0x',' ').split()
            # strRt = ''
            # for c in strStrs:
            #     if not c.strip():
            #         continue
            #     a = r'\x' + c.strip().decode()
            #     strRt += a.decode('string-escape')
            # strRt = strRt.strip().decode('utf-8')
            # return strRt
        except Exception as e:
            print(e)

    def onUnicodeToCodeBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()

            strRt=self.unicodeToCode(strSrc)
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def unicodeToCode(self, strSrc):
        try:
            strRt = ''
            for c in strSrc:
                # strRt += hex(ord(c)) + ' '
                strRt += '\\u%04x'%ord(c)
            strRt = strRt.strip()
            return strRt
        except Exception as e:
            print(e)

    def onCodeToUnicodeBtnClick(self):
        try:
            strSrc=self.ui.m_textEdit.toPlainText()
            strSrc=strSrc.replace(' ','')
            strRt = self.codeToUnicode(strSrc)
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def unicodeCodeToChinese(self,strStrs):
        bStrs=strStrs.encode('latin-1')
        strRt=bStrs.decode('unicode_escape')
        return strRt
        pass

    def codeToUnicode(self, strSrc):
        try:
            strStrs = strSrc.replace('0x','\\u').replace(' ','')
            strRt = ''
            # bStrs=strStrs.encode('latin-1')
            # strRt=bStrs.decode('unicode_escape')
            strRt=self.unicodeCodeToChinese(strStrs)
            # for c in strStrs:
            #     if not c.strip():
            #         continue
            #     strTmp = r'\u' + c.strip()
            #     try:
            #         strRt += strTmp.decode('string-escape').decode('unicode-escape')
            #     except Exception as e:
            #         print(e)
            #         strTmp = strTmp.replace(r'\u', r'\x')
            #         strRt += strTmp.decode('string-escape').decode('utf-8')
        except Exception as e:
            print(e)
        return strRt

    def onShowCodesBtnClick(self):
        try:
            strUnicodeSrc=self.ui.m_textEdit.toPlainText()
            strRt=''
            for itemStr in strUnicodeSrc:
                #print('itemStr:%s:%s'%(type(itemStr),itemStr))
                #gbk codecs value
                strGb2312 = itemStr.encode('gb2312')
                #print('strGb2312:%s:%s'%(type(itemStr),itemStr))
                strGb2312Code=''
                for item in strGb2312:
                    #print('item:%s:%s'%(type(item),item))
                    strGb2312Code+=hex(item)[2:]
                    #for byte in item:
                        #strGb2312Code+=hex(ord(item))[2:]

                #utf8 codecs value
                strUtf8 = itemStr.encode('utf-8')
                strUtf8Code=''
                for item in strUtf8:
                    #print('utf8 item:%s:%s'%(type(item),item))
                    strUtf8Code+=hex(item)[2:]
                    #for byte in item:
                        #strUtf8Code+=hex(ord(item))[2:]

                #unicode codecs value
                strUnicode = itemStr
                strUnicodeCode=''
                for item in strUnicode:
                    strUnicodeCode+=hex(ord(item))[2:]
                    #for byte in item:
                        #strUnicodeCode+=hex(ord(item))[2:]

                itemStrs=itemStr+'\t'+strGb2312Code+'\t'+strUnicodeCode+'\t'+strUtf8Code+'\n'
                strRt+=itemStrs
            title=u'show'+'\t'+'gb2312'+'\t'+'unicode'+'\t'+'utf-8'+'\n'
            strRt=title+strRt
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def onUrlEncodeBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            # strUtf8=str.encode('gb2312')
            # strRt=urllib.urlencode({'name':strUtf8})
            # strRt=strRt.replace('name=','')
            strFoceUrlEncode=self.ui.m_foceUrlEncodeEdit.text()
            strRt=HtmlEntities.encode(str,strFoceUrlEncode)
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def onUrlDecodeBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            # str=urllib.unquote(str.encode('gb2312'))
            str=HtmlEntities.decode(str)
            #str=urllib.unquote(str.encode('utf-8'))
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
            print(e)
        pass

    # def urlEncode(self,strSrc):
    #     tmp=strSrc
    #     force=''
    #     len = tmp.length();
    #     i = 0;
    #     '''
    #     while( i<len ):
    #         c= QtCore.QChar(tmp[i])
    #         type(c)
    #         if( c.unicode() > 128 or force.contains(tmp[i]) ):
    #             rp = QtCore.QString("&#"+QtCore.QString.number(c.unicode())+";")
    #             tmp.replace(i,1,rp)
    #             len += rp.length()-1
    #             i += rp.length()
    #         else:
    #             i+=1
    #     '''
    #
    #
    #     return tmp
    #
    # def urlDecode(self,strSrc):
    #     ret=strSrc;
    #     re=QtCore.QRegExp("&#([0-9]+);");
    #     re.setMinimal(True);
    #
    #     pos = 0;
    #     pos = re.indexIn(strSrc, pos)
    #     while pos != -1:
    #         ret = ret.replace(re.cap(0), QtCore.QChar(re.cap(1).toInt(0,10)))
    #         pos += re.matchedLength()
    #         pos = re.indexIn(strSrc, pos)
    #     return ret;

    def onBase64EncodeBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            str=base64.b64encode(str.encode('utf-8'))
            str=str.decode('unicode_escape')
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
            print(e)
        pass

    def onBase64DecodeBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            str=base64.b64decode(str.encode('utf-8'))
            str=str.decode('unicode_escape')
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
            print(type(e))
        pass

    def onMD5EncodeBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            # str1=hashlib.md5(str.encode('gbk')).hexdigest()
            str=hashlib.md5(str.encode('utf-8')).hexdigest()
            # str=hashlib.md5(str.encode('utf-8')).hexdigest()
            # self.ui.m_textEdit.setPlainText(str.decode('utf-8'))
            self.ui.m_textEdit.setPlainText(str)
        except Exception as e:
            print(e)
        pass

    def onMD5DecodeBtnClick(self):
        try:
            asciimap={'\r':'\\r',
                      '\x1e':'\\x1e',
                      '\x00':'\\x00',
                      '\x01':'\\x01',
                      '\x02':'\\x02',
                      '\x03':'\\x03',
                      '\x04':'\\x04',
                      '\x05':'\\x05',
                      '\x06':'\\x06',
                      '\x07':'\\x07',
                      '\x08':'\\x08',
                      '\x09':'\\x09',
                      '\x0a':'\\x0a',
                      '\x0b':'\\x0b',
                      '\x0c':'\\x0c',
                      '\x0d':'\\x0d',
                      '\x0e':'\\x0e',
                      '\x0f':'\\x0f',
                      '\x10':'\\x10',
                      '\x11':'\\x11',
                      '\x12':'\\x12',
                      '\x13':'\\x13',
                      '\x14':'\\x14',
                      '\x15':'\\x15',
                      '\x16':'\\x16',
                      '\x17':'\\x17',
                      '\x18':'\\x18',
                      '\x19':'\\x19',
                      '\x1a':'\\x1a',
                      '\x1b':'\\x1b',
                      '\x1c':'\\x1c',
                      '\x1d':'\\x1d',
                      '\x1e':'\\x1e',
                      '\x1f':'\\x1f',
                      '\x7f':'\\x7f',

                      }
            str=self.ui.m_textEdit.toPlainText()
            str=hashlib.md5(str.encode('utf-8')).digest()
            tmp_str=str.decode('unicode_escape')
            strResult=''
            a=tmp_str[0]
            for i in tmp_str:
                tmpchar=''
                try:
                    # tmpchar=i.encode('ascii').decode('unicode_escape')\
                    #     .replace('\r','\\r')\
                    #     .replace('\n','\\n')\
                    #     .replace('\\','\\\\')\
                    #     .replace('\x1e','\\x1e')

                    tmpchar=i.encode('ascii').decode('unicode_escape')
                    if tmpchar in asciimap:
                        tmpchar=asciimap[tmpchar]
                    # tmpchar='%s'%i

                except Exception as e:
                    tmpchar='\\x%02x'%(ord(i))
                    # if tmpchar in asciis:
                    #     tmpchar=asciiTostr[i]
                strResult+=tmpchar
            # a=str.decode('unicode_escape')
            # b=a.encode('latin-1')
            # c=b.decode('gbk')
            self.ui.m_textEdit.setPlainText(strResult)
        except Exception as e:
            print(e)
        pass

    def onReplaceBtnClick(self):
        try:
            str=self.ui.m_textEdit.toPlainText()
            strFrom=self.ui.m_replaceFromEdit.text()
            strTo=self.ui.m_replaceToEdit.text()
            strRt=str.replace(strFrom,strTo)
            self.ui.m_textEdit.setPlainText(strRt)
        except Exception as e:
            print(e)
        pass

    def onLinkWebBtnClick(self):
        try:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('www.pamxy.com'))
        except Exception as e:
            print(e)
        pass
        
    # def onUnicodeToChineseBtnClick(self):
    #     try:
    #         # u'\u4e2d\u6587' -> 'Chinese' -> u'Chinese'
    #         str=self.ui.m_textEdit.toPlainText()
    #         str=self.unicodeCodeToChinese(str)
    #         # str=str.encode('utf-8').decode('unicode-escape')
    #         self.ui.m_textEdit.setPlainText(str)
    #         pass
    #     except Exception as e:
    #         print(e)
    #     pass
    #
    # def onUtf8ToChineseBtnClick(self):
    #     try:
    #         # u'\x4E2D;\x6587;' -> '\x4E2D;\x6587;'  -> u'Chinese'
    #         #str=self.ui.m_textEdit.toPlainText()
    #         #print('%s:%s'%(type(str),str))
    #         str=self.ui.m_textEdit.toPlainText()
    #         str=self.utf8CodeToChinese(str)
    #         # print('%s:%s'%(type(str),str))
    #         #
    #         # str=str.decode('string-escape')
    #         # #str=str.replace('\\x','\\\\x').decode('string-escape')
    #         # print('%s:%s 2'%(type(str),str))
    #         #
    #         # str=str.decode('utf-8')
    #
    #         #str=str.encode('utf-8')
    #         #print('%s:%s'%(type(str),str))
    #         #str=str.encode('raw_unicode_escape')
    #         #print('%s:%s'%(type(str),str))
    #         #str=str.decode('ascii')
    #         #print('%s:%s 1'%(type(str),str))
    #         #print(str[0])
    #         self.ui.m_textEdit.setPlainText(str)
    #         pass
    #     except Exception as e:
    #         print(e)
    #     pass
    #
    # def onGBKToChineseBtnClick(self):
    #     try:
    #         str=self.ui.m_textEdit.toPlainText()
    #         str=self.gbkCodeToChinese(str)
    #         # print('%s:%s'%(type(str),str))
    #         #
    #         # str=str.decode('string-escape')
    #         # #str=str.replace('\\x','\\\\x').decode('string-escape')
    #         # print('%s:%s 2'%(type(str),str))
    #         #
    #         # str=str.decode('gbk')
    #         self.ui.m_textEdit.setPlainText(str)
    #         pass
    #     except Exception as e:
    #         print(e)
    #     pass
        


if __name__ == '__main__':
    #print('__main__')
    app = QtGui.QApplication(sys.argv)
    QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForLocale())
    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForLocale())
    QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForLocale())
    win = MyWindow()
    win.show()
    app.exec_()
