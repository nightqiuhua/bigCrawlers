from  pyhanlp import *
import zipfile
import os

from pyhanlp.static import download, remove_file, HANLP_DATA_PATH


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
POS_MODEL = os.path.join('E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\html_ex', 'pos.bin') # 获取空模型
POSTrainer = JClass('com.hankcs.hanlp.model.perceptron.POSTrainer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')

def train_perceptron_pos(corpus):
    trainer = POSTrainer()
    #model = trainer.train(corpus, POS_MODEL).getModel()  # 标注训练并保存文件
    model = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\html_ex\\pos.bin' # 指定模型文件路径
    
    tagger = PerceptronPOSTagger(model)  # 加载模型文件
    #print(', '.join(tagger.tag("他", "的", "希望", "是", "希望", "上学")))  # 预测
    analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), tagger)  # 构造词法分析器
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
    #print(analyzer.analyze("项目名称：,杭州至临安城际铁路工程;"))  # 分词+词性标注
    return tagger

train_perceptron_pos(PKU199801_TRAIN)