import time
from urllib import request
import requests
import re


def getWebimage(weburl,image_pattern="jpg"):
    """
    用于下载指定web页面的图片
    :param weburl: web页面对应的url
    :param image_pattern: 所要下载的图片的类型，默认为jpg图片
    :return:
    """

    # 设置匹配图片地址的表达式
    reimg = r'https://\S*?\.%s' % image_pattern
    img_re = re.compile(reimg)

    # 读取指定的web页面内容
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    url = request.Request(url=weburl,headers=headers)
    html = request.urlopen(url)
    s = str(html.read())

    # 生成web页面中所有图片的地址列表
    img_list = img_re.findall(s)

    # 如果列表不为空，则进行下载
    if img_list:
        # 图片命名中加入时间
        now = time.strftime("%Y%m%d%H%M%S")
        # 图片序号
        index = 1
        # 下载失败的图片数量
        fail_count = 0
        # 对图片列表中的图片逐一下载
        for img in img_list:
            print("正在下载第%s个,共%s个..." % (index,len(img_list)))
            try:
                request.urlretrieve(img,r"C:\Users\Administrator\Desktop\img\{0}-{1}.{2}".format(now,index,image_pattern))
                success = True
            except Exception:
                print("第%s个图片下载失败" % index)
                success = False
                index += 1
                fail_count += 1
                # 对于下载失败的，尝试用另一种方式重新下载
                if not success:
                    print("重新尝试下载...")
                    res = requests.get(img)
                    with open(r"C:\Users\Administrator\Desktop\img\{0}-{1}.{2}".format(now,(index-1),image_pattern), "wb") as f:
                        f.write(res.content)
                    print("下载成功...")
                    fail_count -= 1
                continue

            index += 1
        print("下载失败：%s" % fail_count)

    else:
        print("此url界面无%s图片！" % image_pattern)



if __name__ =="__main__":
    getWebimage("https://zhidao.baidu.com/question/1447655141570242420.html")
