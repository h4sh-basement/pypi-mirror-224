from pathlib import Path
from nonebot.matcher import Matcher
from nonebot.plugin import on_startswith
from uvdiviner.divine import quick_check, make_trigram
from uvdiviner.evolution import trigram, diagram
from uvdiviner.main import get_useful_data
from uvdiviner import colorize
from .multilogging import multilogger
from nonebot.plugin import PluginMetadata
from nonebot.adapters import Event
from .utils import version as __version__, init, reset_limit, minus_limit, get_limit, has_group, has_user, set_user

import nonebot
import logging
import sys
import asyncio

__plugin_meta__ = PluginMetadata(
    name="周易蓍草占卜",
    description="基于古蓍草占卜的算法, 简单的使用`.divine`指令.",
    usage="安装即可使用.",
    type="application",
    homepage="https://gitee.com/unvisitor/nonebot-plugin-uvdiviner",
)

DEBUG = False
colorize.disable()
driver = nonebot.get_driver()
current_dir = Path(__file__).resolve().parent
logger = multilogger(name="UV Diviner", payload="Nonebot2")
scheduler = nonebot.require("nonebot_plugin_apscheduler").scheduler

divinecommand = on_startswith(".divine", priority=2, block=True)
dqccommand = on_startswith(".dqc", priority=2, block=True)

async def divine(matcher: Matcher):
    global DEBUG
    
    await matcher.send(
        "天何言哉，叩之即应；神之灵矣，感而遂通。\n"
        "今有某人，有事关心，罔知休咎，罔释厥疑，\n"
        "惟神惟灵，望垂昭报，若可若否，尚明告之。"
        )
    logger.warning(
        "天何言哉，叩之即应；神之灵矣，感而遂通。\n"
        "今有某人，有事关心，罔知休咎，罔释厥疑，\n"
        "惟神惟灵，望垂昭报，若可若否，尚明告之。"
    )
    trigrams = [make_trigram(), make_trigram(), make_trigram(),] if not DEBUG else [trigram(8), trigram(8), trigram(6),]

    for _ in range(1, 28):
        if not DEBUG:
            await asyncio.sleep(1)

    await matcher.send("某宫三象，吉凶未判，再求外象三爻，以成一卦，以决忧疑。")
    logger.warning("某宫三象，吉凶未判，再求外象三爻，以成一卦，以决忧疑。")

    for _ in range(28, 56):
        if not DEBUG:
            await asyncio.sleep(1)

    trigrams += [make_trigram(), make_trigram(), make_trigram()] if not DEBUG else [trigram(9), trigram(8), trigram(8)]

    if not DEBUG: await asyncio.sleep(1)

    dia = diagram(trigrams)

    static, variable, result = get_useful_data(dia)

    if not static["卦名"] == variable["卦名"]:
        await matcher.send(
                "占卜结果: " + static["卦名"][:-1] + "之" + variable["卦名"][:-1]
                )
        logger.info("占卜结果: " + static["卦名"][:-1] + "之" + variable["卦名"][:-1])
    else:
        await matcher.send("占卜结果:", static["卦名"])
        logger.info("占卜结果:", static["卦名"])

    if not DEBUG: await asyncio.sleep(1)

    await matcher.send("本卦: " + static["卦名"] + "\n" + "卦辞: " + static["卦辞"])
    logger.info("本卦: " + static["卦名"] + "\n" + "卦辞: " + static["卦辞"])

    if not DEBUG: await asyncio.sleep(1)

    if dia.variated != 0:
        await matcher.send("变卦:" + variable["卦名"] + "\n   卦辞: " + variable["卦辞"] + "\n" + "变爻数:" + str(dia.variated))
        logger.info("变卦:" + variable["卦名"] + "\n   卦辞: " + variable["卦辞"] + "\n" + "变爻数:" + str(dia.variated))

    if not DEBUG: await asyncio.sleep(2)

    await matcher.send(result)
    logger.info(result)

@driver.on_startup
async def _():
    global DEBUG
    logger.info("欧若可卜师初始化中...")
    if DEBUG:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.remove()
        logger.add(
            sys.stdout,
            level = "DEBUG"
        )
        logger.info("DEBUG 模式已启动.")
    init()
    logger.success("欧若可卜师初始化完毕.")

@divinecommand.handle()
async def divinehandler(matcher: Matcher, event: Event):
    logger.warning("用户尝试发起一场占卜.")
    if not has_user(event):
        set_user(event)

    if get_limit(event) <= 0 and not DEBUG:
        await matcher.send("今日占卜次数已达安全上限, 欧若可拒绝继续进行占卜.")
        logger.warning("今日占卜次数已达安全上限, 欧若可拒绝继续进行占卜.")
        return
    minus_limit(event)
    await divine(matcher)
    logger.success("占卜完成.")

@dqccommand.handle()
async def dqchandler(matcher: Matcher, event: Event):
    logger.warning("用户尝试发起一场快速占卜检定.")
    if not has_user(event):
        set_user(event)

    if get_limit(event) <= 0 and not DEBUG:
        await matcher.send("今日占卜次数已达安全上限, 欧若可拒绝继续进行占卜.")
        logger.warning("今日占卜次数已达安全上限, 欧若可拒绝继续进行占卜.")
        return
    minus_limit(event)
    result = str(quick_check())
    await matcher.send(result)
    logger.info(f"占卜结果: {result}")
    logger.success("快速检定完成.")

@scheduler.scheduled_job("cron", hour='1', minute='00', id="reset")
async def schedulerhandler(matcher: Matcher, event: Event):
    reset_limit()
    await matcher.send("新的一天开始了, 占卜限制已重置.")