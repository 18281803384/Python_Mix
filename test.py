# 作者: ZengCheng
# 时间: 2022/10/8


import random as rd
import re
# import threading
import tkinter.ttk
from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import askstring

root = Tk()
root.title("文字勇者冒险闯关小游戏v1.0")
root.geometry("1000x600+300+100")


# 画辅助线
def line():
    w = Canvas(root, width=1000, height=600)
    w.place(x=0, y=0)
    # 左边竖线
    line01 = w.create_line(250, 0, 250, 600, fill='blue', width=2)
    # 底边横线
    line02 = w.create_line(0, 400, 1000, 400, fill='blue', width=2)
    # 右边竖线
    line03 = w.create_line(750, 0, 750, 600, fill='blue', width=2)


line()


class Warrior:  # 定义一个勇者的类
    # 传入的参数((名称,等级,金钱,剩余血,剩余蓝,当前经验,穿戴武器序号,穿戴防具序号,当前层,当前关),背包物品{[武器编号,数量],[防具编号,数量],[药剂编号,数量]})
    def __init__(self, params=('蒙蒙', 1, 0, 100, 10, 0, 0, 0, 1, 1),
                 baggage=None):
        if baggage is None:
            baggage = {'我的武器': [0, 1], '我的防具': [0, 1], '我的药剂': [0, 1]}
        self.Name = params[0]
        self.Lv = params[1]
        self.Money = params[2]
        self.My_Hp = params[3]
        self.My_Mp = params[4]
        self.My_Exp = params[5]
        self.My_Weapon = (Items.weapons[params[6]], params[6])  # ((武器数据),武器编号)
        self.My_Aromr = (Items.armors[params[7]], params[7])
        self.floor = params[8]
        self.level = params[9]
        self.MExp = 50 + (self.Lv - 1) * 10  # 升级所需经验值每升一级在50基础上加10
        self.MHp = 100 + (self.Lv - 1) * 10  # 基础最大生命值是100，每升一级加10上限
        self.MMp = 10 + (self.Lv - 1) * 10  # 最大魔法值计算同上
        self.Atk = 20 + (self.Lv - 1) * 2 + (self.My_Weapon[0][1])  # 总攻击力为基础攻击力20加每升一级增加的2加武器攻击力
        self.Def = (self.Lv - 1) * 2 + self.My_Aromr[0][1]  # 默认为无基础防御力,每升一级加2点防御加防具的防御力
        self.Baggage = baggage

    # 更新玩家数据
    def renew_data(self):
        self.MExp = 50 + (self.Lv - 1) * 10
        self.MHp = 100 + (self.Lv - 1) * 10
        self.MMp = 10 + (self.Lv - 1) * 10
        self.Atk = 20 + (self.Lv - 1) * 2 + (self.My_Weapon[0][1])
        self.Def = (self.Lv - 1) * 2 + self.My_Aromr[0][1]

    # 血量、蓝变化(p为0时hm_value是血量变化量，p为其他时hm_value是蓝变化量)
    def hp_mp(self, p, hm_value):
        if p == 0:
            if player.My_Hp + hm_value >= player.MHp:
                player.My_Hp = player.MHp
            elif player.My_Hp + hm_value <= 0:
                player.My_Hp = 0
                print('您已阵亡')
            else:
                player.My_Hp += hm_value
            cl.lb_hp1.config(text=f'{player.My_Hp}/{player.MHp}')
        else:
            if player.My_Mp + hm_value >= player.MMp:
                player.My_Mp = player.MMp
            else:
                player.My_Mp += hm_value
            cl.lb_mp1.config(text=f'{player.My_Mp}/{player.MMp}')

    # 金钱、经验值变化
    def gold_exp(self, add_gold, add_exp):
        player.Money += add_gold
        if add_gold > 0:
            cl.txt_infor.insert(0.0, "获得金币%d！\n" % add_gold)
        else:
            cl.txt_infor.insert(0.0, "花费金币%d\n" % add_gold)
        cl.lb_money1.config(text=player.Money)
        if add_exp + player.My_Exp >= player.MExp:
            if player.Lv == 100:
                cl.txt_infor.insert(0.0, "您已满级!无法再升级\n")
            else:
                over_exp = add_exp + player.My_Exp - player.MExp
                player.Lv += 1
                player.renew_data()
                while True:
                    if over_exp >= player.MExp:
                        over_exp -= player.MExp
                        player.Lv += 1
                        player.renew_data()
                        continue
                    else:
                        player.My_Exp = over_exp
                        break

                else:
                    player.My_Exp = over_exp
                player.My_Hp = player.MHp
                player.My_Mp = player.MMp
                cl.lb_lv1.config(text=player.Lv)
                cl.lb_hp1.config(text=f'{player.My_Hp}/{player.MHp}')
                cl.lb_mp1.config(text=f'{player.My_Mp}/{player.MMp}')
                cl.txt_infor.insert(0.0, "升级啦，当前等级为:%d级\n" % player.Lv)
        else:
            if add_exp == 0:
                return
            else:
                player.My_Exp += add_exp
                cl.txt_infor.insert(0.0, "获得经验值%d\n" % add_exp)
        cl.lb_money1.config(text=player.Money)
        cl.lb_exp1.config(text=f'{player.My_Exp}/{player.MExp}')

    # 背包物品变化(变化类型:武器\防具\药剂,编号,变化量)
    def bag_chg(self, typ, number, value):
        item = player.Baggage[typ]
        for i in range(0, len(item), 2):
            if item[i] == number:  # 判断背包中是否已有该编号的物品
                if player.Baggage[typ][i + 1] + value <= 0:  # 如果该物品变化后数目为0
                    player.Baggage[typ][i + 1] = 0
                    cl.renew_bag(p=1)
                    cl.renew_wear(p=1)
                    return
                else:
                    player.Baggage[typ][i + 1] += value  # 已有的该物品数量+value
                    cl.renew_bag(w=1, a=1, p=1)
                    cl.renew_wear(w=1, a=1, p=1)
                    return
        player.Baggage[typ].append(number)
        player.Baggage[typ].append(value)
        if typ == '我的武器':  # 更新装备栏和背包栏信息
            cl.renew_bag(w=1)
            cl.renew_wear(w=1)
        elif typ == '我的防具':
            cl.renew_bag(a=1)
            cl.renew_wear(a=1)
        else:
            cl.renew_bag(p=1)
            cl.renew_wear(p=1)


class Items:
    # weapons 武器一览表，武器编号:(武器名称,攻击力,稀有度颜色,售价)
    weapons = {
        0: ('无', 0, "#fffef9", 0),
        1: ('生锈的短剑', 60, "#f2eada", 50), 2: ('铁剑', 70, "#f2eada", 50),
        3: ('青铜剑', 80, "#90d7ec", 60), 4: ('玄铁剑', 90, "#90d7ec", 60),
        5: ('黄金剑', 100, "#00ae9d", 80), 6: ('青虹镰刀', 110, "#00ae9d", 80),
        7: ('赤炎剑', 120, "#1d953f", 100), 8: ('青影剑', 130, "#1d953f", 100),
        9: ('血月长刃', 145, "#afb4db", 120), 10: ('冥王剑', 155, "#afb4db", 120),
        11: ('雷霆·鸳鸯钺', 170, "#694d9f", 140), 12: ('雷霆·虎慑', 180, "#694d9f", 140),
        13: ('虚空·炎龙', 195, "#f8aba6", 200), 14: ('虚空·裂空斩', 215, "#f8aba6", 200),
        15: ('龙域·龙渊之狱', 230, "#de773f", 250), 16: ('上古·鲲', 270, "#de773f", 250),
        17: ('流光·祝融之怒', 310, "#694d9f", 310), 18: ('流光·天师法杖', 310, "#694d9f", 310),
        99: ('创世·诛仙', 99999, "#fcf16e", 99999, "外挂神器，无法正常获得")
    }
    # armors 装备一览表，装备编号:(装备名称,防御力,稀有度颜色,售价)
    armors = {
        0: ('无', 0, "#fffef9", 0),
        1: ('破旧的布衣', 40, "#f2eada", 50), 2: ('铁锁甲', 50, "#f2eada", 50),
        3: ('青铜锁甲', 60, "#90d7ec", 60), 4: ('玄铁盔甲', 70, "#90d7ec", 60),
        5: ('黄金盔甲', 90, "#00ae9d", 80), 6: ('青光项甲', 100, "#00ae9d", 80),
        7: ('赤炎项甲', 120, "#1d953f", 100), 8: ('彩虹长袍', 130, "#1d953f", 100),
        9: ('长者斗篷', 150, "#afb4db", 120), 10: ('冥王守护', 160, "#afb4db", 120),
        11: ('雷霆·鸳鸯斗篷', 180, "#694d9f", 140), 12: ('雷霆·虎啸刺甲', 190, "#694d9f", 140),
        13: ('虚空·龙吟战袍', 220, "#f8aba6", 200), 14: ('虚空·虚无斗篷', 230, "#f8aba6", 200),
        15: ('龙域·黑龙鳞甲', 250, "#de773f", 250), 16: ('上古·泰坦', 260, "#de773f", 250),
        17: ('流光·蛮王守护', 280, "#694d9f", 310), 18: ('流光·天师长袍', 290, "#694d9f", 310),
        99: ('创世·圣言', 99999, "#fcf16e", 99999, "外挂神器，无法正常获得")
    }
    # 药剂一览表，药剂编号:(药剂名称,回复血量,回复蓝量,售价)
    potions = {
        0: ('无', 0, 0, 0),
        1: ("小瓶Hp药剂", 100, 0, 30), 2: ('中瓶Hp药剂', 200, 0, 70), 3: ('大瓶Hp药剂', 400, 0, 110),
        4: ('特制Hp药剂', 600, 0, 150), 5: ('生命之源', 900, 0, 300),
        6: ("小瓶Mp药剂", 0, 60, 30), 7: ('中瓶Mp药剂', 0, 100, 70), 8: ('大瓶Mp药剂', 0, 150, 110),
        9: ('特制Mp药剂', 0, 200, 150), 10: ('魔力之源', 0, 600, 300)
    }
    # 技能一览表_玩家，技能编号:(技能名称,伤害值(攻击力),所需蓝)
    skills_player = {
        0: ('普通攻击', 40, 0), 1: ('蓄力斩击', 80, 0), 2: ('威慑', 0, 0), 3: ('逃跑', 0, 0),
        4: ('暗影突刺', 80, 6), 5: ('破甲强袭', 100, 9), 6: ('十字斩', 140, 12), 7: ('生命回复', 0, 20), 8: ('恶灵诅咒', 170, 30),
        9: ('乱舞', 220, 40), 10: ('尘虚剑意', 340, 60), 11: ('银月狼爪', 450, 80), 12: ('治愈之心', 550, 90), 13: ('神罚', 610, 150)
    }
    # 技能一览表_怪物，技能编号:(技能名称,伤害值(攻击力))
    skills_monster = {
        0: ('泥浆弹', 30), 1: ('冲撞', 30), 2: ('撕咬', 30),
        3: ('生命虹吸', 30), 4: ('高速冲击', 30), 5: ('寒影蛇息', 30),
        6: ('贯穿长矛', 30), 7: ('砍击', 30), 8: ('冲撞', 30),
        9: ('獠牙击', 30), 10: ('死亡冲撞', 30), 11: ('狂乱', 30),
        12: ('岩浆弹', 30), 13: ('炽热灯火', 30), 14: ('七月流火', 30),
        15: ('食梦', 30), 16: ('幽灵诅咒', 30), 17: ('冲击死光', 30),
        18: ('电磁风暴', 30), 19: ('电弧', 30), 20: ('雷霆之怒', 30),
        21: ('不灭之炎', 30), 22: ('威慑咆哮', 30), 23: ('湮灭', 30),
        24: ('冰咆哮', 30), 25: ('虚无打击', 30), 26: ('扫尾', 30),
        27: ('摄魂夺取', 30), 28: ('骑士之拳', 30), 29: ('堕落深渊', 30),
        30: ('圣光十字', 30), 31: ('破魔圣光', 30), 32: ('传说力量', 30)
    }
    # monster怪物一览表，怪物编号:(怪物名称,攻击力,防御力,血量,基础掉落经验值,基础掉落金币,'(可能使用的技能)')
    monster = {
        0: ('史莱姆', 10, 0, 80, 28, 10, '(0,1)'), 1: ('食人虫', 15, 0, 90, 30, 10, '(0,1)'),
        2: ('巨型食人花', 40, 15, 400, 200, 50, '(0,1,2)'),
        3: ('吸血蝙蝠', 25, 7, 100, 40, 14, '(3,4)'), 4: ('蜘蛛怪', 30, 8, 110, 45, 16, "(3,4)"),
        5: ('独眼蛇怪', 50, 25, 500, 300, 60, '(3,4,5)'),
        6: ('哥布林投手', 40, 15, 150, 70, 20, "(6,7)"), 7: ('哥布林战士', 42, 18, 165, 75, 22, "(6,7)"),
        8: ('哥布林首领', 60, 30, 600, 400, 65, "(6,7,8)"),
        9: ('荒漠狼', 47, 20, 200, 90, 23, "(9,10)"), 10: ('披毛犀', 50, 22, 210, 93, 25, "(9,10)"),
        11: ('魔化剑齿虎', 70, 35, 700, 500, 70, "(9,10,11)"),
        12: ('岩浆虫', 55, 25, 225, 110, 30, "(12,13)"), 13: ('火蜥蜴', 58, 27, 230, 113, 35, "(12,13)"),
        14: ('熔岩领主', 80, 40, 800, 600, 90, "(12,13,14)"),
        15: ('梦魇', 65, 40, 400, 115, 40, '(15,16)'), 16: ('无主幽灵', 68, 45, 410, 117, 45, '(15,16)'),
        17: ('幽冥之主', 90, 45, 900, 700, 110, '(15,16,17)'),
        18: ('雷鸟', 75, 50, 500, 130, 50, '(18,19)'), 19: ('闪电豹', 77, 55, 510, 135, 52, '(18,19)'),
        20: ('雷霆虎王', 120, 55, 1000, 750, 130, '(18,19,20)'),
        21: ('火凤', 90, 70, 610, 155, 57, '(21,22)'), 22: ('浴火麒麟', 95, 75, 620, 160, 59, '(21,22)'),
        23: ('虚空领主', 150, 70, 1100, 810, 150, '(21,22,23)'),
        24: ('冰祝龙', 100, 90, 700, 180, 65, '(24,25)'), 25: ('裂空玄鸟', 110, 100, 720, 185, 67, '(24,25)'),
        26: ('硬甲黑龙', 180, 90, 1200, 920, 160, '(24,25,26)'),
        27: ('堕天使', 120, 100, 800, 208, 70, '(27,28)'), 28: ('暗黑骑士', 130, 110, 820, 210, 74, '(27,28)'),
        29: ('暗黑阿努比斯', 270, 150, 1500, 1100, 170, '(27,28,29)'),
        30: ('六翼天使', 250, 200, 1100, 400, 100, '(30,31)'), 31: ('流光独角兽', 280, 250, 1300, 400, 110, '(30,31)'),
        32: ('远古利维坦', 350, 350, 2000, 1000, 500, '(30,31,32)')
    }


class Action(Warrior):
    def __init__(self):
        self.war_peace = False  # True为战斗中 False为战斗外
        self.boss = False  # True为boss， False为普通小怪
        self.welfare = False  # True战胜boss时的奖励关闭，False为奖励关闭，用于第10层和11层
        self.rounds = False  # True为怪物回合 False玩家回合
        self.monster = Items.monster[0]  # 怪物的数据
        self.monster_name = self.monster[0]
        self.monster_atk = self.monster[1]
        self.monster_def = self.monster[2]
        self.monster_hp = self.monster[3]
        self.monster_skill = self.monster[6]  # 怪物可使用的技能

    # 怪物回合
    def monster_round(self):
        num = rd.choice(eval(self.monster_skill))  # 随机一个技能
        skill = Items.skills_monster[num]  # 随机到的技能信息
        hp_value = self.monster_atk + skill[1] - player.Def  # 造成的伤害=怪物攻击力+怪物技能伤害-玩家防御力
        if hp_value < 0:  # 如果计算出来的的伤害值为负，则伤害值变成1
            hp_value = 1
        player.hp_mp(0, -hp_value)
        cl.lb_hp1.config(text=f'{player.My_Hp}/{player.MHp}')
        cl.txt_infor.insert(0.0, f'{self.monster_name} 使用了: {skill[0]} ,造成了 {hp_value} 点伤害\n')
        self.rounds = False  # 怪物回合结束
        # 判断玩家是否阵亡
        if player.My_Hp <= 0:
            cl.txt_infor.insert(0.0, '很遗憾，您已阵亡！\n游戏结束！\n')
            ac.war_peace = False  # 战斗结束
            self.welfare = False
            Y_N = tkinter.messagebox.askyesno('游戏结束', '您已阵亡，是否复活?(不限次数)')  # 是/否,返回值true/false
            if Y_N:
                cl.txt_infor.insert(0.0, '===========您已复活!==========\n===========战斗终止==========\n')
                player.My_Hp = player.MHp
                player.My_Mp = player.MMp
                cl.lb_hp1.config(text=f'{player.My_Hp}/{player.MHp}')
                cl.lb_mp1.config(text=f'{player.My_Mp}/{player.MMp}')
                return
            else:
                cl.txt_infor.delete(0.0, END)
                cl.txt_infor.insert(0.0, '===========您已开始新游戏==========\n')
                player.Lv = 1
                player.Money = 0
                player.My_Hp = 100
                player.My_Mp = 10
                player.My_Exp = 0
                player.My_Weapon = (Items.weapons[0], 0)  # ((武器数据),武器编号)
                player.My_Aromr = (Items.armors[0], 0)
                player.floor = 1
                player.level = 1
                player.Baggage = {'我的武器': [0, 1], '我的防具': [0, 1], '我的药剂': [0, 1]}
                player.renew_data()
                cl.renew_infor()
                cl.renew_wear(w=1, a=1, p=1)
                cl.renew_bag(w=1, a=1, p=1)
                return

    # 战斗函数(怪物序号)
    def war(self, num):
        ac.war_peace = True  # 切换战斗状态为 战斗中
        self.monster_num = num  # 怪物编号
        self.monster = Items.monster[num]  # 对应的怪物信息
        self.monster_name = self.monster[0]
        self.monster_atk = self.monster[1]
        self.monster_def = self.monster[2]
        self.monster_hp = self.monster[3]
        self.monster_skill = self.monster[6]  # 怪物可使用的技能
        cl.txt_infor.insert(0.0, f'{"战斗开始！":=^20}\n')
        if (num + 1) % 3 == 0:
            self.boss = True  # 确定为boss
            if player.floor < 10:
                self.welfare = True  # 战胜boss时的奖励激活
                cl.txt_infor.insert(0.0, '/////遭遇本层领主!击败可获得专属奖励！/////\n')
            else:
                cl.txt_infor.insert(0.0, '/////////boss较强，谨慎行动////////\n')
            cl.txt_infor.insert(0.0, f'boss信息：\nboss名称:{self.monster_name}, 血量:{self.monster_hp}, '
                                     f'攻击力:{self.monster_atk}, 防御力:{self.monster_def}\n')
        else:
            cl.txt_infor.insert(0.0, f'怪物信息：\n怪物名称:{self.monster_name}, 血量:{self.monster_hp}, '
                                     f'攻击力:{self.monster_atk}, 防御力:{self.monster_def}\n')

    # 读档函数
    def read_data(self):
        try:
            f = open('文字冒险小游戏玩家数据.txt', 'r+', encoding='UTF-8')
            file1 = f.readline()  # 读取文件第一行的内容
            file2 = f.readline()  # 读取文件第二行的内容
            print('读档开始')
            data1 = re.findall("(\(.*?\))", file1)[0]
            data2 = re.findall("(\{.*?\})", file2)[0]
            params = eval(data1)
            baggage = eval(data2)
            player.__init__(params, baggage)
            player.renew_data()
            cl.renew_infor()
            if player.level != 1:  # 判断是否在每层的第一关，不是则关闭窗口
                cl.btn_shop.place(x=0, y=0, width=0, height=0)
            else:
                cl.btn_shop.place(x=650, y=300, width=60, height=50)
            cl.txt_infor.insert(0.0, '存档读取成功！游戏继续！\n')
            print('读档结束')
        except FileNotFoundError:
            cl.txt_infor.insert(0.0, '没有存档或存档出错,将开始新游戏\n')
            cl.txt_infor.insert(0.0, '==========开始新游戏=========\n')
            print('没有存档或存档出错')

    # 存档函数,每5分钟自动存档
    def save_data(self):
        w_items = []
        a_items = []
        p_items = []
        params = (player.Name, player.Lv, player.Money, player.My_Hp, \
                  player.My_Mp, player.My_Exp, player.My_Weapon[1], player.My_Aromr[1],
                  player.floor, player.level)
        for i in range(0, len(player.Baggage['我的武器']), 2):
            if player.Baggage['我的武器'][i + 1] != 0:
                w_items.append(i)  # 武器编号
                w_items.append(player.Baggage['我的武器'][i + 1])  # 武器数量
        for j in range(0, len(player.Baggage['我的防具']), 2):
            if player.Baggage['我的防具'][j + 1] != 0:
                a_items.append(j)
                a_items.append(player.Baggage['我的防具'][j + 1])
        for k in range(0, len(player.Baggage['我的药剂']), 2):
            if player.Baggage['我的药剂'][k + 1] != 0:
                p_items.append(k)
                p_items.append(player.Baggage['我的药剂'][k + 1])
        f = open('文字冒险小游戏玩家数据.txt', 'w+', encoding='UTF-8')
        f.write(f'人物基本数据：{params}\n')
        f.write("背包数据：{'我的武器':%s,'我的防具':%s,'我的药剂':%s}" % (w_items, a_items, p_items))
        f.close()
        cl.txt_infor.insert(0.0, '保存成功\n')
        print('保存成功')

    # 金手指添加物品函数,可选择添加其中一项(等级,金钱,药剂,武器,防具,数量,编号)
    def vip_add(self, lv=0, moy=0, p=0, w=0, a=0, num=0, item=0):
        if item == -1:
            print('未选中')
            return
        elif num == '':
            print('未输入数值')
            return
        try:
            num = int(num)
            if lv:
                lv_num = num
                if player.Lv + lv_num < 1:
                    player.Lv = 1
                    cl.txt_infor.insert(0.0, f'等级降低{-lv_num},当前等级Lv=1\n')
                elif player.Lv + lv_num > 100:
                    player.Lv = 100
                    cl.txt_infor.insert(0.0, f'等级增加{lv_num},当前等级Lv=100\n')
                else:
                    player.Lv += lv_num
                    cl.txt_infor.insert(0.0, f'等级增加{lv_num},当前等级Lv={player.Lv}\n')
                player.renew_data()
                cl.lb_lv1.config(text=player.Lv)
                cl.lb_exp1.config(text=f'{player.My_Exp}/{player.MExp}')
                cl.lb_hp1.config(text=f'{player.My_Hp}/{player.MHp}')
                cl.lb_mp1.config(text=f'{player.My_Mp}/{player.MMp}')
            if moy:
                moy_num = num
                if player.Money + moy_num <= 0:
                    player.gold_exp(-player.Money, 0)
                else:
                    player.gold_exp(moy_num, 0)
            if p:
                potion_num = num
                if potion_num < 0:  # 输入的数量如果小于0，则默认+1
                    potion_num = 1
                player.bag_chg('我的药剂', item, potion_num)
                cl.txt_infor.insert(0.0, f'---获得药剂“{Items.potions[item][0]}”×{potion_num}\n')
            if w:
                if item == 19:
                    player.bag_chg('我的武器', 99, 1)
                    cl.txt_infor.insert(0.0, '>>>获得神器:“创世·诛仙”×1\n')
                else:
                    player.bag_chg("我的武器", item, 1)
                    cl.txt_infor.insert(0.0, f'---获得武器:“{Items.weapons[item][0]}”×1\n')
            if a:
                if item == 19:
                    player.bag_chg('我的防具', 99, 1)
                    cl.txt_infor.insert(0.0, '>>>获得神器:“创世·圣言”×1\n')
                else:
                    player.bag_chg("我的防具", item, 1)
                    cl.txt_infor.insert(0.0, f'---获得防具:“{Items.armors[item][0]}”×1\n')
        except:
            print("获取出错")

    # 打开金手指窗口
    def vip(self):
        win1 = Toplevel(root)  # 金手指窗体
        win1.geometry('260x170+30+100')
        win1.title('金手指')
        cv = Canvas(win1, width="260", height="200", bg="pink")  # 制作画布，在窗口中设置
        cv.place(x=0, y=0)

        inp_lv = Entry(win1)
        inp_lv.place(x=100, y=10, width=40, height=20)
        btn_addlv = Button(win1, text='等级增加', bg='#afb4db', font=('黑体', 12),
                           command=(lambda: ac.vip_add(lv=1, num=inp_lv.get())))
        btn_addlv.place(x=15, y=10, width=80, height=20)  # 等级增加按钮

        inp_gold = Entry(win1)
        inp_gold.place(x=100, y=40, width=40, height=20)
        btn_addgold = Button(win1, text='金钱增加', bg='#afb4db', font=('黑体', 12),
                             command=(lambda: ac.vip_add(moy=1, num=inp_gold.get())))  # 金钱增加按钮
        btn_addgold.place(x=15, y=40, width=80, height=20)

        inp_p = Entry(win1)
        inp_p.place(x=100, y=70, width=40, height=20)
        var1 = StringVar()
        items_p = []
        for i in range(0, 11):
            items_p.append(Items.potions[i][0])
        comb1 = tkinter.ttk.Combobox(win1, textvariable=var1, value=items_p)  # 药剂的组合选择框
        comb1.place(x=150, y=70, width=90, height=20)
        btn_getp = Button(win1, text='获得药剂', bg='#afb4db', font=('黑体', 12),
                          command=(lambda: ac.vip_add(p=1, num=inp_p.get(), item=comb1.current())))  # 药剂获得按钮
        btn_getp.place(x=15, y=70, width=80, height=20)

        var2 = StringVar()
        items_w = []
        for j in range(0, 19):
            items_w.append(Items.weapons[j][0])
        items_w.append(Items.weapons[99][0])
        comb2 = tkinter.ttk.Combobox(win1, textvariable=var2, value=items_w)  # 武器的组合选择框
        comb2.place(x=100, y=100, width=110, height=20)
        btn_getw = Button(win1, text='获得武器', bg='#afb4db', font=('黑体', 12),
                          command=(lambda: ac.vip_add(w=1, item=comb2.current())))  # 获得武器按钮
        btn_getw.place(x=15, y=100, width=80, height=20)

        var3 = StringVar()
        items_a = []
        for k in range(0, 19):
            items_a.append(Items.armors[k][0])
        items_a.append(Items.armors[99][0])
        comb3 = tkinter.ttk.Combobox(win1, textvariable=var3, value=items_a)  # 防具的组合选择框
        comb3.place(x=100, y=130, width=110, height=20)
        btn_geta = Button(win1, text='获得防具', bg='#afb4db', font=('黑体', 12),
                          command=(lambda: ac.vip_add(a=1, item=comb3.current())))  # 获得防具按钮
        btn_geta.place(x=15, y=130, width=80, height=20)

    # 修改昵称
    def id_edit(self):
        new_id = askstring('改名', '请输入玩家名字')
        player.Name = new_id
        cl.lb_name1.config(text=new_id)

    # 探索函数
    def explore(self):
        if ac.war_peace:  # True为战斗内,False在战斗外
            cl.txt_infor.insert(0.0, '战斗中，无法探索！\n')
        elif player.floor == 11:
            monster = rd.choice([30, 31])
            cl.txt_infor.insert(0.0, '///遭遇最后一层守卫 "%s"///\n' % Items.monster[monster][0])
            ac.war(monster)
        else:
            event = rd.choice(['无事发生', '遇到怪物!', '发现了一个宝箱！'])
            if event == '遇到怪物!':
                monster = rd.choice([player.floor * 3 - 3, player.floor * 3 - 2])
                ac.war(monster)
                cl.txt_infor.insert(0.0, "！！遇到怪物！！\n")
            elif event == '发现了一个宝箱！':
                cl.txt_infor.insert(0.0, ">>>发现了一个宝箱<<<\n")
                if player.floor == 10:
                    item = rd.choices(['我的药剂', '金钱'], weights=[1, 1])
                else:
                    item = rd.choices(['我的武器', '我的防具', '我的药剂', '金钱'], weights=[1, 1, 2, 2])
                if item[0] == '金钱':
                    gold = player.floor * 6
                    player.gold_exp(gold, 0)
                elif item[0] == '我的药剂':
                    number = rd.choice([round(player.floor / 2 + 0.2), round(player.floor / 2 + 5)])
                    player.bag_chg(item[0], number, 1)
                    cl.txt_infor.insert(0.0, '获得药剂“%s”×1\n' % (Items.potions[number][0]))
                elif item[0] == '我的武器':
                    number = player.floor * 2 - 1
                    player.bag_chg(item[0], number, 1)
                    cl.txt_infor.insert(0.0, '获得武器“%s”×1\n' % (Items.weapons[number][0]))
                else:
                    number = player.floor * 2 - 1
                    player.bag_chg(item[0], number, 1)
                    cl.txt_infor.insert(0.0, '获得防具“%s”×1\n' % (Items.armors[number][0]))
                walfale = 0
            else:
                cl.txt_infor.insert(0.0, "无事发生\n")

    # 上一关
    def backlevel(self):
        if ac.war_peace:  # True为战斗内,False在战斗外
            cl.txt_infor.insert(0.0, '战斗中，无法前往上一关！\n')
            return
        else:
            if player.level == 1:
                if player.floor == 1:
                    cl.txt_infor.insert(0.0, '当前在第一关,无法再后退\n')
                    return
                else:
                    player.floor -= 1
                    player.level = 5
            else:
                player.level -= 1
        if player.level != 1:
            cl.btn_shop.place(x=0, y=0, width=0, height=0)
        else:
            cl.btn_shop.place(x=650, y=300, width=60, height=50)
        cl.txt_infor.insert(0.0, '成功前往上一关，当前在%d-%d\n' % (player.floor, player.level))
        cl.lb_level1.config(text=f'{player.floor}-{player.level}')

    # 下一关
    def nextlevel(self):
        if ac.war_peace:  # 判断是否在战斗中，True为战斗内,False在战斗外
            cl.txt_infor.insert(0.0, '战斗中，无法前往下一关！\n')
            return
        elif player.floor == 11:  # 判断是否在最后一层
            if player.level == 5:
                boss_war = tkinter.messagebox.askyesno(
                    '最终boss', '即将挑战本游戏最终boss\n是否继续？')  # 是/否，返回值true/false
                if boss_war:
                    num = player.floor * 3 - 1
                    ac.war(num)
                    return
            else:
                player.level += 1
        else:
            if player.level == 5:
                boss_war = tkinter.messagebox.askyesno(
                    '遭遇强敌', '继续前往下一关需要先挑战本层boss\n是否继续？')  # 是/否，返回值true/false
                if boss_war:
                    num = player.floor * 3 - 1
                    ac.war(num)
                    return
                else:
                    pass
            else:
                player.level += 1
        if player.level != 1:
            cl.btn_shop.place(x=0, y=0, width=0, height=0)
        else:
            cl.btn_shop.place(x=650, y=300, width=60, height=50)
        cl.txt_infor.insert(0.0, '成功前往下一关，当前在%d-%d\n' % (player.floor, player.level))
        cl.lb_level1.config(text=f'{player.floor}-{player.level}')

    # 购买商品(购买武器,防具,药剂,是否购买)
    def shop_buy(self, w_num=0, a_num=0, p_num=0):
        if w_num:
            price = Items.weapons[w_num][3]
            if player.Money < price:
                cl.txt_infor.insert(0.0, '金钱不足\n')
            else:
                player.gold_exp(-price, 0)
                player.bag_chg('我的武器', w_num, 1)
                cl.txt_infor.insert(0.0, '购买成功！\n')
        elif a_num:
            price = Items.armors[a_num][3]
            if player.Money < price:
                cl.txt_infor.insert(0.0, '金钱不足\n')
            else:
                player.gold_exp(-price, 0)
                player.bag_chg('我的防具', a_num, 1)
                cl.txt_infor.insert(0.0, '购买成功！\n')
        elif p_num:
            price = Items.potions[p_num][3]
            if player.Money < price:
                cl.txt_infor.insert(0.0, '金钱不足\n')
            else:
                player.gold_exp(-price, 0)
                player.bag_chg('我的药剂', p_num, 1)
                cl.txt_infor.insert(0.0, '购买成功！\n')
        else:
            pass

    # 打开商店窗口
    def shop_win(self, price=0):
        win = Toplevel(root)
        win.title("商店")
        win.geometry('310x150+600+200')
        cv = Canvas(win, width="310", height="150", bg="#d3d7d4")  # 制作画布，在窗口中放置
        cv.place(x=0, y=0)

        lb_price1 = Label(win, text='售价', bg='#afb4db', font=('黑体', 12))
        lb_price1.place(x=210, y=10, width=80, height=20)
        var1 = StringVar()
        items_w = []
        i = 0
        for i in range(0, 19):
            items_w.append(Items.weapons[i][0])
        comb1 = tkinter.ttk.Combobox(win, textvariable=var1, value=items_w)
        comb1.place(x=100, y=10, width=100, height=20)
        comb1.bind('<<ComboboxSelected>>',
                   lambda event: lb_price1.config(text=f"售价:{Items.weapons[comb1.current()][3]}"))
        btn_buy_w = Button(win, text='购买武器', bg='#fab27b', font=('黑体', 12),
                           command=lambda: ac.shop_buy(w_num=comb1.current()))
        btn_buy_w.place(x=15, y=10, width=80, height=20)  # 购买武器按钮

        lb_price2 = Label(win, text='售价', bg='#afb4db', font=('黑体', 12))
        lb_price2.place(x=210, y=50, width=80, height=20)
        var2 = StringVar()
        items_a = []
        i = 0
        for i in range(0, 19):
            items_a.append(Items.armors[i][0])
        comb2 = tkinter.ttk.Combobox(win, textvariable=var2, value=items_a)
        comb2.place(x=100, y=50, width=100, height=20)
        comb2.bind('<<ComboboxSelected>>',
                   lambda event: lb_price2.config(text=f"售价:{Items.armors[comb2.current()][3]}"))
        btn_buy_a = Button(win, text='购买防具', bg='#fab27b', font=('黑体', 12),
                           command=lambda: ac.shop_buy(a_num=comb2.current()))
        btn_buy_a.place(x=15, y=50, width=80, height=20)  # 购买防具按钮

        lb_price3 = Label(win, text='售价', bg='#afb4db', font=('黑体', 12))
        lb_price3.place(x=210, y=90, width=80, height=20)
        var3 = StringVar()
        items_p = []
        i = 0
        for i in range(0, 11):
            items_p.append(Items.potions[i][0])
        comb3 = tkinter.ttk.Combobox(win, textvariable=var3, value=items_p)
        comb3.place(x=100, y=90, width=100, height=20)
        comb3.bind('<<ComboboxSelected>>',
                   lambda event: lb_price3.config(text=f"售价:{Items.potions[comb3.current()][3]}"))
        btn_buy_p = Button(win, text='购买药剂', bg='#fab27b', font=('黑体', 12),
                           command=lambda: ac.shop_buy(p_num=comb3.current()))
        btn_buy_p.place(x=15, y=90, width=80, height=20)  # 购买药剂按钮

    # 穿戴装备/防具/使用药剂（武器,防具,药剂,装备在背包内的位置）
    def wear_w_a_p(self, w=0, a=0, p=0, num=0):
        try:
            if num < 0:
                print('未选中任何武器/防具/药剂')
                return
            else:
                num = num * 2
            if w:
                if ac.war_peace:
                    cl.txt_infor.insert(0.0, '战斗中不能更换装备\n')
                    return
                else:
                    item = player.Baggage['我的武器'][num]  # 此时item为武器所在Item库中的的序号
                    player.My_Weapon = (Items.weapons[item], item)
                    cl.lb_weapon1.config(text=Items.weapons[item][0], bg=player.My_Weapon[0][2])
                    cl.txt_infor.insert(0.0, f'成功装备武器“{Items.weapons[item][0]}”\n')
            if a:
                if ac.war_peace:
                    cl.txt_infor.insert(0.0, '战斗中不能更换装备\n')
                    return
                else:
                    item = player.Baggage['我的防具'][num]  # 此时item为防具所在Item库中的的序号
                    player.My_Aromr = (Items.armors[item], item)
                    cl.lb_armor1.config(text=Items.armors[item][0], bg=player.My_Aromr[0][2])
                    cl.txt_infor.insert(0.0, f'成功装备防具“{Items.armors[item][0]}”\n')
            if p:
                if num == 0:
                    return
                if player.Baggage['我的药剂'][num + 1] < 1:
                    cl.txt_infor.insert(0.0, '药剂数量不足，无法使用\n')
                else:
                    item = player.Baggage['我的药剂'][num]  # 此时item为药剂所在Item库中的的序号
                    if item < 6:  # 序号1-5是血瓶
                        player.Baggage['我的药剂'][num + 1] -= 1
                        player.hp_mp(0, Items.potions[item][1])
                        cl.txt_infor.insert(0.0, f'使用了{Items.potions[item][0]},血量增加{Items.potions[item][1]}\n')
                    else:
                        player.Baggage['我的药剂'][num + 1] -= 1
                        player.hp_mp(1, Items.potions[item][2])
                        cl.txt_infor.insert(0.0, f'使用了{Items.potions[item][0]},魔法值增加{Items.potions[item][2]}\n')
                    cl.renew_bag(p=1)
            player.renew_data()
        except:
            print('出错')

    # 背包栏选中的装备信息
    def infor_w_a_p(self, w=0, a=0, p=0):
        if w:
            num = cl.w_list.curselection()[0]
            item = player.Baggage['我的武器'][num * 2]  # 此时item是Item中武器对应的编号
            cl.w_infor.config(text=f'攻击力：\n{Items.weapons[item][1]}')
        if a:
            num = cl.a_list.curselection()[0]
            item = player.Baggage['我的防具'][num * 2]  # 此时item是Item中防具对应的编号
            cl.a_infor.config(text=f'防御力：\n{Items.armors[item][1]}')
        if p:
            num = cl.p_list.curselection()[0]
            item = player.Baggage['我的药剂'][num * 2]  # 此时item是Item中药剂对应的编号
            cl.p_infor.config(text=f'回血量:{Items.potions[item][1]}\n回蓝量:{Items.potions[item][2]}')

    # 玩家使用技能(技能编号,技能使用所需等级)
    def use_skill(self, num, able):
        if ac.war_peace:
            if self.rounds:
                cl.txt_infor.insert(0.0, '当前是怪物回合,无法使用技能\n')
                return
            else:
                need_mp = Items.skills_player[num][2]
                if player.Lv < able:
                    cl.txt_infor.insert(0.0, '等级不足，%d级才能使用\n' % able)
                    return
                elif player.My_Mp < need_mp:
                    cl.txt_infor.insert(0.0, '当前魔法值不足,使用失败,所需魔法值:%d\n' % need_mp)
                    return
                else:
                    if num < 3:
                        skill_name = Items.skills_player[num][0]
                        hp_lavue = Items.skills_player[num][1] + player.Atk
                        self.monster_hp -= hp_lavue
                        cl.txt_infor.insert(0.0, f'{player.Name}使用了 {skill_name} 造成了 {hp_lavue} 点伤害\n')
                        self.rounds = True
                    elif num == 3:
                        ac.war_peace = False
                        self.rounds = False
                        cl.txt_infor.insert(0.0, '=====逃跑成功，战斗结束=====\n')
                        return
                    elif num == 7:
                        skill_name = Items.skills_player[num][0]
                        hp_lavue = int(player.MHp * 0.1)  # '生命回复'技能增加最大生命值的10%
                        player.hp_mp(1, -need_mp)
                        player.hp_mp(0, hp_lavue)
                        cl.txt_infor.insert(0.0, f'{player.Name}使用了 {skill_name},生命值增加{hp_lavue}\n')
                    elif num == 12:
                        skill_name = Items.skills_player[num][0]
                        hp_lavue = int(player.MHp * 0.3)  # '治愈之心'技能增加最大生命值的30%'
                        player.hp_mp(1, -need_mp)
                        player.hp_mp(0, hp_lavue)
                        cl.txt_infor.insert(0.0, f'{player.Name}使用了 {skill_name},生命值增加{hp_lavue}\n')
                    else:
                        skill_name = Items.skills_player[num][0]
                        hp_lavue = Items.skills_player[num][1] + int(player.Atk * 0.6)  # 技能造成的伤害值等于武器攻击力加60%玩家攻击力
                        player.hp_mp(1, -need_mp)
                        self.monster_hp -= hp_lavue
                        cl.txt_infor.insert(0.0, f'{player.Name}使用了 {skill_name} 造成了 {hp_lavue} 点伤害\n')
                        self.rounds = True
                    if self.monster_hp <= 0:
                        cl.txt_infor.insert(0.0, "怪物已阵亡，战斗胜利！\n")
                        add_gold = int(self.monster[5] * rd.uniform(1.0, 1.3))  # 掉落金币在基础值上增加0到0.3倍
                        add_exp = int(self.monster[4] * rd.uniform(1.0, 1.3))
                        player.gold_exp(add_gold, add_exp)
                        if self.boss:
                            self.boss = False
                            if self.welfare:
                                num = int((self.monster_num + 1) / 3 * 2)  # 获取武器的编号
                                typ = rd.choice(["我的武器", "我的防具"])
                                self.welfare = False
                                if typ == "我的武器":
                                    player.bag_chg(typ, num, 1)
                                    cl.txt_infor.insert(0.0, f'获得boss专属武器{Items.weapons[num][0]}×1\n')
                                else:
                                    player.bag_chg(typ, num, 1)
                                    cl.txt_infor.insert(0.0, f'获得boss专属防具{Items.armors[num][0]}×1\n')
                                player.floor += 1
                                player.level = 1
                                cl.btn_shop.place(x=650, y=300, width=60, height=50)
                                cl.lb_level1.config(text=f'{player.floor}-{player.level}')
                            elif player.floor == 10:
                                player.floor += 1
                                player.level = 1
                                cl.btn_shop.place(x=650, y=300, width=60, height=50)
                                cl.txt_infor.insert(0.0, "本层boss没有专属奖励\n")
                                cl.lb_level1.config(text=f'{player.floor}-{player.level}')
                            else:
                                player.floor = 11
                                player.level = 5
                                cl.txt_infor.insert(0.0, '>>>您已战胜最后一关boss，恭喜通关!<<<')
                                # cl.txt_infor.insert(0.0,
                                #                     '===========&#9836;&#9834;&#10026;&#10026;&#10026;&#10026;&#10026;&#9834;&#9836;==========')
                                print('您已战胜最后一关boss，恭喜通关!')
                        cl.txt_infor.insert(0.0, f"{'战斗结束':=^20}\n")
                        self.war_peace = False
                        self.rounds = False
                        return
                    else:
                        ac.monster_round()
        else:
            cl.txt_infor.insert(0.0, '当前不在战斗内，无法使用技能\n')


# 初始化玩家信息
player = Warrior()
ac = Action()


# 按钮类
class Control:
    # 菜单栏
    mainmenu = Menu(root)
    menuFile = Menu(mainmenu)

    mainmenu.add_cascade(label='文件', menu=menuFile)
    menuFile.add_command(label='保存存档', command=ac.save_data)
    menuFile.add_command(label='读取存档', command=ac.read_data)

    menuEdit = Menu(mainmenu)
    mainmenu.add_cascade(label='工具', menu=menuEdit)
    menuEdit.add_command(label='金手指', command=ac.vip)
    root.config(menu=mainmenu)
    # 菜单栏结束

    # 个人信息栏
    lb_infor = Label(root, text='个人信息', bg='#f391a9', bd=2, font=('黑体', 20))
    lb_infor.place(x=50, y=40, width=150, height=50)

    lb_name0 = Label(root, text='昵称:', bg='pink', font=('黑体', 10))
    lb_name0.place(x=15, y=100, width=50, height=20)
    lb_name1 = Label(root, text=player.Name, bg='#f391a9', font=('黑体', 15))  # 名字变量
    lb_name1.place(x=80, y=100, width=150, height=20)
    btn_id_edit = Button(root, text='&#9998;', bg='#cde6c7', font=('黑体', 20), command=ac.id_edit)
    btn_id_edit.place(x=225, y=100, width=20, height=20)

    lb_lv0 = Label(root, text='当前等级:', bg='pink', font=('黑体', 10))
    lb_lv0.place(x=15, y=135, width=80, height=20)
    lb_lv1 = Label(root, text=player.Lv, font=('黑体', 15))  # 等级变量
    lb_lv1.place(x=100, y=135, width=145, height=20)

    lb_exp0 = Label(root, text='当前经验:', bg='pink', font=('黑体', 10))
    lb_exp0.place(x=15, y=170, width=80, height=20)
    lb_exp1 = Label(root, text=f'{player.My_Exp}/{player.MExp}', font=('黑体', 13))  # 当前经验变量
    lb_exp1.place(x=100, y=170, width=145, height=20)

    lb_hp0 = Label(root, text='剩余生命:', bg='pink', font=('黑体', 10))
    lb_hp0.place(x=15, y=205, width=80, height=20)
    lb_hp1 = Label(root, text=f"{player.My_Hp}/{player.MHp}", font=('黑体', 13))  # 当前生命变量
    lb_hp1.place(x=100, y=205, width=145, height=20)

    lb_mp0 = Label(root, text='剩余魔法:', bg='pink', font=('黑体', 10))
    lb_mp0.place(x=15, y=240, width=80, height=20)
    lb_mp1 = Label(root, text=f'{player.My_Mp}/{player.MMp}', font=('黑体', 13))  # 当前魔法变量
    lb_mp1.place(x=100, y=240, width=145, height=20)

    lb_money0 = Label(root, text='持有金钱:', bg='pink', font=('黑体', 10))
    lb_money0.place(x=15, y=275, width=80, height=20)
    lb_money1 = Label(root, text=player.Money, font=('黑体', 15))  # 金钱变量
    lb_money1.place(x=100, y=275, width=145, height=20)

    lb_weapon0 = Label(root, text='当前武器:', bg='pink', font=('黑体', 10))
    lb_weapon0.place(x=15, y=305, width=80, height=20)
    lb_weapon1 = Label(root, text=player.My_Weapon[0][0], bg=player.My_Weapon[0][2], font=('黑体', 13))  # 当前武器变量
    lb_weapon1.place(x=100, y=305, width=145, height=20)

    lb_armor0 = Label(root, text='当前防具:', bg='pink', font=('黑体', 10))
    lb_armor0.place(x=15, y=340, width=80, height=20)
    lb_armor1 = Label(root, text=player.My_Aromr[0][0], bg=player.My_Aromr[0][2], font=('黑体', 13))  # 当前防具变量
    lb_armor1.place(x=100, y=340, width=145, height=20)

    lb_level0 = Label(root, text='当前关卡:', bg='pink', font=('黑体', 10))
    lb_level0.place(x=15, y=375, width=80, height=20)
    lb_level1 = Label(root, text=f'{player.floor}-{player.level}', bg='#f2eada', font=('黑体', 13))  # 当前关卡变量
    lb_level1.place(x=100, y=375, width=145, height=20)
    # 个人信息栏结束

    # 操作栏
    btn_explore = Button(root, text='探索本层', bg='#d3d7d4', font=('黑体', 15), command=ac.explore)
    btn_explore.place(x=50, y=420, width=150, height=40)

    btn_backlevel = Button(root, text='上一关', bg='#d3d7d4', font=('黑体', 15), command=ac.backlevel)
    btn_backlevel.place(x=50, y=480, width=150, height=40)

    btn_nextlevel = Button(root, text='下一关', bg='#d3d7d4', font=('黑体', 15), command=ac.nextlevel)
    btn_nextlevel.place(x=50, y=540, width=150, height=40)

    lb_fight = Label(root, text='战斗行动', fg='#006c54', font=('黑体', 12))
    lb_fight.place(x=260, y=405, width=80, height=20)

    lb_basic_action = Label(root, text='基本技能:', fg='#006c54', font=('黑体', 15))
    lb_basic_action.place(x=260, y=430, width=100, height=40)

    lb_special_action = Label(root, text='特殊技能:', fg='#006c54', font=('黑体', 15))
    lb_special_action.place(x=260, y=480, width=100, height=40)

    btn_basic_skill0 = Button(root, text=Items.skills_player[0][0], bg='#d3d7d4',
                              font=('黑体', 12), command=lambda: ac.use_skill(0, 0))  # 传入的参数:(技能编号,使用等级)，下同
    btn_basic_skill0.place(x=370, y=430, width=70, height=30)

    btn_basic_skill1 = Button(root, text=Items.skills_player[1][0], bg='#d3d7d4',
                              font=('黑体', 12), command=lambda: ac.use_skill(1, 0))
    btn_basic_skill1.place(x=460, y=430, width=70, height=30)

    btn_basic_skill2 = Button(root, text=Items.skills_player[2][0], bg='#d3d7d4',
                              font=('黑体', 12), command=lambda: ac.use_skill(2, 0))
    btn_basic_skill2.place(x=550, y=430, width=70, height=30)

    btn_basic_skill3 = Button(root, text=Items.skills_player[3][0], bg='#d3d7d4',
                              font=('黑体', 12), command=lambda: ac.use_skill(3, 0))
    btn_basic_skill3.place(x=640, y=430, width=70, height=30)

    btn_special_skill4 = Button(root, text=Items.skills_player[4][0], bg='#d3d7d4',
                                font=('黑体', 12), command=lambda: ac.use_skill(4, 5))
    btn_special_skill4.place(x=370, y=480, width=70, height=30)

    btn_special_skill5 = Button(root, text=Items.skills_player[5][0], bg='#d3d7d4',
                                font=('黑体', 12), command=lambda: ac.use_skill(5, 10))
    btn_special_skill5.place(x=460, y=480, width=70, height=30)

    btn_special_skill6 = Button(root, text=Items.skills_player[6][0], bg='#d3d7d4',
                                font=('黑体', 12), command=lambda: ac.use_skill(6, 15))
    btn_special_skill6.place(x=550, y=480, width=70, height=30)

    btn_special_skill7 = Button(root, text=Items.skills_player[7][0], bg='#d3d7d4',
                                font=('黑体', 12), command=lambda: ac.use_skill(7, 25))
    btn_special_skill7.place(x=640, y=480, width=70, height=30)

    btn_special_skill8 = Button(root, text=Items.skills_player[8][0], bg='#d3d7d4',
                                font=('黑体', 12), command=lambda: ac.use_skill(8, 35))
    btn_special_skill8.place(x=370, y=520, width=70, height=30)

    btn_special_skill9 = Button(root, text=Items.skills_player[9][0], bg='#d3d7d4',
                                font=('黑体', 12), command=lambda: ac.use_skill(9, 45))
    btn_special_skill9.place(x=460, y=520, width=70, height=30)

    btn_special_skill10 = Button(root, text=Items.skills_player[10][0], bg='#d3d7d4',
                                 font=('黑体', 12), command=lambda: ac.use_skill(10, 55))
    btn_special_skill10.place(x=550, y=520, width=70, height=30)

    btn_special_skill11 = Button(root, text=Items.skills_player[11][0], bg='#d3d7d4',
                                 font=('黑体', 12), command=lambda: ac.use_skill(11, 65))
    btn_special_skill11.place(x=640, y=520, width=70, height=30)

    btn_special_skill12 = Button(root, text=Items.skills_player[12][0], bg='#d3d7d4',
                                 font=('黑体', 12), command=lambda: ac.use_skill(12, 75))
    btn_special_skill12.place(x=370, y=560, width=70, height=30)

    btn_special_skill13 = Button(root, text=Items.skills_player[13][0], bg='#d3d7d4',
                                 font=('黑体', 12), command=lambda: ac.use_skill(13, 85))
    btn_special_skill13.place(x=460, y=560, width=70, height=30)

    items_w = []
    i = 0
    for i in range(0, len(player.Baggage['我的武器']), 2):
        items_w.append(Items.weapons[player.Baggage['我的武器'][i]][0])
    var0 = StringVar()
    comb_w = tkinter.ttk.Combobox(root, textvariable=var0, value=items_w)
    comb_w.place(x=850, y=430, width=100, height=30)
    btn_wear_w = Button(root, text='装备武器', bg='#d3d7d4', font=('黑体', 12),
                        command=(lambda: ac.wear_w_a_p(w=1, num=cl.comb_w.current())))
    btn_wear_w.place(x=760, y=430, width=80, height=30)  # 装备武器按钮

    items_a = []
    for j in range(0, len(player.Baggage['我的防具']), 2):
        items_a.append(Items.armors[player.Baggage['我的防具'][j]][0])
    var1 = StringVar()
    comb_a = tkinter.ttk.Combobox(root, textvariable=var1, value=items_a)
    comb_a.place(x=850, y=480, width=100, height=30)
    btn_wear_a = Button(root, text='装备防具', bg='#d3d7d4', font=('黑体', 12),
                        command=(lambda: ac.wear_w_a_p(a=1, num=cl.comb_a.current())))
    btn_wear_a.place(x=760, y=480, width=80, height=30)  # 装备防具按钮

    items_p = []
    for k in range(0, len(player.Baggage['我的药剂']), 2):
        # if player.Baggage['我的药剂'][k+1] != 0:
        items_p.append(Items.potions[player.Baggage['我的药剂'][k]][0])
    var2 = StringVar()
    comb_p = tkinter.ttk.Combobox(root, textvariable=var2, value=items_p)
    comb_p.place(x=850, y=530, width=100, height=30)
    btn_drink_p = Button(root, text='饮用药剂', bg='#d3d7d4', font=('黑体', 12),
                         command=(lambda: ac.wear_w_a_p(p=1, num=cl.comb_p.current())))
    btn_drink_p.place(x=760, y=530, width=80, height=30)  # 使用药剂按钮
    # 操作栏结束

    # 背包栏
    lb_bag = Label(root, text='背包', bg='#f391a9', bd=2, font=('黑体', 20))
    lb_bag.place(x=830, y=20, width=100, height=30)

    lb_my_wearpon = Label(root, text='我的武器', bg='pink', bd=2, font=('黑体', 12))
    lb_my_wearpon.place(x=760, y=60, width=80, height=20)
    list_var0 = StringVar()
    w_list = Listbox(root, listvariable=list_var0, font=('黑体', 12))
    for l in range(0, len(player.Baggage['我的武器']), 2):
        w_list.insert(END, f'{Items.weapons[player.Baggage["我的武器"][l]][0]}×{player.Baggage["我的武器"][l + 1]}')
    w_list.place(x=840, y=80, width=150, height=100)
    w_list.bind('<ButtonRelease-1>', (lambda event: ac.infor_w_a_p(w=1)))  # 当鼠标点击背包内的物品时，调用函数
    w_infor = Label(root, text='攻击力：\n', bg='#f2eada', font=('黑体', 12))
    w_infor.place(x=760, y=110, width=80, height=40)

    lb_my_aromr = Label(root, text='我的防具', bg='pink', bd=2, font=('黑体', 12))
    lb_my_aromr.place(x=760, y=180, width=80, height=20)
    list_var1 = StringVar()
    a_list = Listbox(root, listvariable=list_var1, font=('黑体', 12))
    j = 0
    for j in range(0, len(player.Baggage['我的防具']), 2):
        a_list.insert(END, f'{Items.armors[player.Baggage["我的防具"][j]][0]}×{player.Baggage["我的防具"][j + 1]}')
    a_list.place(x=840, y=200, width=150, height=100)
    a_list.bind('<ButtonRelease-1>', lambda event: ac.infor_w_a_p(a=1))  # 当鼠标点击背包内的物品时，调用函数
    a_infor = Label(root, text='防御力：\n', bg='#f2eada', font=('黑体', 12))
    a_infor.place(x=760, y=230, width=80, height=40)

    list_var2 = StringVar()
    lb_my_potions = Label(root, text='我的药剂', bg='pink', bd=2, font=('黑体', 12))
    lb_my_potions.place(x=760, y=300, width=80, height=20)
    p_list = Listbox(root, listvariable=list_var2, font=('黑体', 12))
    k = 0
    for k in range(0, len(player.Baggage['我的药剂']), 2):
        # if player.Baggage['我的药剂'][k + 1] != 0:
        p_list.insert(END, f'{Items.potions[player.Baggage["我的药剂"][k]][0]}×{player.Baggage["我的药剂"][k + 1]}')
    p_list.place(x=840, y=320, width=150, height=70)
    p_list.bind('<ButtonRelease-1>', lambda event: ac.infor_w_a_p(p=1))  # 当鼠标点击背包内的物品时，调用函数
    p_infor = Label(root, text='回血量:\n回蓝量:', bg='#f2eada', font=('黑体', 12))
    p_infor.place(x=760, y=340, width=80, height=40)
    # 背包栏结束

    # 消息栏
    txt_infor = Text(root, bg='#f2eada', font=('黑体', 12))
    txt_infor.place(x=255, y=10, width=490, height=380)
    l = 0

    # 商店按钮
    btn_shop = Button(root, text='商店', bg='#d3d7d4', command=ac.shop_win)
    btn_shop.place(x=650, y=300, width=60, height=50)

    # 更新信息栏所有信息(昵称,等级,经验,生命,魔法,金钱,武器,防具,关卡)
    def renew_infor(self):
        cl.lb_name1.config(text=player.Name)
        cl.lb_lv1.config(text=player.Lv)
        cl.lb_exp1.config(text=f'{player.My_Exp}/{player.MExp}')
        cl.lb_hp1.config(text=f'{player.My_Hp}/{player.MHp}')
        cl.lb_mp1.config(text=f'{player.My_Mp}/{player.MMp}')
        cl.lb_money1.config(text=player.Money)
        cl.lb_weapon1.config(text=player.My_Weapon[0][0], bg=player.My_Weapon[0][2])
        cl.lb_armor1.config(text=player.My_Aromr[0][0], bg=player.My_Aromr[0][2])
        cl.lb_level1.config(text=f'{player.floor}-{player.level}')

    # 更新操作栏穿戴部分装备选择信息,可选择更新武器、防具、药剂(w=1,a=1,p=1)
    def renew_wear(self, w=0, a=0, p=0):
        if w:
            items_w = []
            for i in range(0, len(player.Baggage['我的武器']), 2):
                items_w.append(Items.weapons[player.Baggage['我的武器'][i]][0])
            cl.comb_w.config(value=items_w)
        if a:
            items_a = []
            for i in range(0, len(player.Baggage['我的防具']), 2):
                items_a.append(Items.armors[player.Baggage['我的防具'][i]][0])
            cl.comb_a.config(value=items_a)
        if p:
            items_p = []
            for i in range(0, len(player.Baggage['我的药剂']), 2):
                name = Items.potions[player.Baggage['我的药剂'][i]][0]
                items_p.append(f"{name}")
            cl.comb_p.config(value=items_p)

    # 更新背包栏信息，可选择更新武器、防具、药剂(w=1,a=1,p=1)
    def renew_bag(self, w=0, a=0, p=0):
        if w:
            cl.w_list.delete(0, END)
            i = 0
            for i in range(0, len(player.Baggage['我的武器']), 2):
                cl.w_list.insert(END, f'{Items.weapons[player.Baggage["我的武器"][i]][0]}×{player.Baggage["我的武器"][i + 1]}')
        if a:
            cl.a_list.delete(0, END)
            i = 0
            for i in range(0, len(player.Baggage['我的防具']), 2):
                cl.a_list.insert(END, f'{Items.armors[player.Baggage["我的防具"][i]][0]}×{player.Baggage["我的防具"][i + 1]}')
        if p:
            cl.p_list.delete(0, END)
            i = 0
            for i in range(0, len(player.Baggage['我的药剂']), 2):
                # if player.Baggage['我的药剂'][i + 1] != 0:
                cl.p_list.insert(END,
                                 f'{Items.potions[player.Baggage["我的药剂"][i]][0]} × {player.Baggage["我的药剂"][i + 1]}')


cl = Control()

# 判断是否读档
Y_N = tkinter.messagebox.askyesno('开始游戏', '是否读取存档')  # 是/否，返回值true/false
if Y_N:
    ac.read_data()
else:
    cl.txt_infor.insert(0.0, '==========开始新游戏=========\n')

root.mainloop()
