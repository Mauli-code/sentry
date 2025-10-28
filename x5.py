a,b,c,d=map(int,input().split())
if a<b<c<d or d<a<c<b or b<d<c<a or a<d<c<b or d<b<c<a or b<a<c<d:
    print("Gaurav")
elif a<c<b<d or a<d<b<c or c<a<b<d or c<d<b<a or d<a<b<c or d<c<b<a:
    print("Anuj")
elif a<c<d<b or a<b<d<c or b<c<d<a or b<a<d<c or c<b<d<a or c<a<d<b:
    print("Ramandeep")
else:
    print("Anubhav")
