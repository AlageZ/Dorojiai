import pyxel
import math
import random
from webbrowser import open as openw
from urllib.parse import quote_plus
SCENE_TITLE = 0
SCENE_TITLE_TO_GAME = 1
SCENE_GAME = 100
SCENE_GAMEOVER = 42
SCENE_GAME_TO_GAMEOVER = 41
ATARIHANTEIMODE = False
ATARIHANTEIMODE_NEARSTRONG = False
INDS_TO_DEG_DICT = {
    "0,-1": 0,
    "1,-1": 45,
    "1,0": 90,
    "1,1": 135,
    "0,1": 180,
    "-1,1": 225,
    "-1,0": 270,
    "-1,-1": 315
}
EQUIP_Q_DICT = {
    "Pick":[205,29],
    "Axe":[16,112],
    "None":[16,160]
}
EQUIP_V_DICT = {
    "Pick":[0,77],
    "Axe":[0,77],
    "None":[0,118]
}
DEG_TO_INDS_DICT = {
    0:[0,-1],
    45:[1,-1],
    90:[1,0],
    135:[1,1],
    180:[0,1],
    225:[-1,1],
    270:[-1,0],
    315:[-1,-1]
}
SSSERT = math.sqrt(0.5)
DEG_TO_FORMATED_INDS_DICT = {
    0:[0,-1],
    45:[SSSERT,-SSSERT],
    90:[1,0],
    135:[SSSERT,SSSERT],
    180:[0,1],
    225:[-SSSERT,SSSERT],
    270:[-1,0],
    315:[-SSSERT,-SSSERT]
}
DEG_TO_SORT_DICT = {
    0:["RightArm","LeftArm","Body","RightLeg","LeftLeg"],
    45:["LeftArm","LeftLeg","Body","RightArm","RightLeg"],
    90:["LeftArm","LeftLeg","Body","RightArm","RightLeg"],
    135:["LeftLeg","LeftArm","Body","RightLeg","RightArm"],
    180:["LeftLeg","RightLeg","Body","LeftArm","RightArm"],
    225:["RightLeg","RightArm","Body","LeftLeg","LeftArm"],
    270:["RightArm","RightLeg","Body","LeftArm","LeftLeg"],
    315: ["RightArm", "RightLeg", "Body", "LeftArm", "LeftLeg"]
}

SUNRAKU_MODE_AND_DEG_TO_SORT_DICT = {
    "None":{
        0:["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],
        45:["Pick", "Arm","Body","RightLeg","LeftLeg","Head"],
        90: ["Body", "RightLeg", "LeftLeg", "Head", "Pick", "Arm"],
        135:["Pick","Arm","RightLeg","LeftLeg","Body","Head"],
        180:["Pick", "Arm", "Body", "RightLeg", "LeftLeg", "Head"], 
        225:["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"], 
        270:["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"], 
        315:["Pick", "Arm","Body", "RightLeg", "LeftLeg", "Head"], 
    },
    "Pick":{
        0:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#2
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
        45:[ #とりあえず0からコピペ
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#2
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
        90:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Pick", "Arm"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Pick", "Arm"],#2
            ["Pick","Arm", "Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Pick","Arm", "Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Pick","Arm", "Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
        135:[
            ["Pick","Arm","RightLeg","LeftLeg","Body","Head"],#1
            ["Pick","Arm","RightLeg","LeftLeg","Body","Head"],#2
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 3
            ["Head", "Arm","Body", "RightLeg", "LeftLeg",  "Pick"],#4
            ["Body", "RightLeg", "LeftLeg",  "Arm", "Head", "Pick"],  # 5
        ],
        180:[
            ["Pick", "Arm", "Body", "RightLeg", "LeftLeg", "Head"],  # 1
            ["Pick", "Arm", "Body", "RightLeg", "LeftLeg", "Head"],  # 2
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#3
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#4
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#5
        ],
        225:[
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 1
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 2
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 3
            ["Head", "Arm", "Body", "RightLeg", "LeftLeg",  "Pick"],  # 4
            ["Body", "RightLeg", "LeftLeg",  "Arm", "Head", "Pick"],  # 5
        ],
        270:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],  # 1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],  # 2
            ["Arm", "Pick", "Body", "RightLeg", "LeftLeg",  "Head"],  # 3
            ["Arm", "Pick", "Body", "RightLeg", "LeftLeg",  "Head"],  # 4
            ["Arm", "Pick", "Body", "RightLeg", "LeftLeg",  "Head"],  # 5
        ],
        315:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#2
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
    },
    
    "NagePick":{
        0:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#2
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
        45:[ #とりあえず0からコピペ
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#2
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
        90:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Pick", "Arm"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Pick", "Arm"],#2
            ["Pick","Arm", "Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Pick","Arm", "Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Pick","Arm", "Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
        135:[
            ["Pick","Arm","RightLeg","LeftLeg","Body","Head"],#1
            ["Pick","Arm","RightLeg","LeftLeg","Body","Head"],#2
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 3
            ["Head", "Arm","Body", "RightLeg", "LeftLeg",  "Pick"],#4
            ["Body", "RightLeg", "LeftLeg",  "Arm", "Head", "Pick"],  # 5
        ],
        180:[
            ["Pick", "Arm", "Body", "RightLeg", "LeftLeg", "Head"],  # 1
            ["Pick", "Arm", "Body", "RightLeg", "LeftLeg", "Head"],  # 2
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#3
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#4
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#5
        ],
        225:[
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 1
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 2
            ["Pick", "Arm", "RightLeg", "LeftLeg", "Body", "Head"],  # 3
            ["Head", "Arm", "Body", "RightLeg", "LeftLeg",  "Pick"],  # 4
            ["Body", "RightLeg", "LeftLeg",  "Arm", "Head", "Pick"],  # 5
        ],
        270:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],  # 1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],  # 2
            ["Arm", "Pick", "Body", "RightLeg", "LeftLeg",  "Head"],  # 3
            ["Arm", "Pick", "Body", "RightLeg", "LeftLeg",  "Head"],  # 4
            ["Arm", "Pick", "Body", "RightLeg", "LeftLeg",  "Head"],  # 5
        ],
        315:[
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#1
            ["Body", "RightLeg", "LeftLeg", "Head", "Arm", "Pick"],#2
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#3
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#4
            ["Arm", "Pick","Body", "RightLeg", "LeftLeg",  "Head"],#5
        ],
    }
}

PALETTE = [
    0x000000,
    0x2B335F,
    0x7E2072,
    0x19959C,
    0x8B4852,
    0x395C98,
    0xA9C1FF,
    0xEEEEEE,
    0xD4186C,
    0xD38441,
    0xE9C35B,
    0x6b383f,
    0x7696DE,
    0xA3A3A3,
    0xFF9798,
    0xEDC7B0
]
SUNRAKU_MOTION_KEYS = {
    "Pick":[1,1,1,1,1,1,1,2,2,3,3,4,4,5,5,5,5,4,4,3,3,2,2,1,1],
    "NagePick":[1,1,1,2,2,3,3,4,4,5,5,5,5,4,4,3,3,2,2,1,1]
}
nagepick_list = []
npc_frogs_list = []
splash_list = []
splash_paints_list = []
rock_list = []
wave_list = []
collisions_list = []
stone_list = []
stone_col_list = []
attack_list = []
scoretext_list = []

class ScoreAddText:
    def __init__(self,parent,app):
        self.app = app
        self.posX = parent.posX
        self.posY = parent.posY
        self.posZ = parent.posZ+4
        self.txt = "+30"
        self.livecount = 0
    def update(self):
        self.livecount += 1
        self.posZ+=1
    def draw(self):
        pyxel.text(self.posX-self.app.scrollX-4*len(self.txt)/2,self.posY-self.app.scrollY-self.posZ-2,self.txt,7)

class Collisioner:
    def __init__(self,parent,posX,posY,posZ,sizeX,sizeY,sizeZ,deg):
        self.parent = parent
        self.posX = parent.posX+posX
        self.posY = parent.posY+posY
        self.posZ = parent.posZ+posZ
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.sizeZ = sizeZ
        self.deg = deg
        self.alive = True

class Collision:
    def __init__(self,parent):
        self.parent = parent
        self.posX = parent.posX
        self.posY = parent.posY
        self.posZ = parent.posZ
        self.sizeX = parent.sizeX
        self.sizeY = parent.sizeY
        self.sizeZ = parent.sizeZ
        self.deg = parent.deg

#https://ikatakos.com/pot/programming_algorithm/geometry/collision_judgement
#ABとCDの交差判定
def check_linecross(ab, cd):
    dax, day = ab[0] - ab[2], ab[1] - ab[3]
    dcx, dcy = cd[0] - cd[2], cd[1] - cd[3]
    ta = dcx * (ab[1] - cd[1]) + dcy * (cd[0] - ab[0])
    tb = dcx * (ab[3] - cd[1]) + dcy * (cd[0] - ab[2])
    tc = dax * (cd[1] - ab[1]) + day * (ab[0] - cd[0])
    td = dax * (cd[3] - ab[1]) + day * (ab[0] - cd[2])
    return tc * td < 0 and ta * tb < 0




def getrectbyobj(obj):
    hw = obj.sizeX/2
    hh = obj.sizeY/2
    unrot = [
        [(obj.posX-hw,obj.posY-hh),(obj.posX+hw,obj.posY-hh)],
        [(obj.posX+hw,obj.posY-hh),(obj.posX+hw,obj.posY+hh)],
        [(obj.posX+hw,obj.posY+hh),(obj.posX-hw,obj.posY+hh)],
        [(obj.posX-hw,obj.posY+hh),(obj.posX-hw,obj.posY-hh)]
    ]
    rotted = []
    for i in unrot:
        rotted.append([])
        for ii in i:
            rotted[-1].append(rotatepos(obj.posX,obj.posY,ii[0],ii[1],obj.deg))
    return rotted

def check_cyclecross(ox1,oy1,r1,ox2,oy2,r2):
    return math.sqrt(abs(ox1-ox2)**2+abs(oy1-oy2)**2) <= r1+r2

def check_objsnear(obj1,obj2):
    return check_cyclecross(obj1.posX,obj1.posY,math.sqrt(obj1.sizeX**2+obj1.sizeY**2)/2+1,obj2.posX,obj2.posY,math.sqrt(obj2.sizeX**2+obj2.sizeY**2)/2+1)

def check_objscross(obj1,obj2):
    f = False
    if check_objsnear(obj1,obj2):
        if obj1.posZ+obj1.sizeZ >= obj2.posZ >= obj1.posZ or obj2.posZ+obj2.sizeZ >= obj1.posZ >= obj2.posZ:
            # 簡易判定（汎用性持たせんのめんどくさかった）
            if obj1.deg == 0:
                if obj1.posX-obj1.sizeX/2 < obj2.posX < obj1.posX+obj1.sizeX/2 and obj1.posY-obj1.sizeY/2 <     obj2.posY < obj1.posY+obj1.sizeY/2:
                    f = True
            if obj2.deg == 0:
                if obj2.posX-obj2.sizeX/2 < obj1.posX < obj2.posX+obj2.sizeX/2 and obj2.posY-obj2.sizeY/2 <     obj1.posY < obj2.posY+obj2.sizeY/2:
                    f = True
            if not f:
                rect1 = getrectbyobj(obj1)
                rect2 = getrectbyobj(obj2)
                for l1 in rect1:
                    for l2 in rect2:
                        if check_linecross(
                            [l1[0][0],l1[0][1],l1[1][0],l1[1][1]],
                            [l2[0][0],l2[0][1],l2[1][0],l2[1][1]]
                        ):
                            f = True
                            break
                    if f:
                        break
    return f

def posgapper(main,checked):
    if len(checked) > 0:
        rect1 = getrectbyobj(main)
        tblr = [0,0,0,0]
        for o in checked:
            rect2 = getrectbyobj(o)
            c = 0
            for l1 in rect1:
                for l2 in rect2:
                    if check_linecross(
                        [l1[0][0],l1[0][1],l1[1][0],l1[1][1]],
                        [l2[0][0],l2[0][1],l2[1][0],l2[1][1]]
                    ):
                        tblr[c] = 1
                c += 1
        s = f"{tblr[1]-tblr[3]},{tblr[2]-tblr[0]}"
        if s == "0,0":
            main.posX -= 1
        else:
            d = INDS_TO_DEG_DICT[s]
            me = DEG_TO_INDS_DICT[(d+540+main.deg)%360]
            main.posX += me[0]
            main.posY += me[1]

def rotatepos(ox,oy,px,py,deg):
    x = px-ox
    y = py-oy
    theta = math.radians(deg)
    xdash = x*math.cos(theta) - y*math.sin(theta)
    ydash = x*math.sin(theta) + y*math.cos(theta)
    return (xdash+ox,ydash+oy)

def getgridpos(i):
    return math.floor((i+200)/8)

def gettileonpos(obj):
    if getgridpos(obj.posX)<0 or getgridpos(obj.posY)<0:
        return 1004
    else:
        return pyxel.tilemap(0).get(getgridpos(obj.posX),getgridpos(obj.posY))

def drawhitbox(obj,app):
    for i in getrectbyobj(obj):
        pyxel.line(i[0][0]-app.scrollX,i[0][1]-app.scrollY-obj.posZ,i[1][0]-app.scrollX,i[1][1]-app.scrollY-obj.posZ,3)
        pyxel.line(i[0][0]-app.scrollX,i[0][1]-app.scrollY-obj.posZ-obj.sizeZ,i[1][0]-app.scrollX,i[1][1]-app.scrollY-obj.posZ-obj.sizeZ,3)
        pyxel.line(i[0][0]-app.scrollX,i[0][1]-app.scrollY-obj.posZ-obj.sizeZ,i[0][0]-app.scrollX,i[0][1]-app.scrollY-obj.posZ,3)

class NagePick:
    def __init__(self,parent):
        self.parent = parent
        self.deg = parent.deg
        self.posposZ = parent.posZ+2
        self.posposX = parent.posX
        self.posposY = parent.posY
        self.sizesizeX = 2
        self.sizesizeY = 30
        self.sizesizeZ = 30
        self.rotlevel = 45
        self.speedX = DEG_TO_FORMATED_INDS_DICT[self.deg][0]*5
        self.speedY = DEG_TO_FORMATED_INDS_DICT[self.deg][1]*5
        self.moving = True
        self.posmover()
    def update(self):
        if self.moving:
            self.rotlevel += 90
            self.rotlevel %= 360
            self.posposX += self.speedX
            self.posposY += self.speedY
            self.posmover()
            f = False
            for i in rock_list:
                if check_objscross(self,i):
                    f = True
            if f:
                self.moving = False
            if not (-200-128 <= self.posX <= 200+128 and -200-128 <= self.posY <= 200+128):
                nagepick_list.remove(self)
    def draw(self):
        ww = 1
        hw = 1
        if self.rotlevel == 45:
            ww = -1
            hw = -1
        elif self.rotlevel == 135:
            ww = -1
            hw = 1
        elif self.rotlevel == 225:
            ww = 1
            hw = 1
        else:
            ww = 1
            hw = -1
        if self.moving and pyxel.frame_count %10 == 0:
            pyxel.play(3,6)
        pyxel.blt(self.posposX-15-self.parent.parent.scrollX,self.posposY-self.parent.parent.scrollY-self.posposZ-self.sizesizeZ,0,205,35,30*ww,30*hw,3)

    def posmover(self):
        posxg = DEG_TO_FORMATED_INDS_DICT[self.deg][0]*self.sizesizeY/4
        posyg = DEG_TO_FORMATED_INDS_DICT[self.deg][1]*self.sizesizeY/4
        self.sizeZ  = self.sizesizeZ/2
        self.sizeX = self.sizesizeX/2
        self.sizeY = self.sizesizeY/2
        if self.rotlevel == 45:
            self.posX = self.posposX+posxg
            self.posY = self.posposY-posyg
            self.posZ = self.posposZ+self.sizesizeZ/4*3
        elif self.rotlevel == 135:
            self.posX = self.posposX+posxg
            self.posY = self.posposY+posyg
            self.posZ = self.posposZ+self.sizesizeZ/4
        elif self.rotlevel == 225:
            self.posX = self.posposX-posxg
            self.posY = self.posposY+posyg
            self.posZ = self.posposZ+self.sizesizeZ/4
        elif self.rotlevel == 315:
            self.posX = self.posposX-posxg
            self.posY = self.posposY-posyg
            self.posZ = self.posposZ+self.sizesizeZ/4*3


class Stone:
    def __init__(self,parent):
        self.start_frame = pyxel.frame_count+0
        self.parent = parent
        self.alive = True
        rad = math.radians(random.randrange(0,180))
        self.posX = parent.posX
        self.posY = parent.posY+10
        self.posZ = parent.posZ+20
        self.speedX = math.cos(rad)*random.randrange(13, 33)*0.1
        self.speedY = math.sin(rad)*random.randrange(13, 33)*0.1
        self.speedZ = 4+random.randrange(-5,5)*0.1
        self.landgapX = 0
        self.landgapY = 0
        self.landgapZ = 0
        self.deg = 0
        self.landon = None
        self.jumping = False
    def update(self):
        self.jumping = self.landon == None
        if self.jumping:
            backX = self.posX+0
            backY = self.posY+0
            self.posX += self.speedX
            self.posY += self.speedY
            f = False
            for i in  [*collisions_list,*stone_col_list]:
                if i.parent != self.parent and i.parent != self:
                    if check_objscross(self,i):
                        f = True
            if f:
                self.posX = backX
                self.posY = backY
            f1 = False
            for i in  [*collisions_list,*stone_col_list]:
                if i.parent != self.parent and i.parent != self:
                    if check_objscross(self,i):
                        f1 = True
            backZ = self.posZ+0
            self.posZ += self.speedZ
            f2 = False
            for i in  [*collisions_list,*stone_col_list]:
                if i.parent != self.parent and i.parent != self:
                    if check_objscross(self,i):
                        f2 = True
            self.posZ = backZ
            if not f1:
                self.posZ += self.speedZ
                self.speedZ -= 1
                if f2:
                    mostland = -1
                    for i in [*collisions_list,*stone_col_list]:
                        if i.parent != self.parent and i.parent != self:
                            if check_objscross(self,i):
                                if i.posZ+i.sizeZ > mostland:
                                    mostland = i.posZ+i.sizeZ
                                    self.landon = i.parent
                    self.posZ = mostland
                    self.landgapX = self.posX-self.landon.posX
                    self.landgapY = self.posY-self.landon.posY
                    self.landgapZ = self.posZ-self.landon.posZ
            else:
                self.speedZ = 0
        else:
            self.posX = self.landon.posX+self.landgapX
            self.posY = self.landon.posY+self.landgapY
            self.posZ = self.landon.posZ+self.landgapZ
        if pyxel.frame_count - self.start_frame > 600:
            self.alive = False

class Stone1(Stone):
    def __init__(self,parent):
        super().__init__(parent)
        self.sizeZ = 9
        self.sizeX = 16
        self.sizeY = 10
        
    def draw(self):
        pyxel.blt(self.posX-8-self.parent.parent.scrollX,self.posY-5-self.parent.parent.scrollY-self.posZ,0,192,16,16,13,3)


class Stone2(Stone):
    def __init__(self,parent):
        super().__init__(parent)
        self.sizeZ = 13
        self.sizeX = 8
        self.sizeY = 8
        
    def draw(self):
        pyxel.blt(self.posX-4-self.parent.parent.scrollX,self.posY-8-self.parent.parent.scrollY-self.posZ,0,200,0,8,16,3)


class Rock1:
    def __init__(self,parent):
        self.alive = True
        self.parent = parent
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.sizeX = 80
        self.sizeY = 30
        self.sizeZ = 60
        self.deg = 0
        self.collsreload()
    def draw(self):
        pyxel.blt(
            self.posX-self.parent.scrollX-44,
            self.posY-self.parent.scrollY-self.posZ-60,
            0,168,176,88,80,3)
    def collsreload(self):
        self.colls = [
            Collisioner(self,0,0,0,80,30,15,0),
            Collisioner(self,10,0,15,50,30,15,0),
            Collisioner(self,10,0,30,30,20,15,0),
            Collisioner(self,15,0,45,20,20,15,0),
        ]

class Rock2:
    def __init__(self,parent):
        self.alive = True
        self.parent = parent
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.sizeX = 60
        self.sizeY = 20
        self.sizeZ = 50
        self.deg = 0
        self.collsreload()
    def draw(self):
        pyxel.blt(
            self.posX-self.parent.scrollX-32,
            self.posY-self.parent.scrollY-self.posZ-55,
            0,96,160,64,64,3)
    def collsreload(self):
        self.colls = [
            Collisioner(self,0,0,0,50,12,10,0),
            Collisioner(self,5,0,10,30,11,15,0),
            Collisioner(self,10,0,25,20,10,10,0),
            Collisioner(self,10,0,35,10,5,10,0),
        ]

class Rock3:
    def __init__(self,parent):
        self.alive = True
        self.parent = parent
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.sizeX = 30
        self.sizeY = 20
        self.sizeZ = 25
        self.deg = 0
        self.collsreload()
    def draw(self):
        pyxel.blt(
            self.posX-self.parent.scrollX-16,
            self.posY-self.parent.scrollY-self.posZ-25,
            0,128,224,32,32,3)
    def collsreload(self):
        self.colls = [
            Collisioner(self,0,0,0,23,12,2,0),
            Collisioner(self,2,0,2,20,10,10,0),
            Collisioner(self,3,0,12,10,10,5,0),
        ]

class Splash_Shadow:
    def __init__(self,parent):
        self.parent = parent
        self.posX = self.parent.posX
        self.posY = self.parent.posY
        self.posZ = self.parent.posZ
        self.scale = self.parent.scale+0
    def update(self):
        self.scale -= 1

    def bord_draw(self):
        pyxel.circ(
            self.posX-self.parent.parent.parent.scrollX,
            self.posY-self.parent.parent.parent.scrollY-self.posZ,
            self.scale+1,
            0
        )
    def draw(self):
        pyxel.circ(
            self.posX-self.parent.parent.parent.scrollX,
            self.posY-self.parent.parent.parent.scrollY-self.posZ,
            self.scale,
            11
        )
class Shade:
    def __init__(self,parent):
        self.parent = parent
    def draw(self):
        pyxel.circ(
            self.parent.posX-self.parent.parent.scrollX,
            self.parent.posY-self.parent.parent.scrollY+5,
            8,
            0
            )
class Mudfrog_RightArm:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
        self.gapX = 0
    def draw(self):
        if self.parent.deg == 0:
            pyxel.blt(
                self.parent.posX+5-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+2-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,22,0,9,11,3)
        elif self.parent.deg == 45:
            pyxel.blt(
                self.parent.posX+9-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-1-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,93,0,-7,11,3)
        elif self.parent.deg == 90:
            pyxel.blt(
                self.parent.posX+1-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,189,0,11,10,3)
        elif self.parent.deg == 135:
            pyxel.blt(
                self.parent.posX-7-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,180,0,9,11,3)
        elif self.parent.deg == 180:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+3-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,54,0,-9,11,3)
        elif self.parent.deg == 225:
            pyxel.blt(
                self.parent.posX-16-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+3-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,142,10,-6,10,3)
        elif self.parent.deg == 270:
            pyxel.blt(
                self.parent.posX-11-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0, 189, 0, -11, 10, 3)
        elif self.parent.deg == 315:
            pass

        
class Mudfrog_RightLeg:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
        self.gapX = 0
    def draw(self):
        if self.parent.deg == 0:
            pyxel.blt(
                self.parent.posX+4-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,22,11,10,11,3)
        if self.parent.deg == 45:
            pyxel.blt(
                self.parent.posX+1-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+5-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,93,11,-9,10,3)
        elif self.parent.deg == 90:
            pyxel.blt(
                self.parent.posX-15-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,142,0,9,10,3)
        elif self.parent.deg == 135:
            pyxel.blt(
                self.parent.posX-15-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,180,11,10,11,3)
        elif self.parent.deg == 180:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+1-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,54,11,10,11,3)
        elif self.parent.deg == 225:
            pass
        elif self.parent.deg == 270:
            pyxel.blt(
                self.parent.posX+7-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,142,0,-9,10,3)
        elif self.parent.deg == 315:
            pyxel.blt(
                self.parent.posX+9-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+3-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,100,0,7,10,3)
class Mudfrog_LeftArm:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
        self.gapX = 0
    def draw(self):
        if self.parent.deg == 0:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+2-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,22,0,-9,11,3)
        elif self.parent.deg == 45:
            pass
        elif self.parent.deg == 90:
            pyxel.blt(
                self.parent.posX+1-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,189,0,11,10,3)
        elif self.parent.deg == 135:
            pyxel.blt(
                self.parent.posX+11-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+3-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,142,10,6,10,3)
        elif self.parent.deg == 180:
            pyxel.blt(
                self.parent.posX+5-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+3-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,54,0,9,11,3)
        elif self.parent.deg == 225:
            pyxel.blt(
                self.parent.posX-1-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,180,0,-9,11,3)
        elif self.parent.deg == 270:
            pyxel.blt(
                self.parent.posX-11-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0, 189, 0, -11, 10, 3)
        elif self.parent.deg == 315:
            pyxel.blt(
                self.parent.posX-15-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-1-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,93,0,7,11,3)
class Mudfrog_LeftLeg:
    def __init__(self, parent):
        self.parent = parent
        self.gapZ = 0
        self.gapX = 0
    def draw(self):
        if self.parent.deg == 0:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,22,11,-10,11,3)
        elif self.parent.deg == 45:
            pyxel.blt(
                self.parent.posX-15-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+3-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,100,0,-7,10,3)
        elif self.parent.deg == 90:
            pyxel.blt(
                self.parent.posX-15-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,142,0,9,10,3)
        elif self.parent.deg == 135:
            pass
        elif self.parent.deg == 180:
            pyxel.blt(
                self.parent.posX+4-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+1-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,54,11,-10,11,3)
        elif self.parent.deg == 225:
            pyxel.blt(
                self.parent.posX+6-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,180,11,-10,11,3)
        elif self.parent.deg == 270:
            pyxel.blt(
                self.parent.posX+7-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+4-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,142,0,-9,10,3)
        elif self.parent.deg == 315:
            pyxel.blt(
                self.parent.posX-9-self.parent.parent.scrollX+self.gapX,
                self.parent.posY+5-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,100,0,7,10,3)
class Mudfrog_Body:
    def __init__(self, parent):
        self.parent = parent
        self.gapZ = 0
        self.gapX = 0
    def draw(self):
        if self.parent.deg == 0:
            pyxel.blt(
                self.parent.posX-11-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-11-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,0,0,22,22,3)
        elif self.parent.deg == 45:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-13-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,64,0,-29,25,3)
        elif self.parent.deg == 90:
            pyxel.blt(
                self.parent.posX-15-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-12-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,111,0,31,22,3)
        elif self.parent.deg == 135:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-13-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,151,0,29,25,3)
        elif self.parent.deg == 180:
            pyxel.blt(
                self.parent.posX-11-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-11-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,32,0,22,22,3)
        elif self.parent.deg == 225:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-13-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,151,0,-29,25,3)
        elif self.parent.deg == 270:
            pyxel.blt(
                self.parent.posX-15-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-12-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,111,0,-31,22,3)
        elif self.parent.deg == 315:
            pyxel.blt(
                self.parent.posX-14-self.parent.parent.scrollX+self.gapX,
                self.parent.posY-13-self.parent.posZ-self.gapZ-self.parent.parent.scrollY,
                0,64,0,29,25,3)

class Splash_Paint:
    def __init__(self,app):
        self.app = app
        self.posX = 0
        self.posY = 0
        self.scale = 0
    def draw(self):
        pyxel.circ(
            self.posX-self.app.scrollX,
            self.posY-self.app.scrollY,
            self.scale,
            11
        )

class Splash:
    def __init__(self,parent):
        self.move_count = 0
        self.parent = parent
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.deg = 0
        self.speedX = 0
        self.speedY = 0
        self.speedZ = 0
        self.alive = True
        self.shadows = []
        self.scale = 6
        self.metaalive = True
        self.sizeX = self.sizeY = self.sizeZ = math.sqrt(self.scale**2*2)
    def update(self):
        self.sizeX = self.sizeY = self.sizeZ = math.sqrt(self.scale**2*2)
        for i in self.shadows:
            i.update()
            if i.scale <= 0:
                self.shadows.remove(i)
        self.shadows.append(Splash_Shadow(self))
        self.speedZ -= 1
        self.posX += self.speedX
        self.posY += self.speedY
        self.posZ += self.speedZ
        self.move_count += (abs(self.speedX)+abs(self.speedY)+abs(self.speedZ))/10
        if self.posZ <= 0:
            if gettileonpos(self) in [0,1004]:
                sp = Splash_Paint(self.parent.parent)
                sp.scale = self.scale
                sp.posX = self.posX
                sp.posY = self.posY
                splash_paints_list.append(sp)
            for i in self.shadows:
                if gettileonpos(i) in [0,1004]:
                    sp = Splash_Paint(self.parent.parent)
                    sp.scale = i.scale
                    sp.posX = i.posX
                    sp.posY = i.posY
                    splash_paints_list.append(sp)
            self.alive = False
        else:
            if check_objscross(self.parent.parent.sunraku,self):
                self.alive = False
                self.parent.parent.score += 30
                self.parent.parent.sunraku.flags["attack"] = True
                scoretext_list.append(ScoreAddText(self,self.parent.parent))
    def bord_draw(self):
        for i in self.shadows:
            i.bord_draw()
        pyxel.circ(
            self.posX-self.parent.parent.scrollX,
            self.posY-self.parent.parent.scrollY-self.posZ,
            self.scale+1,
            0
        )
    def draw(self):
        for i in self.shadows:
            i.draw()
        pyxel.circ(
            self.posX-self.parent.parent.scrollX,
            self.posY-self.parent.parent.scrollY-self.posZ,
            self.scale,
            11
        )

class Aether:
    def __init__(self,parent):
        self.alive = True
        self.deg = 0
        self.parent = parent
        self.sizeZ = 1
        self.posZ = -1
        self.sizeY = 800
        self.sizeX = 800
        self.posX = 0
        self.posY = 0

class Dispmud:
    def __init__(self,x,y):
        self.posX = x*pyxel.width/4+pyxel.width/8+random.randint(-10,10)
        self.posY = y*pyxel.height/4+pyxel.height/8+random.randint(-10,10)
        self.scale = 64*math.sqrt(2)+random.randint(-5,5)
    def bord_draw(self):
        pyxel.circb(self.posX,self.posY,self.scale/2+1,4)
    def draw(self):
        pyxel.circ(self.posX,self.posY,self.scale/2,11)
    
class Mudfrog:
    def __init__(self,parent):
        self.landon = parent.aether
        self.sizeZ = 13
        self.sizeY = 24
        self.sizeX = 22
        self.speedZ = 0
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.parent = parent
        self.alive = True
        self.deg = 90
        self.degonjump = 90
        self.gotojumping = False
        self.jumping = False
        self.jumpstartflag = False
        self.landingflag = False
        self.landedlevel = 0
        self.jumplevel = 0
        self.shade = Shade(self)
        self.jumpchargecount = 0
        self.parts = {
            "RightArm": Mudfrog_RightArm(self),
            "LeftArm": Mudfrog_LeftArm(self),
            "RightLeg": Mudfrog_RightLeg(self),
            "LeftLeg": Mudfrog_LeftLeg(self),
            "Body": Mudfrog_Body(self)
        }
    def update(self):
        if self.alive:
            checked = []
            for i in collisions_list:
                if i.parent != self.landon and i.parent != self:
                    if check_objscross(self,i):
                        checked.append(i)
            posgapper(self,checked)
            if self.jumping:
                ind = DEG_TO_INDS_DICT[self.deg]
                backX = self.posX+0
                backY = self.posY+0
                if ind[0]*ind[1] == 0:
                    self.posX += ind[0]*(4+self.jumplevel*1.5)
                    self.posY += ind[1]*(4+self.jumplevel*1.5)
                else:
                    self.posX += ind[0]*(4+self.jumplevel*1.5)*math.sqrt(2)/2
                    self.posY += ind[1]*(4+self.jumplevel*1.5)*math.sqrt(2)/2
                f = False
                for i in collisions_list:
                    if i.parent != self:
                        if check_objscross(self,i):
                            f = True
                if f:
                    self.posX = backX
                    self.posY = backY
            f1 = False
            for i in collisions_list:
                if i.parent != self:
                    if check_objscross(self,i):
                        f1 = True
            backZ = self.posZ+0
            self.posZ += self.speedZ
            f2 = False
            for i in collisions_list:
                if i.parent != self:
                    if check_objscross(self,i):
                        f2 = True
            self.posZ = backZ
            if not f1:
                self.posZ += self.speedZ
                self.speedZ -= 1
                if f2:
                    self.landing()
            else:
                self.speedZ = 0
            if check_objscross(self,self.landon) and not self.gotojumping:
                self.deg = self.degonjump+0
            if not self.gotojumping:
                self.gaprev()
    def draw(self):
        if self.alive:
            for i in DEG_TO_SORT_DICT[self.deg]:
                self.parts[i].draw()
            if self.jumpstartflag:
                pyxel.play(0,1)
                self.jumpstartflag = False
            elif self.landingflag:
                if gettileonpos(self) not in [1004,0]:
                    pyxel.play(1,5)
                else:
                    pyxel.play(1,6)
                self.landingflag = False
            elif check_objscross(self,self.landon):
                if self.jumpchargecount == 15:
                    pyxel.play(0,2)
                if self.jumpchargecount == 30:
                    pyxel.play(0,3)
                if self.jumpchargecount == 45:
                    pyxel.play(0,4)
        else:
            pyxel.blt(self.posX-8-self.parent.scrollX,self.posY-8-self.parent.scrollY,0,192,64,16,16,3)
    def jumpstart(self,jumplevel):
        self.jumpstartflag = True
        self.gotojumping = False
        self.jumping = True
        self.speedZ = (jumplevel+2)**1.5
        self.jumplevel = jumplevel
        self.posZ += self.speedZ
    def jumpstandby(self,adder):
        self.parts["Body"].gapZ = -adder
        if self.deg in [45, 315, 0]:
            self.parts["RightArm"].gapX = adder
            self.parts["RightLeg"].gapX = adder
            self.parts["LeftArm"].gapX = -adder
            self.parts["LeftLeg"].gapX = -adder
        elif self.deg in [225,180,135]:
            self.parts["RightArm"].gapX = -adder
            self.parts["RightLeg"].gapX = -adder
            self.parts["LeftArm"].gapX = adder
            self.parts["LeftLeg"].gapX = adder
        elif self.deg == 270:
            self.parts["RightArm"].gapX = -adder
            self.parts["RightLeg"].gapX = adder
            self.parts["LeftArm"].gapX = -adder
            self.parts["LeftLeg"].gapX = adder
        else:
            self.parts["RightArm"].gapX = adder
            self.parts["RightLeg"].gapX = -adder
            self.parts["LeftArm"].gapX = adder
            self.parts["LeftLeg"].gapX = -adder
    def gaprev(self):
        if pyxel.frame_count % 3 == 0:
            for k in self.parts.keys():
                if self.parts[k].gapX > 0:
                    self.parts[k].gapX -= 1
                if self.parts[k].gapZ > 0:
                    self.parts[k].gapZ -= 1
                if self.parts[k].gapX < 0:
                    self.parts[k].gapX += 1
                if self.parts[k].gapZ < 0:
                    self.parts[k].gapZ += 1
    def landing(self):
        mostland = -1
        for i in collisions_list:
            if i.parent != self:
                if check_objscross(self,i):
                    if i.posZ+i.sizeZ > mostland:
                        mostland = i.posZ+i.sizeZ
                        self.landon = i.parent
        self.landingflag = True
        self.landedlevel = self.jumplevel
        self.posZ = mostland
        self.jumpchargecount = 0
        self.jumping = False
        self.parts["Body"].gapZ = -self.jumplevel-2
        self.deg = self.degonjump+0
        if gettileonpos(self) not in [1004,0] and self.landon == self.parent.aether:
            for r in range(10+random.randrange(-5,5)+3*self.jumplevel**2):
                s = Splash(self)
                rad = math.radians(random.randrange(0,359))
                s.posX = self.posX+math.cos(rad)*19
                s.posY = self.posY+math.sin(rad)*19
                s.posZ = 1
                s.speedX = math.cos(rad)*random.randrange(5, 30+7*self.jumplevel)*0.1
                s.speedY = math.sin(rad)*random.randrange(5, 30+7*self.jumplevel)*0.1
                s.speedZ = 4
                s.scale = self.jumplevel/2+5
                splash_list.append(s)

class Mudfrog_Player(Mudfrog):
    def update(self):
        if self.alive:
            inds = [0,0]
            if self.parent.scene != SCENE_TITLE:
                if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
                    inds[1] -= 1
                if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
                    inds[1] += 1
                if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
                    inds[0] -= 1
                if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
                    inds[0] += 1
                if inds != [0,0]:
                    self.degonjump = INDS_TO_DEG_DICT[f"{inds[0]},{inds[1]}"]
                elif self.parent.mousemoved:
                    self.degonjump = math.floor(((math.degrees(math.atan2(self.posY-pyxel.mouse_y-self.posZ-self.parent.scrollY,  self.posX-pyxel.mouse_x-self.parent.scrollX))+360+360-90+22.5)%360)/45)*45
            super().update()
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and self.parent.scene != SCENE_TITLE :
                self.gotojumping = True
                self.jumpchargecount += 1
            elif not self.jumping:
                if self.gotojumping:
                    self.jumpstart(math.floor(min(45,self.jumpchargecount)/15))
            if self.gotojumping:
                if not self.jumping:
                    self.jumpstandby(math.floor(min(45,self.jumpchargecount)/15))
            else:
                self.gaprev()
            for i in [*attack_list,*[iii for iii in nagepick_list if iii.moving]]:
                if check_objscross(self,i):
                    self.alive = False

class Mudfrog_NPC(Mudfrog):
    def __init__(self,parent):
        super().__init__(parent)
        self.nextjump = None
        self.jcounter = 0
    def update(self):
        if self.nextjump == None:
            if pyxel.frame_count%30 == 0:
                if random.randint(1,10) <= 3:
                    self.nextjump = None
                else:
                    self.nextjump = {"deg":random.randint(0,7)*45,"level":random.randint(0,3)}
        else:
            if self.jumping:
                pass
            elif self.gotojumping:
                self.jcounter += 1
                if self.jcounter > self.nextjump["level"]*15+5:
                    self.gotojumping = False
                    self.jumping = True
                    self.jumpstart(self.nextjump["level"])
                else:
                    self.jumpstandby(math.floor(min(45,self.jcounter)/15))
            else:
                self.degonjump = self.nextjump["deg"]
                self.gotojumping = True
                self.jcounter = 0
        super().update()
    def landing(self):
        super().landing()
        self.nextjump = None

class Sunraku_Head:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
    def draw(self):
        dx = self.parent.posX-8-self.parent.parent.scrollX
        dy = self.parent.posY-24-self.parent.parent.scrollY-self.parent.posZ-40+self.gapZ+5
        if self.parent.deg == 0:
            pyxel.blt(dx,dy,0,240,0,-16,24,3)
            pyxel.blt(dx,dy,0,241,24,15,24,3)
        elif self.parent.deg == 45:
            pyxel.blt(dx,dy,0,208,0,16,24,3)
            pyxel.blt(dx,dy,0,241,24,15,24,3)
        elif self.parent.deg == 90:
            pyxel.blt(dx,dy,0,241,24,15,24,3)
            pyxel.blt(dx,dy,0,224,0,16,24,3)
        elif self.parent.deg == 135:
            pyxel.blt(dx,dy,0,241,24,15,24,3)
            pyxel.blt(dx,dy,0,208,0,16,24,3)
        elif self.parent.deg == 180:
            pyxel.blt(dx,dy,0,241,24,15,24,3)
            pyxel.blt(dx,dy,0,240,0,16,24,3)
        elif self.parent.deg == 225:
            pyxel.blt(dx,dy,0,241,24,15,24,3)
            pyxel.blt(dx,dy,0,208,0,-16,24,3)
        elif self.parent.deg == 270:
            pyxel.blt(dx,dy,0,241,24,15,24,3)
            pyxel.blt(dx,dy,0,224,0,-16,24,3)
        elif self.parent.deg == 315:
            pyxel.blt(dx,dy,0,208,0,-16,24,3)
            pyxel.blt(dx,dy,0,241,24,15,24,3)
class Sunraku_Body:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
    def draw(self):
        ddx = self.parent.posX-self.parent.parent.scrollX
        ddy = self.parent.posY-self.parent.parent.scrollY-self.parent.posZ+self.gapZ+5
        if self.parent.deg == 0:
            pyxel.blt(ddx-13,ddy-41+19,0,24,22,-26,11,3)
            pyxel.blt(ddx-12,ddy-41,0,0,22,-24,31,3)
        elif self.parent.deg == 45:
            pyxel.blt(ddx-13,ddy-44,0,27,53,-26,37,3)
        elif self.parent.deg == 90:
            pyxel.blt(ddx-7,ddy-41,0,6,77,14,31,3)
        elif self.parent.deg == 135:
            pyxel.blt(ddx-11,ddy-44,0,27,53,26,37,3)
        elif self.parent.deg == 180:
            pyxel.blt(ddx-12,ddy-41,0,0,22,24,31,3)
            pyxel.blt(ddx-13,ddy-41+19,0,24,22,26,11,3)
        elif self.parent.deg == 225:
            pyxel.blt(ddx-15,ddy-44,0,27,53,-26,37,3)
        elif self.parent.deg == 270:
            pyxel.blt(ddx-7,ddy-41,0,6,77,-14,31,3)
        elif self.parent.deg == 315:
            pyxel.blt(ddx-13,ddy-44,0,27,53,26,37,3)
class Sunraku_RightLeg:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
    def draw(self):
        ddx = self.parent.posX-self.parent.parent.scrollX
        ddy = self.parent.posY-self.parent.parent.scrollY-self.parent.posZ+self.gapZ+5
        if self.parent.deg == 0:
            pyxel.blt(ddx+3,ddy-10,0,24,33,11,10,3)
        elif self.parent.deg == 45:
            pyxel.blt(ddx,ddy-10,0,24,33,11,10,3)
        if self.parent.deg == 90:
            pyxel.blt(ddx-3,ddy-10,0,24,33,11,10,3)
        elif self.parent.deg == 135:
            pyxel.blt(ddx-5,ddy-10,0,24,33,11,10,3)
        elif self.parent.deg == 180:
            pyxel.blt(ddx-14,ddy-10,0,24,33,-11,10,3)
        elif self.parent.deg == 225:
            pyxel.blt(ddx-15,ddy-11,0,24,33,-11,10,3)
        if self.parent.deg == 270:
            pyxel.blt(ddx-8,ddy-10,0,24,33,-11,10,3)
        elif self.parent.deg == 315:
            pyxel.blt(ddx-2,ddy-11,0,24,33,-11,10,3)

class Sunraku_LeftLeg:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
    def draw(self):
        ddx = self.parent.posX-self.parent.parent.scrollX
        ddy = self.parent.posY-self.parent.parent.scrollY-self.parent.posZ+self.gapZ+5
        if self.parent.deg == 0:
            pyxel.blt(ddx-14,ddy-10,0,24,33,-11,10,3)
        elif self.parent.deg == 45:
            pyxel.blt(ddx-8,ddy-10-2,0,24,33,11,10,3)
        if self.parent.deg == 90:
            pyxel.blt(ddx-3, ddy-10, 0, 24, 33, 11, 10, 3)
        elif self.parent.deg == 135:
            pyxel.blt(ddx-5+9, ddy-10-2, 0, 24, 33, 11, 10, 3)
        elif self.parent.deg == 180:
            pyxel.blt(ddx+3,ddy-10,0,24,33,11,10,3)
        elif self.parent.deg == 225:
            pyxel.blt(ddx-15+9,ddy-11+2,0,24,33,-11,10,3)
        if self.parent.deg == 270:
            pyxel.blt(ddx-8,ddy-10,0,24,33,-11,10,3)
        elif self.parent.deg == 315:
            pyxel.blt(ddx-2-9,ddy-11+2,0,24,33,-11,10,3)

class Sunraku_Arm:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
    def draw(self):
        ddx = self.parent.posX-self.parent.parent.scrollX
        ddy = self.parent.posY-self.parent.parent.scrollY-self.parent.posZ+self.gapZ+5
        if self.parent.now_motion in ["Pick","NagePick"]:
            keyf = SUNRAKU_MOTION_KEYS["Pick"][self.parent.motion_count]
            self.pickdrawer(keyf,ddx,ddy)
        elif self.parent.now_motion == "None":
            self.pickdrawer(1,ddx,ddy)
    def pickdrawer(self,keyf,ddx,ddy):
        if self.parent.deg == 0:
            if keyf in [1,2,3]:
                pyxel.blt(ddx-13.5,ddy-60,0,0,53,27,24,3)
            elif keyf in [4]:
                pyxel.blt(ddx-13.5,ddy-37,0,0,53,-27,24,3)
            elif keyf in [5]:
                pyxel.blt(ddx-13.5,ddy-37,0,0,53,-27,-24,3)
        elif self.parent.deg == 90:
            if keyf in [1]:
                pyxel.blt(ddx-22,ddy-50,0,22,43,24,10,3)
            if keyf in [2]:
                pyxel.blt(ddx-4,ddy-62,0,17,53,10,24,3)
            if keyf in [3]:
                pyxel.blt(ddx+7,ddy-55,0,17,53,-10,-24,3)
            if keyf in [4]:
                pyxel.blt(ddx+1,ddy-32,0,22,43,-24,-10,3)
            if keyf in [5]:
                pyxel.blt(ddx+2,ddy-35,0,17,53,-10,-24,3)
        elif self.parent.deg == 135:
            if keyf in [1]:
                pyxel.blt(ddx-11, ddy-53, 0, 22, 43, 24, 10, 3)
                pyxel.blt(ddx-15, ddy-50, 0, 17, 53, -10, -24, 3)
            if keyf in [2,3]:
                pyxel.blt(ddx-12, ddy-62, 0, 17, 53, -10, 24, 3)
                pyxel.blt(ddx+4, ddy-65, 0, 17, 53, 10, 24, 3)
            if keyf in [4]:
                pyxel.blt(ddx-3,ddy-44,0,22,43,24,-10,3)
                pyxel.blt(ddx-7,ddy-50,0,22,43,-24,10,3)
            if keyf in [5]:
                pyxel.blt(ddx-9,ddy-33,0,22,43,-24,-10,3)
                pyxel.blt(ddx+9, ddy-45, 0, 17, 53, 10, 24, 3)
        elif self.parent.deg == 180:
            if keyf in [1, 2, 3]:
                pyxel.blt(ddx-13.5, ddy-60, 0, 0, 53, 27, 24, 3)
            elif keyf in [4]:
                pyxel.blt(ddx-13.5, ddy-37, 0, 0, 53, -27, 24, 3)
            elif keyf in [5]:
                pyxel.blt(ddx-13.5, ddy-37, 0, 0, 53, -27, -24, 3)
        elif self.parent.deg == 225:
            if keyf in [1]:
                pyxel.blt(ddx+11-24, ddy-53, 0, 22, 43, -24, 10, 3)
                pyxel.blt(ddx+15-10, ddy-50, 0, 17, 53, 10, -24, 3)
            if keyf in [2,3]:
                pyxel.blt(ddx+12-10, ddy-62, 0, 17, 53, 10, 24, 3)
                pyxel.blt(ddx-4-10, ddy-65, 0, 17, 53, -10, 24, 3)
            if keyf in [4]:
                pyxel.blt(ddx+3-24,ddy-44,0,22,43,24,-10,3)
                pyxel.blt(ddx+7-24,ddy-50,0,22,43,24,10,3)
            if keyf in [5]:
                pyxel.blt(ddx+9-24,ddy-33,0,22,43,24,-10,3)
                pyxel.blt(ddx-9-10, ddy-45, 0, 17, 53, -10, 24, 3)
        elif self.parent.deg == 270:
            if keyf in [1]:
                pyxel.blt(ddx-2+2,ddy-50,0,22,43,-24,10,3)
            if keyf in [2]:
                pyxel.blt(ddx-6+2,ddy-62,0,17,53,-10,24,3)
            if keyf in [3]:
                pyxel.blt(ddx-17+2,ddy-55,0,17,53,-10,-24,3)
            if keyf in [4]:
                pyxel.blt(ddx-24+2,ddy-32,0,22,43,24,-10,3)
            if keyf in [5]:
                pyxel.blt(ddx-15+2,ddy-35,0,17,53,10,-24,3)

class Sunraku_Pick:
    def __init__(self,parent):
        self.parent = parent
        self.gapZ = 0
    def draw(self):
        ddx = self.parent.posX-self.parent.parent.scrollX
        ddy = self.parent.posY-self.parent.parent.scrollY-self.parent.posZ+self.gapZ+5
        if self.parent.now_motion in ["Pick","NagePick"]:
            keyf = SUNRAKU_MOTION_KEYS["Pick"][self.parent.motion_count]
            self.pickldrawer(keyf,ddx,ddy)
        elif self.parent.now_motion == "None":
            self.pickldrawer(1,ddx,ddy)
    def pickldrawer(self,keyf,ddx,ddy):
        if self.parent.flags["armschange"] > 0:
            for i in range(16):
                pyxel.pal(i,7)
            self.parent.flags["armschange"] -= 1
        if self.parent.deg == 0:
            if keyf in [1]:
                pyxel.blt(ddx-3,ddy-65,0,*EQUIP_V_DICT[self.parent.equip],6,41,3)
            elif keyf in [2,3]:
                pyxel.blt(ddx-3,ddy-87,0,*EQUIP_V_DICT[self.parent.equip],-6,-41,3)
            elif keyf in [4]:
                pyxel.blt(ddx-3,ddy-49,0,*EQUIP_V_DICT[self.parent.equip],-6,-41,3)
            elif keyf in [5]:
                pyxel.blt(ddx-3,ddy-28,0,*EQUIP_V_DICT[self.parent.equip],6,41,3)
        
        elif self.parent.deg == 90:
            if keyf in [1]:
                pyxel.blt(ddx-59+4,ddy-48,0,*EQUIP_Q_DICT[self.parent.equip],36,36,3)
            elif keyf in [2]:
                pyxel.blt(ddx-42+4,ddy-97+4,0,*EQUIP_Q_DICT[self.parent.equip],36,-36,3)
            elif keyf in [3]:
                pyxel.blt(ddx-26+4,ddy-90+4,0,*EQUIP_Q_DICT[self.parent.equip],36,-36,3)
            elif keyf in [4]:
                pyxel.blt(ddx+22,ddy-63+4,0,*EQUIP_Q_DICT[self.parent.equip],-36,-36,3)
            elif keyf in [5]:
                pyxel.blt(ddx+9,ddy-16+4,0,*EQUIP_Q_DICT[self.parent.equip],-36,36,3)
        elif self.parent.deg in [45,135]:
            if keyf in [1]:
                pyxel.blt(ddx-43,ddy-53,0,*EQUIP_Q_DICT[self.parent.equip],36,36,3)
            elif keyf in [2]:
                pyxel.blt(ddx-31,ddy-64,0,*EQUIP_Q_DICT[self.parent.equip],36,36,3)
            elif keyf in [3]:
                pyxel.blt(ddx-31,ddy-93,0,*EQUIP_Q_DICT[self.parent.equip],36,-36,3)
            elif keyf in [4]:
                pyxel.blt(ddx+16,ddy-80,0,*EQUIP_Q_DICT[self.parent.equip],-36,-36,3)
            elif keyf in [5]:
                pyxel.blt(ddx+13,ddy-29,0,*EQUIP_Q_DICT[self.parent.equip],-36,36,3)
        elif self.parent.deg == 180:
            if keyf in [1]:
                pyxel.blt(ddx-3,ddy-65,0,*EQUIP_V_DICT[self.parent.equip],6,41,3)
            elif keyf in [2,3]:
                pyxel.blt(ddx-3,ddy-87,0,*EQUIP_V_DICT[self.parent.equip],-6,-41,3)
            elif keyf in [4]:
                pyxel.blt(ddx-3,ddy-49,0,*EQUIP_V_DICT[self.parent.equip],-6,-41,3)
            elif keyf in [5]:
                pyxel.blt(ddx-3, ddy-28, 0, *EQUIP_V_DICT[self.parent.equip], 6, 41, 3)
        elif self.parent.deg in [225,315]:
            if keyf in [1]:
                pyxel.blt(ddx+43-36,ddy-53,0,*EQUIP_Q_DICT[self.parent.equip],-36,36,3)
            elif keyf in [2]:
                pyxel.blt(ddx+31-36,ddy-64,0,*EQUIP_Q_DICT[self.parent.equip],-36,36,3)
            elif keyf in [3]:
                pyxel.blt(ddx+31-36,ddy-93,0,*EQUIP_Q_DICT[self.parent.equip],-36,-36,3)
            elif keyf in [4]:
                pyxel.blt(ddx-16-36,ddy-80,0,*EQUIP_Q_DICT[self.parent.equip],36,-36,3)
            elif keyf in [5]:
                pyxel.blt(ddx-13-36,ddy-29,0,*EQUIP_Q_DICT[self.parent.equip],36,36,3)
        elif self.parent.deg == 270:
            if keyf in [1]:
                pyxel.blt(ddx+19, ddy-36-4-2, 0, *EQUIP_Q_DICT[self.parent.equip], -36, 36, 3)
            elif keyf in [2]:
                pyxel.blt(ddx+2, ddy-97+4, 0, *EQUIP_Q_DICT[self.parent.equip], -36, -36, 3)
            elif keyf in [3]:
                pyxel.blt(ddx-17+4, ddy-90+4, 0, *EQUIP_Q_DICT[self.parent.equip], -36, -36, 3)
            elif keyf in [4]:
                pyxel.blt(ddx-62+4+2, ddy-63+4, 0, *EQUIP_Q_DICT[self.parent.equip], 36, -36, 3)
            elif keyf in [5]:
                pyxel.blt(ddx-49, ddy-16+4, 0, *EQUIP_Q_DICT[self.parent.equip], 36, 36, 3)
        pyxel.pal()
class Sunraku:
    def __init__(self,parent):
        self.equip = "Pick"
        self.walker = "LeftLeg"
        self.walkcount = 0
        self.stm = 40
        self.hp = 30
        self.parent = parent
        self.deg = 0
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.sizeX = 20
        self.sizeY = 12
        self.sizeZ = 50
        self.speed = 1.4
        self.parts = {
            "Head":Sunraku_Head(self),
            "Body":Sunraku_Body(self),
            "RightLeg":Sunraku_RightLeg(self),
            "LeftLeg":Sunraku_LeftLeg(self),
            "Arm":Sunraku_Arm(self),
            "Pick":Sunraku_Pick(self)
        }
        self.now_motion = "None"
        self.flags = {
            "attack":False,
            "hit":False,
            "armschange":0
        }
        self.motion_count = 0
    def update(self):
        if gettileonpos(self) in [1004,0]:
            self.speed = 3
        else:
            self.speed = 1.4
        if self.stm <= 20:
            self.speed = 1.1
            if self.stm <= 10:
                self.speed = 0.8
        self.motion_count += 1
        if self.flags["attack"]:
            checked = []
            for i in rock_list:
                if check_objscross(self,i):
                    checked.append(i)
            posgapper(self,checked)
            if not check_cyclecross(self.posX,self.posY,16,self.parent.player.posX,self.parent.player.posY,16):
                if self.stm > 20:
                    if math.sqrt((self.posX-self.parent.player.posX)**2+(self.posY-self.parent.player.posY)**2) > 100:
                        plr = getrectbyobj(self.parent.player)
                        f = False
                        for i in range(0,360,45):
                            l2 = [(self.posX,self.posY),(self.posX+DEG_TO_FORMATED_INDS_DICT[i][0]*400,self.posY        +DEG_TO_FORMATED_INDS_DICT[i][1]*400)]
                            for l1 in plr:
                                if check_linecross(
                                    [l1[0][0],l1[0][1],l1[1][0],l1[1][1]],
                                    [l2[0][0],l2[0][1],l2[1][0],l2[1][1]]
                                ):
                                    f = True
                        if f:
                            self.deg = math.degrees(math.atan2(self.parent.player.posY-self.posY,self.parent.player.    posX-self.posX))+90+360+22.5
                            self.deg %= 360
                            self.deg = math.floor(self.deg/45)*45
                            self.now_motion = "NagePick"
                            self.motion_count = 0
                            if self.equip != "Pick":
                                self.flags["armschange"] = 3
                            self.equip = "Pick"
                if self.now_motion not in ["Pick","NagePick"]:
                    candeg = []
                    candegsind = []
                    defposX = self.posX+0
                    defposY = self.posY+0
                    defdeg = self.deg+0
                    mrrr = 0
                    for i in range(0,360,45):
                        self.deg = i
                        f = False
                        self.posX =  defposX
                        self.posY =  defposY
                        for r in range(6):
                            self.posX += DEG_TO_FORMATED_INDS_DICT[i][0]*self.speed
                            self.posY += DEG_TO_FORMATED_INDS_DICT[i][1]*self.speed
                            for ii in rock_list:
                                if check_objsnear(self,ii):
                                    if check_objscross(self,ii):
                                        f = True
                        if not f and i != (defdeg+180)%360:
                            candeg.append(i)
                            candegsind.append(math.sqrt((self.posX-self.parent.player.posX)**2+(self.posY-self.parent.  player.posY)**2))
                        if i == defdeg:
                            mrrr = math.sqrt((self.posX-self.parent.player.posX)**2+(self.posY-self.parent.player.posY) **2)
                    self.posX = defposX
                    self.posY = defposY
                    self.deg = defdeg
                    if len(candeg)>0:
                        c = sorted(zip(candegsind,candeg))
                        if self.deg not in candeg or abs(mrrr - c[0][0]) > 0.8:
                            self.deg = c[0][1]
                        if self.deg == defdeg:
                            self.parts["RightLeg"].gapZ = 0
                            self.parts["LeftLeg"].gapZ = 0
                            if self.walkcount >= 7:
                                self.walkcount = 0
                                self.walker = "LeftLeg" if self.walker == "RightLeg" else "RightLeg"
                            if math.floor(self.walkcount) < 4:
                                self.parts[self.walker].gapZ = -self.walkcount+0
                            else:
                                self.parts[self.walker].gapZ = self.walkcount-6
                            self.walkcount+=self.speed
                            self.posX += DEG_TO_FORMATED_INDS_DICT[self.deg][0]*self.speed
                            self.posY += DEG_TO_FORMATED_INDS_DICT[self.deg][1]*self.speed
                            if check_objscross(self.parent.player,self) or self.parent.player.landon == self:
                                self.parent.player.posX += DEG_TO_FORMATED_INDS_DICT[self.deg][0]*self.speed
                                self.parent.player.posY += DEG_TO_FORMATED_INDS_DICT[self.deg][1]*self.speed
                            
            else:
                if self.now_motion == "None":
                    self.deg = math.degrees(math.atan2(self.parent.player.posY-self.posY,self.parent.player.posX-self.posX))+90+360+22.5
                    self.deg %= 360
                    self.deg = math.floor(self.deg/45)*45
                    if self.stm > 20:
                        if self.equip != "Axe":
                            self.flags["armschange"] = 3
                        self.equip = "Axe"
                        self.now_motion = "Pick"
                        self.motion_count = 0
        self.stm = min(self.stm+0.25,40)
        if self.now_motion == "None":
            if not self.flags["attack"] and self.stm > 30:
                self.now_motion = "Pick"
                self.motion_count = 0
                self.flags["hit"] = False
#
        elif self.now_motion == "Pick":
            if self.motion_count > 24:
                self.motion_count = 0
                self.now_motion = "None"
                if not self.flags["hit"]:
                    self.stm -= 15
            if self.motion_count == 14:
                attack_list.clear()
                ac = Collisioner(
                    self,
                    math.cos(math.radians(self.deg-90))*15,
                    math.sin(math.radians(self.deg-90))*15,
                    0,
                    40,
                    6,
                    self.sizeZ+5,
                    self.deg+90)
                attack_list.append(ac)
            if self.motion_count == 18:
                if len(attack_list) > 0:
                    attack_list.clear()
            for a in attack_list:
                if check_objscross(rock_list[0],a):
                    self.stm -= 30
                    self.flags["hit"] = True
                    if random.randrange(0,100) < 10:
                        stone_list.append(Stone2(self))
                    else:
                        stone_list.append(Stone1(self))
                    attack_list.remove(a)
        elif self.now_motion == "NagePick":
            if self.motion_count > 20:
                self.stm -= 20
                self.motion_count = 0
                self.now_motion = "None"
                self.equip = "Pick"
                self.flags["armschange"] = 3
            if self.motion_count == 10:
                nagepick_list.append(NagePick(self))
                self.equip = "None"

    def draw(self):
        if self.now_motion == "None":
            for i in SUNRAKU_MODE_AND_DEG_TO_SORT_DICT["None"][self.deg]:
                self.parts[i].draw()
        elif self.now_motion == "Pick":
            for i in SUNRAKU_MODE_AND_DEG_TO_SORT_DICT["Pick"][self.deg][SUNRAKU_MOTION_KEYS["Pick"][self.motion_count]-1]:
                self.parts[i].draw()
            if self.motion_count == 11:
                pyxel.play(2,11)
        elif self.now_motion == "NagePick":
            for i in SUNRAKU_MODE_AND_DEG_TO_SORT_DICT["NagePick"][self.deg][SUNRAKU_MOTION_KEYS["Pick"][self.motion_count]-1]:
                self.parts[i].draw()
        dx = self.posX+16-self.parent.scrollX
        dy = self.posY-self.parent.scrollY-self.posZ-64+5
        pyxel.blt(dx,dy,0,192,144,64,32,14)
        if self.stm > 0:
            color = 10
            if self.stm > 27:
                color = 10
            elif self.stm > 13:
                color = 9
            else:
                color = 8
            pyxel.line(dx+19,dy+21,dx+19+self.stm,dy+21,color)
        
            

    

class App:
    def __init__(self):
        pyxel.init(230, 230,palette=PALETTE)
        pyxel.load("assets/main.pyxres")
        self.initer()
        pyxel.run(self.update, self.draw)
    def initer(self):
        npc_frogs_list.clear()
        splash_list.clear()
        splash_paints_list.clear()
        rock_list.clear()
        wave_list.clear()
        collisions_list.clear()
        stone_list.clear()
        stone_col_list.clear()
        attack_list.clear()
        nagepick_list.clear()
        scoretext_list.clear()
        self.scene_changed_frame = 0
        self.aether = Aether(self)
        self.scene = SCENE_TITLE
        self.scrollX = -pyxel.width/2
        self.scrollY = -pyxel.height/2
        self.player = Mudfrog_Player(self)
        self.player.posX = 100
        self.player.posY = 100
        self.player.deg = 0
        #for i in range(30):
        #    m = Mudfrog_NPC(self)
        #    m.posX = random.randint(-200, 200)
        #    m.posY = random.randint(-200, 200)
        #    m.deg = random.randint(0, 7)*45
        #    npc_frogs_list.append(m)
        self.sunraku = Sunraku(self)
        self.sunraku.posX = 0
        self.sunraku.posY = 30
        self.dstk = []
        for x in range(4):
            for y in range(4):
                self.dstk.append([x,y])
        self.dd_list = []
        rock_list.append(Rock1(self))
        for i in [(-70,-80),(160,-30),(-140,90)]:
            r = Rock2(self)
            r.posX = i[0]
            r.posY = i[1]
            r.collsreload()
            rock_list.append(r)
        for i in [(-170,20),(-70,180),(10,-200),(90,20),(100,150)]:
            r = Rock3(self)
            r.posX = i[0]
            r.posY = i[1]
            r.collsreload()
            rock_list.append(r)
        self.lastcursorX = pyxel.mouse_x
        self.lastcursorY = pyxel.mouse_y
        self.mousemoved = False
        pyxel.mouse(True)
        self.score = 0
        self.long = 0
    def update(self):
        if self.lastcursorX == pyxel.mouse_x and self.lastcursorY == pyxel.mouse_y:
            self.mousemoved = False
        else:
            self.mousemoved = True
        self.lastcursorX = pyxel.mouse_x
        self.lastcursorY = pyxel.mouse_y
        if self.scene in [SCENE_TITLE,SCENE_GAME]:
            collisions_list.clear()
            for i in [self.sunraku,*rock_list,self.aether,self.player]:
                if "colls" in i.__dict__.keys():
                    for ii in i.colls:
                        collisions_list.append(Collision(ii))
                else:
                    collisions_list.append(Collision(i))
            stone_col_list.clear()
            for i in stone_list:
                stone_col_list.append(Collision(i))
            self.sunraku.update()
            self.player.update()
            for i in stone_col_list:
                if i.parent.landon != None:
                    if not i.parent.landon.alive:
                        i.parent.landon = None
            for i in stone_col_list:
                if i.parent.alive:
                    i.parent.update()
                else:
                    stone_list.remove(i.parent)
                    stone_col_list.remove(i)
            for i in splash_list:
                if i.alive:
                    i.update()
                else:
                    splash_list.remove(i)
            for i in scoretext_list:
                if i.livecount > 10:
                    scoretext_list.remove(i)
                else:
                    i.update()
            for i in nagepick_list:
                i.update()
            for i in wave_list:
                if i.alive:
                    i.update()
                else:
                    wave_list.remove(i)
            for i in npc_frogs_list:
                i.update()
            self.scrollX = min(200,max(-200,self.player.posX)) - pyxel.width/2
            self.scrollY = min(200,max(-200,self.player.posY)) - pyxel.height/2
        elif self.scene == SCENE_GAME_TO_GAMEOVER:
            if pyxel.frame_count-self.scene_changed_frame > 4*16:
                self.scene = SCENE_GAMEOVER
                self.scene_changed_frame = pyxel.frame_count+0
            elif (pyxel.frame_count-self.scene_changed_frame)%4 == 0:
                random.shuffle(self.dstk)
                self.dd_list.append(Dispmud(*self.dstk.pop()))
        elif self.scene == SCENE_GAMEOVER:
            l = pyxel.frame_count-self.scene_changed_frame
            if l >= 40:
                if pyxel.width/2-len("G A M E  O V E R")*4 <= pyxel.mouse_x <= pyxel.width/2-len("G A M E  O V E R")*4  +len("TWEET")*4 and  90<= pyxel.mouse_y <= 96:
                    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                        openw(
                            "https://twitter.com/intent/tweet?text=" + quote_plus("SCORE:".upper()+str(self.score)+"\nTIME:"+str(self.long)+"\n#MudFrog_Dorojiai\nhttps://github.com/AlageZ/Dorojiai/releases/"))
            if l >= 50:
                if pyxel.width/2-len("G A M E  O V E R")*4 <= pyxel.mouse_x <= pyxel.width/2-len("G A M E  O V E R")*4+len("RETRY")*4 and  110<= pyxel.mouse_y <= 116:
                    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                        self.initer()

        if self.scene == SCENE_TITLE and (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) or pyxel.btnp(pyxel.KEY_SPACE)):
            self.scene = SCENE_GAME
            self.scene_changed_frame = pyxel.frame_count+0
        if not self.player.alive and self.scene == SCENE_GAME:
            self.scene = SCENE_GAME_TO_GAMEOVER
            self.long = pyxel.frame_count-self.scene_changed_frame
            self.scene_changed_frame = pyxel.frame_count+0


    def draw(self):
        pyxel.cls(15)
        pyxel.bltm(-200-self.scrollX,-200-self.scrollY,0,0,0,50,50,3)
        for i in splash_paints_list:
            i.draw()
        for s in [self.player,* npc_frogs_list]:
            s.shade.draw()
        d_spl_list = []
        for e in sorted([self.player,*splash_list,*npc_frogs_list,self.sunraku,*rock_list,*stone_list,*nagepick_list,*scoretext_list],key=lambda o:o.posY+o.posZ):
            if e.__class__.__name__ == "Splash":
                e.bord_draw()
                d_spl_list.append(e)
            else:
                if len(d_spl_list)>0:
                    for ee in d_spl_list:
                        ee.draw()
                    d_spl_list = []
                e.draw()
        if len(d_spl_list)>0:
            for ee in d_spl_list:
                ee.draw()
            d_spl_list = []
        if ATARIHANTEIMODE:
            for i in [*splash_list, *collisions_list,*stone_col_list,*attack_list,*nagepick_list]:
                f = False
                if ATARIHANTEIMODE_NEARSTRONG:
                    f = check_objsnear(i,self.player)
                else:
                    f = check_objscross(i, self.player)
                if f:
                    pyxel.pal(3,8)
                drawhitbox(i, self)
                pyxel.pal()
        if self.scene == SCENE_TITLE:
            pyxel.blt(pyxel.width/2-64,pyxel.height/4-32,0,64,32,128,64,3)
            pyxel.text(pyxel.width/2-15*4/2,pyxel.height/4+32+4,"- ATTACK START -".upper(),7)
            pyxel.pal(7,0)
            pyxel.blt(0,pyxel.height-8,0,20,96,230,8,3)
            pyxel.pal()
        else:
            pyxel.text(0,0,"SCORE:"+str(self.score),7)
        if self.scene in [SCENE_GAME_TO_GAMEOVER,SCENE_GAMEOVER]:
            for d in self.dd_list:
                d.bord_draw()
            for d in self.dd_list:
                d.draw()
            if self.scene == SCENE_GAME_TO_GAMEOVER:
                if (pyxel.frame_count-self.scene_changed_frame)%4 == 0:
                    pyxel.play(3,13)
            else:
                pyxel.stop()
                l = pyxel.frame_count-self.scene_changed_frame
                if l >= 10:
                    pyxel.text(pyxel.width/2-len("G A M E  O V E R")*4/2,30,"G A M E  O V E R",9)
                if l >= 20:
                    pyxel.text(pyxel.width/2-len("G A M E  O V E R")*4,50,f"SCORE: {self.score}",7)
                if l >= 30:
                    pyxel.text(pyxel.width/2-len("G A M E  O V E R")*4,70,f"TIME: {self.long}",7)
                cf = False
                if pyxel.width/2-len("G A M E  O V E R")*4 <= pyxel.mouse_x <= pyxel.width/2-len("G A M E  O V E R")*4+len("TWEET")*4 and  90<= pyxel.mouse_y <= 96:
                    cf = True
                if l >= 40:
                    pyxel.text(pyxel.width/2-len("G A M E  O V E R")*4-(4 if cf else 0),90,">TWEET" if cf else "TWEET",12)
                cf = False
                if pyxel.width/2-len("G A M E  O V E R")*4 <= pyxel.mouse_x <= pyxel.width/2-len("G A M E  O V E R")*4+len("RETRY")*4 and  110<= pyxel.mouse_y <= 116:
                    cf = True
                if l >= 50:
                    pyxel.text(pyxel.width/2-len("G A M E  O V E R")*4-(4 if cf else 0),110,">RETRY" if cf else "RETRY",0)


app = App()
