import helpers as hp
from config import *
from time import time as ttime
from random import randint
import os
off=[]
from time import sleep

print("Generating 100 Randomized mods...")
sleep(3)

for i in range(100):
    kbaseSettings["id offset"]=randint(40000,50000)
    print(">>chosen id offset: "+str(kbaseSettings["id offset"]))
    off.append(kbaseSettings["id offset"])

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

    core=hp.Block(
        ["COMMAND"],
        [("command={}"),("sort=1")],
        extends=hp.randitem(bases),
        extras=kblockSettings["features"]["COMMAND"]["extras"],
    )
    core.actualize()
    print(">> generated core with features "+"|".join(core.features))
    hp.blocks.append(core)

    count=0
    for shape in bpal["hull"]:
        for s in range(bscales[0],bscales[1]+1):
            for b in bases:
                hp.blocks.append(hp.Block([],[("shape="+shape),("scale="+str(s)),("name=\"hull\""),("sort=2")],extends=b))
                count+=1
                #it feels wrong this is all the code needed to do this
                #but that's just because of all the library work happening here
    print("\n finished hull generation with "+str(count)+" blocks!")

    print("\n>> generating unique blocks")
    amount=randint(2,7)
    extend=hp.randitem(bases)
    sc=randint(bscales[0],bscales[1])
    print(">> count: "+str(amount))
    print(">> extending base id "+str(extend.id))
    print(">> scale: "+str(sc))

    shapes=[hp.randitem(bpal["hull"]) for i in range(amount)]
    print(">> shapes:\n "+"\n ".join([i for i in shapes]))

    for shape in shapes:
        fcount=randint(1,4)
        feats=[hp.randitem(list(kblockSettings["features"].keys())) for i in range(fcount)]
        print(">> generating unique: "+" ".join(feats))
        ars=[]
        exts=[]
        chd=[]
        for f in feats:
            data=kblockSettings["features"][f]
            ar=hp.trykey("args",data)
            et=hp.trykey("extras",data)
            cd=hp.trykey("child",data)
            if ar:
                ars+=ar
            if et:
                exts+=et
            if cd:
                chd.append(cd)
        hp.blocks.append(hp.Block(
            feats,
            [("shape="+shape),("scale="+str(sc)),("name=\"hull\""),("sort=10")]+ars,
            extras=exts,
            extends=extend,
            children=chd
        ))

    print("\n finished unique generation with "+str(amount)+" blocks!")

    print("\n>> generating thrusters")

    thrust_scale_mult = hp.randfloat(.9,1.2)
    thrust_shape=hp.randitem(["THRUSTER","THRUSTER_PENT","DISH_THRUSTER","THRUSTER_RECT"])
    thrusterForce=hp.randfloat(7000,15000)
    extend=hp.randitem(bases)

    print(">> INFO: each thruster's thrusterForce will be base force * scale * thrusterForce scale")
    print(">> base thrusterForce: "+str(thrusterForce))
    print(">> thrusterForce scale: "+str(thrust_scale_mult))
    print(">> thruster shape:" +str(thrust_shape))
    print(">> palette-inherited scales: "+str(bscales[0])+"-"+str(bscales[1]))
    print(">> extending from base "+str(extend.id)[-1])

    count=[]
    for scale in range(bscales[0],bscales[1]+1):
        force=int(thrusterForce*scale*thrust_scale_mult)
        count.append((scale,force))
        hp.blocks.append(hp.Block(
            ["THRUSTER"],
            [("thrusterForce="+str(force)),("sort=3")] + kblockSettings["features"]["THRUSTER"]["args"][1:],
            extends=extend,
        ))

    print("\n finished thruster generation with "+str(len(count))+" thrusters!")
    print(">> "+" | ".join(["scale: "+str(i[0])+", thrusterForce="+str(i[1]) for i in count]))

    print("\n>> generating weapon blocks")
    count=[]
    for i in range(wcount):
        kind=hp.randitem(["LASER","CANNON","LAUNCHER"])
        data=kblockSettings["features"][kind]
        blonk=hp.Block(
            [kind],
            data["args"]+[("sort=5")],
            extras=data["extras"],
            extends=hp.randitem(bases),
        )
        blonk.children.append(data["child"])
        blonk.actualize()#have to actualize to do shape
        count.append(kind)

        if "AUTOFIRE" in blonk.features:
            blonk.args[-1]=("sort=4")
            blonk.args.append(("name=\"PD\""))
            count[-1]+=" (PD)"
        elif kind=="LAUNCHER":
            blonk.args.append(("shape",bpal["launchers"]))
            blonk.args.append(("name=\"launcher\""))
        elif "TURRET" in blonk.features:
            blonk.args.append(("shape",bpal["turrets"]))
            blonk.args.append(("name=\"turreted weapon\""))
            count[-1]+=" (turreted)"
        else:
            blonk.args.append(("shape",bpal["spinals"]))
            blonk.args.append(("name=\"spinal weapon\""))
            count[-1]+=" (spinal)"

        hp.blocks.append(blonk)

    print("\n finished weapon generation with "+str(len(count))+" weapons!")
    print(">> "+", ".join(count))

    # out=input("\ndump data to file?(y/n) ")
    out="y"
    if out=="y":
        data=""
        for b in hp.blocks:
            b.actualize()
            data+=b.text()

        gen_hash = hash(ttime())
        name=gamePath+"Mods/RANDOM_"+str(gen_hash)
        os.system("mkdir \""+name+"\"")
        name+="/blocks.lua"
        with open(name,"w") as file:
            file.write("{\n"+data+"\n}")
        print("dumped block data to "+name)
print(";".join(["palette "+str(i) for i in off]))
