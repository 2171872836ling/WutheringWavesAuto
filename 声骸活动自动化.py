from AutomaticSimulationClass import AutomaticSimulation
automaticsimulation = AutomaticSimulation()


# 临时
def auto_test(necessary_cards:str)->bool:
    results=0# 场上多少声骸
    nums=14# 少于14只声骸才选择
    while True:

        if automaticsimulation.match_char((1626, 924), (1841, 975), "进入下一天", 0.25):
            automaticsimulation.mouse_once_click(1726, 949)
        # 检测当前场上多少声骸：识别到才报
        elif result:= automaticsimulation.recognize_char(352,330,443,359):
            results = int(result[0][0].replace("/20", ""))
            print("当前场上声骸",results,"只")
        # ----------------------------------------------卡牌界面------------------------------------------------------ #
        # 第一个卡牌选择
        elif nums<=results and automaticsimulation.match_char((345, 190), (560, 225), necessary_cards, 0.25):
            automaticsimulation.mouse_once_click(345, 190)
        # 第二个卡牌选择
        elif nums<=results and automaticsimulation.match_char((800, 190), (915, 225), necessary_cards, 0.25):
            automaticsimulation.mouse_once_click(800, 190)
        # 第三个卡牌选择
        elif nums<=results and automaticsimulation.match_char((1250, 190), (1365, 225), necessary_cards, 0.25):
            automaticsimulation.mouse_once_click(1250, 190)
        # 消耗刷新卡牌的免费次数
        elif automaticsimulation.match_char((390,840), (540,880), "免费刷新", 0.25):
            automaticsimulation.mouse_once_click(484,855)
        # 确认卡牌
        elif (nums<=results and automaticsimulation.match_char((1448,847), (1510,880), "确认", 0.25) and
              automaticsimulation.get_three_pixel_color(1498,854  ,"FFFFFF",1485,868 ,"FFFFFF" ,1469,868,"FFFFFF"  )):
            automaticsimulation.mouse_once_click(1478,852)
        # 确认跳过
        elif (nums>results and automaticsimulation.match_char((1096, 847), (1161, 880), "跳过", 0.25)and
              automaticsimulation.get_three_pixel_color(1498,854  ,"365146",1485,868 ,"365146" ,1469,868,"365146"  )):
            automaticsimulation.mouse_once_click(1125, 857)


        # ----------------------------------------------卡牌界面------------------------------------------------------ #
        elif automaticsimulation.match_char((1154, 698), (1217, 730), "确认", 0.25):
            automaticsimulation.mouse_once_click(1186, 716)
        elif automaticsimulation.match_char((929, 699), (990, 728), "确认", 0.25):
            automaticsimulation.mouse_once_click(956, 710)
        elif automaticsimulation.match_char((1529, 54), (1589, 87), "关闭", 0.25):
            automaticsimulation.mouse_once_click(1562, 66)
        automaticsimulation.random_delay(500, 500)


# auto_test("刺玫菇|异梦·浮灵偶")

if (result:=result if result := automaticsimulation.recognize_char((180, 180), (239, 206)) else "0"):
    pass

# and result[0][0].replace(
#     "+", "").isdigit() and int(result[0][0].replace("+", "")) >= 0: