from random import randint
from config import *

def boundName(num, bounds=[("1 zeros",0,100),("2 zeros",100,1000),("3 zeros",1000,10000)]):
    for bound in bounds:
        if bound[0]<=num<bound[1]:
            return bound[2]
    return False

def boundNum(name, bounds=[("1 zeros",0,100),("2 zeros",100,1000),("3 zeros",1000,10000)]):
    for bound in bounds:
        if bound[2]==name:
            return randint(bound[0],bound[1])
    return False

def randColor(min=(0,0,0),max=(255,255,255)):
    out=""
    for val in [hex(randint(min[i],max[i])) for i in range(3)]:
        out+=val[2:]
        if len(val[2:])<2:
            out+="0"
    return out

def randfloat(mn,mx):
    if type(mn)==type(mx)==int:
        return randint(mn,mx)

    decimals=max(len(str(mn))-2,len(str(mx))-2)
    return randint(mn*(10**decimals),mx*(10**decimals))/(10**decimals)

def randitem(lst):
    return lst[random.randint(0,len(lst)-1)]

blocks=[]

class Block:
    def __init__(self,color,features,args,shape,extends=True):
        if extends:
            self.extends=True
            self.extendBlock=random.randint(1,kbaseSettings["colors"])
        self.id=len(blocks)
        self.colors=[color,color,"000000"]
        self.args=args+["shape="+shape+","]
        self.features=features
        self.extras=[]
        self.children=[]

    def actualize(self):
        for extra in self.extras:
            if randfloat(0.0,1)>extra[0]:#chance
                self.features+=extra[1]
                if len(extra)!=2:
                    self.args+=extra[2]

        new_children=[]
        for child in children:
            new_child=(child["name"],
                Block(
                    "ff0000",
                    child["features"],
                    randitem(child["shape"]),
                    #..?
                ).actualize()
            )



    def __str__(self):
        return "\n".join([str(i) for i in "{"+self.id+self.features+"}"])

def genBases(num=kbaseSettings["colors"],features=kbaseSettings["features"],args=kbaseSettings["args"]):
    blocks=[]
    for i in range(num):
        block=""
