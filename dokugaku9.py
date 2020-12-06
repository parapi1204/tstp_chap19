import os,csv
#9-2
#with open("answer.txt","w",encoding="utf-8") as f:
#    f.write(input("あなたの好きな色を教えてください："))

#9-3
list1 = ["Top Gun","Risky Business","Minority Report"]
list2 = ["Titanic","Tge Revenant","INception"]
list3 = ["Training Day","Man on Fire","Flight"]

list4 = []

list4.append(list1)
list4.append(list2)
list4.append(list3)

with open("movie.csv","w",encoding="utf-8") as f:
    for i in list4:
        w = csv.writer(f,delimiter=",")
        w.writerow(i)
       
#9-4
list1 = ["賢者の石","秘密の部屋","アズカバンの囚人"]
list2 = ["炎のゴブレット","不死鳥の騎士団","謎のプリンス"]
list3 = ["死の秘宝","王の帰還","二つの塔"]

list4 = []

list4.append(list1)
list4.append(list2)
list4.append(list3)

with open("movie.csv","w",encoding="utf-8") as f:
    for i in list4:
        w = csv.writer(f,delimiter=",")
        w.writerow(i)
