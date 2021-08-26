# 回合制遊戲備忘日誌 (開發版本2.0.0)

# 更1:三大職業模式(附職業模式)
# 更2:MP系統
# 更3:回合計算機制
# 更4:命中率機制
# 更5:絕招說明
# 更6:對戰挑戰模式，共3關
# 更7:金幣計算累計
# 修1:小寫輸入絕招也可(210521已修正)
# 修2:更改技能代碼 Z, X, C, V
# --------------
# 未來更新
# 更1:傷害爆擊系統

from colorama import init
init()

import random as rd
import sys, time, os

def tprint(message):
    for x in message:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.04) #原0.05      
def tprint_slow(message):
    for x in message:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.08)  

class tcolors:
    bold = '\033[1m' # 粗體
    red = '\033[31m' # 紅色
    gre = '\033[32m' # 綠色
    yel = '\033[33m' # 黃色
    yelB = '\033[1;33m' #黃色_粗體
    blu = '\033[34m' # 藍色
    mag = '\033[35m' # 品紅色
    cya = '\033[36m' # 青色
    res = '\033[0m' # 回復原本設定

class texts:
    enter = tcolors.gre + "(按Enter繼續)" + tcolors.res
    def gameover():
        for i in range(len(PL.rolelist)):
            if PL.rolelist[i]["code"]==my_who:
                me = PL.rolelist[i]["name"]
        tprint("恭喜您，用{}打敗了最後的大魔王！　　\n".format(me))
        tprint("(小提示:也可以試試其他職業挑戰看看喔。)\n\n")
        tprint("此版本開發內容到此，感謝您的遊玩。　　(雷克物語 v2.0.0)\n")
        tprint("Powered by RexTuan. 2021/06/06\n")
        print("------------------------------------------------------------------------")
        input()
        print(tcolors.bold, end='')
        tprint_slow("　　　 * ×　雷 克 物 語　× * \n")
        tprint_slow("　　　 *  Story of Recks   *\n\n"), print(tcolors.res, end='')
        print("------------------------------------------------------------------------")
    def welcome():
        print(tcolors.bold, end='')
        tprint_slow("　　　 * ×　雷 克 物 語　× * \n")
        tprint_slow("　　　 *  Story of Recks   *\n\n"), print(tcolors.res, end='')
    def announce():
        tprint("更新摘要　(開發版本2.0.0)\n1.新增職業模式\n2.新增多樣化絕招\n3.新增更多的挑戰對手\n4.新增絕招說明\n5.改進戰鬥計算機制\n6.修正輸入小寫不能被讀取的機制　　\n\n")
    def mission_exp():
        tprint("討伐任務為當地政府或居民提供獎賞，雇用旅行家擊退野怪的活動。\n")
        tprint("以回合制戰鬥進行，遊戲獲勝條件為將對手HP歸零，反之則為落敗。\n")        
        tprint("另外，當遊戲獲勝時，擊退的野怪越強或您剩餘的HP越多，獲得的獎勵也將越豐盛。　　\n")
    def rl_exp():
        tprint("騎士 ，經常配戴長劍與騎乘英國純血馬，以強健的體格著稱的職業。\n")
        tprint("吸血士 ，據說成為吸血士後，會漸有躲避陽光的習性。\n")
        tprint("術士 ，聽說由於常練習法術的關係，回復MP的速度也是三職業中最快的。　　")       
    class SK:
        def rl1():
            print("騎士技能說明\n劍擊(Z):不消耗MP，朝對方揮擊造成傷害。\n衝刺(X):不消耗MP，朝對方猛力一衝，有少許反傷傷害。\n驚鴻一劈(C):消耗"+ tcolors.blu + "30MP" + tcolors.res + "，朝對方發動仰天劈砍，造成大量傷害。\n正義光環(V):消耗"+ tcolors.blu + "80MP" + tcolors.res + "，騎士被光環圍繞護體，在往後8回合獲得" + tcolors.cya + "防禦減傷25%" + tcolors.res + "以及" + tcolors.mag + "自身傷害加成25%" + tcolors.res + "的效果。　　" + texts.enter)
            input()
        def rl2():
            print("吸血士技能說明\n抓(Z):不消耗MP，朝對方揮擊造成傷害。\n啃咬(X):不消耗MP，朝對方猛烈啃咬，有少許反傷傷害。\n鮮血之夜(C):消耗"+ tcolors.blu + "40MP" + tcolors.res + "，朝對方施以吸血儀式，造成傷害並回復自身生命。\n蝙蝠黑夜(V):消耗"+ tcolors.blu + "100MP" + tcolors.res + "，敵方被大量蝙蝠包圍，在往後5回合造成傷害並回復自身生命。　　" + texts.enter)
            input()
        def rl3():
            print("術士技能說明\n魔導彈(Z):消耗"+ tcolors.blu + "5MP" + tcolors.res + "，朝對方發射能量凝聚球造成傷害。\n衝擊砲(X):消耗"+ tcolors.blu + "20MP" + tcolors.res + "，朝對方發射能量脈衝造成傷害。\n結界封印(C):消耗"+ tcolors.blu + "60MP" + tcolors.res + "，佈下能量結界將對方封印造成大量傷害，有一定機率使對方下回合無法攻擊。\n聖光治癒(V):消耗"+ tcolors.blu + "120MP" + tcolors.res + "，召喚聖光回復生命，有一定機率召喚光耀聖光，大幅增加回復比例。" + texts.enter)
            input()

class PT: # 各項數值紀錄(HP、MP、MPC魔力消耗、HR命中率、TD總傷、Buff)
    class NM: # Name 職業名稱
        rl1="騎士"
        rl2="吸血士"
        rl3="術士"
        op1="雪山小猴"
        op2="花狸"
        op3="藏青虎"
    class HP:
        rl1=1000
        rl2=800
        rl3=900
        op1=750
        op2=950
        op3=1600
    class MP:
        rl1=100
        rl2=125
        rl3=150
        op1=50
        op2=50
        op3=100
        class RC: # recover 恢復
            rl1=5
            rl2=10
            rl3=15
            op1=5
            op2=5
            op3=10
    class SK:
        class NM: # Name 招式名稱
            rl1z="劍擊"
            rl1x="衝刺"
            rl1c="驚鴻一劈"
            rl1v="正義光環"
            rl2z="抓"
            rl2x="啃咬"
            rl2c="鮮血之夜"
            rl2v="蝙蝠黑夜"
            rl3z="魔導彈"
            rl3x="衝擊砲"
            rl3c="結界封印"
            rl3v="聖光治癒"
            op1z="抓"
            op1x="猛咬"
            op1c="痴狂吼叫"
            op2z="撞擊"
            op2x="衝撞"
            op2c="花形穿梭"
            op3z="抓"
            op3x="啃咬"
            op3c="藏青之尾"
            op3v="藏青之氣"
        class TD: # Total Damage(技能總傷害)
            rl1z=90
            rl1x=150
            rl1c=195
            rl1v=60
            rl2z=110
            rl2x=175
            rl2c=150
            rl3z=100
            rl3x=140
            rl3c=150
            rl3v=200
            op1z=90
            op1x=140
            op2z=100
            op2x=160
            op2c=50
            op3z=110
            op3x=170
            op3c=200
            op3v=100
        class HR: # Hit Rate(命中率)
            rl1z=100
            rl1x=75
            rl1c=90
            rl1v=100
            rl2z=100
            rl2x=75
            rl2c=100
            rl2v=100
            rl3z=100
            rl3x=75
            rl3c=90
            rl3v=100
            op1z=80
            op1x=60
            op1c=100
            op2z=100
            op2x=70
            op2c=100
            op3z=75
            op3x=60
            op3c=90
            op3v=90         
        class MPC: # Magic Point Cost(消耗MP)
            rl1z=0
            rl1x=0
            rl1c=30
            rl1v=80
            rl2z=0
            rl2x=0
            rl2c=40
            rl2v=100
            rl3z=5
            rl3x=20
            rl3c=60
            rl3v=120
            op1z=0
            op1x=0
            op1c=25
            op2z=0
            op2x=0
            op2c=35
            op3z=0
            op3x=0
            op3c=70
            op3v=80
        class BF: #額外加乘效果
            rl1v1=0.3
            rl1v2=-0.3
            rl2v=80
            op1c=0.15
            op2c=0.85 
            op3v=-0.2

class RD: # 戰鬥系統相關（損增傷系統、Buff狀態顯示系統、命中率系統...）
    def Buff(mD=1,oD=1):
        CC1=0
        CC2=0
        CC3=0
        CC4=0
        if rdc<rdc_rl1v+1: # 正義光環
            CC1=PT.SK.BF.rl1v1
            CC2=PT.SK.BF.rl1v2
        if rdc<rdc_op1c+1: # 痴狂吼叫
            CC3=PT.SK.BF.op1c
        if rdc<rdc_op3v+1: #藏青之氣
            CC4=PT.SK.BF.op3v
        mACC=1+CC1 # 我方傷害修正係數 my Attack Correction Coefficient
        mDCC=1+CC2 # 我方防禦修正係數 my Defence Correction Coefficient
        oACC=1+CC3 # 對方傷害修正係數 op Attack Correction Coefficient
        oDCC=1+CC4 # 對方防禦修正係數 op Defence Correction Coefficient
        mD=mD*mACC*oDCC
        oD=oD*mDCC*oACC
        return mD, oD
    def BuffAttack():
        global ophpst, myhpst
        ophp=ophpst
        myhp=myhpst
        if rdc<rdc_rl2v+1: #蝙蝠黑夜
            A=PT.SK.BF.rl2v
            rdc_rl2vat=-A*0.75+rd.normalvariate(-A*0.25, -A*0.1)
            ophp+=rdc_rl2vat
            myhp+=-rdc_rl2vat*0.2
            tprint("\n{}召喚的蝙蝠仍持續攻擊，使敵方受到了{}傷害，並讓自己回復{}生命。　　".format(myname, round(rdc_rl2vat), round(-rdc_rl2vat*0.15)))
        ophpst=ophp
        myhpst=myhp
    def BuffStop():
        s=rd.random()
        if rdc==rdc_rl3c:
            if s>=0.75:
                tprint("受到{}的效果，無法動彈。\n".format(PT.SK.NM.rl3c))
                return False
            else:
                return True
        else:
            return True
    def Buffshow():
        if rdc<rdc_rl1v+1: # 正義光環
            tprint("\n{}受到{}的加持效果，金黃色光環仍瑩瑩圍繞著。　　".format(myname, PT.SK.NM.rl1v))
        if rdc==rdc_rl1v+1 and rdc!=1: # 正義光環 
            tprint("\n{}的光環在剎那間消失了。　　".format(myname))      
        if rdc<rdc_op1c+1: #痴狂吼叫
            tprint("\n{}受到{}的加持效果，情緒仍在亢奮中。　　".format(PT.NM.op1, PT.SK.NM.op1c))
        if rdc==rdc_op1c+1 and rdc!=1: #痴狂吼叫
            tprint("\n{}的情緒平復下來了。　　".format(PT.NM.op1))   
        if rdc==rdc_rl2v+1 and rdc!=1: # 蝙蝠黑夜   
            tprint("\n{}召喚的蝙蝠消散了。　　".format(myname))  
        if rdc<rdc_op3v+1: # 藏青之氣
            tprint("\n{}受到{}的護體效果，裊裊雲煙仍環繞著。　　".format(PT.NM.op3, PT.SK.NM.op3v))
        if rdc==rdc_op3v+1 and rdc!=1: # 藏青之氣
            tprint("\n{}召喚的{}消失了。　　".format(PT.NM.op3, PT.SK.NM.op3v))            
    def HitRate(H):
        s=rd.random()
        if x==1: #輪到對手的回合
            if s>(1-0.01*H):
                return True
            else:
                return False            
        else:  #輪到自己的回合
            if s>(1-0.01*H*(PT.SK.BF.op2c**lv_op2c)):
                return True
            else:
                return False  
    def Reset(my_who,op_who): #戰鬥開始時，回復一切HP、MP、Buff #只要有global 就可行儲存回主程序
        global myhpst, myhpmax, mympst, mympmax, ophpst, ophpmax, opmpst, opmpmax, mymprc, opmprc, rdc_rl1v, rdc_rl2v, rdc_op1c, rdc_rl3c, lv_op2c, rdc_op3v
        rdc_rl1v=0
        rdc_rl2v=0
        rdc_op1c=0
        rdc_rl3c=0
        lv_op2c=0
        rdc_op3v=0
        if my_who=="rl1":
            myhpst=PT.HP.rl1
            myhpmax=PT.HP.rl1
            mympst=PT.MP.rl1
            mympmax=PT.MP.rl1
            mymprc=PT.MP.RC.rl1
        if my_who=="rl2":
            myhpst=PT.HP.rl2
            myhpmax=PT.HP.rl2
            mympst=PT.MP.rl2
            mympmax=PT.MP.rl2
            mymprc=PT.MP.RC.rl2
        if my_who=="rl3":
            myhpst=PT.HP.rl3
            myhpmax=PT.HP.rl3
            mympst=PT.MP.rl3
            mympmax=PT.MP.rl3
            mymprc=PT.MP.RC.rl3          
        if op_who=="op1":
            ophpst=PT.HP.op1
            ophpmax=PT.HP.op1
            opmpst=PT.MP.op1
            opmpmax=PT.MP.op1
            opmprc=PT.MP.RC.op1
        if op_who=="op2":
            ophpst=PT.HP.op2
            ophpmax=PT.HP.op2
            opmpst=PT.MP.op2
            opmpmax=PT.MP.op2
            opmprc=PT.MP.RC.op2
        if op_who=="op3":
            ophpst=PT.HP.op3
            ophpmax=PT.HP.op3
            opmpst=PT.MP.op3
            opmpmax=PT.MP.op3
            opmprc=PT.MP.RC.op3

class PL: # 各項人物、任務、地名紀錄
    rolelist=[
        {"name":"騎士","code":"rl1"},
        {"name":"吸血士","code":"rl2"},
        {"name":"術士","code":"rl3"},  ]
    oplist=[
        {"name":"雪山小猴","code":"op1"},
        {"name":"花狸","code":"op2"},
        {"name":"藏青虎","code":"op3"},    ]
    placelist=[
        {"place":"皮金港"}]
    missionlist=[
        {"code":"0001","place":"皮金港","mission":"醉月山山腰","button":"Z","op1":"op1","op1_nm":"雪山小猴","op2":"op2","op2_nm":"花狸","op3":"op3","op3_nm":"藏青虎"}]

class GN: # 一般劇情相關（職業切換、任務統計、金幣統計、戰鬥輪流判定...）
    def LifeChange():
        global my_who
        while True:
            tprint("請問{}的職業是？　　\n\n".format(myname))
            tprint("{}(Z)\n".format(PT.NM.rl1))
            tprint("{}(X)\n".format(PT.NM.rl2))
            tprint("{}(C)\n".format(PT.NM.rl3))
            tprint("職業說明(Q)\n")
            print(tcolors.yelB, end=''), tprint("請輸入欲執行的動作："), print(tcolors.res, end='')
            ans=input()
            if ans=="Z" or ans=="z":
                tprint("\n{}的職業是 {}，對嗎？\n".format(myname, PT.NM.rl1))
                print(tcolors.yelB, end=''),  tprint("請選擇確認(Enter)或取消(N)："), print(tcolors.res, end='')
                ans=input()
                if ans=="N" or ans=="n":
                    continue
                else:
                    my_who="rl1"
                    tprint("原來是 {}阿！　　".format(PT.NM.rl1))
                    print(texts.enter)
                    input()
                    break
            elif ans=="X" or ans=="x":
                tprint("\n{}的職業是 {}，對嗎？\n".format(myname, PT.NM.rl2))
                print(tcolors.yelB, end=''),  tprint("請選擇確認(Enter)或取消(N)："), print(tcolors.res, end='')
                ans=input()
                if ans=="N" or ans=="n":
                    continue
                else:
                    my_who="rl2"
                    tprint("原來是 {}阿！　　".format(PT.NM.rl2))
                    print(texts.enter)
                    input()
                    break    
            elif ans=="C" or ans=="c":
                tprint("\n{}的職業是 {}，對嗎？\n".format(myname, PT.NM.rl3))
                print(tcolors.yelB, end=''),  tprint("請選擇確認(Enter)或取消(N)："), print(tcolors.res, end='')
                ans=input()
                if ans=="N" or ans=="n":
                    continue
                else:
                    my_who="rl3"
                    tprint("原來是 {}阿！　　".format(PT.NM.rl3))
                    print(texts.enter)
                    input()
                    break    
            elif ans=="Q" or ans=="q":
                texts.rl_exp()
                print(texts.enter)
                input()
                continue
            else:
                tprint("\n無法辨識的動作，請重新輸入。\n")
                continue
    def Mission():
        while True:
            tprint("目前{}的討伐任務，共有{}項。\n\n".format(place, GN.MissionCount(place)))    
            GN.MissionPrint(place) 
            tprint("其他動作：什麼是討伐任務(?)、回到{}(Q)\n".format(place))
            print(tcolors.yelB, end=''),  tprint("請輸入欲執行的動作：\n"), print(tcolors.res, end='')            
            ans = input()   
            if GN.MissionApply(ans)== True:
                N = GN.Start() #op1~3在MissionApply()中被指定
                if N == "B": # (從內層來的) 贏了，但不繼續下一輪，回到選單
                    tprint("準備回到{}...。　　\n".format(place))
                    print(texts.enter)                
                    input()
                    break
            elif ans.upper()=="?":
                texts.mission_exp()
                print(texts.enter)                
                input()
                continue
            elif ans.upper()=="Q":
                tprint("準備回到{}...。　　".format(place))
                print(texts.enter)                
                input()
                break
            else:
                tprint("\n無法辨識的動作，請重新輸入。\n")
                continue                
    def MissionCount(a): # 計算place有的討伐任務有幾項
        missioncount=0
        for i in range(len(PL.missionlist)):
            if PL.missionlist[i]["place"]==a:
                missioncount+=1
        return missioncount
    def MissionPrint(a): #將place的討伐任務另外新建realmission表單
        global placemission
        placemission=[]
        for i in range(len(PL.missionlist)):
            if PL.missionlist[i]["place"]==a:
                tprint(PL.missionlist[i]["mission"]+" ("+PL.missionlist[i]["button"]+") "+"\n")
                placemission=placemission+[PL.missionlist[i]]
    def MissionApply(a): #將 玩家想要執行的任務 和 realmission 中的任務配對 並 指定後續的戰鬥順序
        global realmission, op1, op2, op3
        realmission = []
        for i in range(len(placemission)):
            if a.upper()== placemission[i]["button"]:
                realmission=placemission[i]
                op1=placemission[i]["op1"]
                op2=placemission[i]["op2"]
                op3=placemission[i]["op3"]
        if realmission != []:
            return True
        else:
            return False
    def WhoFirst(opwho): #戰鬥一開始，誰先出招?
        global rdc, x
        rdc=0
        tprint("擲骰子決定第一回合順序，點數大的即可先發制人！　　")
        print(texts.enter)
        input()
        while True:
            p1=rd.choice([1,2,3,4,5,6])
            p2=rd.choice([1,2,3,4,5,6])
            tprint("{}擲出骰子為{}點。　　".format(myname, p1))
            print(texts.enter)
            input()
            tprint("{}擲出骰子為{}點。　　".format(opwho, p2))
            print(texts.enter)
            input()
            if p1>p2:
                tprint("{}擲出的點子較高。太棒了，搶得先機！　　".format(myname))
                print(texts.enter)
                input()
                x=1
                return 
            elif p1<p2:
                tprint("{}擲出的點子較高，由對方先攻。　　".format(opwho))
                print(texts.enter)
                input()
                x=0
                return 
            else:
                tprint("雙方骰出同樣點數，再骰一次！　　")
                print(texts.enter)
                input()
                continue             
    def WhoAreMe(a): # 我方角色連結機制
        global x
        if a=="rl1":
            x=RL.rl1()
        elif a=="rl2":
            x=RL.rl2()
        elif a=="rl3":
            x=RL.rl3()
    def WhoAreYou(a): # 敵方角色連結機制
        global x
        if a=="op1":
            x=OP.op1()
        elif a=="op2":
            x=OP.op2()
        elif a=="op3":
            x=OP.op3()
    def MoneyCount(life): # 戰鬥結束後結算金錢
        if op_who=="op1":
            return round(100*(1+0.5*life/myhpmax))
        if op_who=="op2":
            return round(200*(1+0.5*life/myhpmax))
        if op_who=="op3":
            return round(400*(1+0.5*life/myhpmax))
    def MoneyShow(): # 顯示錢包(累積金幣、目前單場最多金幣獲取及其資訊)
        tprint("目前 {} 共累積了 {} 金幣。\n\n".format(myname, money))
        if money==0:
            tprint("截止至今，{}尚未打贏過任何一場戰鬥喔！　　".format(myname))
        else:
            for i in range(len(PL.rolelist)):
                if record_rl==PL.rolelist[i]["code"]:
                    A = PL.rolelist[i]["name"]
            for i in range(len(PL.oplist)):
                if record_op==PL.oplist[i]["code"]:
                    B = PL.oplist[i]["name"]
            tprint("截止至今，單場獲得最多的金幣為使用{}打敗{}時，獲得的{}金幣！　　".format(A, B, record_money))
    def Start():
        while True:
            global order, op_who
            if order==0: # 第一輪
                op_who=op1
                RD.Reset(my_who, op_who)
                print("------------------------------------------------------------------------")
                tprint("{}您好，您已進入{}的{}討伐任務（第{}輪）。\n".format(myname, place, realmission["mission"], order+1))
                tprint("{} 出現了！\n\n".format(realmission["op1_nm"])) #(待優化)利用order的數字指定op幾
                tprint("(請依照系統指示，輸入對應符號發動絕招，將對手擊敗吧！)　　\n")
                print(texts.enter)
                input()
                GN.WhoFirst(realmission["op1_nm"]) # 順序的x在WhoFirst()裡面被指定 #(待優化)利用order的數字指定op幾
                N = GN.turn()
                if N =="A":
                    continue
                elif N =="B":
                    return "B"
            elif order==1: 
                op_who=op2
                RD.Reset(my_who, op_who)
                print("------------------------------------------------------------------------")
                tprint("{}您好，您已進入{}的{}討伐任務（第{}輪）。\n".format(myname, place, realmission["mission"], order+1))
                tprint("{} 出現了！\n\n".format(realmission["op2_nm"])) #(待優化)利用order的數字指定op幾
                tprint("(請依照系統指示，輸入對應符號發動絕招，將對手擊敗吧！)　　\n")
                print(texts.enter)
                input()
                GN.WhoFirst(realmission["op2_nm"]) # 順序的x在WhoFirst()裡面被指定 #(待優化)利用order的數字指定op幾
                N = GN.turn()
                if N =="A":
                    continue
                elif N =="B":
                    return "B"      
            elif order==2: # 第三輪
                op_who=op3
                RD.Reset(my_who, op_who)
                print("------------------------------------------------------------------------")
                tprint("{}您好，您已進入{}的{}討伐任務（第{}輪）。\n".format(myname, place, realmission["mission"], order+1))
                tprint("{} 出現了！\n\n".format(realmission["op3_nm"])) #(待優化)利用order的數字指定op幾
                tprint("(請依照系統指示，輸入對應符號發動絕招，將對手擊敗吧！)　　\n")
                print(texts.enter)
                input()
                GN.WhoFirst(realmission["op3_nm"]) # 順序的x在WhoFirst()裡面被指定 #(待優化)利用order的數字指定op幾
                N = GN.turn()
                if N =="A":
                    continue
                elif N =="B":
                    return "B" 
    def turn():
        global x, money, order, record_money, record_op, record_rl, record_rdc
        while True:
            if myhpst>0 and ophpst>0:
                if x==0:
                    GN.WhoAreYou(op_who)
                    continue
                elif x==1:                 
                    GN.WhoAreMe(my_who)
                    continue
            elif ophpst<0 and myhpst>0 and order!=2:
                get=GN.MoneyCount(round(myhpst))    
                tprint("恭喜{}，您已贏得勝利，獲得{}金幣。　　".format(myname, get))
                order=order+1
                money+=get
                if get>record_money:
                    record_money=get
                    record_rl=my_who
                    record_op=op_who
                    record_rdc=rdc
                print(texts.enter)
                input()
                tprint("請問要繼續下一輪的討伐任務嗎? (注意：若結束任務下次須從第一輪重新開始）\n")
                print(tcolors.yelB, end=''),  tprint("請按Enter繼續或輸入(N)來結束任務。\n"), print(tcolors.res, end='')
                ans=input()
                if ans.upper() =="N":
                    order=0
                    return "B" # 贏了，但不繼續下一輪，回到選單
                else:
                    return "A" # 贏了，繼續下一輪
            elif ophpst<0 and myhpst>0 and order==2:
                get=GN.MoneyCount(round(myhpst))
                tprint("恭喜{}，您已贏得勝利，獲得{}金幣。　　".format(myname, get))
                money+=get
                if get>record_money:
                    record_money=get
                    record_rl=my_who
                    record_op=op_who
                    record_rdc=rdc
                print(texts.enter)
                input()
                texts.gameover()
                order=0
                return "B"
            elif ophpst>0 and myhpst<0:
                tprint("您已被擊敗，再挑戰看看吧。　　\n")
                tprint("(小提示:隨時都能透過"), print(tcolors.yelB, end=''),  tprint("轉生器"), print(tcolors.res, end=''), tprint("轉職再次挑戰喔！)　　\n")
                print(texts.enter)
                input()
                order=0
                return "B"
            elif ophpst<0 and myhpst<0:
                tprint("好可惜，差一點就贏了，此局平手，再挑戰看看吧。　　\n")
                tprint("(小提示:隨時都能透過"), print(tcolors.yelB, end=''),  tprint("轉生器"), print(tcolors.res, end=''), tprint("轉職再次挑戰喔！)　　\n")
                print(texts.enter)
                input()
                order=0
                return "B"    

class RL: # 角色的回合
    def rl1():
        global ophpst, opmpst, myhpst, mympst, mACC, mDCC, oACC, oDCC, rdc, rdc_rl1v
        rdc+=1
        tprint("目前為第{}回合，此為你的回合。　　".format(rdc))
        RD.BuffAttack()
        RD.Buffshow()       
        ophp=ophpst
        opmp=opmpst
        myhp=myhpst
        mymp=mympst
        mymp+=mymprc
        if mymp>mympmax:
            mymp=mympmax
        opmp+=opmprc
        if opmp>opmpmax:
            opmp=opmpmax
        tprint("\n\n對手HP/MP: {} / {}\n".format(round(ophp), round(opmp)))
        tprint("我方HP/MP: {} / {}　　".format(round(myhp), round(mymp)))
        print(texts.enter)
        input()
        while True:
            print("選單代號：技能說明(Q)")
            print("絕招代號：{}(Z)、{}(X)、{}(C)、{}(V):".format(PT.SK.NM.rl1z, PT.SK.NM.rl1x, PT.SK.NM.rl1c, PT.SK.NM.rl1v))
            print(tcolors.yelB + "請輸入欲執行的動作：" + tcolors.res)
            od=input() # 指令 Order
            if od=="Q" or od=="q":
                texts.SK.rl1()
                continue
            elif od=="Z" or od=="z":
                D=PT.SK.TD.rl1z
                H=PT.SK.HR.rl1z
                M=PT.SK.MPC.rl1z
                if mymp>=M:
                    mymp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d) # 實際傷害 Real Damage
                        ophp+=Rd[0]
                        tprint("{}使用了{}，造成了{}傷害！\n".format(myname, PT.SK.NM.rl1z, round(Rd[0])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl1z))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue
            elif od=="X" or od=="x":
                D=PT.SK.TD.rl1x
                H=PT.SK.HR.rl1x
                M=PT.SK.MPC.rl1x
                if mymp>=M:
                    mymp+=-M                
                    if RD.HitRate(H)==True:
                        d1=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1) # 造成的傷害
                        d2=-D*0.75*0.3+rd.normalvariate(-D*0.25*0.3,-D*0.1*0.3) # 反傷
                        Rd1=RD.Buff(d1)
                        Rd2=RD.Buff(d2)
                        ophp+=Rd1[0]
                        myhp+=Rd2[0]
                        tprint("{}使用了{}，造成了{}傷害，\n".format(myname, PT.SK.NM.rl1x, round(Rd1[0])))
                        tprint("但{}也讓自己受到{}損傷！\n".format(PT.SK.NM.rl1x, round(Rd2[0])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl1x))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue
            elif od=="C" or od=="c":
                D=PT.SK.TD.rl1c
                H=PT.SK.HR.rl1c
                M=PT.SK.MPC.rl1c
                if mymp>=M:
                    mymp+=-M    
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d)
                        ophp+=Rd[0]
                        tprint("{}奮力躍起使用了{}，伴隨著碎石落地造成了{}傷害！\n".format(myname, PT.SK.NM.rl1c, round(Rd[0])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl1c))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue                    
            elif od=="V" or od=="v":
                D=PT.SK.TD.rl1v
                H=PT.SK.HR.rl1v
                M=PT.SK.MPC.rl1v
                if mymp>=M:
                    mymp+=-M                   
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d)
                        ophp+=Rd[0]
                        rdc_rl1v=rdc+8
                        tprint("{}身邊浮現了金黃色的{}，突然形成的旋風造成了{}傷害！\n".format(myname, PT.SK.NM.rl1v, round(Rd[0])))
                        tprint("{}的傷害與防禦似乎變得更高了。\n".format(myname))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl1v))
                        break                         
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue 
            else: 
                tprint("指令無法辨識，請重新輸入。\n") 
                continue
        input()
        print("\n你的回合結束。")
        print("對手HP: {}\n我方HP: {}".format(round(ophp), round(myhp)))
        print("------------------------------------------------------------------------")
        myhpst=myhp
        ophpst=ophp
        mympst=mymp
        opmpst=opmp
        return 0                            
    def rl2():
        global ophpst, opmpst, myhpst, mympst, mACC, mDCC, oACC, oDCC, rdc, rdc_rl2v
        rdc+=1
        tprint("目前為第{}回合，此為你的回合。　　".format(rdc))
        RD.BuffAttack()
        RD.Buffshow()        
        ophp=ophpst
        opmp=opmpst
        myhp=myhpst
        mymp=mympst
        mymp+=mymprc
        if mymp>mympmax:
            mymp=mympmax
        opmp+=opmprc
        if opmp>opmpmax:
            opmp=opmpmax
        tprint("\n\n對手HP/MP: {} / {}\n".format(round(ophp), round(opmp)))
        tprint("我方HP/MP: {} / {}　　".format(round(myhp), round(mymp)))
        print(texts.enter)
        input()
        while True:
            print("選單代號：技能說明(Q)")
            print("絕招代號：{}(Z)、{}(X)、{}(C)、{}(V):".format(PT.SK.NM.rl2z, PT.SK.NM.rl2x, PT.SK.NM.rl2c, PT.SK.NM.rl2v))
            print(tcolors.yelB + "請輸入欲執行的動作：" + tcolors.res)
            od=input() # 指令 Order
            if od=="Q" or od=="q":
                texts.SK.rl2()
                continue
            elif od=="Z" or od=="z":
                D=PT.SK.TD.rl2z
                H=PT.SK.HR.rl2z
                M=PT.SK.MPC.rl2z
                if mymp>=M:
                    mymp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d) # 實際傷害 Real Damage
                        ophp+=Rd[0]
                        tprint("{}使用了{}，造成了{}傷害！\n".format(myname, PT.SK.NM.rl2z, round(Rd[0])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl2z))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue
            elif od=="X" or od=="x":
                D=PT.SK.TD.rl2x
                H=PT.SK.HR.rl2x
                M=PT.SK.MPC.rl2x
                if mymp>=M:
                    mymp+=-M                
                    if RD.HitRate(H)==True:
                        d1=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1) # 造成的傷害
                        d2=-D*0.75*0.3+rd.normalvariate(-D*0.25*0.3,-D*0.1*0.3) # 反傷
                        Rd1=RD.Buff(d1)
                        Rd2=RD.Buff(d2)
                        ophp+=Rd1[0]
                        myhp+=Rd2[0]
                        tprint("{}使用了{}，造成了{}傷害，\n".format(myname, PT.SK.NM.rl2x, round(Rd1[0])))
                        tprint("但{}也讓自己受到{}損傷！\n".format(PT.SK.NM.rl2x, round(Rd2[0])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！".format(myname, PT.SK.NM.rl2x))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue                       
            elif od=="C" or od=="c":
                D=PT.SK.TD.rl2c
                H=PT.SK.HR.rl2c
                M=PT.SK.MPC.rl2c
                if mymp>=M:
                    mymp+=-M 
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d)
                        Rd2=-Rd[0]*0.3                        
                        ophp+=Rd[0]
                        myhp+=Rd2
                        tprint("{}的瞳孔轉為鮮紅，在{}的儀式後造成了{}傷害，\n".format(myname, PT.SK.NM.rl2c, round(Rd[0])))
                        tprint("對方的鮮血同時也讓自己回復了{}生命。\n".format(round(Rd2)))
                        break                       
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl2c))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue  
            elif od=="V" or od=="v":
                H=PT.SK.HR.rl2v
                M=PT.SK.MPC.rl2v      
                if mymp>=M:
                    mymp+=-M
                    if RD.HitRate(H)==True:
                        rdc_rl2v=rdc+5 
                        tprint("受到{}的召喚，天空被無數的烏黑蝙蝠遮蔽。\n".format(myname))
                        tprint("不斷有蝙蝠向下俯衝攻擊對方。\n".format(myname))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl2v))
                        break                                                           
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue 
            else:
                tprint("指令無法辨識，請重新輸入。\n") 
                continue                                  
        input()
        print("\n你的回合結束。")
        print("對手HP: {}\n我方HP: {}".format(round(ophp), round(myhp)))
        print("------------------------------------------------------------------------")
        myhpst=myhp
        ophpst=ophp
        mympst=mymp
        opmpst=opmp
        return 0 
    def rl3():
        global ophpst, opmpst, myhpst, mympst, mACC, mDCC, oACC, oDCC, rdc, rdc_rl3c
        rdc+=1
        tprint("目前為第{}回合，此為你的回合。　　".format(rdc))
        RD.BuffAttack()
        RD.Buffshow() 
        ophp=ophpst
        opmp=opmpst
        myhp=myhpst
        mymp=mympst
        mymp+=mymprc
        if mymp>mympmax:
            mymp=mympmax
        opmp+=opmprc
        if opmp>opmpmax:
            opmp=opmpmax
        tprint("\n\n對手HP/MP: {} / {}\n".format(round(ophp), round(opmp)))
        tprint("我方HP/MP: {} / {}　　".format(round(myhp), round(mymp)))
        print(texts.enter)
        input()
        while True:
            print("選單代號：技能說明(Q)")
            print("絕招代號：{}(Z)、{}(X)、{}(C)、{}(V):".format(PT.SK.NM.rl3z, PT.SK.NM.rl3x, PT.SK.NM.rl3c, PT.SK.NM.rl3v))
            print(tcolors.yelB + "請輸入欲執行的動作：" + tcolors.res)
            od=input() # 指令 Order
            if od=="Q" or od=="q":
                texts.SK.rl3()
                continue
            elif od=="Z" or od=="z":
                D=PT.SK.TD.rl3z
                H=PT.SK.HR.rl3z
                M=PT.SK.MPC.rl3z
                if mymp>=M:
                    mymp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d) # 實際傷害 Real Damage
                        ophp+=Rd[0]
                        tprint("{}使用了{}，造成了{}傷害！\n".format(myname, PT.SK.NM.rl3z, round(Rd[0])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl3z))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue
            elif od=="X" or od=="x":
                D=PT.SK.TD.rl3x
                H=PT.SK.HR.rl3x
                M=PT.SK.MPC.rl3x
                if mymp>=M:
                    mymp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d) # 實際傷害 Real Damage
                        ophp+=Rd[0]
                        tprint("{}使用了{}，造成了{}傷害！\n".format(myname, PT.SK.NM.rl3x, round(Rd[0])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl3x))
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue
            elif od=="C" or od=="c":
                D=PT.SK.TD.rl3c
                H=PT.SK.HR.rl3c
                M=PT.SK.MPC.rl3c
                if mymp>=M:
                    mymp+=-M 
                    if RD.HitRate(H)==True:               
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(d)
                        ophp+=Rd[0]
                        rdc_rl3c=rdc+1
                        tprint("{}發動了{}，結界中的能量磁場造成了{}傷害。\n".format(myname, PT.SK.NM.rl3c, round(Rd[0])))
                        tprint("對方亦被封印的咒文佈滿全身。\n")    
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl3c)) 
                        break
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue  
            elif od=="V" or od=="v":
                D=PT.SK.TD.rl3v
                H=PT.SK.HR.rl3v
                M=PT.SK.MPC.rl3v
                light=False
                if mymp>=M:
                    mymp+=-M 
                    if RD.HitRate(H)==True:                
                        r1=D*0.75+rd.normalvariate(D*0.25, D*0.1)
                        r2=0
                        if myhp+r1>PT.HP.rl3:
                            r1=PT.HP.rl3-myhp
                        myhp+=r1
                        if rd.random()>=0.65: # 光耀聖光35%再補
                            r2=(PT.HP.rl3-myhp)*0.2
                            light= True
                        myhp+=r2
                        tprint("{}揮動魔杖使用{}，自天灑下了一道潔白光芒，使自己回復了{}生命。\n".format(myname, PT.SK.NM.rl3v, round(r1)))
                        if light==True:
                            tprint("不過半晌，天空再次灑下七彩的光耀聖光，額外使自己回復了{}生命。\n".format(round(r2)))
                            break
                        else:
                            break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(myname, PT.SK.NM.rl3v))
                        break                           
                else:
                    tprint("MP不足，請重新選擇。\n")
                    continue 
            else: 
                tprint("指令無法辨識，請重新輸入。\n") 
                continue
        input()
        print("\n你的回合結束。")
        print("對手HP: {}\n我方HP: {}".format(round(ophp), round(myhp)))
        print("------------------------------------------------------------------------")
        myhpst=myhp
        ophpst=ophp
        mympst=mymp
        opmpst=opmp
        return 0   

class OP: # 對手的回合
    def op1():
        global ophpst, opmpst, myhpst, mympst, mACC, mDCC, oACC, oDCC, rdc, rdc_op1c
        rdc+=1
        tprint("目前為第{}回合，此為對手的回合。　　".format(rdc))
        RD.BuffAttack()
        RD.Buffshow()
        ophp=ophpst
        opmp=opmpst
        myhp=myhpst
        mymp=mympst
        mymp+=mymprc
        if mymp>mympmax:
            mymp=mympmax
        opmp+=opmprc
        if opmp>opmpmax:
            opmp=opmpmax
        tprint("\n\n對手HP/MP: {} / {}\n".format(round(ophp), round(opmp)))
        tprint("我方HP/MP: {} / {}　　".format(round(myhp), round(mymp)))
        print(texts.enter)
        input()
        while RD.BuffStop()==True: 
            p=rd.choice([1,1,1,1,1,2,2,2,3,3])
            if p==1:
                D=PT.SK.TD.op1z
                H=PT.SK.HR.op1z
                M=PT.SK.MPC.op1z
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(0,d) 
                        myhp+=Rd[1]
                        tprint("{}使用了{}，造成了{}傷害！\n".format(PT.NM.op1, PT.SK.NM.op1z, round(Rd[1])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op1,PT.SK.NM.op1z))
                        break                
                else:
                    continue
            elif p==2:
                D=PT.SK.TD.op1x
                H=PT.SK.HR.op1x
                M=PT.SK.MPC.op1x
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d1=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1) # 造成的傷害
                        d2=-D*0.75*0.3+rd.normalvariate(-D*0.25*0.3,-D*0.1*0.3) # 反傷
                        Rd1=RD.Buff(0,d1)
                        Rd2=RD.Buff(0,d2)
                        myhp+=Rd1[1]
                        ophp+=Rd2[1]
                        tprint("{}使用了{}，造成了{}傷害，\n".format(PT.NM.op1, PT.SK.NM.op1x, round(Rd1[1])))
                        tprint("但{}也讓自己受到{}損傷！\n".format(PT.SK.NM.op1x, round(Rd2[1])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op1,PT.SK.NM.op1x))
                        break                      
                else:
                    continue
            elif p==3:
                H=PT.SK.HR.op1c
                M=PT.SK.MPC.op1c            
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        rdc_op1c=rdc+4
                        tprint("{}使用了{}，激烈的吼叫讓{}變得異常亢奮！\n".format(PT.NM.op1, PT.SK.NM.op1c, PT.NM.op1))
                        tprint("{}的傷害似乎變得更高了。\n".format(PT.NM.op1))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op1, PT.SK.NM.op1c))
                        break  
                else:
                    continue     
        input()
        print("\n對方回合結束。")
        print("對手HP: {}\n我方HP: {}　　".format(round(ophp), round(myhp)))
        print("------------------------------------------------------------------------")
        myhpst=myhp
        ophpst=ophp
        mympst=mymp
        opmpst=opmp
        return 1    
    def op2():
        global ophpst, opmpst, myhpst, mympst, mACC, mDCC, oACC, oDCC, rdc, lv_op2c
        rdc+=1
        tprint("目前為第{}回合，此為對手的回合。　　".format(rdc))
        RD.BuffAttack()
        RD.Buffshow()
        ophp=ophpst
        opmp=opmpst
        myhp=myhpst
        mymp=mympst
        mymp+=mymprc
        if mymp>mympmax:
            mymp=mympmax
        opmp+=opmprc
        if opmp>opmpmax:
            opmp=opmpmax
        tprint("\n\n對手HP/MP: {} / {}\n".format(round(ophp), round(opmp)))
        tprint("我方HP/MP: {} / {}　　".format(round(myhp), round(mymp)))
        print(texts.enter)
        input()
        while RD.BuffStop()==True: 
            p=rd.choice([1,1,1,1,2,2,2,2,3,3,3])
            if p==1:
                D=PT.SK.TD.op2z
                H=PT.SK.HR.op2z
                M=PT.SK.MPC.op2z
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(0,d) 
                        myhp+=Rd[1]
                        tprint("{}使用了{}，造成了{}傷害！\n".format(PT.NM.op2, PT.SK.NM.op2z, round(Rd[1])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op2,PT.SK.NM.op2z))
                        break   
                else:
                    continue                        
            elif p==2:
                D=PT.SK.TD.op2x
                H=PT.SK.HR.op2x
                M=PT.SK.MPC.op2x
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d1=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1) # 造成的傷害
                        d2=-D*0.75*0.3+rd.normalvariate(-D*0.25*0.3,-D*0.1*0.3) # 反傷
                        Rd1=RD.Buff(0,d1)
                        Rd2=RD.Buff(0,d2)
                        myhp+=Rd1[1]
                        ophp+=Rd2[1]
                        tprint("{}使用了{}，造成了{}傷害，\n".format(PT.NM.op2, PT.SK.NM.op2x, round(Rd1[1])))
                        tprint("但{}也讓自己受到{}損傷！\n".format(PT.SK.NM.op2x, round(Rd2[1])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op2,PT.SK.NM.op2x))
                        break       
                else:
                    continue
            elif p==3:
                D=PT.SK.TD.op2c
                H=PT.SK.HR.op2c
                M=PT.SK.MPC.op2c  
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(0,d) 
                        myhp+=Rd[1]
                        lv_op2c+=1
                        tprint("{}使用了{}，身上的斑紋漸漸融合在背景中，在恍惚之間被衝撞了{}傷害\n".format(PT.NM.op2, PT.SK.NM.op2c, round(Rd[1])))
                        if lv_op2c>3:
                            lv_op2c=3
                            tprint("但似乎沒辦法再提高迴避率......。\n")
                            break
                        else :
                            tprint("受惠於{}的隱匿效果，{}提高了迴避率。\n".format(PT.SK.NM.op2c, PT.NM.op2))
                            break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op2, PT.SK.NM.op2c))
                        break                         
                else:
                    continue   
        input()
        print("\n對方回合結束。")
        print("對手HP: {}\n我方HP: {}　　".format(round(ophp), round(myhp)))
        print("------------------------------------------------------------------------")
        myhpst=myhp
        ophpst=ophp
        mympst=mymp
        opmpst=opmp
        return 1     
    def op3():
        global ophpst, opmpst, myhpst, mympst, mACC, mDCC, oACC, oDCC, rdc, rdc_op3v
        rdc+=1
        tprint("目前為第{}回合，此為對手的回合。　　".format(rdc))
        RD.BuffAttack()
        RD.Buffshow()
        ophp=ophpst
        opmp=opmpst
        myhp=myhpst
        mymp=mympst
        mymp+=mymprc
        if mymp>mympmax:
            mymp=mympmax
        opmp+=opmprc
        if opmp>opmpmax:
            opmp=opmpmax
        tprint("\n\n對手HP/MP: {} / {}\n".format(round(ophp), round(opmp)))
        tprint("我方HP/MP: {} / {}　　".format(round(myhp), round(mymp)))
        print(texts.enter)
        input()       
        while RD.BuffStop()==True: 
            p=rd.choice([1,1,1,1,2,2,2,3,3,4])
            if p==1:
                D=PT.SK.TD.op3z
                H=PT.SK.HR.op3z
                M=PT.SK.MPC.op3z
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(0,d) 
                        myhp+=Rd[1]                    
                        tprint("{}使用了{}，造成了{}傷害！\n".format(PT.NM.op3, PT.SK.NM.op3z, round(Rd[1])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op3,PT.SK.NM.op3z))
                        break   
                else:
                    continue  
            elif p==2:
                D=PT.SK.TD.op3x
                H=PT.SK.HR.op3x
                M=PT.SK.MPC.op3x
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d1=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1) # 造成的傷害
                        d2=-D*0.75*0.3+rd.normalvariate(-D*0.25*0.3,-D*0.1*0.3) # 反傷
                        Rd1=RD.Buff(0,d1)
                        Rd2=RD.Buff(0,d2)
                        myhp+=Rd1[1]
                        ophp+=Rd2[1]
                        tprint("{}使用了{}，造成了{}傷害，\n".format(PT.NM.op3, PT.SK.NM.op3x, round(Rd1[1])))
                        tprint("但{}也讓自己受到{}損傷！\n".format(PT.SK.NM.op3x, round(Rd2[1])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op3,PT.SK.NM.op3x))
                        break       
                else:
                    continue
            elif p==3:
                D=PT.SK.TD.op3c
                H=PT.SK.HR.op3c
                M=PT.SK.MPC.op3c  
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(0,d) 
                        myhp+=Rd[1]                       
                        tprint("{}使用了{}，在被青色光芒包覆的尾巴重擊下，造成了{}傷害！\n".format(PT.NM.op3, PT.SK.NM.op3c, round(Rd[1])))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op3, PT.SK.NM.op3c))
                        break                          
                else:
                    continue
            elif p==4:
                D=PT.SK.TD.op3v
                H=PT.SK.HR.op3v
                M=PT.SK.MPC.op3v  
                if opmp>=M:
                    opmp+=-M
                    if RD.HitRate(H)==True:
                        d=-D*0.75+rd.normalvariate(-D*0.25, -D*0.1)
                        Rd=RD.Buff(0,d) 
                        myhp+=Rd[1]
                        rdc_op3v=rdc+4
                        tprint("{}召喚了{}，暗青色的霧氣降臨大地，如刃似的霧氣造成了{}傷害。\n".format(PT.NM.op3, PT.SK.NM.op3v, round(Rd[1])))
                        tprint("{}被霧氣環身，防禦似乎變得更高了。\n".format(PT.NM.op3))
                        break
                    else:
                        tprint("{}欲使用{}，但沒有命中！\n".format(PT.NM.op3, PT.SK.NM.op3v))
                        break   
                else:
                    continue
        input()
        print("\n對方回合結束。")
        print("對手HP: {}\n我方HP: {}　　".format(round(ophp), round(myhp)))
        print("------------------------------------------------------------------------")
        myhpst=myhp
        ophpst=ophp
        mympst=mymp
        opmpst=opmp
        return 1                      


# 即時使用數值
# 錢區
money=0
record_money=0
record_rl=0
record_op=0
record_rdc=0

# 戰鬥幾輪區
order=0

# 即時戰鬥數值
myhpst=0
myhpmax=0
mympst=0
mympmax=0
mymprc=0
ophpst=0
ophpmax=0
opmpst=0
opmpmax=0
opmprc=0

rdc_rl1v=0
rdc_rl2v=0
rdc_op1c=0
rdc_rl3c=0
lv_op2c=0
rdc_op3v=0

# 主程序
texts.welcome()
while True:
    print(tcolors.yelB, end='')
    tprint("\n請按Enter進入遊戲或輸入(Q)查看更新。\n"), print(tcolors.res, end='')
    key=input()
    if key=="Q" or key=="q":
        texts.announce()
        print(texts.enter)
        input()
        break
    else:
        break
print("------------------------------------------------------------------------")
tprint("久等了！經歷了這麼長的路程，終於抵達目的地了，請問該怎麼稱呼您呢？　　\n")
print(tcolors.yelB, end='')
tprint("請輸入您的稱呼："), print(tcolors.res, end='')
myname = input()
while True:
    place="皮金港"
    tprint("\n{}您好，歡迎來到雷克曼地區 皮金港，請問您是第一次來到雷克曼地區嗎？　　\n".format(myname))
    print(tcolors.yelB, end='')
    tprint("請按Enter聽取解說或輸入(N)跳過解說。\n"), print(tcolors.res, end='')
    ans = input()
    if ans=="N" or ans=="n":
        tprint("\n哇！看起來你已經對這個地方瞭若指掌了！　　")
        print(texts.enter)
        input()
        break
    else:
        tprint("雷克曼地區擁有十分豐富的地形供旅行家去探險。\n")
        tprint("而目前我們的所在地 皮金港，是一處位於雷克曼地區西方的港口，\n")
        tprint("以鄰近醉月山山脈及皮金礦場著稱，近來也有不少像{}一樣的旅行家前來造訪喔！　　".format(myname))
        print(texts.enter)
        input()
        break
tprint("對了，冒昧請問一下，\n")

GN.LifeChange()

tprint("噢，你可別擔心，在您任務失敗被送回城市急救時，\n")
tprint("您隨時可以透過"), print(tcolors.yelB, end=''), tprint("轉生器"), print(tcolors.res, end=''), tprint("再次轉職。　　")
print(texts.enter)
input()
tprint("還有，在{}離開皮金港之前，給你這個。　　".format(myname))
print(texts.enter)
input()
tprint("獲得 "), print(tcolors.yelB, end=''), tprint("討伐任務憑證"), print(tcolors.res, end=''), tprint(" ！　　")
print(texts.enter)
input()
tprint("有了這枚 討伐任務憑證 之後就可以在雷克曼地區執行討伐任務了。\n")
tprint("但要注意的是，有些地區的討伐任務，會有資格限制喔。\n")
tprint("相信你已經做好準備，開啟接下來的旅程了！\n")
tprint("希望你會喜歡雷克曼地區的一切:)　　")
print(texts.enter)
input()
print(tcolors.bold, end=''), tprint_slow("　　　 　　* ×　雷 克 物 語　× * \n")
tprint("Story of Recks (c) 2021, All Rights Reserved.　　\n\n"), print(tcolors.res, end='')
print(texts.enter)
input()
tprint("微風徐徐，{}的天氣十分晴朗。\n".format(place))
while True:
    tprint("接下來，想要做什麼事情呢？\n\n")
    tprint("參與討伐任務(Z)\n")
    tprint("使用轉生器(X)\n")
    tprint("查看錢包(C)\n")
    tprint("前往皮金港市場(V)\n")
    print(tcolors.yelB, end=''), tprint("請輸入欲執行的動作："), print(tcolors.res, end='')
    ans=input()
    if ans=="Z" or ans=="z":
        GN.Mission()
        continue
    elif ans=="X" or ans=="x":
        GN.LifeChange()
        continue
    elif ans=="C" or ans=="c":
        GN.MoneyShow()
        print(texts.enter)
        input()        
        continue
    elif ans=="V" or ans=="v":
        tprint("往皮金港市場的路正在施工中，現在沒辦法過去，不妨先去參加討伐任務看看？　　")
        print(texts.enter)
        input()
        continue
    else:
        tprint("\n無法辨識的動作，請重新輸入。\n")
        continue
