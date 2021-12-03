aoc_crus_du_beaujolais = ["EMILE", "EMMANUEL", "PHENIX", "AMIRAL MOORSON", "SPRING", "LA FELICITE", "BATEAU PECHEUR", "SPECULART", "CREVETTIER", "CATHERINA CRISTINA"]

x=aoc_crus_du_beaujolais

aoc_beaujolais = ["PRIDE OF THE GANGE", "TROIS-MATS ALLEMAND"]

y=aoc_beaujolais

def test2(x, y):

    l1=len(x)
    l2=len(y)
    l=l1+l2
    res=[None] * l
    k=0
    for k in range(l):
        res[k]='test'
    
    i=0
    while i<l1:
        res[i]=x[i]
        i=i+1
    i=l1
    j=0
    while j<l2:
        res[i]=y[j]
        i=i+1
        j=j+1
    
    return res

a=test2(x,y)
print(a)