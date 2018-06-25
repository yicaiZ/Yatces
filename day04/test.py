# -*- coding:utf-8 -*-
# Author:Yatces

import itchat
from collections import Counter
from pyecharts import Bar

dict_sex = {}
count_city = None

# itchat微信登录，hotReload表示热登录，如果是True，下一次就不用扫码了（时间不能过长），会在根目录生成一个 itchat.pkl 的文件
itchat.auto_login(hotReload=False)
# itchat 的get_friends接口，获取微信好友列表，返回的列表第一位是你自己，如果想过滤掉自己，改为：itchat.get_friends()[1:]
member_list = itchat.get_friends()[0:]


def calc_all_sex():
    """
    微信联系人总男女信息
    :return:
    """
    man = woman = others = 0
    city = []
    for index, name in enumerate(member_list):
        print("\t{}、{}({})".format(index, name["RemarkName"] if name["RemarkName"] is not "" else name["NickName"],
                                   name["UserName"]))
        sex = name["Sex"]
        if sex == 1:
            man += 1
        elif sex == 2:
            woman += 1
        else:
            others += 1
        if name["City"] == "":
            city.append("未知城市")
        else:
            city.append(name["City"])

    global count_city
    count_city = Counter(city)
    total = len(member_list)
    man_percent = (float(man) / total * 100)
    woman_percent = (float(woman) / total * 100)
    others_percent = (float(others) / total * 100)

    print("\n>>>>>>>>>>>>>微信联系人总男女信息：")
    print("男性好友：%.2f%%" % man_percent)
    print("女性好友：%.2f%%" % woman_percent)
    print("其    它：%.2f%%" % others_percent)


class PeopleInfo:
    def __init__(self, man_, woman_, _others, total_):
        self.man = man_
        self.woman = woman_
        self.others = _others
        self.total = total_


def count(dict_={}):
    """
    计算各个地区的男女人数
    :param dict_:
    :return:
    """
    print("\n>>>>>>>>>>>>>各地区男女分布信息：")
    for val in dict_:
        city_tmp = "" if val == "未知城市" else val
        man = woman = others = 0
        for member in member_list:
            if member["City"] == city_tmp:
                sex = member["Sex"]
                if sex == 1:
                    man += 1
                elif sex == 2:
                    woman += 1
                else:
                    others += 1
        people_info = PeopleInfo(man, woman, others, dict_[val])
        dict_sex[val] = people_info
        print("【{}】男性：{}，女性：{}，其它：{}".format(city_tmp, man, woman, others))


def count_sex_area():
    """
    统计联系人性别、地区
    :return:
    """
    calc_all_sex()
    attr = ["{}".format(i) for i in count_city]
    count(count_city)
    v1 = []
    man_count = []
    woman_count = []
    others_count = []
    for i in attr:
        v1.append(count_city[i])
        man_count.append(dict_sex[i].man)
        woman_count.append(dict_sex[i].woman)
        others_count.append(dict_sex[i].others)

    bar = Bar(title="{}的微信联系人分布".format(member_list[0]["NickName"]), subtitle="微信联系人分布情况", width=2024, height=768)
    bar.add("地区人数", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("男性", attr, man_count, mark_line=["average"], mark_point=["max", "min"])
    bar.add("女性", attr, woman_count, mark_line=["average"], mark_point=["max", "min"])
    bar.render(path="地区统计.html")


def get_signatare():
    """
    获取微信联系人的签名信息
    :return:
    """
    for member in member_list:
        signatare = str(member["Signature"])
        print("\n{}:\n\t>>>>>:{}".format(member["RemarkName"], signatare))


if __name__ == '__main__':
    count_sex_area()
    get_signatare()
