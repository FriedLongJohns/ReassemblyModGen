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
    if lst:
        return lst[random.randint(0,len(lst)-1)]
    return None

def trykey(ky,dct,excep=None):
    if ky in dct.keys():
        return dct[ky]
    return excep

blocks=[]

class Block:
    def __init__(self,features,args,extends=None,extras=[],children=[]):
        self.extends=False
        if extends:
            self.extends=True
            self.extendBlock=extends
        self.id=len(blocks)+1
        self.args=args
        self.features=features
        self.extras=extras
        self.children=children

    def actualize(self):
        # unintentionally, you *could* recursively make a launcher with this
        # but the main point of actualize() is to finish all features and prepare the block for randomization
        if self.extras:
            for extra in self.extras:
                if randfloat(0.0,1)>extra[0]:#chance
                    self.features.append(extra[1])
                    if len(extra)!=2:
                        self.args+=extra[2]

        new_children=[]
        for child in self.children:
            blk=Block(
                trykey("features",child,excep=[]),
                child["args"],
                extends=False,
                extras=trykey("extras",child,excep=[]),
            )
            blk.actualize()
            new_child=(child["name"],blk)
            new_children.append(new_child)
        self.children=new_children



    def text(self,out="str"):#out can be str or list
        features=self.features
        args=self.args
        if self.extends:
            features+=self.extendBlock.features#append their features

            args=[]
            for i in range(len(self.args)):#and make sure not to ovverwrite their args
                ine=False
                a=self.args[i]
                for ea in self.extendBlock.args:
                    if a[0]==ea[0]:
                        ine=True
                if not ine:
                    args.append(a)

        lines=["{"]
        if features:
            lines+=["\t"+str(self.id)+",","\tfeatures="+"|".join(features)+","]#{id,feats=x|y|z,

        for arg in args:#arg=value,
            if len(arg)==3:
                lines.append("\t"+arg[0]+"="+str(randfloat(arg[1],arg[2]))+",")
            elif arg[1] in ["0x","0xff"]:
                lines.append("\t"+arg[0]+"="+arg[1]+randColor()+",")
            else:
                lines.append("\t"+arg+",")

        for child in self.children:
            lines.append("\t"+child[0]+"={\n"+"".join(["\t\t"+i+"\n" for i in child[1].text(out="list")[1:-1]])+"\n\t}")
        lines.append("}")

        if out=="str":
            return "\n".join(lines)
        return lines

# print("input: LASER features+extras+child, with baseSettings")
# print("expected block: LASER w/ chance of TURRET and/or CHARGING")
# blk=Block(["LASER"],kbaseSettings["args"],extras=kblockSettings["features"]["LASER"]["extras"],children=[kblockSettings["features"]["LASER"]["child"]])
# blk.actualize()
# print(blk.text())

def genBases(num=kbaseSettings["colors"],features=kbaseSettings["features"],args=kbaseSettings["args"]):
    global blocks
    for i in range(num):
        block=Block(features,args)
        block.actualize()
        blocks.append(block)
