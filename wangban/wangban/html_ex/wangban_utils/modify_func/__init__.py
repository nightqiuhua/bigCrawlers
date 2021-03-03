# -*- coding: utf-8 -*-
import sys 
import os
#BASH_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(BASH_DIR)

#zhejiang
from .zhejiang.zhejiang import zhejiang_modifier
##jinhua
from .jinhua.jinhua import jinhua_modifier
##lishui
from .lishui.lishui import lishui_modifier
from .jiaxing.jiaxing import jiaxing_modifier
#

#hangzhou
from .hangzhou.tonglu import tonglu_modifier
from .hangzhou.jiande import jiande_modifier
from .hangzhou.chunan import chunan_modifier
from .hangzhou.fuyang import fuyang_modifier
from .hangzhou.xihuqu import xihuqu_modifier
from .hangzhou.xiaoshan import xiaoshan_modifier
from .hangzhou.yuhang import yuhang_modifier
from .hangzhou.linan import linan_modifier
from .hangzhou.gongshu import gongshu_modifier
from .hangzhou.jianggan import jianggan_modifier
from .hangzhou.dajiangdong import dajiangdong_modifier
from .hangzhou.hangzhou import hangzhou_modifier
##ningbo
from .ningbo.cixi import cixi_modifier
from .ningbo.fenghua import fenghua_modifier
from .ningbo.haishu import haishu_modifier
from .ningbo.xiangshan import xiangshan_modifier
from .ningbo.ningbobaoshuiqu import ningbobaoshuiqu_modifier
from .ningbo.beilun import beilun_modifier
from .ningbo.jiangbei import jiangbei_modifier
from .ningbo.ninghai import ninghai_modifier
from .ningbo.yinzhou import yinzhou_modifier
from .ningbo.yuyao import yuyao_modifier
from .ningbo.zhenhai import zhenhai_modifier
from .ningbo.daxiekaifaqu import daxiekaifaqu_modifier
from .ningbo.guojiagaoxinqu import guojiagaoxinqu_modifier
from .ningbo.hangzhouwanxinqu import hangzhouwanxinqu_modifier
from .ningbo.ninghai_ajax import ninghai_ajax_modifier
from .ningbo.yuyao_ajax import yuyao_ajax_modifier
from .ningbo.ningboshi import ningboshi_modifier
##shaoxing.
from .shaoxing.xinchang import xinchang_modifier
from .shaoxing.shangyu import shangyu_modifier
from .shaoxing.shengzhou import shengzhou_modifier
from .shaoxing.zhuji import zhuji_modifier
from .shaoxing.yuecheng import yuecheng_modifier
from .shaoxing.shaoxing import shaoxing_modifier
##taizhou.
from .taizhou.huangyan import huangyan_modifier
#from .taizhou.linhai import linhai_modifier
from .taizhou.luqiao import luqiao_modifier
from .taizhou.tiantai import tiantai_modifier
from .taizhou.xianju import xianju_modifier
from .taizhou.wenling import wenling_modifier
from .taizhou.yuhuan import yuhuan_modifier
#from .taizhou.yuhuan_ajax import CRAWL_YUHUAN_AJAX_TASKS
from .taizhou.taizhou import taizhou_modifier
#from .jiaojiang import CRAWL_JIAOJIANG_TASKS
##wenzhou.
from .wenzhou.cangnan import cangnan_modifier
from .wenzhou.dongtou import dongtou_modifier
from .wenzhou.leqing import leqing_modifier
from .wenzhou.longwan import longwan_modifier
from .wenzhou.lucheng import lucheng_modifier
from .wenzhou.ouhai import ouhai_modifier
from .wenzhou.pingyang import pingyang_modifier
from .wenzhou.ruian import ruian_modifier
from .wenzhou.taishun import taishun_modifier
from .wenzhou.wencheng import wencheng_modifier
from .wenzhou.yongjia import yongjia_modifier
from .wenzhou.wenzhou import wenzhou_modifier
##zhoushan.
from .zhoushan.putuo import putuo_modifier
from .zhoushan.daishan import daishan_modifier
from .zhoushan.dinghaiqu import dinghaiqu_modifier
from .zhoushan.shengsi import shengsi_modifier
from .zhoushan.zhoushan import zhoushan_modifier
##huzhou.
from .huzhou.anji import anji_modifier
from .huzhou.nanxun import nanxun_modifier
from .huzhou.wuxing import wuxing_modifier
from .huzhou.changxing import changxing_modifier
from .huzhou.deqing import deqing_modifier
from .huzhou.huzhou import huzhou_modifier
##quzhou.
from .quzhou.haining import haining_modifier
from .quzhou.qujiang import qujiang_modifier
from .quzhou.kaihua import kaihua_modifier
from .quzhou.jiangshan import jiangshan_modifier
from .quzhou.changshan import changshan_modifier
#from .quzhou.longyou import changshan_modifier
from .quzhou.kecheng import kecheng_modifier
#from .quzhou.longyou_ajax import CRAWL_LONGYOU_AJAX_TASKS
from .quzhou.quzhou import quzhou_modifier


all_modify_func = {
            #zhejiang
            'zhejiang':zhejiang_modifier,
            ##jinhua
            'jinhua':jinhua_modifier,
            ##lishui
            'lishui':lishui_modifier,
            'jiaxing':jiaxing_modifier,
            ##huzhou
            'anji':anji_modifier,'nanxun':nanxun_modifier,
            'changxing':changxing_modifier,'wuxing':wuxing_modifier,'deqing':deqing_modifier,
            'hangzhou':hangzhou_modifier,
            'huzhou':huzhou_modifier,
            ##qú zhōu
            'haining':haining_modifier,'qujiang':qujiang_modifier,'jiangshan':jiangshan_modifier,
            'kaihua':kaihua_modifier,'changshan':changshan_modifier,#'longyou':CRAWL_LONGYOU_TASKS,
            'kecheng':kecheng_modifier,#'longyou_ajax':CRAWL_LONGYOU_AJAX_TASKS,
            'quzhou':quzhou_modifier,
            ##NINGBO
            'cixi':cixi_modifier,'fenghua':fenghua_modifier,
            'haishu':haishu_modifier,'xiangshan':xiangshan_modifier,
            'ningbobaoshuiqu':ningbobaoshuiqu_modifier,'beilun':beilun_modifier,
            'jiangbei':jiangbei_modifier,'ninghai':ninghai_modifier,'yinzhou':yinzhou_modifier,
            'yuyao':yuyao_modifier,'zhenhai':zhenhai_modifier,'daxiekaifaqu':daxiekaifaqu_modifier,
            'guojiagaoxinqu':guojiagaoxinqu_modifier,'hangzhouwanxinqu':hangzhouwanxinqu_modifier,
            'ninghai_ajax':ninghai_ajax_modifier,'yuyao_ajax':yuyao_ajax_modifier,'ningboshi':ningboshi_modifier,
            ###zhoushan
            'putuo':putuo_modifier,'daishan':daishan_modifier,'dinghaiqu':dinghaiqu_modifier,
            'shengsi':shengsi_modifier,
            'zhoushan':zhoushan_modifier,
            ##shaoxing
            'zhuji':zhuji_modifier,'xinchang':xinchang_modifier,'shangyu':shangyu_modifier,
            'shengzhou':shengzhou_modifier,'yuecheng':yuecheng_modifier,'shaoxing':shaoxing_modifier,
            ##taizhou
            'xianju':xianju_modifier,'luqiao':luqiao_modifier,
            'wenling':wenling_modifier,#'linhai':CRAWL_LINHAI_TASKS,'yuhuan_ajax':CRAWL_YUHUAN_AJAX_TASKS,
            'huangyan':huangyan_modifier,
            'yuhuan':yuhuan_modifier,'tiantai':tiantai_modifier,
            'taizhou':taizhou_modifier,
            ##wenzhou
            'cangnan':cangnan_modifier,'leqing':leqing_modifier,'yongjia':yongjia_modifier,
            'dongtou':dongtou_modifier,'longwan':longwan_modifier,'lucheng':lucheng_modifier,'wencheng':wencheng_modifier,
            'ouhai':ouhai_modifier,'pingyang':pingyang_modifier,'ruian':ruian_modifier,'taishun':taishun_modifier,
            'wenzhou':wenzhou_modifier,
            #hangzhou
            'jiande':jiande_modifier,'tonglu':tonglu_modifier,'dajiangdong':dajiangdong_modifier,
            'chunan':chunan_modifier,'jianggan':jianggan_modifier,'gongshu':gongshu_modifier,
            'fuyang':fuyang_modifier,
            'xihuqu':xihuqu_modifier,'xiaoshan':xiaoshan_modifier,
            'yuhang':yuhang_modifier,'linan':linan_modifier,#'fuyang':CRAWL_FUYANG_TASKS,
            }