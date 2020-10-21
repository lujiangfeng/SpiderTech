# 淘宝的搜索接口
# 翻页
import re
import requests


def getHTMLText(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    cookies ={
        'cookies':'thw=cn; miid=1411732543336672353; cna=RUPJFch5fyUCASvjizeWpN9r; tracknick=%5Cu950B%5Cu4E4B%5Cu6C5F; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; t=288daaea9c4908a9e790c6380ec28b46; enc=uUmTe81eQtW1EhQUAwBuoreZVtLoFEUbniTVqWvaPPWaJBISY%2FmVfxc5ZjCHfRfSEjlM4fzWpdF24PYHckXkIw%3D%3D; v=0; cookie2=199a9ad37ca1682ea65ce0276eddad02; _tb_token_=eeb7b8333e534; _samesite_flag_=true; tfstk=c4hfBONUlijjoqcVacTzQ-LACLNOZo57r_qrlYb_goxhJy0fif1UAdVTlg18pz1..; sgcookie=EOzVwG4mlUlOwyUH4mk0X; unb=2264177646; uc3=vt3=F8dBxGZvs3sr28D8wyE%3D&lg2=URm48syIIVrSKA%3D%3D&nk2=1CGIEumj&id2=UUpnjMGYg6YcUA%3D%3D; csg=3c72cb4f; lgc=%5Cu950B%5Cu4E4B%5Cu6C5F; cookie17=UUpnjMGYg6YcUA%3D%3D; dnk=%5Cu950B%5Cu4E4B%5Cu6C5F; skt=71eb48a3efa43224; existShop=MTU4OTk3NjQ4MA%3D%3D; uc4=nk4=0%401vCZh6ZZVGTGPGHliY4gDIk%3D&id4=0%40U2gtHRBqBrUk12NpKOlfimjkIrHa; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%B1%9F66; _nk_=%5Cu950B%5Cu4E4B%5Cu6C5F; cookie1=AimRdWfl5HUfKXjEqcYXnzkOYjX5POKfsZDAEM6yNgk%3D; mt=ci=3_1; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie14=UoTUM2nV0npaxA%3D%3D&existShop=false&pas=0&cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D; isg=BGFhXEVEm_VPtjQGZqAGaBFpcC17DtUAAHIxnsM2XWjHKoH8C17l0I9ojF6s-W04; l=eBTXYNUgqYGq-r4EBOfanurza77OSIRYYuPzaNbMiOCPOR5B5Pl5WZAWVfT6C3GVh6b9R354uljBBeYBqQAonxv92j-la_kmn'
    }
    try:
        r = requests.get(url, timeout=30,headers=headers,cookies=cookies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
        # print(r.text)
    except:
        return ""

# 正则
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)  # *? 最小匹配

        for i in range(len(plt)):  # findall plt --- len(plt)
            price = eval(plt[i].split(':')[1])  # eval 去双引号
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])

    except:
        print("")

# 打印
def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

#
if __name__ == '__main__':

    infoList = []
    goods = '书包'
    start_url = 'https://s.taobao.com/search?q=' + goods
    depth = 2
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)


