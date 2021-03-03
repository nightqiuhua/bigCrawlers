# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-29 15:06
# 《自然语言处理入门》8.5.3 基于感知机序列标注的命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *
from pyhanlp.static import download, remove_file, HANLP_DATA_PATH
import os
import re


def test_data_path():
    """
    获取测试数据路径，位于$root/data/test，根目录由配置文件指定。
    :return:
    """
    data_path = os.path.join(HANLP_DATA_PATH, 'test')
    if not os.path.isdir(data_path):
        os.mkdir(data_path)
    return data_path


def ensure_data(data_name, data_url):
    root_path = test_data_path()
    dest_path = os.path.join(root_path, data_name)
    if os.path.exists(dest_path):
        return dest_path
    if data_url.endswith('.zip'):
        dest_path += '.zip'
    download(data_url, dest_path)
    if data_url.endswith('.zip'):
        with zipfile.ZipFile(dest_path, "r") as archive:
            archive.extractall(root_path)
        remove_file(dest_path)
        dest_path = dest_path[:-len('.zip')]
    return dest_path


PKU98 = ensure_data("pku98", "http://file.hankcs.com/corpus/pku98.zip")
PKU199801 = os.path.join(PKU98, '199801.txt')
PKU199801_TRAIN = os.path.join(PKU98, '199801-train.txt')
PKU199801_TEST = os.path.join(PKU98, '199801-test.txt')
POS_MODEL = os.path.join('E:\\工作\\万邦\\工作成果\\crawler_project\\NLP\\wangban-is', 'pos.bin')
NER_MODEL = os.path.join('E:\\工作\\万邦\\工作成果\\crawler_project\\NLP\\wangban-is', 'ner.bin')

NERTrainer = JClass('com.hankcs.hanlp.model.perceptron.NERTrainer')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')


def train(corpus, model):
    trainer = NERTrainer()
    real_model = trainer.train(PKU199801_TRAIN, NER_MODEL).getModel()
    return PerceptronNERecognizer(real_model)


if __name__ == '__main__':
    #trainer = NERTrainer()
    #real_model = trainer.train(PKU199801_TRAIN, NER_MODEL).getModel()
    real_model = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\html_ex\\ner.bin'
    recognizer = PerceptronNERecognizer(real_model)
    analyzer = PerceptronLexicalAnalyzer(PerceptronSegmenter(), PerceptronPOSTagger(), recognizer)
    import re
    with open('new_NLP.txt','r',encoding='utf-8') as fp:
        content = fp.read()
        for i,line in enumerate(content.split(';')):
            line = re.sub(r'\s+','',line)
            try:
                if '元' in line:
                    result = analyzer.analyze(line)
                    with open('NLPYL_sample_nm.txt','a') as fp2:
                        fp2.write(str(result)+';'+'\r\n')
            except Exception as e:
                print('error',e)