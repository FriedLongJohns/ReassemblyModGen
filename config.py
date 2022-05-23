kbaseSettings = {
    "id offset": 50000,
    "features": ["PALETTE"],
    "colors": 3,
    "args": [
        ("density",.03,.1),
        ("durability",.75,4),
        # ("scale=1"),#three arguments means [0]+"="+random num (see randfloat() in helpers) between [1] and [2]
        ("fillColor","0x"),#0x signifies [0]+"="+[1]+(random hex RGB) format
        ("fillColor1","0x"),
        ("lineColor=0x000000"),#one argument (or an incorrect format) means "add this as is"
        ("group=1"),
        #("text", [a,b,c...]) or ("text", (a,b,c...)) signifies "pick one from the list"
        #line color is always black because that's how I like it.
    ]
}


kblockSettings = {
    "scale bounds": [(1,3),(3,3),(1,2),(2,4)],#only hull blocks scale
    "weapon count": [3,5,7,10,15,20],#amount of weapons to make
    "unique count": [4,10,11,12,13,14],#amount of UNIQUE 1 (or feature group) feature blocks
    "features": {#pick features from the set...
        "LASER": {#add the feature and it's arguments...
            "extras": [
                (.8,"TURRET",[("turretSpeed",.5,5)]),#and chance it's extra features + arguments (if len 3 then args, len 2 no args)
                (.1,"CHARGING",[("chargeMaxTime",1,10),("chargeMin",.2,.9)]),
                (.3,"AUTOFIRE",[]),
            ],
            "args":[],
            "child": {
                "name": "laser",
                "args": [
                    ("pulsesPerSec",0,5),
                    ("damage",-100,500),
                    ("range",100,2500),
                    ("power",1,100),
                    ("decay",0,1.2),
                    ("width",.1,3),
                    ("color","0xff"),
                ],
            },
        },
        "CANNON": {
            "extras": [
                (.8,"TURRET",[("turretSpeed",.5,5)]),
                (.1,"CHARGING",[("chargeMaxTime",1,10),("chargeMin",.2,.9)]),
                (.3,"AUTOFIRE",[]),
            ],
            "args":[],
            "child": {
                "name": "cannon",
                "args": [
                    ("roundsPerSec",.1,50),
                    ("damage",5,500),
                    ("range",100,2500),
                    ("power",1,100),
                    ("muzzleVel",500,2400),
                    ("recoil",0.0,3),
                    ("burstyness",0.0,1),
                    ("spread",0.0,1.4),
                    ("color","0xff")
                ]
            },
        },
        "LAUNCHER": {
            "extras": [
                (.1,"LAUNCHER_BARRAGE"),
            ],
            "args":[
                ("replicateTime",.1,10),
                ("launcherPower",50,200),
                ("launcherOutSpeed",-500,1500),
            ],
            "child": {
                "name": "replicateBlock",
                "features": ["COMMAND","EXPLODE"],
                "extras": [
                    (.9,"THRUSTER",[("thrusterForce",400,2000)]),
                    (.9,"TORQUER",[("torquerTorque",200,750)]),
                    (.1,"FIN",[("finForce",5,20)]),
                ],
                "args": [
                    ("density",.01,.01),
                    ("durability",.05,.1),
                    ("scale",1,2),
                    ("explodeRadius",10,80),
                    ("explodeDamage",30,400),
                    ("lifetime",1,9),
                    ("fillColor","0x"),
                    ("fillColor1","0x"),
                    ("lineColor=0x000000"),
                    ("shape",("MISSILE","DISH_MISSILE","ISOTRI_25_MISSILE","ISOTRI_13_MISSILE","SQUARE_MISSILE","COMMAND_MISSILE"))
                ]
            },
        },

        "SHIELD":{
            "args":[],
            "child": {
                "name": "shield",
                "args": [
                    ("strength",100,1000),
                    ("regen",10,500),
                    ("delay",.5,3),
                    ("radius",20,250),
                    ("power",.5,1.5),
                    ("color","0x"),
                    ("damagedColor","0x"),
                    ("lineColor","0x"),
                ]
            },
        },

        "THRUSTER": {
            "extras": [(.1,"ACTIVATE",[("activatePower",1,100)])],
            "args": [
                ("thrusterForce",10000,50000),
                ("thrusterColor","0x"),
                ("thrusterColor1","0x"),
            ]
        },

        "COMMAND": {
            "extras": [
                (1,"GENERATOR",[("generatorCapacityPerSec",100,1000),("powerCapacity",100,1500)]),
                (1,"REGROWER",[]),
                (.5,"ASSEMBLER",[]),
                (.2,"TORQUER",[("torquerTorque",100,5000)]),
                (.2,"TELEPORTER",[("teleporterRadius",100,1000),("teleporterPower",0.0,2)]),
            ],
            "args":[],
        },

        #short ones after here
        "TRACTOR":{"args":[("tractorRadius",100,1200)]},
        "FIN":{"args":[("finForce",5,20)]},
        "EXPLODE":{"args":[("explodeDamage",10,500),("explodeRadius",10,100)]},
        "GENERATOR":{"args":[("generatorCapacityPerSec",10,500),("powerCapacity",50,1500)]},
        "TELEPORTER":{"args":[("teleporterRadius",100,1000),("teleporterPower",0.0,2)]},
        "TORQUER":{"args":[("torquerTorque",100,500)]},
        "MELEE":{"args":[("meleeDamage",.75,5)]},

        #no-args after here
        "FACTORY":{"args":[]},
    }

}

kblockPals = [
    {
        "hull": ["SQUARE","RECT","RIGHT_TRI","RIGHT_TRI2R","RIGHT_TRI2L","ADAPTER"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER"],
        "spinals": ["CANNON","CANNON2","RECT"],
        "turrets": ["SQUARE","OCTAGON","RIGHT_TRI"],
    },
    {
        "hull": ["SQUARE","RIGHT_TRI","RIGHT_TRI2R","RIGHT_TRI2L"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER"],
        "spinals": ["CANNON","CANNON2"],
        "turrets": ["SQUARE","OCTAGON","RIGHT_TRI","RIGHT_TRI2R","RIGHT_TRI2L"],
    },
    {
        "hull": ["HEXAGON","TRI"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER","GEM_3_LAUNCHER","GEM_4_LAUNCHER"],
        "spinals": ["HEXAGON","TRI"],
        "turrets": ["HEXAGON","TRI"],
    },
    {
        "hull": ["PENTAGON","RHOMBUS_36_144","RHOMBUS_72_108"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER","GEM_3_LAUNCHER","GEM_4_LAUNCHER"],
        "spinals": ["RHOMBUS_36_144","RHOMBUS_72_108"],
        "turrets": ["PENTAGON","RHOMBUS_72_108"],
    },
    {
        "hull": ["GEM_2","GEM_3","GEM_4","ISOTRI_36","ISOTRI_72"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER","GEM_3_LAUNCHER","GEM_4_LAUNCHER","HEPTAGON_LAUNCHER"],
        "spinals": ["CANNON","CANNON2","GEM_2"],
        "turrets": ["OCTAGON","HEPTAGON","GEM_4","GEM_3"],
    },
    {
        "hull": ["TRI","HEXAGON","RHOMBUS_72_108","RHOMBUS_36_144","ISOTRI_80","ISOTRI_72","ISOTRI_36","ISOTRI_25","ISOTRI_13","ISOTRI_6","ISOTRI_3"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER","GEM_3_LAUNCHER","GEM_4_LAUNCHER"],
        "spinals": ["RHOMBUS_36_144","RHOMBUS_72_108","TRI","HEXAGON"],
        "turrets": ["PENTAGON","RHOMBUS_72_108","HEXAGON","TRI"],
    },
    {
        "hull": ["ISOTRI_80","ISOTRI_72","ISOTRI_36","ISOTRI_25","ISOTRI_13","ISOTRI_6","ISOTRI_3"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER","GEM_3_LAUNCHER","GEM_4_LAUNCHER","HEPTAGON_LAUNCHER"],
        "spinals": ["ISOTRI_36","ISOTRI_25","ISOTRI_13"],
        "turrets": ["PENTAGON","TRI","HEPTAGON"],
    },
]
