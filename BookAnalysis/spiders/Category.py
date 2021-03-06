import csv
import os.path
import re

import requests
from lxml import etree


class Category:
    def __init__(self, outfile=None):
        self._url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }
        if outfile is None:
            outfile = 'categories.csv'
        self._outfile = outfile

    def crawl(self):
        resp = requests.get(self._url, headers=self._headers)
        content = resp.content.decode(resp.encoding)
        return content

    def parse(self, html):
        _ans = [['parentTag', 'tag', 'num', 'url']]
        root = etree.HTML(html)
        categories = root.xpath('//*[@id="content"]/div/div[1]/div[2]/div')
        for category in categories:
            parentTag = category.xpath('./a/h2//text()')[0].strip().replace(' · · · · · ·', '')
            tags = category.xpath('.//table[@class="tagCol"]')[0].xpath('.//td')

            for _tag in tags:
                tag = _tag.xpath('./a//text()')[0].strip()
                num = _tag.xpath('./b//text()')[0].strip()
                url = 'https://book.douban.com' + _tag.xpath('./a//@href')[0].strip()
                num = re.findall(r'\d+', num)[0]
                _ans.append([parentTag, tag, num, url])
                # print(tag, num, url)
            # print(parentTag, etree.tostring(table))
            # print(parentTag, tags)
        return _ans

    def save(self, data):
        with open(self._outfile, mode='w', encoding='utf-8', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def run(self):
        html = self.crawl()
        data = self.parse(html)
        print(data)
        self.save(data)


if __name__ == '__main__':
    dir_ = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    data_file = os.path.join(dir_, 'data', 'categories.csv')
    category = Category(data_file)
    category.run()
    # data = [['parentTag', 'tag', 'num', 'url'], ['文学', '小说', '7341079', 'https://book.douban.com/tag/小说'], ['文学', '文学', '2934623', 'https://book.douban.com/tag/文学'], ['文学', '外国文学', '2910982', 'https://book.douban.com/tag/外国文学'], ['文学', '经典', '1825626', 'https://book.douban.com/tag/经典'], ['文学', '中国文学', '1723771', 'https://book.douban.com/tag/中国文学'], ['文学', '随笔', '1559280', 'https://book.douban.com/tag/随笔'], ['文学', '日本文学', '1302509', 'https://book.douban.com/tag/日本文学'], ['文学', '散文', '928964', 'https://book.douban.com/tag/散文'], ['文学', '村上春树', '533583', 'https://book.douban.com/tag/村上春树'], ['文学', '诗歌', '491446', 'https://book.douban.com/tag/诗歌'], ['文学', '童话', '412650', 'https://book.douban.com/tag/童话'], ['文学', '名著', '408998', 'https://book.douban.com/tag/名著'], ['文学', '儿童文学', '396328', 'https://book.douban.com/tag/儿童文学'], ['文学', '古典文学', '363033', 'https://book.douban.com/tag/古典文学'], ['文学', '余华', '341064', 'https://book.douban.com/tag/余华'], ['文学', '王小波', '301847', 'https://book.douban.com/tag/王小波'], ['文学', '当代文学', '281553', 'https://book.douban.com/tag/当代文学'], ['文学', '杂文', '277724', 'https://book.douban.com/tag/杂文'], ['文学', '张爱玲', '235624', 'https://book.douban.com/tag/张爱玲'], ['文学', '外国名著', '171174', 'https://book.douban.com/tag/外国名著'], ['文学', '鲁迅', '161414', 'https://book.douban.com/tag/鲁迅'], ['文学', '钱钟书', '151263', 'https://book.douban.com/tag/钱钟书'], ['文学', '诗词', '116833', 'https://book.douban.com/tag/诗词'], ['文学', '茨威格', '87071', 'https://book.douban.com/tag/茨威格'], ['文学', '米兰·昆德拉', '67678', 'https://book.douban.com/tag/米兰·昆德拉'], ['文学', '杜拉斯', '48707', 'https://book.douban.com/tag/杜拉斯'], ['文学', '港台', '10718', 'https://book.douban.com/tag/港台'], ['流行', '漫画', '1658087', 'https://book.douban.com/tag/漫画'], ['流行', '推理', '1413132', 'https://book.douban.com/tag/推理'], ['流行', '绘本', '1191784', 'https://book.douban.com/tag/绘本'], ['流行', '悬疑', '877064', 'https://book.douban.com/tag/悬疑'], ['流行', '东野圭吾', '867745', 'https://book.douban.com/tag/东野圭吾'], ['流行', '青春', '832155', 'https://book.douban.com/tag/青春'], ['流行', '科幻', '824536', 'https://book.douban.com/tag/科幻'], ['流行', '言情', '632565', 'https://book.douban.com/tag/言情'], ['流行', '推理小说', '531696', 'https://book.douban.com/tag/推理小说'], ['流行', '奇幻', '457280', 'https://book.douban.com/tag/奇幻'], ['流行', '武侠', '398964', 'https://book.douban.com/tag/武侠'], ['流行', '日本漫画', '392965', 'https://book.douban.com/tag/日本漫画'], ['流行', '耽美', '385082', 'https://book.douban.com/tag/耽美'], ['流行', '科幻小说', '324521', 'https://book.douban.com/tag/科幻小说'], ['流行', '网络小说', '292935', 'https://book.douban.com/tag/网络小说'], ['流行', '三毛', '276147', 'https://book.douban.com/tag/三毛'], ['流行', '韩寒', '271679', 'https://book.douban.com/tag/韩寒'], ['流行', '亦舒', '248401', 'https://book.douban.com/tag/亦舒'], ['流行', '阿加莎·克里斯蒂', '242060', 'https://book.douban.com/tag/阿加莎·克里斯蒂'], ['流行', '金庸', '204039', 'https://book.douban.com/tag/金庸'], ['流行', '穿越', '178704', 'https://book.douban.com/tag/穿越'], ['流行', '安妮宝贝', '178229', 'https://book.douban.com/tag/安妮宝贝'], ['流行', '魔幻', '166311', 'https://book.douban.com/tag/魔幻'], ['流行', '轻小说', '165950', 'https://book.douban.com/tag/轻小说'], ['流行', '郭敬明', '160171', 'https://book.douban.com/tag/郭敬明'], ['流行', '青春文学', '155071', 'https://book.douban.com/tag/青春文学'], ['流行', '几米', '122383', 'https://book.douban.com/tag/几米'], ['流行', 'J.K.罗琳', '120962', 'https://book.douban.com/tag/J.K.罗琳'], ['流行', '幾米', '106292', 'https://book.douban.com/tag/幾米'], ['流行', '张小娴', '98953', 'https://book.douban.com/tag/张小娴'], ['流行', '校园', '98057', 'https://book.douban.com/tag/校园'], ['流行', '古龙', '88906', 'https://book.douban.com/tag/古龙'], ['流行', '高木直子', '80277', 'https://book.douban.com/tag/高木直子'], ['流行', '沧月', '69391', 'https://book.douban.com/tag/沧月'], ['流行', '余秋雨', '65455', 'https://book.douban.com/tag/余秋雨'], ['流行', '张悦然', '58595', 'https://book.douban.com/tag/张悦然'], ['文化', '历史', '3239425', 'https://book.douban.com/tag/历史'], ['文化', '心理学', '2149144', 'https://book.douban.com/tag/心理学'], ['文化', '哲学', '1895579', 'https://book.douban.com/tag/哲学'], ['文化', '社会学', '1380631', 'https://book.douban.com/tag/社会学'], ['文化', '传记', '1132387', 'https://book.douban.com/tag/传记'], ['文化', '文化', '1082811', 'https://book.douban.com/tag/文化'], ['文化', '艺术', '835610', 'https://book.douban.com/tag/艺术'], ['文化', '社会', '799024', 'https://book.douban.com/tag/社会'], ['文化', '政治', '617467', 'https://book.douban.com/tag/政治'], ['文化', '设计', '522475', 'https://book.douban.com/tag/设计'], ['文化', '政治学', '403155', 'https://book.douban.com/tag/政治学'], ['文化', '宗教', '364101', 'https://book.douban.com/tag/宗教'], ['文化', '建筑', '347368', 'https://book.douban.com/tag/建筑'], ['文化', '电影', '347094', 'https://book.douban.com/tag/电影'], ['文化', '中国历史', '338698', 'https://book.douban.com/tag/中国历史'], ['文化', '数学', '326941', 'https://book.douban.com/tag/数学'], ['文化', '回忆录', '288812', 'https://book.douban.com/tag/回忆录'], ['文化', '思想', '246709', 'https://book.douban.com/tag/思想'], ['文化', '人物传记', '231211', 'https://book.douban.com/tag/人物传记'], ['文化', '艺术史', '213290', 'https://book.douban.com/tag/艺术史'], ['文化', '国学', '210144', 'https://book.douban.com/tag/国学'], ['文化', '人文', '187817', 'https://book.douban.com/tag/人文'], ['文化', '音乐', '168886', 'https://book.douban.com/tag/音乐'], ['文化', '绘画', '166376', 'https://book.douban.com/tag/绘画'], ['文化', '西方哲学', '165604', 'https://book.douban.com/tag/西方哲学'], ['文化', '戏剧', '163463', 'https://book.douban.com/tag/戏剧'], ['文化', '近代史', '138001', 'https://book.douban.com/tag/近代史'], ['文化', '二战', '132326', 'https://book.douban.com/tag/二战'], ['文化', '军事', '114345', 'https://book.douban.com/tag/军事'], ['文化', '佛教', '109661', 'https://book.douban.com/tag/佛教'], ['文化', '考古', '80409', 'https://book.douban.com/tag/考古'], ['文化', '自由主义', '65404', 'https://book.douban.com/tag/自由主义'], ['文化', '美术', '61183', 'https://book.douban.com/tag/美术'], ['生活', '爱情', '1388807', 'https://book.douban.com/tag/爱情'], ['生活', '成长', '1077090', 'https://book.douban.com/tag/成长'], ['生活', '生活', '836063', 'https://book.douban.com/tag/生活'], ['生活', '心理', '754438', 'https://book.douban.com/tag/心理'], ['生活', '女性', '732284', 'https://book.douban.com/tag/女性'], ['生活', '旅行', '673982', 'https://book.douban.com/tag/旅行'], ['生活', '励志', '554217', 'https://book.douban.com/tag/励志'], ['生活', '教育', '415858', 'https://book.douban.com/tag/教育'], ['生活', '摄影', '387890', 'https://book.douban.com/tag/摄影'], ['生活', '职场', '287557', 'https://book.douban.com/tag/职场'], ['生活', '美食', '250374', 'https://book.douban.com/tag/美食'], ['生活', '游记', '209117', 'https://book.douban.com/tag/游记'], ['生活', '灵修', '156347', 'https://book.douban.com/tag/灵修'], ['生活', '健康', '143705', 'https://book.douban.com/tag/健康'], ['生活', '情感', '134012', 'https://book.douban.com/tag/情感'], ['生活', '人际关系', '83737', 'https://book.douban.com/tag/人际关系'], ['生活', '两性', '80959', 'https://book.douban.com/tag/两性'], ['生活', '养生', '49818', 'https://book.douban.com/tag/养生'], ['生活', '手工', '45516', 'https://book.douban.com/tag/手工'], ['生活', '家居', '35652', 'https://book.douban.com/tag/家居'], ['生活', '自助游', '2781', 'https://book.douban.com/tag/自助游'], ['经管', '经济学', '654941', 'https://book.douban.com/tag/经济学'], ['经管', '管理', '601593', 'https://book.douban.com/tag/管理'], ['经管', '经济', '546642', 'https://book.douban.com/tag/经济'], ['经管', '商业', '503263', 'https://book.douban.com/tag/商业'], ['经管', '金融', '418860', 'https://book.douban.com/tag/金融'], ['经管', '投资', '382584', 'https://book.douban.com/tag/投资'], ['经管', '营销', '218686', 'https://book.douban.com/tag/营销'], ['经管', '理财', '198912', 'https://book.douban.com/tag/理财'], ['经管', '创业', '161951', 'https://book.douban.com/tag/创业'], ['经管', '股票', '105743', 'https://book.douban.com/tag/股票'], ['经管', '广告', '86303', 'https://book.douban.com/tag/广告'], ['经管', '企业史', '30721', 'https://book.douban.com/tag/企业史'], ['经管', '策划', '10947', 'https://book.douban.com/tag/策划'], ['科技', '科普', '1004331', 'https://book.douban.com/tag/科普'], ['科技', '互联网', '317872', 'https://book.douban.com/tag/互联网'], ['科技', '科学', '231632', 'https://book.douban.com/tag/科学'], ['科技', '编程', '208974', 'https://book.douban.com/tag/编程'], ['科技', '交互设计', '81600', 'https://book.douban.com/tag/交互设计'], ['科技', '算法', '69750', 'https://book.douban.com/tag/算法'], ['科技', '用户体验', '68224', 'https://book.douban.com/tag/用户体验'], ['科技', '科技', '47831', 'https://book.douban.com/tag/科技'], ['科技', 'web', '23397', 'https://book.douban.com/tag/web'], ['科技', '交互', '6812', 'https://book.douban.com/tag/交互'], ['科技', '通信', '6659', 'https://book.douban.com/tag/通信'], ['科技', 'UE', '5765', 'https://book.douban.com/tag/UE'], ['科技', '神经网络', '4936', 'https://book.douban.com/tag/神经网络'], ['科技', 'UCD', '3611', 'https://book.douban.com/tag/UCD'], ['科技', '程序', '1455', 'https://book.douban.com/tag/程序']]
