client=[["ClientID","Sex","Selling","Class"],
        ["m1","Erkek", "Düşük", "A"],
        ["m2" ,"Kadın", "Yüksek", "A"],
        ["m3" ,"Erkek", "Yüksek", "B"],
        ["m4","Erkek", "Normal", "A"],
        ["m5","Kadın", "Düşük", "B"]]


def tseperate():

    global t
    t={}
    liste=[]
    for i in range(len(client)-1):
        for j in range(len(client[i])):
            try:
                liste.append(client[j+1][i])
                t[client[0][i]] = [liste[x:x+len(client)-2] for x in range(0, len(liste), len(client)-2)][i]
                
            except:
                pass
    return t

#Input string without whitespace For example Sex=Erkek
def Psol(x):
    global a
    global b
    a,b =x.split("=")
    return t[a].count(b)/(len(client)-1)

#Input string without whitespace For example Class=A
def Pxsol(y):
    m,n=y.split("=")
    count=0
    for i in range(len(t[a])):
        if t[a][i] == b and t["Class"][i]==n:
            count+=1
    return count/ t[a].count(b)        
            
def main():
    tseperate()
    Psol("Sex=Erkek")
    print(Pxsol(y="Class=A"))     


if __name__ == "__main__":
    main()