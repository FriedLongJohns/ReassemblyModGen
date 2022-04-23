kbaseSettings = {
    "features": "PALETTE",
    "colors": 3,
    "args": [
        ("density",.03,.1),
        ("durability",.75,4),
        ("scale",1,3),
    ]
}


kblockSettings = {
    "scale bounds": [(1,3),(3,3),(1,2),(2,4)],#only hull blocks scale
    "weapon bounds": [(3,7),(5,10),(10,20)],
    "feature groups": [
        #block features: baseSettings[features] + (1 random feature OR 1 random featureGroup)
        #ones that can be added without block change, put as element 0, else put in list
        ("ACTIVATE",["THRUSTER"]),
        ("ACTIVATE",["CANNON"]),
    ],

    "features": {#pick features from the set...
        "LASER": {#add the feature and it's arguments...
            "extras": [
                (.8,"TURRET",[("turretSpeed",.5,5)]),#and chance it's extra features + arguments (if len 3 then args, len 2 no args)
                (.1,"CHARGING",[("chargeMaxTime",1,10),("chargeMin",.2,.9)]),
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
                ],
            },
        },
        "CANNON": {
            "extras": [
                (.8,"TURRET",[("turretSpeed",.5,5)]),
                (.1,"CHARGING",[("chargeMaxTime",1,10),("chargeMin",.2,.9)]),
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
                ]
            },
        },
        "LAUNCHER": {
            "extras": [
                (.1,"LAUNCHER_BARRAGE"),
            ],
            "args":[
                ("replicateTime",.1,10),
                ("replicatePower",50,700),
                ("launcherOutForce",0,500),
            ],
            "child": {
                "name": "replicateBlock",
                "features": "COMMAND|EXPLOSIVE",
                "shape": ("MISSILE","DISH_MISSILE","ISOTRI_25_MISSILE","ISOTRI_13_MISSILE","SQUARE_MISSILE","COMMAND_MISSILE"),
                "extras": [
                    (.9,"THRUSTER",[("thrusterForce",1000,5000)]),
                    (.9,"TORQUER",[("torquerTorque",10,100)]),
                    (.1,"FIN",[("finForce",5,20)]),
                ],
                "args": [
                    ("density",.001,.01),
                    ("durability",.05,.1),
                    ("scale",1,2),
                    ("explodeRadius",10,80),
                    ("explodeDamage",30,400),
                ]
            },
        },
        "THRUSTER": {
            "extras": [(.1,"ACTIVATE",[("activatePower",1,100)])],
            "shape": ("DISH_THRUSTER","THRUSTER","THRUSTER_PENT","THRUSTER_RECT"),
            "args": [
                (.9,"THRUSTER",[("thrusterForce",10000,50000)]),
            ]
        },
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
        "hull": ["TRI","HEXAGON","RHOMBUS_72_108","RHOMBUS_36_144","ISTOTRI_80","ISTOTRI_72","ISTOTRI_36","ISTOTRI_25","ISTOTRI_13","ISTOTRI_6","ISTOTRI_3"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER","GEM_3_LAUNCHER","GEM_4_LAUNCHER"],
        "spinals": ["RHOMBUS_36_144","RHOMBUS_72_108","TRI","HEXAGON"],
        "turrets": ["PENTAGON","RHOMBUS_72_108","HEXAGON","TRI"],
    },
    {
        "hull": ["ISTOTRI_80","ISTOTRI_72","ISTOTRI_36","ISTOTRI_25","ISTOTRI_13","ISTOTRI_6","ISTOTRI_3"],
        "launchers": ["RECT_LAUNCHER1","RECT_LAUNCHER","GEM_3_LAUNCHER","GEM_4_LAUNCHER","HEPTAGON_LAUNCHER"],
        "spinals": ["ISTOTRI_36","ISTOTRI_25","ISTOTRI_13"],
        "turrets": ["PENTAGON","TRI","HEPTAGON"],
    },
]
