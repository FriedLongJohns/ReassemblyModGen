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

core=hp.Block(
    ["COMMAND"],
    [("command={}"),("sort=1")],
    extends=hp.randitem(bases),
    extras=kblockSettings["features"]["COMMAND"]["extras"],
)
core.actualize()
print("\n>> generated core with features "+"|".join(core.features))
hp.blocks.append(core)

count=0
for shape in bpal["hull"]:
    for s in range(bscales[0],bscales[1]+1):
        for b in bases:
            hp.blocks.append(hp.Block([],[("shape="+shape),("scale="+str(s)),("name=\"hull\""),("sort=2")],extends=b))
            count+=1
            #it feels wrong this is all the code needed to do this
            #but that's just because of all the library work happening here
print("\n>> finished hull generation with "+str(count)+" blocks")

thrust_scale_mult = hp.randfloat(.9,1.2)
thrust_shape=hp.randitem(["THRUSTER","THRUSTER_PENT","DISH_THRUSTER","THRUSTER_RECT"])
thrusterForce=hp.randfloat(7000,15000)
extend=hp.randitem(bases)
print("\n>> generating thrusters")
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

count=[]
for i in range(wcount):
    kind=hp.randitem(["LASER","CANNON","LAUNCHER"])
    data=kblockSettings["features"][kind]

    blonk=hp.Block(
        [kind],
        data["args"]+[("sort=5")],
        extras=data["extras"],
        children=[data["child"]],
        extends=hp.randitem(bases),
    )
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

print("\n>> finished weapon generation with "+str(len(count))+" weapons!")
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
