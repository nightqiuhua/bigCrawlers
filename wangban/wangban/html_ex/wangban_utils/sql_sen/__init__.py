# -*- coding: utf-8 -*-
import sys 
import os
#BASH_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(BASH_DIR)
#sys.path.append('..')
#
from .t_zhaobiao import sql_t_zhaobiao_create_table,sql_t_zhaobiao_insert
from .xunjia import sql_xunjia_create_table,sql_xunjia_insert
from .t_zhaobiao_2 import sql_t_zhaobiao_2_create_table,sql_t_zhaobiao_2_insert
from .t_zhaobiao_2_1 import sql_t_zhaobiao_2_1_create_table,sql_t_zhaobiao_2_1_insert
from .xinxijia import sql_xinxijia_create_table,sql_xinxijia_insert
#zhejiang
from .zhejiang import sql_zhejiang_create_table,sql_zhejiang_insert
#jinhua
from .jinhua import sql_jinhua_create_table,sql_jinhua_insert
#lishui
from .lishui import sql_lishui_create_table,sql_lishui_insert
#jiaxing
from .jiaxing import sql_jiaxing_create_table,sql_jiaxing_insert
#hangzhou
from .jiande import sql_jiande_create_table,sql_jiande_insert
from .tonglu import sql_tonglu_create_table,sql_tonglu_insert
from .yuhang import sql_yuhang_create_table,sql_yuhang_insert
from .xiaoshan import sql_xiaoshan_create_table,sql_xiaoshan_insert
from .xihuqu import sql_xihuqu_create_table,sql_xihuqu_insert
from .linan import sql_linan_create_table,sql_linan_insert
from .fuyang import sql_fuyang_create_table,sql_fuyang_insert
from .gongshu import sql_gongshu_create_table,sql_gongshu_insert
from .jianggan import sql_jianggan_create_table,sql_jianggan_insert
from .chunan import sql_chunan_create_table,sql_chunan_insert
from .dajiangdong import sql_dajiangdong_create_table,sql_dajiangdong_insert
from .hangzhou import sql_hangzhou_create_table,sql_hangzhou_insert
#ningbo
from .cixi import sql_cixi_create_table,sql_cixi_insert
from .fenghua import sql_fenghua_create_table,sql_fenghua_insert
from .haishu import sql_haishu_create_table,sql_haishu_insert
from .xiangshan import sql_xiangshan_create_table,sql_xiangshan_insert
from .ningbobaoshuiqu import sql_ningbobaoshuiqu_create_table,sql_ningbobaoshuiqu_insert
from .hangzhouwanxinqu import sql_hangzhouwanxinqu_create_table,sql_hangzhouwanxinqu_insert
from .guojiagaoxinqu import sql_guojiagaoxinqu_create_table,sql_guojiagaoxinqu_insert
from .daxiekaifaqu import sql_daxiekaifaqu_create_table,sql_daxiekaifaqu_insert
from .zhenhai import sql_zhenhai_create_table,sql_zhenhai_insert
from .yuyao import sql_yuyao_create_table,sql_yuyao_insert
from .yinzhou import sql_yinzhou_create_table,sql_yinzhou_insert
from .jiangbei import sql_jiangbei_create_table,sql_jiangbei_insert
from .beilun import sql_beilun_create_table,sql_beilun_insert
from .ninghai import sql_ninghai_create_table,sql_ninghai_insert
from .ninghai_ajax import sql_ninghai_ajax_create_table,sql_ninghai_ajax_insert
from .yuyao_ajax import sql_yuyao_ajax_create_table,sql_yuyao_ajax_insert
from .ningboshi import sql_ningboshi_create_table,sql_ningboshi_insert

#shaoxing
from .shengzhou import sql_shengzhou_create_table,sql_shengzhou_insert
from .xinchang import sql_xinchang_create_table,sql_xinchang_insert
from .zhuji import sql_zhuji_create_table,sql_zhuji_insert
from .shangyu import sql_shangyu_create_table,sql_shangyu_insert
from .yuecheng import sql_yuecheng_create_table,sql_yuecheng_insert
from .shaoxing import sql_shaoxing_create_table,sql_shaoxing_insert

#huzhou
from .changxing import sql_changxing_create_table,sql_changxing_insert
from .anji import sql_anji_create_table,sql_anji_insert
from .nanxun import sql_nanxun_create_table,sql_nanxun_insert
from .wuxing import sql_wuxing_create_table,sql_wuxing_insert
from .deqing import sql_deqing_create_table,sql_deqing_insert
from .huzhou import sql_huzhou_create_table,sql_huzhou_insert
#taizhou
from .huangyan import sql_huangyan_create_table,sql_huangyan_insert
from .linhai import sql_linhai_create_table,sql_linhai_insert
from .luqiao import sql_luqiao_create_table,sql_luqiao_insert
from .tiantai import sql_tiantai_create_table,sql_tiantai_insert
from .xianju import sql_xianju_create_table,sql_xianju_insert
from .wenling import sql_wenling_create_table,sql_wenling_insert
from .yuhuan import sql_yuhuan_create_table,sql_yuhuan_insert
from .yuhuan_ajax import sql_yuhuan_ajax_create_table,sql_yuhuan_ajax_insert
from .taizhou import sql_taizhou_create_table,sql_taizhou_insert
#from .jiaojiang import sql_ruian_create_table,sql_ruian_insert

#wenzhou
from .ruian import sql_ruian_create_table,sql_ruian_insert
from .cangnan import sql_cangnan_create_table,sql_cangnan_insert
from .dongtou import sql_dongtou_create_table,sql_dongtou_insert
from .longwan import sql_longwan_create_table,sql_longwan_insert
from .lucheng import sql_lucheng_create_table,sql_lucheng_insert
from .ouhai import sql_ouhai_create_table,sql_ouhai_insert
from .leqing import sql_leqing_create_table,sql_leqing_insert
from .pingyang import sql_pingyang_create_table,sql_pingyang_insert
from .taishun import sql_taishun_create_table,sql_taishun_insert
from .wencheng import sql_wencheng_create_table,sql_wencheng_insert
from .yongjia import sql_yongjia_create_table,sql_yongjia_insert
from .wenzhou import sql_wenzhou_create_table,sql_wenzhou_insert
#zhoushan
from .putuo import sql_putuo_create_table,sql_putuo_insert
from .daishan import sql_daishan_create_table,sql_daishan_insert
from .dinghaiqu import sql_dinghaiqu_create_table,sql_dinghaiqu_insert
from .shengsi import sql_shengsi_create_table,sql_shengsi_insert
from .zhoushan import sql_zhoushan_create_table,sql_zhoushan_insert
#qú zhōu
from .qujiang import sql_qujiang_create_table,sql_qujiang_insert
from .longyou import sql_longyou_create_table,sql_longyou_insert
from .jiangshan import sql_jiangshan_create_table,sql_jiangshan_insert
from .haining import sql_haining_create_table,sql_haining_insert
from .kaihua import sql_kaihua_create_table,sql_kaihua_insert
from .changshan import sql_changshan_create_table,sql_changshan_insert
from .kecheng import sql_kecheng_create_table,sql_kecheng_insert
from .longyou_ajax import sql_longyou_ajax_create_table,sql_longyou_ajax_insert
from .quzhou import sql_quzhou_create_table,sql_quzhou_insert


all_sql_sentence = {
        'xinxijia':{'create_table':sql_xinxijia_create_table,'sql_insert':sql_xinxijia_insert},
        'xunjia':{'create_table':sql_xunjia_create_table,'sql_insert':sql_xunjia_insert},
        'zhejiang':{'create_table':sql_zhejiang_create_table,'sql_insert':sql_zhejiang_insert},
        'hangzhou':{'create_table':sql_hangzhou_create_table,'sql_insert':sql_hangzhou_insert},
        'ningboshi':{'create_table':sql_ningboshi_create_table,'sql_insert':sql_ningboshi_insert},
        'jiaxing':{'create_table':sql_jiaxing_create_table,'sql_insert':sql_jiaxing_insert},
        'jinhua':{'create_table':sql_jinhua_create_table,'sql_insert':sql_jinhua_insert},
        'lishui':{'create_table':sql_lishui_create_table,'sql_insert':sql_lishui_insert},
        'quzhou':{'create_table':sql_quzhou_create_table,'sql_insert':sql_quzhou_insert},
        'shaoxing':{'create_table':sql_shaoxing_create_table,'sql_insert':sql_shaoxing_insert},
        'taizhou':{'create_table':sql_taizhou_create_table,'sql_insert':sql_taizhou_insert},
        'wenzhou':{'create_table':sql_wenzhou_create_table,'sql_insert':sql_wenzhou_insert},
        'zhoushan':{'create_table':sql_zhoushan_create_table,'sql_insert':sql_zhoushan_insert},
        'huzhou':{'create_table':sql_huzhou_create_table,'sql_insert':sql_huzhou_insert},
        #zhoushan
        'putuo':{'create_table':sql_putuo_create_table,'sql_insert':sql_putuo_insert},
        'daishan':{'create_table':sql_daishan_create_table,'sql_insert':sql_daishan_insert},
        'dinghaiqu':{'create_table':sql_dinghaiqu_create_table,'sql_insert':sql_dinghaiqu_insert},
        'shengsi':{'create_table':sql_shengsi_create_table,'sql_insert':sql_shengsi_insert},
        #huzhou
        'changxing':{'create_table':sql_changxing_create_table,'sql_insert':sql_changxing_insert},
        'anji':{'create_table':sql_anji_create_table,'sql_insert':sql_anji_insert},
        'nanxun':{'create_table':sql_nanxun_create_table,'sql_insert':sql_nanxun_insert},
        'wuxing':{'create_table':sql_wuxing_create_table,'sql_insert':sql_wuxing_insert},
        'deqing':{'create_table':sql_deqing_create_table,'sql_insert':sql_deqing_insert},
        #taizhou
        'huangyan':{'create_table':sql_huangyan_create_table,'sql_insert':sql_huangyan_insert},
        'linhai':{'create_table':sql_linhai_create_table,'sql_insert':sql_linhai_insert},
        'luqiao':{'create_table':sql_luqiao_create_table,'sql_insert':sql_luqiao_insert},
        'tiantai':{'create_table':sql_tiantai_create_table,'sql_insert':sql_tiantai_insert},
        'xianju':{'create_table':sql_xianju_create_table,'sql_insert':sql_xianju_insert},
        'wenling':{'create_table':sql_wenling_create_table,'sql_insert':sql_wenling_insert},
        'yuhuan':{'create_table':sql_yuhuan_create_table,'sql_insert':sql_yuhuan_insert},
        'yuhuan_ajax':{'create_table':sql_yuhuan_ajax_create_table,'sql_insert':sql_yuhuan_ajax_insert},
        'yongjia':{'create_table':sql_yongjia_create_table,'sql_insert':sql_yongjia_insert},
        #shaoxing
        'shengzhou':{'create_table':sql_shengzhou_create_table,'sql_insert':sql_shengzhou_insert},
        'xinchang':{'create_table':sql_xinchang_create_table,'sql_insert':sql_xinchang_insert},
        'zhuji':{'create_table':sql_zhuji_create_table,'sql_insert':sql_zhuji_insert},
        'shangyu':{'create_table':sql_shangyu_create_table,'sql_insert':sql_shangyu_insert},
        'yuecheng':{'create_table':sql_yuecheng_create_table,'sql_insert':sql_yuecheng_insert},
        #wenzhou
        'ruian':{'create_table':sql_ruian_create_table,'sql_insert':sql_ruian_insert},
        'cangnan':{'create_table':sql_cangnan_create_table,'sql_insert':sql_cangnan_insert},
        'dongtou':{'create_table':sql_dongtou_create_table,'sql_insert':sql_dongtou_insert},
        'longwan':{'create_table':sql_longwan_create_table,'sql_insert':sql_longwan_insert},
        'lucheng':{'create_table':sql_lucheng_create_table,'sql_insert':sql_lucheng_insert},
        'ouhai':{'create_table':sql_ouhai_create_table,'sql_insert':sql_ouhai_insert},
        'leqing':{'create_table':sql_leqing_create_table,'sql_insert':sql_leqing_insert},
        'pingyang':{'create_table':sql_pingyang_create_table,'sql_insert':sql_pingyang_insert},
        'taishun':{'create_table':sql_taishun_create_table,'sql_insert':sql_taishun_insert},
        'wencheng':{'create_table':sql_wencheng_create_table,'sql_insert':sql_wencheng_insert},
        'yongjia':{'create_table':sql_yongjia_create_table,'sql_insert':sql_yongjia_insert},
        #qú zhōu
        'qujiang':{'create_table':sql_qujiang_create_table,'sql_insert':sql_qujiang_insert},
        'longyou':{'create_table':sql_longyou_create_table,'sql_insert':sql_longyou_insert},
        'jiangshan':{'create_table':sql_jiangshan_create_table,'sql_insert':sql_jiangshan_insert},
        'haining':{'create_table':sql_haining_create_table,'sql_insert':sql_haining_insert},
        'kaihua':{'create_table':sql_kaihua_create_table,'sql_insert':sql_kaihua_insert},
        'changshan':{'create_table':sql_changshan_create_table,'sql_insert':sql_changshan_insert},
        'kecheng':{'create_table':sql_kecheng_create_table,'sql_insert':sql_kecheng_insert},
        'longyou_ajax':{'create_table':sql_longyou_ajax_create_table,'sql_insert':sql_longyou_ajax_insert},
        ##hangzhou
        'yuhang':{'create_table':sql_yuhang_create_table,'sql_insert':sql_yuhang_insert},
        'xiaoshan':{'create_table':sql_xiaoshan_create_table,'sql_insert':sql_xiaoshan_insert},
        'xihuqu':{'create_table':sql_xihuqu_create_table,'sql_insert':sql_xihuqu_insert},
        'linan':{'create_table':sql_linan_create_table,'sql_insert':sql_linan_insert},
        'fuyang':{'create_table':sql_fuyang_create_table,'sql_insert':sql_fuyang_insert},
        'gongshu':{'create_table':sql_gongshu_create_table,'sql_insert':sql_gongshu_insert},
        'jianggan':{'create_table':sql_jianggan_create_table,'sql_insert':sql_jianggan_insert},
        'chunan':{'create_table':sql_chunan_create_table,'sql_insert':sql_chunan_insert},
        'jiande':{'create_table':sql_jiande_create_table,'sql_insert':sql_jiande_insert},
        'tonglu':{'create_table':sql_tonglu_create_table,'sql_insert':sql_tonglu_insert},
        'dajiangdong':{'create_table':sql_dajiangdong_create_table,'sql_insert':sql_dajiangdong_insert},
        #ningbo
        'cixi':{'create_table':sql_cixi_create_table,'sql_insert':sql_cixi_insert},
        'haishu':{'create_table':sql_haishu_create_table,'sql_insert':sql_haishu_insert},
        'ningbobaoshuiqu':{'create_table':sql_ningbobaoshuiqu_create_table,'sql_insert':sql_ningbobaoshuiqu_insert},
        'fenghua':{'create_table':sql_fenghua_create_table,'sql_insert':sql_fenghua_insert},
        'xiangshan':{'create_table':sql_xiangshan_create_table,'sql_insert':sql_xiangshan_insert},
        'hangzhouwanxinqu':{'create_table':sql_hangzhouwanxinqu_create_table,'sql_insert':sql_hangzhouwanxinqu_insert},
        'guojiagaoxinqu':{'create_table':sql_guojiagaoxinqu_create_table,'sql_insert':sql_guojiagaoxinqu_insert},
        'daxiekaifaqu':{'create_table':sql_daxiekaifaqu_create_table,'sql_insert':sql_daxiekaifaqu_insert},
        'zhenhai':{'create_table':sql_zhenhai_create_table,'sql_insert':sql_zhenhai_insert},
        'yuyao':{'create_table':sql_yuyao_create_table,'sql_insert':sql_yuyao_insert},
        'yinzhou':{'create_table':sql_yinzhou_create_table,'sql_insert':sql_yinzhou_insert},
        'jiangbei':{'create_table':sql_jiangbei_create_table,'sql_insert':sql_jiangbei_insert},
        'beilun':{'create_table':sql_beilun_create_table,'sql_insert':sql_beilun_insert},
        'ninghai':{'create_table':sql_ninghai_create_table,'sql_insert':sql_ninghai_insert},
        'ninghai_ajax':{'create_table':sql_ninghai_ajax_create_table,'sql_insert':sql_ninghai_ajax_insert},
        'yuyao_ajax':{'create_table':sql_yuyao_ajax_create_table,'sql_insert':sql_yuyao_ajax_insert},
        #
        't_zhaobiao_2':{'create_table':sql_t_zhaobiao_2_create_table,'sql_insert':sql_t_zhaobiao_2_insert},
        't_zhaobiao_2_1':{'create_table':sql_t_zhaobiao_2_1_create_table,'sql_insert':sql_t_zhaobiao_2_1_insert},
        't_zhaobiao':{'create_table':sql_t_zhaobiao_create_table,'sql_insert':sql_t_zhaobiao_insert},
}