scp_attrs_dict = {
    "名字": ["name", "名字", "名称", "姓名"],
    "性别": ["sex", "性别"],
    "年龄": ["age", "年龄"],
    "强度": ["str", "强度", "力量", "攻击"],
    "健康": ["hth", "健康", "体质"],
    "感知": ["per", "感知", "灵感"],
    "灵巧": ["dex", "灵巧", "敏捷"],
    "命运": ["fte", "命运", "幸运", "气运", "运气"],
    "魅力": ["chr", "魅力", "外貌"],
    "情报": ["int", "情报", "智力", "侦查"],
    "意志": ["wil", "意志", "精神", "理智"],
    "生命": ["hp", "生命"]
}

knowledge_data = {
    "解剖": ["解剖", "急救"],
    "古代语言": ["古代语言"],
    "建筑": ["建筑"],
    "天文学": ["天文学"],
    "护理": ["护理", "养育"],
    "计算机": ["计算机", "黑客攻击"],
    "烹饪": ["烹饪"],
    "拆除": ["拆除"],
    "时尚": ["时尚", "礼仪"],
    "赌博": ["赌博", "游戏"],
    "一般知识": ["一般知识"],
    "历史": ["历史", "知识"],
    "识别味道": ["识别味道", "气味"],
    "调查": ["调查"],
    "法律": ["法律", "政治"],
    "数学": ["数学"],
    "机械": ["机械"],
    "导航": ["导航"],
    "神秘": ["神秘", "SCP 知识"],
    "心理学": ["心理学"],
    "宗教": ["宗教"],
    "研究": ["研究", "互联网"],
    "科学": ["科学", "物理"],
    "生存": ["生存", "追踪"],
    "技术": ["技术"],
    "视觉信号": ["视觉信号", "手势语言"],
}

skills_data = {
    "近战": ["近战"],
    "突击步枪": ["突击步枪"],
    "手枪": ["手枪"],
    "重型火炮": ["重型火炮"],
    "猎枪": ["猎枪", "狙击步枪"],
    "霰弹枪": ["霰弹枪"],
    "冲锋枪": ["冲锋枪"],
    "演戏": ["演戏", "说谎"],
    "艺术": ["艺术", "音乐"],
    "挣脱": ["挣脱", "逃脱"],
    "抛投": ["抛投", "接"],
    "攀爬": ["攀爬"],
    "伪装": ["伪装", "混合"],
    "驾驶": ["驾驶"],
    "开锁": ["开锁"],
    "扒手": ["扒手"],
    "飞行员": ["飞行员"],
    "潜行": ["潜行", "隐藏"],
    "表演技巧": ["表演技巧"],
    "游泳": ["游泳"],
    "教导": ["教导"],
    "摔跤": ["摔跤", "缴械"],
    "写作": ["写作"],
}

ability_data = {
    "意识": ["意识", "反应"],
    "闪避": ["闪避", "格挡"],
    "动物驯服": ["动物驯服"],
    "运动": ["运动"],
    "同理心": ["同理心"],
    "耐力": ["耐力"],
    "主动权": ["主动权"],
    "威吓": ["威吓", "嘲弄"],
    "直觉": ["直觉"],
    "跳跃": ["跳跃"],
    "领导能力": ["领导能力"],
    "提拉力量": ["提拉力量"],
    "谈判": ["谈判", "说服"],
    "倒地": ["倒地", "死亡抗性"],
    "疼痛抗性": ["疼痛抗性"],
    "自我控制": ["自我控制"],
}

all_names = list(set().union(scp_attrs_dict, knowledge_data, skills_data, ability_data))