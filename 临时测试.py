from PyInstaller.log import level

from AutomaticSimulationClass import AutomaticSimulation

automaticsimulation = AutomaticSimulation()








def assembly_lock_or_discard(entry: str):
    """
       1.装配界面，检测词条
       2.根据entry词条进行锁定或丢弃
       :param entry: 是否锁定的词条判断
       :return: None
       """
    # 锁定：True
    lock = automaticsimulation.get_three_pixel_color(1814, 209, "1A1A1A", 1735, 208, "1A1A1A", 1810, 215, "1A1A1A")
    # 未丢弃：True
    discard = automaticsimulation.get_three_pixel_color(1730, 209, "1A1A1A", 1740, 215, "1A1A1A", 1735, 201, "FFFFFF")
    key_judge = automaticsimulation.match_char((1456, 314), (1643, 477), entry)
    # -----------------------未锁定+词条正确->按C----------------------- #
    if not lock and key_judge:
        automaticsimulation.key_down_times("C", 1, 50, 200)
    # ------------------------未丢弃+词条错误>按Z----------------------- #
    elif discard and not key_judge:
        automaticsimulation.key_down_times("Z", 1, 50, 200)


# assembly_lock_or_discard("暴击")

def Initialization_Game_Inferface(KeyDownEsc=False, initialization_time=30, dayle=800, func=None, *args,**kwargs) -> bool:
    """
    1.初始化界面，检测到游戏界面返回真
    2.检测时间默认30秒,30次，一秒一次
    :return:布尔值
    """
    for i in range(initialization_time):  # 检测次数
        # 识别初始化界面
        if automaticsimulation.match_char((1770, 79), (1869, 102), "ms"):
            print("初始化游戏主界面完成")
            return True
        # 没检测到调用其他函数
        else:
            # 按Esc
            if KeyDownEsc:
                automaticsimulation.key_down_times(27)
            # 调用回调函数
            if func is not None:
                func(*args, **kwargs)
        automaticsimulation.random_delay((800 if 800 > dayle else dayle), 0)
    # 循环结束后检测不到返回假
    print("初始化游戏主界面失败")
    return False

def initialization_jueshe():
    """
    初始化角色界面的声骸
    :return:
    """
    automaticsimulation.random_delay(2000, 0)
    # -------------------------------------------------遍历声骸------------------------------------------------------ #
    # 1.选择排序方式：等级排序-倒序
    automaticsimulation.mouse_once_click(363, 995, 2, 1000)  # 打开面板
    automaticsimulation.mouse_once_click(900, 321, 2, 1000)  # 选等级排序
    automaticsimulation.mouse_once_click(1561, 901, 2, 1000)  # 确认
    automaticsimulation.mouse_once_click(512, 996, 2, 1000)  # 倒序
    # 2.检测
    # level = automaticsimulation.recognize_char((1423,212), (1468, 232))
    # print(level)
    # baoji=automaticsimulation.match_char((1456, 314), (1643, 477), "暴击")
    # print(baoji)
    # --------------------------------装配声骸界面（第一界面）---------------------------------- #
    # level=automaticsimulation.recognize_char((1423,212), (1468,232)) # 检测声骸等级
    # 声骸>0级
    # if automaticsimulation.match_char((1456, 314), (1643, 477), "暴击"):
    #
    # # 声骸>0级
    # if

    # 初始坐标（240，242），位移（130，154）

    # 无法使用该方案，滚轮不一致
    # for k in range(15):# 页
    #     for j in range(5):# 行
    #         for i in range(3):# 列
    #             automaticsimulation.mouse_once_click(240 + 130 * i, 242 + 154 * j)
    #     automaticsimulation.mouse_wheel(times=30)  # 无法使用翻页，有时候是29/30，除非检测到空白停止





def initialization_bag()->bool:
    """
    初始化背包界面
    :return: bool
    """
    try:
        Initialization_Game_Inferface(True)
        while True:
            # 1.主界面：点击背包
            if automaticsimulation.match_char((1770, 79), (1869, 102), "ms"):
                automaticsimulation.key_down_times("B")  # 点击背包
            # 2.声骸提示，背包已满：点击确定
            elif automaticsimulation.match_char((712, 502),(1193, 537),"背包已满"):
                automaticsimulation.mouse_once_click(1276, 670)  # 点击确定
                print("背包已满")
            # 3.背包界面：滚轮到最上面，点击声骸
            elif not automaticsimulation.match_char((105, 52), (164, 86), "声骸"):
                automaticsimulation.mouse_once_click(75, 325)  # 移动鼠标位置
                automaticsimulation.mouse_wheel(10, up=True)  # 滚轮到最上面
                automaticsimulation.mouse_once_click(75, 325)  # 点击声骸
            # 4.选择顺序：点击等级顺序
            elif automaticsimulation.match_char((339, 615), (451, 649), "等级顺序"):
                automaticsimulation.mouse_once_click(365, 620)  # 点击等级顺序
            # 5.检测顺序：打开顺序
            elif not automaticsimulation.match_char((339, 969), (451, 1001), "等级顺序",0.2):
                automaticsimulation.mouse_once_click(410,984  )# 点击顺序
            # 6.排序：倒序
            elif automaticsimulation.get_pixel_color(649, 982, "92DFF7"):
                automaticsimulation.mouse_once_click(629, 982)  # 点击倒序
            # 7.检测声骸等级：存在等级，等级=0
            elif (result := automaticsimulation.recognize_char((1770, 250), (1830, 280))) and int(result[0][0].replace("+", "") or -1) == 0:
                print("初始化背包声骸界面成功！")
                return True
            # 8.检测声骸等级：不存在等级/等级>0
            elif not (result := automaticsimulation.recognize_char((1770, 250), (1830, 280))) or int(result[0][0].replace("+", "")) > 0:
                print("无声骸升级")
                return False
    except Exception as e:
        print(e)
        return False


def initialization_strengthen_sound_core(strengthen_level: int, entry: str)-> bool:
    """
    通用的声骸强化界面
    :param strengthen_level: 强化到的等级
    :param entry: 强化后指定的词条,决定弃置还是锁定
    :return:
    """
    try:
        while True:
            # 1.检测声骸等级:等级存在>0,培养
            if (
                    ((result := automaticsimulation.recognize_char((1770, 250), (1830, 280)))
                     and (result := result[0][0].replace("+", ""))
                     and result.isdigit()
                     and (result :=int(result))) == 0
                or
                    automaticsimulation.match_char((934, 510), (1052, 547), "暂无内容")
            ):
                automaticsimulation.mouse_once_click(1720,1000)# 点击培养
            # ---------------------------------------------------------------强化材料设置---------------------------------------------------------------------- #
            # 2.检测强化材料设置:点击四星及以下道具
            elif automaticsimulation.match_char((204, 623), (360, 650), "四星及以下道具") and automaticsimulation.get_three_pixel_color(395, 631, "FFFFFF", 402, 642, "FFFFFF", 388, 642, "FFFFFF"):
                automaticsimulation.mouse_once_click(280, 640)  # 点击四星及以下道具
            # 3.检测强化材料为四星及以下道具:不是四星,点击道具设置
            elif automaticsimulation.match_char((190, 740), (350, 770), "一|二|三|不限"):
                automaticsimulation.mouse_once_click(278, 756)  # 点击道具设置

            # ---------------------------------------------------------------自动放入设置---------------------------------------------------------------------- #

            # # 4.清空升级材料：点击清除
            # elif automaticsimulation.match_char((450, 740), (543, 774), "去除"):
            #     automaticsimulation.mouse_once_click(500,750)# 点击清除

            # 8.检测是否开启阶段放入/同步调谐:没有标志,点击自动放入设置
            elif automaticsimulation.get_three_pixel_color(660,844,"FFFFFF",653,844,"FFFFFF",660,838,"FFFFFF") or automaticsimulation.match_char((450, 740), (543,774), "快捷"):
                automaticsimulation.mouse_once_click(654, 757)  # 点击自动放入设置

            # 阶段放入按键:点击阶段放入
            elif automaticsimulation.match_char((1010, 305), (1123, 336),"阶段放入") and automaticsimulation.get_pixel_color(1655, 350,"FFFFFF"):
                automaticsimulation.mouse_once_click(1200, 346)  # 点击阶段放入
            # 6.同步调谐按键:点击同步调谐
            elif automaticsimulation.match_char((1015, 537), (1174, 566), "开启同步调谐") and automaticsimulation.get_pixel_color(1655, 540, "FFFFFF"):
                automaticsimulation.mouse_once_click(1192, 544)  # 点击同步调谐

            # 7.检测自动放入设置:点击确定
            elif automaticsimulation.match_char((1531, 884), (1596, 916), "确认"):
                automaticsimulation.mouse_once_click(1563, 895)  # 点击确认

            # # ---------------------------------------------------------------强化圣遗物---------------------------------------------------------------------- #
            # # 9.放入升级材料
            # elif automaticsimulation.match_char((451, 742), (538, 768), "阶段放入"):
            #     automaticsimulation.mouse_once_click(495, 756)  # 点击放入
            # # 10点击强化并调谐
            # elif automaticsimulation.match_char((373,980), (500,1012), "强化并调谐"):
            #     automaticsimulation.mouse_once_click(431, 993)  # 点击强化并调谐
            # # 11.谐成功:点击任意位置返回
            # elif automaticsimulation.match_char((885, 275), (1029, 310), "调谐成功"):
            #     automaticsimulation.mouse_once_click(935, 219)  # 点击任意位置返回
            # # 12.检测词条:有指定词条,没有锁定,点击锁定
            # elif automaticsimulation.match_char((221, 324), (414, 522),entry) and not automaticsimulation.get_three_pixel_color(674, 129,"1A1A1A", 674,128, "1A1A1A",670, 135,"1A1A1A"):
            #     automaticsimulation.key_down_times("C", 1, 50, 200)
            # # 13.检测词条:没有指定词条,没有弃置,点击弃置
            # elif not automaticsimulation.match_char((221, 324), (414, 522),entry) and automaticsimulation.get_three_pixel_color(610, 129,"1A1A1A", 623,133, "1A1A1A",616, 122,"FFFFFF"):
            #     automaticsimulation.key_down_times("Z", 1, 50, 200)
            # # 14.检测等级:等级=5/10,完成一次
            # elif (
            #         (result := automaticsimulation.recognize_char((180, 180), (239, 206)))
            #         and (result := result[0][0].replace("+", ""))
            #         and result.isdigit()
            #         and int(result) >= strengthen_level
            # ):
            #     automaticsimulation.key_down_times(27)  # 返回背包界面
            # # 15.声骸提示，背包已满：点击确定
            # elif automaticsimulation.match_char((712, 502), (1193, 537), "背包已满"):
            #     automaticsimulation.mouse_once_click(1276, 670)  # 点击确定
            # # 16.检测声骸等级：不存在等级/等级>0
            elif result>0:
                print("无声骸升级")
                return True
    except Exception as e:
        print(e)
        return  False


def Dinitialization_strengthen_sound_core(strengthen_level: int, entry: str)-> bool:
    """
    通用的声骸强化界面
    :param strengthen_level: 强化到的等级
    :param entry: 强化后指定的词条,决定弃置还是锁定
    :return:
    """
    try:
        while True:
            # 1.检测声骸等级:等级存在>0,培养
            if (result := automaticsimulation.recognize_char((1770, 250), (1830, 280))) and int(result[0][0].replace("+", "") or -1) == 0:
                automaticsimulation.mouse_once_click(1720,1000)# 点击培养
            # 2.同步调谐按键:点击同步调谐
            elif automaticsimulation.match_char((1015, 537), (1174, 566), "开启同步调谐"):
                automaticsimulation.mouse_once_click(1192, 544)  # 点击同步调谐
            # 3.检测自动放入设置:点击确定
            elif automaticsimulation.match_char((1531, 884), (1596, 916), "确认"):
                automaticsimulation.mouse_once_click(1563, 895)  # 点击确认
            # 4.检测是否开启同步调谐标志:点击设置
            elif not automaticsimulation.match_char((621, 882), (685, 898), "/"):
                automaticsimulation.mouse_once_click(654, 757)  # 点击设置
            # 4.放入升级材料
            elif automaticsimulation.match_char((451, 742), (538, 768), "阶段放入"):
                automaticsimulation.mouse_once_click(495, 756)  # 点击放入
            # 5.点击强化并调谐
            elif automaticsimulation.match_char((451, 742), (498, 1010), "强化并调谐"):
                automaticsimulation.mouse_once_click(431, 993)  # 点击强化并调谐
            # 6.调谐成功:点击任意位置返回
            elif automaticsimulation.match_char((885, 275), (1029, 310), "调谐成功"):
                automaticsimulation.mouse_once_click(935, 219)  # 点击任意位置返回
            # 7.检测词条:有指定词条,没有锁定,点击锁定
            elif automaticsimulation.match_char((221, 324), (414, 522), entry) and not automaticsimulation.get_three_pixel_color(674, 129, "1A1A1A", 674, 128, "1A1A1A", 670, 135, "1A1A1A"):
                automaticsimulation.key_down_times("C", 1, 50, 200)
            # 8.检测词条:没有指定词条,没有弃置,点击弃置
            elif not automaticsimulation.match_char((221, 324), (414, 522), entry) and automaticsimulation.get_three_pixel_color(610, 129, "1A1A1A", 623, 133, "1A1A1A", 616, 122, "FFFFFF"):
                automaticsimulation.key_down_times("Z", 1, 50, 200)
            # 9.检测等级:等级=5,完成一次
            elif not (result := automaticsimulation.recognize_char((180, 180), (239, 206))) or int(result[0][0].replace("+", "")) >=  strengthen_level:
                automaticsimulation.key_down_times(13)  # 返回背包界面
            # 10.声骸提示，背包已满：点击确定
            elif automaticsimulation.match_char((712, 502), (1193, 537), "背包已满"):
                automaticsimulation.mouse_once_click(1276, 670)  # 点击确定
            # 11检测声骸等级：不存在等级/等级>0
            elif not (result := automaticsimulation.recognize_char((1770, 250), (1830, 280))) or int(result[0][0].replace("+", "")) > 0:
                print("无声骸升级")
                return True
    except Exception as e:
        print(e)
        return  False



# Initialization_Game_Inferface()
# auto_upgrade_sound_core()
# print(initialization_bag())
initialization_strengthen_sound_core(5,"暴击")



















# from torchgen.executorch.api.et_cpp import return_type
#
# from 前台按键模拟 import FrontEndAutomation
# from EasyOCR库文字识别 import OCRCharRecognit
# import time
# feat=FrontEndAutomation()
# charcor=OCRCharRecognit()
#
#
# # i=0
# def hecheng():
#     if charcor.ocr_find_match_char((1335,968,1441,998),"批量融合")[0]:
#         feat.mouse_once_click(1296,979)
#     elif charcor.ocr_find_match_char((481,979,525,1004),"全部")[0]:
#         feat.mouse_once_click(1296,979)#点击筛选
#     elif charcor.ocr_find_match_char((126,110,189,142),"筛选")[0]:
#         feat.mouse_once_click(1720, 221)#初始化滚轮
#         feat.mouse_once_click(1722, 607)#合鸣
#     elif charcor.ocr_find_match_char((242,769,290,794),"属性")[0]:
#
#         pass
# # feat.random_delay(2000,0)
# # hecheng()
#
# # input()
# # (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
#
# def ChooseChorus(select:int):
#     Chorus={
#         0:"凝夜白霜",
#         1:"啸谷长风",
#         2:"隐世回光",
#         3:"凌冽决断之心",
#         4:"高天共奏之曲",
#         5:"熔山裂谷",
#         6:"浮星祛暗",
#         7:"轻云出月",
#         8:"此间永驻之光",
#         9:"无惧浪涛之勇",
#         10:"彻空冥雷",
#         11:"沉日劫明",
#         12:"不绝余音",
#         13:"幽夜隐匿之帷",
#         14:"流云逝尽之空",
#     }
#     #检测参数是否超标
#     if len(select)>len(Chorus):
#         print("select列表超出选项数量")
#         return False
#     elif max(select)>max(Chorus):
#         print("select列表超出序号最大值")
#         return False
#     feat.mouse_once_click(1720, 221)#初始化滚轮
#     feat.mouse_once_click(1190,892 )# 点击重置
#     feat.mouse_once_click(1722, 607)#点击合鸣位置
#     # 点击初始坐标(239+236,244+52), 点击相隔(473,103)。识别初始区域(292,265,490,310)
#     for i in range(3):#三列
#         for j in range(5):#五行
#             if charcor.ocr_find_match_char((292 + i * 473, 265 + j * 103, 490 + i * 473, 310 + j * 103),Chorus[select])[0]:
#                 feat.mouse_once_click(475 + i * 473, 296 + j * 103)
#                 print(f"匹配{Chorus[select]}成功")
#                 break
#
#
# def ChooseAttribute(select:list[int]):
#     Chorus_Attribute = {
#         0: "生命值百分比",
#         1: "暴击率",
#         2: "冷凝伤害加成",
#         3: "气动伤害加成",
#         4: "共鸣效率",
#         5: "防御力",
#         6: "攻击力百分比",
#         7: "暴击伤害",
#         8: "热熔伤害加成",
#         9: "衍射伤害加成",
#         10: "生命值",
#         11: "防御力百分比",
#         12: "治疗效果加成",
#         13: "导电伤害加成",
#         14: "湮灭伤害加成",
#         15: "攻击力",
#     }
#     #检测参数是否超标
#     if len(select)>len(Chorus_Attribute):
#         print("select列表超出选项数量")
#         return False
#     elif max(select)>max(Chorus_Attribute):
#         print("select列表超出序号最大值")
#         return False
#     feat.mouse_once_click(1720, 221)  # 初始化滚轮
#     feat.mouse_once_click(1190, 892)  # 点击重置
#     feat.mouse_once_click(1720, 799)  # 点击属性位置
#     # 点击初始坐标(239+236,204+52), 点击相隔(473,103)。识别初始区域(290，240，535，270)
#     for i in range(3):  # 三列
#         for j in range(6):  # 五行
#             result = charcor.ocr_find_match_char((290 + i * 473, 240 + j * 103, 535 + i * 473, 270 + j * 103))
#             # 检测选项单里面是否有主属性
#             for k in select:
#                 if result[0] and result[2].find(Chorus_Attribute[k])!=-1:
#                     feat.mouse_once_click(475 + i * 473, 256 + j * 103)
#                     print(f"成功匹配主属性： “{Chorus_Attribute[k]}”")
#                     break

result=None
if automaticsimulation.match_char((885, 275), (1029, 310), "调谐成功") result:=1:
