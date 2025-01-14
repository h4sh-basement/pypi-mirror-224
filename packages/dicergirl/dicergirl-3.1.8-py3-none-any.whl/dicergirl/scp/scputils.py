try:
    from ..utils.messages import help_messages, help_message
    from ..utils.dicer import Dice, scp_doc, expr
    from .scpcards import scp_cards
    from .attributes import all_names, scp_attrs_dict as attrs_dict
    from .agent import Agent
    from ..utils.multilogging import multilogger
except ImportError:
    from dicergirl.utils.messages import help_messages, help_message
    from dicergirl.utils.dicer import Dice, scp_doc, expr
    from dicergirl.scp.scpcards import scp_cards
    from dicergirl.scp.attributes import scp_attrs_dict as attrs_dict, all_names
    from dicergirl.scp.agent import Agent
    from dicergirl.utils.multilogging import multilogger

import random

logger = multilogger(name="Dicer Girl", payload="SCPUtil")

def st():
    result = random.randint(1, 20)
    if result < 4:
        rstr = "右腿"
    elif result < 7:
        rstr = "左腿"
    elif result < 11:
        rstr = "腹部"
    elif result < 16:
        rstr = "胸部"
    elif result < 18:
        rstr = "右臂"
    elif result < 20:
        rstr = "左臂"
    elif result < 21:
        rstr = "头部"
    return "[Oracle] 命中了%s" % (rstr)

def at(args, event):
    inv = Agent().load(scp_cards.get(event))
    method = "+"

    if args:
        d = Dice().parse(args).roll()
    else:
        d = Dice().parse("1d6").roll()

    if "d" in inv.db():
        db = Dice(inv.db()).roll()
        dbtotal = db.total
        db = db.db
    else:
        db = int(inv.db())
        dbtotal = db
        if db < 0:
            method = ""

    return f"[Oracle] 投掷 {d.db}{method}{db}=({d.total}+{dbtotal})={d.total+dbtotal}\n造成了 {d.total+dbtotal}点 伤害."

def scp_dam(args, message):
    card = scp_cards.get(message)

    if not card:
        return "[Oracle] 未找到缓存数据, 请先使用`.scp`指令进行车卡生成角色卡并`.set`进行保存."

    max_hp = card["hp_max"]

    if len(args) == 1:
        if not args[0] in ["check", "c"]:
            arg = int(args[0])
            card["hp"] -= arg
            r = f"[Orcale] {card['name']} 失去了 {arg}点 生命"
        else:
            r = "检查特工状态"
    elif len(args) == 0:
        d = Dice().parse("1d6").roll()
        card["hp"] -= d.total
        r = "[Oracle] 投掷 1D6={d}\n受到了 {d}点 伤害".format(d=d.calc())
    elif len(args) == 3:
        if args[1] != "d":
            r = "[Oracle] 未知的指令格式."
        else:
            d = Dice().parse(f"{args[0]}{args[1]}{args[2]}").roll()
            card["hp"] -= d.total
            r = f"[Oracle] 投掷 {args[0]}D{args[2]}={d.calc()}\n受到了 {d.calc()}点 伤害"

    if card["hp"] <= 0:
        card["hp"] = 0
        r += f", 特工 {card['name']} 已死亡."
    elif (max_hp * 0.8 <= card["hp"]) and (card["hp"] < max_hp):
        r += f", 特工 {card['name']} 具有轻微伤势."
    elif (max_hp * 0.6 <= card["hp"]) and (card['hp'] <= max_hp * 0.8):
        r += f", 特工 {card['name']} 具有轻微伤."
    elif (max_hp * 0.4 <= card["hp"]) and (card["hp"] <= max_hp * 0.6):
        r += f", 特工 {card['name']} 具有轻伤."
    elif (max_hp * 0.2 <= card["hp"]) and (card["hp"] <= max_hp * 0.4):
        r += f", 特工 {card['name']} 身负重伤."
    elif max_hp * 0.2 >= card["hp"]:
        r += f", 特工 {card['name']} 濒死."
    else:
        r += "."

    scp_cards.update(message, card)
    return r

def sra(args, event):
    if len(args) == 0:
        return help_message("sra")

    if len(args) > 2:
        return "[Oracle] 错误: 参数过多(最多2需要但%d给予)." % len(args)
    
    if len(args) == 2:
        difficulty = int(args[1])
    else:
        difficulty = 12

    card_data = scp_cards.get(event)

    if not card_data:
        return "[Oracle] 在执行参数检定前, 请先执行`.scp`车卡并执行`.set`保存."

    inv = Agent().load(card_data)

    is_base = False
    for _, alias in attrs_dict.items():
        if args[0] in alias:
            dices = [dice for dice in inv.dices[alias[0]]]
            is_base = True
            break

    is_skill = False
    if not is_base:
        for skill in inv.skills:
            if args[0] == skill:
                v = inv.skills[skill]
                is_skill = True
                break

    if not is_base and not is_skill:
        return "[Oracle] 错误: 没有这个数据或技能."
    
    if not is_base and is_skill:
        return expr(Dice(), int(v))

    all_dices = []

    if len(dices) > 4:
        while len(all_dices) != 4:
            choice = random.choice(dices)
            all_dices.append(choice)
            dices.remove(choice)
    elif len(dices) <= 4:
        all_dices = dices

    results = []
    great = False
    for dice in all_dices:
        dice = Dice("1"+dice.lower()).roll()
        results.append(dice.total)
        if dice.great:
            great = True
    
    result = max(results)

    if len(results) > 1:
        results.remove(result)
        result += max(results)

    r = scp_doc(result, difficulty, agent=inv.name, great=great)
    return r

def scp_en(event, args):
    if not args:
        return help_messages.en

    try:
        en = int(args[1])
    except ValueError:
        return help_messages.en

    check = random.randint(1, 100)

    if check > arg or check > 95:
        plus = random.randint(1, 10)
        r = "判定值%d, 判定成功, 技能成长%d+%d=%d" % (check, arg, plus, arg+plus)
    else:
        return "判定值%d, 判定失败, 技能无成长。" % check