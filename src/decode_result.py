# coding: utf-8
import os
import sys

### config
config = [
    {
        "key": "﻿调查人",
        "type": "input"
    },
    {
        "key": "调查日期",
        "type": "input"
    },
    {
        "key": "编号",
        "type": "input"
    },
    {
        "key": "姓名",
        "type": "input"
    },
    {
        "key": "手机号",
        "type": "input"
    },
    {
        "key": "姓别",
        "type": "choice",
        "value": ["男","女"]
    },
    {
        "key": "出生年月",
        "type": "input"
    },
    {
        "key": "身高",
        "type": "input"
    },
    {
        "key": "体重",
        "type": "input"
    },
    {
        "key": "民族",
        "type": "choice",
        "value": ["汉族","回族","蒙古族","藏族","满族"]
    },
    {
        "key": "职业",
        "type": "input"
    },
    {
        "key": "粉尘",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "辐射",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "噪声",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "高温",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "有毒化学品",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "其他",
        "type": "input"
    },
    {
        "key": "出生地",
        "type": "input"
    },
    {
        "key": "常住地",
        "type": "input"
    },
    {
        "key": "婚姻状况",
        "type": "choice",
        "value": ["已婚","未婚","离异","丧偶"]
    },
    {
        "key": "生育史",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "血型",
        "type": "choice",
        "value": ["O","B","A","AB","不详"]
    },
    {
        "key": "吸烟史",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "平均吸烟量(支/天)",
        "type": "input"
    },
    {
        "key": "吸烟时间(年)",
        "type": "input"
    },
    {
        "key": "是否已戒烟",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "戒烟时间",
        "type": "input"
    },
    {
        "key": "饮酒史",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "种类",
        "type": "choice",
        "value": ["白酒","啤酒","黄酒","红酒","米酒"]
    },
    {
        "key": "平均饮酒量(两/天)",
        "type": "input"
    },
    {
        "key": "饮酒时间(年)",
        "type": "input"
    },
    {
        "key": "是否已戒酒",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "戒酒时间",
        "type": "input"
    },
    {
        "key": "首次确诊时间",
        "type": "input"
    },
    {
        "key": "电子胃镜",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "上消化道造影",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "使用抗幽门螺旋杆菌药物",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "使用抗生素",
        "type": "choice",
        "value": ["有","无"]
    },
    {
        "key": "用药详情",
        "type": "input"
    },
    {
        "key": "其他病史",
        "type": "choice",
        "value": ["胃息肉","手术后残胃","返流性食管炎","胃溃疡","十二指肠溃疡","恶性贫血","脑卒中","冠心病","糖尿病","高血压","高脂血症"]
    },
    {
        "key": "一级亲属是否患有胃癌",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "患胃癌亲属",
        "type": "choice",
        "value": ["父亲","母亲","兄弟姐妹","子女"]
    },
    {
        "key": "其他家族史",
        "type": "choice",
        "value": ["慢性胃炎","胃息肉","手术后残胃","返流性食管炎","胃溃疡","十二指肠溃疡","恶性贫血","脑卒中","冠心病","糖尿病","高血压","高脂血症"]
    },
    {
        "key": "饮用水",
        "type": "choice",
        "value": ["自来水","井水","河水"]
    },
    {
        "key": "饮食时间",
        "type": "choice",
        "value": ["饮食规律","偶尔规律","经常不规律"]
    },
    {
        "key": "油腻",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "甜食",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "辛辣",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "酸",
        "type": "choice",
        "value": ["是","否"]
    },
    {
        "key": "其他",
        "type": "input"
    },
    {
        "key": "咸淡",
        "type": "choice",
        "value": ["清淡","教咸","很咸"]
    },
    {
        "key": "冷热",
        "type": "choice",
        "value": ["无偏好","温热食物","冷食"]
    },
    {
        "key": "隔夜菜",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "腌/熏制食品",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "煎/炸制食品",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "高糖饮料",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "鱼露频率",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "食用时间",
        "type": "input"
    },
    {
        "key": "虾油频率",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "食用时间",
        "type": "input"
    },
    {
        "key": "新鲜蔬菜",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "新鲜水果",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "茶叶摄入频率",
        "type": "choice",
        "value": ["从不","很少","有时","经常"]
    },
    {
        "key": "种类",
        "type": "choice",
        "value": ["绿茶","红茶","黑茶","黄茶","白茶","乌龙茶"]
    },
    {
        "key": "摄入时间",
        "type": "input"
    },
    {
        "key": "胃疼",
        "type": "choice",
        "value": ["无","有"]
    },
    {
        "key": "类型",
        "type": "choice",
        "value": ["隐痛","灼痛","刺痛","胀痛"]
    },
    {
        "key": "程度",
        "type": "choice",
        "value": ["1","2","3","4","5","6","7","8","9","10"]
    },
    {
        "key": "补充说明",
        "type": "input"
    },
    {
        "key": "胃部寒热",
        "type": "choice",
        "value": ["胃部喜温","胃部喜凉"]
    },
    {
        "key": "胃胀",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "胁肋疼痛",
        "type": "choice",
        "value": ["无","有"]
    },
    {
        "key": "类型",
        "type": "choice",
        "value": ["隐痛","刺痛","胀痛","窜痛"]
    },
    {
        "key": "胸闷",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "嗳气",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "声音",
        "type": "choice",
        "value": ["声音低弱","声音洪亮"]
    },
    {
        "key": "反酸",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "口干",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "口苦",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "食欲不振",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "恶心呕吐",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "畏寒肢冷",
        "type": "choice",
        "value": ["手脚发冷","全身怕冷","手脚发热","全身怕热"]
    },
    {
        "key": "失眠",
        "type": "choice",
        "value": ["无","轻度","中度","重度"]
    },
    {
        "key": "大便形态",
        "type": "choice",
        "value": ["水样","稀溏","粘稠","成形","干结","球状"]
    },
    {
        "key": "舌质/舌体",
        "type": "input"
    },
    {
        "key": "舌苔",
        "type": "input"
    },
    {
        "key": "脉象",
        "type": "input"
    },
    {
        "key": "其他症状",
        "type": "input"
    },
    {
        "key": "备注",
        "type": "input"
    }
]


# confirm it is integer
def is_not_integer(s):
    try:
        int(s)
        return False
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return False
    except (TypeError, ValueError):
        pass
 
    return True


if __name__ == '__main__':
    ### read the choice list
    f = open("choice.txt", "r")
    choice_list = f.read().split("\n")
    f.close()

    all_result = []
    for cl in choice_list:
        if len(cl.strip()) == 0:
            continue
        cl = cl.split(";")
        result = []
        ### decode the choice for loop
        for i in range(len(cl)):
            value = cl[i].strip()
            cf = config[i]
            if cf["type"] == "choice":
                if value == "0":
                    result.append("NA")
                else:
                    all_value = []
                    for i in value.split(","):
                        if is_not_integer(i) or int(i) > len(cf["value"]):
                            all_value.append(i)
                        else:
                            all_value.append(cf["value"][int(i)-1])
                    result.append(";".join(all_value))
            elif cf["type"] == "input":
                if value == "0":
                    result.append("NA")
                else:
                    result.append(value)
        all_result.append("\t".join(result))
    print("\n".join(all_result))

