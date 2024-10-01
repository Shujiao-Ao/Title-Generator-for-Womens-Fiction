# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:43:33 2024

@author: ASJ
"""

import random

def part_adv():
    list_A=["重生",
            "穿越",
            "嫁进豪门",
            "进入娱乐圈",
            "失忆",
            "抑制剂失效",
            "获得金手指",
            "C位出道",
            "分手",
            "逃婚"]
    random_number = random.randrange(0, 9)
    return list_A[random_number]
def part_adj():
    list_B=["遍地仇家",
            "被虐得体无完肤",
            "想当绿茶",
            "不愿再当替身",
            "沉迷赚钱",
            "只想当咸鱼",
            "觉醒精神体",
            "变成美强惨",
            "拒绝恋爱脑",
            "带球跑"]
    random_number = random.randint(0, 9)
    return list_B[random_number]
def part_n():
    list_C=["渣攻",
            "男神",
            "白月光",
            "前男友",
            "反派BOSS",
            "死对头",
            "超人气主播",
            "暗恋对象",
            "影帝",
            "最强战力"]
    random_number = random.randint(0, 9)
    return list_C[random_number]
def part_v():
    list_D=["成为了双人机甲驾驶员",
            "被系统绑定了",
            "HE了",
            "双向攻略了",
            "一起种田了",
            "称霸末世了",
            "崩人设了",
            "改写了原作剧情",
            "通关了逃生游戏",
            "联手复仇了"]
    random_number = random.randint(0, 9)
    return list_D[random_number]

def main():
    print(part_adv()+"后"+part_adj()+"的我和"+part_n()+part_v())   

if __name__ =="__main__":
    main()