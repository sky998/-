import jieba
excludes={"将军","却说","荆州","二人","不可",\
          "不能","如此","如何","军士","主公","左右",\
          "军马","商议","大喜","次日","引兵","于是","天下",\
          "东吴","不敢","今日","魏兵","一人","陛下",\
          "都督","人马","不知","汉中","只见","众将"}
txt=open("threekingdoms.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮" or word == "孔明曰":
        rword="孔明"
    elif word=="关公" or word == "云长":
        rword="关羽"
    elif word=="玄德" or word == "玄德曰":
        rword="刘备"
    elif word=="孟德" or word == "丞相":
        rword="曹操"
    elif word=="后主" or word == "刘禅":
        rword="刘禅"
    else:
        rword=word
        counts[word]=counts.get(word,0)+1

for word in excludes:
    del counts[word]

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
