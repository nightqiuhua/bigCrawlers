from pyhanlp import *
import os
#训练模型
#保存模型
#加载模型
#预测
#
#
# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-29 23:24
# 《自然语言处理入门》8.6 自定义领域命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
# 
from pyhanlp import *
import os
from pyhanlp.static import download, remove_file, HANLP_DATA_PATH
import zipfile


Sentence = JClass('com.hankcs.hanlp.corpus.document.sentence.Sentence')
NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
CWSTrainer = JClass('com.hankcs.hanlp.model.perceptron.CWSTrainer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')

PLANE_ROOT = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\html_ex'
PLANE_CORPUS = os.path.join(PLANE_ROOT, 'NLP_sample.txt')
PLANE_MODEL = os.path.join(PLANE_ROOT, 'model.bin')

if __name__ == '__main__':
    import re
    #money = re.findall(r',(\d+.*?元)',"Y3300000007000248002001,第JDSG-04标段,浙江交工集团股份有限公司,陈真伟,71168963.00元,105;")
    #print(money)
    #训练模型并保存模型
    #trainer = NERTrainer()#命令实体分词器
    #trainer.tagSet.nerLabels.clear()  # 不识别nr、ns、nt
    #trainer.tagSet.nerLabels.add("nw")  # 目标是识别np
    ##trainer.tagSet.nerLabels.add("nm")  # 目标是识别nm
    #trainer.train(PLANE_CORPUS, PLANE_MODEL).getModel() #生成命令实体分词模型，并保存
    ##
    ##加载模型
    recognizer = PerceptronNERecognizer(os.path.join(PLANE_ROOT, 'model.bin')) #加载命令实体分词模型
    ## 在NER预测前，需要一个分词器，最好训练自同源语料库
    #CWS_MODEL = CWSTrainer().train(PLANE_CORPUS, PLANE_MODEL.replace('model.bin', 'cws.bin')).getModel() #普通分词器训练后得到的分词模型并保存模型
    CWS_MODEL = os.path.join(PLANE_ROOT, 'cws.bin')
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(CWS_MODEL), PerceptronPOSTagger(), recognizer)
    
    #sentence = Sentence.create(",/w 招标人/n ：/w ,/w [中铁一局集团有限公司/ntc]/nw")
    #while not analyzer.analyze(sentence.text()).equals(sentence):
    #    analyzer.learn(sentence)
    print(analyzer.analyze(",招标人：,中铁一局集团有限公司;"))
