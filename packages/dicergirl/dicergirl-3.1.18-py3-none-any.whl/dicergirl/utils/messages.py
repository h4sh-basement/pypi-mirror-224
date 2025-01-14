try:
    from .utils import version
except ImportError:
    from dicergirl.utils.utils import version

class Help_Messages():
    def __init__(self):
        self.main = f"""欧若可骰娘 Version {version}
此骰娘基于腾讯 QQ频道(qq-botpy)及 Nonebot2 搭建, \
由欧若可(Oracle)提供部分算法支持.
最终版本由未知访客团队(Unknow Visitor, 原左旋联盟)完成.
感谢 灵冬-老孙 提供相关技术支持.

.help 帮助信息
.su   进行超级管理员鉴权
.coc  进行车卡, 完成 COC 角色作成
.scp  进行车卡, 完成 SCP 角色作成
.dnd  进行车卡, 完成 DND 角色作成
.mode 切换当前跑团模式
.r    投掷指令 例如:
            .r 10 100 (10D100)
            .r 10d100 (10D100)
        d   制定骰子面数
        a   检定
            .ra [str: 数据名] 例如:
                .ra 幸运 (默认为幸运值D100)
                .ra 幸运 80 (幸运值D80)
                .ra 力量 90 (力量值D90)
        h   暗骰 - 无效算法
        #   多轮检定
        bp  奖励骰&惩罚骰 - 无效算法
        +/- 附加计算 - 无效算法
.sra  基金会特工标准检定
.dam  调查员或特工承伤检定
.at   调查员或特工伤害检定
.sc   疯狂检定
.st   射击命中判定
.ti   临时疯狂症状
.li   总结疯狂症状
.en   技能成长 - 无效算法
.set  角色卡设定
        .set [str: 数据名] [int: 数据]
.show 角色卡查询
.sa   COC快速检定
.del  删除数据
        .del c  删除临时数据
        .del card 删除存储数据
输入`.help [指令名]`获取该指令的详细信息
注: 以上的 "aDb" 格式(例如10D100)的内容, 表示模拟投掷100面骰子, 投掷10次, 结果小于检定值则检定通过.

欧若可骰娘 版本 {version}, 未知访客版权所有.
Copyright © 2011-2023 Unknown Visitor. All Rights Reserved."""
        self.r = """.r[a#d]    投掷指令 例如:
            .r 10 100 (10D100)
        d   制定骰子面数
        a   检定
            .ra [str: 数据名] 例如:
                .ra 幸运 (默认为幸运值D100)
                .ra 幸运 80 (幸运值D80)
                .ra 力量 90 (力量值D90)
        h   暗骰指令, 骰子结构将会私聊发送给该指令者, 遗憾的是, 该指令的算法无效
        #   多轮投掷指令, `#`后接数字即可设定多轮投掷
        bp  奖励骰与惩罚骰, 但是遗憾的是, 该指令的算法无效
        +/- 附加计算指令, 遗憾的是, 该指令的算法无效"""
        self.sc = """.sc [int: success]/[int: failure] [int: SAN]   疯狂检定
        success: 判定成功降低san值, 支持aDb语法(a、b与x为数字)
        failure: 判定失败降低san值, 支持aDb语法(a、b与x为数字)
        SAN: 当前SAN值, 缺省该参数则会自动使用该用户已保存的人物卡数据."""
        self.set = """.set [str: name] [(num or str): data]
        name: 属性名称
        data: 目标属性值 例如:
            .set 名字 阿斯塔特 (将你的名字设置为 “阿斯塔特”, 注意, 设置中文参数不支持无间隔传参)
            .set 幸运 80 (将你的幸运设置为 80)
            .set 计算机 99 (将你的计算机技能设置为 99)            
        可以单独输入`.set`指令, 欧若可将自动读取最近一次coc指令结果进行保存.
        .set 指令已经支持批量数据传输, 例如:
            .set 名字 阿斯塔特 幸运 80 (将你的名字设置为 “阿斯塔特” 并将你的幸运设置为 80)"""
        self.show = """.show [skill(skills, s)|all]
        目前仅支持查询自身人物卡.
            .show skill 查看自身人物卡技能
            .show all 查询所有存储的人物卡"""
        self.ra = """.ra [str: name]    快速检定
        name: 属性名称 例如:
            .ra 幸运 快速检定幸运
            .ra 力量 快速检定力量"""
        self.sra = """.sra [str: name]    SCP标准检定
        name: 属性名称 例如:
            .sra 命运 检定命运属性
            .sra 健康 检定健康属性"""
        self.en = ".en skill_level\n" \
            "skill_level: 需要成长的技能当前等级。"
        self.del_ = """.[s]del [c|card|str: talent]
        删除数据, args可以有以下值
        c: 清空暂存数据
        card: 删除使用中的人物卡(慎用)
        talent: 其他任意技能名
        该命令支持多个参数混合使用, 可以一次指定多个技能名, 使用空格隔开"""
        self.mode = """.mode [str: mode]
        切换跑团模式 例如:
            .mode coc 切换到COC跑团模式"""

help_messages = Help_Messages()

def help_message(args: str):
    if args in help_messages.__dict__.keys():
        return help_messages.__dict__[args]
    else:
        return help_messages.main

temporary_madness = [
    "1) 失忆: 调查员会发现自己身处于一个安全的地点却没有任何来到这里的记忆。例如, 调查员前一刻还在家中吃着早饭, 下一刻就已经直面着不知名的怪物。这将会持续1D10轮。",
    "2) 假性残疾:调查员陷入了心理性的失明, 失聪以及躯体缺失感中, 持续1D10轮。",
    "3) 暴力倾向: 调查员陷入了六亲不认的暴力行为中, 对周围的敌人与友方进行着无差别的攻击, 持续1D10轮。",
    "4) 偏执: 调查员陷入了严重的偏执妄想之中, 持续1D10轮。有人在暗中窥视着他们, 同伴中有人背叛了他们, 没有人可以信任, 万事皆虚。",
    "5) 人际依赖: 守密人适当参考调查员的背景中重要之人的条目, 调查员因为一些原因而降他人误认为了他重要的人并且努力的会与那个人保持那种关系, 持续1D10轮。",
    "6) 昏厥: 调查员当场昏倒, 并需要1D10轮才能苏醒。",
    "7) 逃避行为: 调查员会用任何的手段试图逃离现在所处的位置, 即使这意味着开走唯一一辆交通工具并将其它人抛诸脑后, 调查员会试图逃离1D10轮。",
    "8) 竭嘶底里:调查员表现出大笑, 哭泣, 嘶吼, 害怕等的极端情绪表现, 持续1D10轮。",
    "9) 恐惧: 调查员通过一次D100或者由守密人选择, 来从恐惧症状表中选择一个恐惧源, 就算这一恐惧的事物是并不存在的, 调查员的症状会持续1D10轮。",
    "10) 躁狂: 调查员通过一次D100或者由守密人选择, 来从躁狂症状表中选择一个躁狂的诱因, 这个症状将会持续1D10轮。"
]
madness_end = [
    "1) 失忆(Amnesia) : 回过神来, 调查员们发现自己身处一个陌生的地方, 并忘记了自己是谁。记忆会随时间恢复。",
    "2) 被窃(Robbed) : 调查员在1D10小时后恢复清醒, 发觉自己被盗, 身体毫发无损。如果调查员携带着宝贵之物(见调查员背景) , 做幸运检定来决定其是否被盗。所有有价值的东西无需检定自动消失。",
    "3) 遍体鳞伤(Battered) : 调查员在1D10小时后恢复清醒, 发现自己身上满是拳痕和瘀伤。生命值减少到疯狂前的一半, 但这不会造成重伤。调查员没有被窃。这种伤害如何持续到现在由守秘人决定。",
    "4) 暴力倾向(Violence) : 调查员陷入强烈的暴力与破坏欲之中。调查员回过神来可能会理解自己做了什么也可能毫无印象。调查员对谁或何物施以暴力, 他们是杀人还是仅仅造成了伤害, 由守秘人决定。",
    "5) 极端信念(Ideology/Beliefs) : 查看调查员背景中的思想信念, 调查员会采取极端和疯狂的表现手段展示他们的思想信念之一。比如一个信教者会在地铁上高声布道。",
    "6) 重要之人(Significant People) : 考虑调查员背景中的重要之人, 及其重要的原因。在1D10小时或更久的时间中, 调查员将不顾一切地接近那个人, 并为他们之间的关系做出行动。",
    "7) 被收容(Institutionalized) : 调查员在精神病院病房或警察局牢房中回过神来, 他们可能会慢慢回想起导致自己被关在这里的事情。",
    "8) 逃避行为(Flee in panic) : 调查员恢复清醒时发现自己在很远的地方, 也许迷失在荒郊野岭, 或是在驶向远方的列车或长途汽车上。",
    "9) 恐惧(Phobia) : 调查员患上一个新的恐惧症状。在表Ⅸ: 恐惧症状表上骰1个D100来决定症状, 或由守秘人选择一个。调查员在1D10小时后回过神来, 并开始为避开恐惧源而采取任何措施。",
    "10) 狂躁(Mania) : 调查员患上一个新的狂躁症状。在表Ⅹ: 狂躁症状表上骰1个D100来决定症状, 或由守秘人选择一个。调查员会在1D10小时后恢复理智。在这次疯狂发作中, 调查员将完全沉浸于其新的狂躁症状。这症状是否会表现给旁人则取决于守秘人和此调查员。"
]
phobias = [
    "1) 洗澡恐惧症(Ablutophobia) : 对于洗涤或洗澡的恐惧。",
    "2) 恐高症(Acrophobia) : 对于身处高处的恐惧。",
    "3) 飞行恐惧症(Aerophobia) : 对飞行的恐惧。",
    "4) 广场恐惧症(Agoraphobia) : 对于开放的(拥挤) 公共场所的恐惧。",
    "5) 恐鸡症(Alektorophobia) : 对鸡的恐惧。",
    "6) 大蒜恐惧症(Alliumphobia) : 对大蒜的恐惧。",
    "7) 乘车恐惧症(Amaxophobia) : 对于乘坐地面载具的恐惧。",
    "8) 恐风症(Ancraophobia) : 对风的恐惧。",
    "9) 男性恐惧症(Androphobia) : 对于成年男性的恐惧。",
    "10) 恐英症(Anglophobia) : 对英格兰或英格兰文化的恐惧。",
    "11) 恐花症(Anthophobia) : 对花的恐惧。",
    "12) 截肢者恐惧症(Apotemnophobia) : 对截肢者的恐惧。",
    "13) 蜘蛛恐惧症(Arachnophobia) : 对蜘蛛的恐惧。",
    "14) 闪电恐惧症(Astraphobia) : 对闪电的恐惧。",
    "15) 废墟恐惧症(Atephobia) : 对遗迹或残址的恐惧。",
    "16) 长笛恐惧症(Aulophobia) : 对长笛的恐惧。",
    "17) 细菌恐惧症(Bacteriophobia) : 对细菌的恐惧。",
    "18) 导弹/子弹恐惧症(Ballistophobia) : 对导弹或子弹的恐惧。",
    "19) 跌落恐惧症(Basophobia) : 对于跌倒或摔落的恐惧。",
    "20) 书籍恐惧症(Bibliophobia) : 对书籍的恐惧。",
    "21) 植物恐惧症(Botanophobia) : 对植物的恐惧。",
    "22) 美女恐惧症(Caligynephobia) : 对美貌女性的恐惧。",
    "23) 寒冷恐惧症(Cheimaphobia) : 对寒冷的恐惧。",
    "24) 恐钟表症(Chronomentrophobia) : 对于钟表的恐惧。",
    "25) 幽闭恐惧症(Claustrophobia) : 对于处在封闭的空间中的恐惧。",
    "26) 小丑恐惧症(Coulrophobia) : 对小丑的恐惧。",
    "27) 恐犬症(Cynophobia) : 对狗的恐惧。",
    "28) 恶魔恐惧症(Demonophobia) : 对邪灵或恶魔的恐惧。",
    "29) 人群恐惧症(Demophobia) : 对人群的恐惧。",
    "30) 牙科恐惧症①(Dentophobia) : 对牙医的恐惧。",
    "31) 丢弃恐惧症(Disposophobia) : 对于丢弃物件的恐惧(贮藏癖) 。",
    "32) 皮毛恐惧症(Doraphobia) : 对动物皮毛的恐惧。",
    "33) 过马路恐惧症(Dromophobia) : 对于过马路的恐惧。",
    "34) 教堂恐惧症(Ecclesiophobia) : 对教堂的恐惧。",
    "35) 镜子恐惧症(Eisoptrophobia) : 对镜子的恐惧。",
    "36) 针尖恐惧症(Enetophobia) : 对针或大头针的恐惧。",
    "37) 昆虫恐惧症(Entomophobia) : 对昆虫的恐惧。",
    "38) 恐猫症(Felinophobia) : 对猫的恐惧。",
    "39) 过桥恐惧症(Gephyrophobia) : 对于过桥的恐惧。",
    "40) 恐老症(Gerontophobia) : 对于老年人或变老的恐惧。",
    "41) 恐女症(Gynophobia) : 对女性的恐惧。",
    "42) 恐血症(Haemaphobia) : 对血的恐惧。",
    "43) 宗教罪行恐惧症(Hamartophobia) : 对宗教罪行的恐惧。",
    "44) 触摸恐惧症(Haphophobia) : 对于被触摸的恐惧。",
    "45) 爬虫恐惧症(Herpetophobia) : 对爬行动物的恐惧。",
    "46) 迷雾恐惧症(Homichlophobia) : 对雾的恐惧。",
    "47) 火器恐惧症(Hoplophobia) : 对火器的恐惧。",
    "48) 恐水症(Hydrophobia) : 对水的恐惧。",
    "49) 催眠恐惧症(Hypnophobia) : 对于睡眠或被催眠的恐惧。",
    "50) 白袍恐惧症(Iatrophobia) : 对医生的恐惧。",
    "51) 鱼类恐惧症(Ichthyophobia) : 对鱼的恐惧。",
    "52) 蟑螂恐惧症(Katsaridaphobia) : 对蟑螂的恐惧。",
    "53) 雷鸣恐惧症(Keraunophobia) : 对雷声的恐惧。",
    "54) 蔬菜恐惧症(Lachanophobia) : 对蔬菜的恐惧。",
    "55) 噪音恐惧症(Ligyrophobia) : 对刺耳噪音的恐惧。",
    "56) 恐湖症(Limnophobia) : 对湖泊的恐惧。",
    "57) 机械恐惧症(Mechanophobia) : 对机器或机械的恐惧。",
    "58) 巨物恐惧症(Megalophobia) : 对于庞大物件的恐惧。",
    "59) 捆绑恐惧症(Merinthophobia) : 对于被捆绑或紧缚的恐惧。",
    "60) 流星恐惧症(Meteorophobia) : 对流星或陨石的恐惧。",
    "61) 孤独恐惧症(Monophobia) : 对于一人独处的恐惧。",
    "62) 不洁恐惧症(Mysophobia) : 对污垢或污染的恐惧。",
    "63) 黏液恐惧症(Myxophobia) : 对黏液(史莱姆) 的恐惧。",
    "64) 尸体恐惧症(Necrophobia) : 对尸体的恐惧。",
    "65) 数字8恐惧症(Octophobia) : 对数字8的恐惧。",
    "66) 恐牙症(Odontophobia) : 对牙齿的恐惧。",
    "67) 恐梦症(Oneirophobia) : 对梦境的恐惧。",
    "68) 称呼恐惧症(Onomatophobia) : 对于特定词语的恐惧。",
    "69) 恐蛇症(Ophidiophobia) : 对蛇的恐惧。",
    "70) 恐鸟症(Ornithophobia) : 对鸟的恐惧。",
    "71) 寄生虫恐惧症(Parasitophobia) : 对寄生虫的恐惧。",
    "72) 人偶恐惧症(Pediophobia) : 对人偶的恐惧。",
    "73) 吞咽恐惧症(Phagophobia) : 对于吞咽或被吞咽的恐惧。",
    "74) 药物恐惧症(Pharmacophobia) : 对药物的恐惧。",
    "75) 幽灵恐惧症(Phasmophobia) : 对鬼魂的恐惧。",
    "76) 日光恐惧症(Phenogophobia) : 对日光的恐惧。",
    "77) 胡须恐惧症(Pogonophobia) : 对胡须的恐惧。",
    "78) 河流恐惧症(Potamophobia) : 对河流的恐惧。",
    "79) 酒精恐惧症(Potophobia) : 对酒或酒精的恐惧。",
    "80) 恐火症(Pyrophobia) : 对火的恐惧。",
    "81) 魔法恐惧症(Rhabdophobia) : 对魔法的恐惧。",
    "82) 黑暗恐惧症(Scotophobia) : 对黑暗或夜晚的恐惧。",
    "83) 恐月症(Selenophobia) : 对月亮的恐惧。",
    "84) 火车恐惧症(Siderodromophobia) : 对于乘坐火车出行的恐惧。",
    "85) 恐星症(Siderophobia) : 对星星的恐惧。",
    "86) 狭室恐惧症(Stenophobia) : 对狭小物件或地点的恐惧。",
    "87) 对称恐惧症(Symmetrophobia) : 对对称的恐惧。",
    "88) 活埋恐惧症(Taphephobia) : 对于被活埋或墓地的恐惧。",
    "89) 公牛恐惧症(Taurophobia) : 对公牛的恐惧。",
    "90) 电话恐惧症(Telephonophobia) : 对电话的恐惧。",
    "91) 怪物恐惧症①(Teratophobia) : 对怪物的恐惧。",
    "92) 深海恐惧症(Thalassophobia) : 对海洋的恐惧。",
    "93) 手术恐惧症(Tomophobia) : 对外科手术的恐惧。",
    "94) 十三恐惧症(Triskadekaphobia) : 对数字13的恐惧症。",
    "95) 衣物恐惧症(Vestiphobia) : 对衣物的恐惧。",
    "96) 女巫恐惧症(Wiccaphobia) : 对女巫与巫术的恐惧。",
    "97) 黄色恐惧症(Xanthophobia) : 对黄色或“黄”字的恐惧。",
    "98) 外语恐惧症(Xenoglossophobia) : 对外语的恐惧。",
    "99) 异域恐惧症(Xenophobia) : 对陌生人或外国人的恐惧。",
    "100) 动物恐惧症(Zoophobia) : 对动物的恐惧。"
]
manias = [
    "1) 沐浴癖(Ablutomania) : 执着于清洗自己。",
    "2) 犹豫癖(Aboulomania) : 病态地犹豫不定。",
    "3) 喜暗狂(Achluomania) : 对黑暗的过度热爱。",
    "4) 喜高狂(Acromaniaheights) : 狂热迷恋高处。",
    "5) 亲切癖(Agathomania) : 病态地对他人友好。",
    "6) 喜旷症(Agromania) : 强烈地倾向于待在开阔空间中。",
    "7) 喜尖狂(Aichmomania) : 痴迷于尖锐或锋利的物体。",
    "8) 恋猫狂(Ailuromania) : 近乎病态地对猫友善。",
    "9) 疼痛癖(Algomania) : 痴迷于疼痛。",
    "10) 喜蒜狂(Alliomania) : 痴迷于大蒜。",
    "11) 乘车癖(Amaxomania) : 痴迷于乘坐车辆。",
    "12) 欣快癖(Amenomania) : 不正常地感到喜悦。",
    "13) 喜花狂(Anthomania) : 痴迷于花朵。",
    "14) 计算癖(Arithmomania) : 狂热地痴迷于数字。",
    "15) 消费癖(Asoticamania) : 鲁莽冲动地消费。",
    "16) 隐居癖(Automania) : 过度地热爱独自隐居(原文如此, 存疑, Automania实际上是恋车癖) 。",
    "17) 芭蕾癖(Balletmania) : 痴迷于芭蕾舞。",
    "18) 窃书癖(Biliokleptomania) : 无法克制偷窃书籍的冲动。",
    "19) 恋书狂(Bibliomania) : 痴迷于书籍和/或阅读。",
    "20) 磨牙癖(Bruxomania) : 无法克制磨牙的冲动。",
    "21) 灵臆症(Cacodemomania) : 病态地坚信自己已被一个邪恶的灵体占据。",
    "22) 美貌狂(Callomania) : 痴迷于自身的美貌。",
    "23) 地图狂(Cartacoethes) : 在何时何处都无法控制查阅地图的冲动。",
    "24) 跳跃狂(Catapedamania) : 痴迷于从高处跳下。",
    "25) 喜冷症(Cheimatomania) : 对寒冷或寒冷的物体的反常喜爱。",
    "26) 舞蹈狂(Choreomania) : 无法控制地起舞或发颤。",
    "27) 恋床癖(Clinomania) : 过度地热爱待在床上。",
    "28) 恋墓狂(Coimetormania) : 痴迷于墓地。",
    "29) 色彩狂(Coloromania) : 痴迷于某种颜色。",
    "30) 小丑狂(Coulromania) : 痴迷于小丑。",
    "31) 恐惧狂(Countermania) : 执着于经历恐怖的场面。",
    "32) 杀戮癖(Dacnomania) : 痴迷于杀戮。",
    "33) 魔臆症(Demonomania) : 病态地坚信自己已被恶魔附身。",
    "34) 抓挠癖(Dermatillomania) : 执着于抓挠自己的皮肤。",
    "35) 正义狂(Dikemania) : 痴迷于目睹正义被伸张。",
    "36) 嗜酒狂(Dipsomania) : 反常地渴求酒精。",
    "37) 毛皮狂(Doramania) : 痴迷于拥有毛皮。(存疑) ",
    "38) 赠物癖(Doromania) : 痴迷于赠送礼物。",
    "39) 漂泊症(Drapetomania) : 执着于逃离。",
    "40) 漫游癖(Ecdemiomania) : 执着于四处漫游。",
    "41) 自恋狂(Egomania) : 近乎病态地以自我为中心或自我崇拜。",
    "42) 职业狂(Empleomania) : 对于工作的无尽病态渴求。",
    "43) 臆罪症(Enosimania) : 病态地坚信自己带有罪孽。",
    "44) 学识狂(Epistemomania) : 痴迷于获取学识。",
    "45) 静止癖(Eremiomania) : 执着于保持安静。",
    "46) 乙醚上瘾(Etheromania) : 渴求乙醚。",
    "47) 求婚狂(Gamomania) : 痴迷于进行奇特的求婚。",
    "48) 狂笑癖(Geliomania) : 无法自制地, 强迫性的大笑。",
    "49) 巫术狂(Goetomania) : 痴迷于女巫与巫术。",
    "50) 写作癖(Graphomania) : 痴迷于将每一件事写下来。",
    "51) 裸体狂(Gymnomania) : 执着于裸露身体。",
    "52) 妄想狂(Habromania) : 近乎病态地充满愉快的妄想(而不顾现实状况如何) 。",
    "53) 蠕虫狂(Helminthomania) : 过度地喜爱蠕虫。",
    "54) 枪械狂(Hoplomania) : 痴迷于火器。",
    "55) 饮水狂(Hydromania) : 反常地渴求水分。",
    "56) 喜鱼癖(Ichthyomania) : 痴迷于鱼类。",
    "57) 图标狂(Iconomania) : 痴迷于图标与肖像。",
    "58) 偶像狂(Idolomania) : 痴迷于甚至愿献身于某个偶像。",
    "59) 信息狂(Infomania) : 痴迷于积累各种信息与资讯。",
    "60) 射击狂(Klazomania) : 反常地执着于射击。",
    "61) 偷窃癖(Kleptomania) : 反常地执着于偷窃。",
    "62) 噪音癖(Ligyromania) : 无法自制地执着于制造响亮或刺耳的噪音。",
    "63) 喜线癖(Linonomania) : 痴迷于线绳。",
    "64) 彩票狂(Lotterymania) : 极端地执着于购买彩票。",
    "65) 抑郁症(Lypemania) : 近乎病态的重度抑郁倾向。",
    "66) 巨石狂(Megalithomania) : 当站在石环中或立起的巨石旁时, 就会近乎病态地写出各种奇怪的创意。",
    "67) 旋律狂(Melomania) : 痴迷于音乐或一段特定的旋律。",
    "68) 作诗癖(Metromania) : 无法抑制地想要不停作诗。",
    "69) 憎恨癖(Misomania) : 憎恨一切事物, 痴迷于憎恨某个事物或团体。",
    "70) 偏执狂(Monomania) : 近乎病态地痴迷与专注某个特定的想法或创意。",
    "71) 夸大癖(Mythomania) : 以一种近乎病态的程度说谎或夸大事物。",
    "72) 臆想症(Nosomania) : 妄想自己正在被某种臆想出的疾病折磨。",
    "73) 记录癖(Notomania) : 执着于记录一切事物(例如摄影) 。",
    "74) 恋名狂(Onomamania) : 痴迷于名字(人物的、地点的、事物的) 。",
    "75) 称名癖(Onomatomania) : 无法抑制地不断重复某个词语的冲动。",
    "76) 剔指癖(Onychotillomania) : 执着于剔指甲。",
    "77) 恋食癖(Opsomania) : 对某种食物的病态热爱。",
    "78) 抱怨癖(Paramania) : 一种在抱怨时产生的近乎病态的愉悦感。",
    "79) 面具狂(Personamania) : 执着于佩戴面具。",
    "80) 幽灵狂(Phasmomania) : 痴迷于幽灵。",
    "81) 谋杀癖(Phonomania) : 病态的谋杀倾向。",
    "82) 渴光癖(Photomania) : 对光的病态渴求。",
    "83) 背德癖(Planomania) : 病态地渴求违背社会道德(原文如此, 存疑, Planomania实际上是漂泊症) 。",
    "84) 求财癖(Plutomania) : 对财富的强迫性的渴望。",
    "85) 欺骗狂(Pseudomania) : 无法抑制的执着于撒谎。",
    "86) 纵火狂(Pyromania) : 执着于纵火。",
    "87) 提问狂(Questiong-Asking Mania) : 执着于提问。",
    "88) 挖鼻癖(Rhinotillexomania) : 执着于挖鼻子。",
    "89) 涂鸦癖(Scribbleomania) : 沉迷于涂鸦。",
    "90) 列车狂(Siderodromomania) : 认为火车或类似的依靠轨道交通的旅行方式充满魅力。",
    "91) 臆智症(Sophomania) : 臆想自己拥有难以置信的智慧。",
    "92) 科技狂(Technomania) : 痴迷于新的科技。",
    "93) 臆咒狂(Thanatomania) : 坚信自己已被某种死亡魔法所诅咒。",
    "94) 臆神狂(Theomania) : 坚信自己是一位神灵。",
    "95) 抓挠癖(Titillomaniac) : 抓挠自己的强迫倾向。",
    "96) 手术狂(Tomomania) : 对进行手术的不正常爱好。",
    "97) 拔毛癖(Trichotillomania) : 执着于拔下自己的头发。",
    "98) 臆盲症(Typhlomania) : 病理性的失明。",
    "99) 嗜外狂(Xenomania) : 痴迷于异国的事物。",
    "100) 喜兽癖(Zoomania) : 对待动物的态度近乎疯狂地友好。"
]
