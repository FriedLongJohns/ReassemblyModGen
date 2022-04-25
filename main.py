import helpers as hp
from config import *

bases=hp.genBases()

bpal=hp.randitem(kblockPals)
print("\nSELECTED PALETTE")
[print("\t"+key+": "+str(bpal[key])) for key in bpal.keys()]

bscales=hp.randitem(kblockSettings["scale bounds"])
wcount=hp.randitem(kblockSettings["weapon count"])
ucount=hp.randitem(kblockSettings["unique count"])
print("\nBLOCK COUNTS")
print("\thull scale range: "+str(bscales))
print("\tweapon count: "+str(wcount))
print("\tunique count: "+str(bscales))

#__init__(self,features,args,extends=None,extras=[],children=[])
for shape in bpal["hull"]:
    for s in range(bscales[0],bscales[1]+1):
        for b in bases:
            hp.blocks.append(hp.Block([],[("shape="+shape),("scale="+str(s))],extends=b))
            #it feels wrong this is all the code needed to do this
            #but that's just because of all the library work happening here
input("finished hull generation")
for b in hp.blocks:
    b.actualize()
    print(b.text())
