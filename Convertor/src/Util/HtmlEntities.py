#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'liangguipeng'
import re
import datetime


class HtmlEntities(object):
    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def decode(strSrc):
        strA=strSrc
        strRegex=r'&#([0-9]+);'
        startTime=datetime.datetime.now()
        result=re.search(strRegex,strA)
        # print(result)
        count=0
        while result:
            count+=1

            strReplaceFrom=result.group(0)

            strReplaceTo=chr(int(result.group(1)))

            strA=strA.replace(strReplaceFrom,strReplaceTo)

            # result=re.search(strRegex,strA)
            matchStartInx=result.span(0)[0]
            matchEndInx=result.span(0)[1]
            # print(matchStartInx)
            # print(matchEndInx)
            # print(strA[matchEndInx:])
            # a=strA[matchStartInx:]

            # result=re.search(strRegex,strA[matchEndInx:])
            result=re.search(strRegex,strA[matchStartInx:])

        strA=strA.replace('\r','\r\n')

        # endTime=datetime.datetime.now()
        # print(strA)
        # print('Count:%s'%count)
        # print(endTime-startTime)
        endTime=datetime.datetime.now()
        print('decode Time:%s'%(endTime-startTime))
        return strA

        # resultList=[]
        # if result is None:
        #     ret=strA
        # while result:
        #     count+=1
        #     strReplaceFrom=result.group(0)
        #     strReplaceTo=unichr(int(result.group(1)))
        #
        #     matchStartInx=result.span(0)[0]
        #     matchEndInx=result.span(0)[1]
        #     match2StartInx=result.span(1)[0]
        #     match2EndInx=result.span(1)[1]
        #
        #     # strA=strA[:match2StartInx]+strReplaceTo+strA[match2EndInx:]
        #     resultList.append(strA[:matchStartInx]+strReplaceTo)
        #     strA=strA[matchEndInx:]
        #
        #     result=re.search(strRegex,strA)
        #     if result is None:
        #         resultList.append(strA)
        #
        # # print(''.join(resultList))
        # ret=''.join(resultList)
        # endTime=datetime.datetime.now()
        # print('decode Time:%s'%(endTime-startTime))
        # return ret

    @staticmethod
    def encode(strSrc,strForce=''):
        # strB=strSrc
        unicodeStr=strSrc
        # unicodeStr=strB.decode('utf-8')
        # print('strB len:%s'%len(strB))
        # print('unicodeStr len:%s'%len(unicodeStr))

        pos=0
        srclen=len(unicodeStr)

        while pos<srclen:

            strUniChar=unicodeStr[pos]

            nUniCharValue=ord(strUniChar)

            if nUniCharValue >128 or strUniChar in strForce:

                strEntityChar=u'&#%s;'%(nUniCharValue)

                nEntityCharLen=len(strEntityChar)

                unicodeStr=unicodeStr[:pos]+strEntityChar+unicodeStr[pos+1:]

                srclen=srclen-1+nEntityCharLen

                pos+=nEntityCharLen
            else:
                pos+=1
        # print(unicodeStr)
        return unicodeStr


if __name__ == '__main__':

    # result=HtmlEntities.encode(strA)
    # print(result)
    #
    # result=HtmlEntities.decode(result)
    # print(result)

    strB="abc123"

    forceResult=HtmlEntities.encode(strB,'a')
    print(forceResult)

    forceResult=HtmlEntities.decode(forceResult)
    print(forceResult)


    pass
