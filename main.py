import helpers as hp
from config import *
from time import time as ttime

bases=hp.genBases()
bpal=hp.randitem(kblockPals)

print("\nSELECTED PALETTE")
[print("\t"+key+": "+str(bpal[key])) for key in bpal.keys()]

bscales=hp.randitem(kblockSettings["scale bounds"])
wcount=hp.randitem(kblockSettings["weapon count"])
ucount=hp.randitem(kblockSettings["unique count"])
print("\nBLOCK DATA")
print("\thull scale range: "+str(bscales))
print("\tweapon count: "+str(wcount))
print("\tunique count: "+str(ucount))

#__init__(self,features,args,extends=None,extras=[],children=[])

print("\nBLOCK GENERATION STARTED")
count=0
for shape in bpal["hull"]:
    for s in range(bscales[0],bscales[1]+1):
        for b in bases:
            hp.blocks.append(hp.Block([],[("shape="+shape),("scale="+str(s)),("name=\"hull\"")],extends=b))
            count+=1
            #it feels wrong this is all the code needed to do this
            #but that's just because of all the library work happening here
print("\n>>finished hull generation with "+str(count)+" blocks")

count=[]
for i in range(wcount):
    kind=hp.randitem(["LASER","CANNON","LAUNCHER"])
    data=kblockSettings["features"][kind]

    blonk=hp.Block(
        [kind],
        data["args"],
        extras=data["extras"],
        children=[data["child"]],
        extends=hp.randitem(bases),
    )
    blonk.actualize()#have to actualize to do shape
    count.append(kind)

    if kind=="LAUNCHER":
        blonk.args.append(("shape",bpal["launchers"]))
        blonk.args.append(("name=\"launcher\""))
    elif not "TURRET" in blonk.args:
        blonk.args.append(("shape",bpal["spinals"]))
        blonk.args.append(("name=\"spinal weapon\""))
        count[-1]+=" (spinal)"
    else:
        blonk.args.append(("shape",bpal["turrets"]))
        blonk.args.append(("name=\"turreted weapon\""))
        count[-1]+=" (turreted)"

    hp.blocks.append(blonk)

print("\n>>finished weapon generation with "+str(len(count))+" weapons!")
print(">> "+", ".join(count))

out=input("\ndump data to file?(y/n) ")
if out=="y":
    data=""
    for b in hp.blocks:
        if not b.actualized:
            b.actualize()
        data+=b.text()

    gen_hash = hash(ttime())
    name="["+str(gen_hash)+"] blocks.lua"
    with open(name,"x") as file:
        file.write(data)
    print("dumped block data to "+name)
