# -*- coding:utf-8 -*-
"""
@Time : 2022/6/30
@Author : skyoceanchen

@TEL: 18916403796
@File : re_operations.py 
@PRODUCT_NAME : PyCharm
https://mp.weixin.qq.com/s/zp5hbawVuKlZp58KxV1ePw
"""
import re


class ReOperation(object):

    def num_rule(self, re_type, m='', n='', ):
        re_gu = {
            1: '(-?\d*)(\.\d+)?',  # 提取信息中的任何数字
            2: "^[0-9]*$",  # 数字
            3: "^\d{%s}$" % (n),  # n位的数字
            4: "^\d{%s,}$" % (n),  # 至少n位的数字
            5: "^\d{%s,%s}$" % (m, n),  # m-n位的数字
            6: "^(0|[1-9][0-9]*)$",  # 零和非零开头的数字
            7: "^([1-9][0-9]*)+(.[0-9]{1,2})?$",  # 非零开头的最多带两位小数的数字
            8: "^(\-)?\d+(\.\d{1,2})?$",  # 带1-2位小数的正数或负数
            9: "^(\-|\+)?\d+(\.\d+)?$",  # 正数、负数、和小数
            10: "^[0-9]+(.[0-9]{2})?$",  # 有两位小数的正实数
            11: "^[0-9]+(.[0-9]{1,3})?$",  # 有1~3位小数的正实数
            12: '^-?\d+$',  # 整数
            13: '^[0-9]*[1-9][0-9]*$',  # 正整数
            14: "^[1-9]\d*$",  # 非零的正整数：^[1-9]\d*$ 或 ^([1-9][0-9]*){1,3}$ 或 ^\+?[1-9][0-9]*$
            15: "^-[1-9]\d*$",  # 非零的负整数：^\-[1-9][]0-9*$ 或 ^-[1-9]\d*$
            16: "^[1-9]\d*|0$",  # 非负整数：^\d+$ 或 ^[1-9]\d*|0$
            17: '^-[0-9]*[1-9][0-9]*$',  # 负整数
            18: "^-[1-9]\d*|0$",  # 非正整数：^-[1-9]\d*|0$ 或 ^((-\d+)|(0+))$
            19: '(-?\d*)\.?\d+',  # 提取信息中的浮点数（即小数）
            20: "^\d+(\.\d+)?$",  # 非负浮点数：^\d+(\.\d+)?$ 或 ^[1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0$
            # 非正浮点数： 或 ^(-([1-9]\d*\.\d*|0\.\d*[1-9]\d*))|0?\.0+|0$ 或'^((-\d+\.\d+)?)|(0+(\.0+)?))$',
            21: "^((-\d+(\.\d+)?)|(0+(\.0+)?))$",
            # 正浮点数：或 ^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$
            22: "^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$",
            # 负浮点数：或 ^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$ 或者^(-((^((0-9)+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)$)))$
            23: "^-([1-9]\d*\.\d*|0\.\d*[1-9]\d*)$",
            24: "^(-?\d+)(\.\d+)?$",  # 浮点数：或 ^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$
        }
        return re_gu.get(re_type)

    def date_rule(self, re_type, m='', n='', ):
        re_gu = {
            1: '^\d{4}-\d{1,2}-\d{1,2}',  # 日期格式
            2: '^(0?[1-9]|1[0-2])$',  # 一年的12个月(01～09和1～12)：
            3: '^((0?[1-9])|((1|2)[0-9])|30|31)$',  # 一个月的31天(01～09和1～31)
            # 校验日期:(“yyyy-mm-dd“ 格式的日期校验，已考虑平闰年。)
            4: '^(?:(?!0000)[0-9]{4}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)|(?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)-02-29)$',
        }
        return re_gu.get(re_type)

    def phone_rule(self, re_type, m='', n='', ):
        re_gu = {
            1: '^((\(\d{2,3}\))|(\d{3}\-))?(\(0\d{2,3}\)|0\d{2,3}-)?[1-9]\d{6,7}(\-\d{1,4})?$',  # 电话号码
            2: '^(\(\d{3,4}-)|\d{3.4}-)?\d{7,8}$',  # 电话号码("XXX-XXXXXXX"、"XXXX-XXXXXXXX"、"XXXXXXX"和"XXXXXXXX)
            3: '(\(\d{3,4}\)|\d{3,4}-|\s)?\d{7,14}',  # 提取信息中的中国电话号码（包括移动和固定电话）
            4: '\d\d\d-(\d\d\d)-(\d\d\d\d)',  # 提取信息中的中国电话号码（包括移动和固定电话） 415-555-4242
            5: '\d{3}-\d{8}|\d{4}-\d{7}',  # 国内电话号码(0511-4405222、021-87888822)
            6: '^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$',  # 手机号码
            7: '^((\(\d{2,3}\))|(\d{3}\-))?13\d{9}$',  # 手机号码
            8: '(86)*0*13\d{9}',  # 提取信息中的中国手机号码
            9: '(\(\d{3,4}\)|\d{3,4}-|\s)?\d{8}',  # 提取信息中的中国固定电话号码
            10: '/^0\d{2,3}$/',  # 电话区号
        }
        return re_gu.get(re_type)

    def html_rules(self, re_type, m='', n='', ):
        re_gu = {
            1: '<(.*)>.*<\/\1>|<(.*) \/>',  # 匹配HTML标记
            2: '<(\S*?)[^>]*>.*?</\1>|<.*? />',  # HTML标记的正则表达式： (网上流传的版本太糟糕，上面这个也仅仅能部分，对于复杂的嵌套标记依旧无能为力)
            3: '/<(.*)>.*<\/\1>|<(.*) \/>/',  # 匹配HTML标记的正则表达式
            4: '^\\s*[a-zA-Z\\-]+\\s*[:]{1}\\s[a-zA-Z0-9\\s.#]+[;]{1}',  # 查找CSS属性
            5: '''^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$''',  # 提取网页颜色代码
            6: '''\\< *[img][^\\\\>]*[src] *= *[\\"\\']{0,1}([^\\"\\'\\ >]*)''',  # 提取信息中的图片链接
            7: '''(s|S)(r|R)(c|C)  *=  *('|")?(\w|\\|\/|\.)+('|"|  *|>)?''',  # 提取信息中的图片链接
            # '^[a-zA-Z]+://(\w+(-\w+)*)(\.(\w+(-\w+)*))*(\?\s*)?$
            # 或:^http:\/\/[A-Za-z0-9]+\.[A-Za-z0-9]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$',
            # 或  [a-zA-z]+://[^\s]*
            # 或 ^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$
            # 或 (h|H)(r|R)(e|E)(f|F)  *=  *('|")?(\w|\\|\/|\.)+('|"|  *|>)?
            9: """[a-zA-z]+://[^\s]*""",  # InternetURL 提取信息中的网络链接
            # 提取页面超链接
            8: '''(<a\\s*(?!.*\\brel=)[^>]*)(href="https?:\\/\\/)((?!(?:(?:www\\.)?'.implode('|(?:www\\.)?', $follow_list).'))[^" rel="external nofollow" ]+)"((?!.*\\brel=)[^>]*)(?:[^>]*)>''',
        }
        return re_gu.get(re_type)

    def ip_rules(self, re_type, m='', n='', ):
        re_gu = {
            1: '(\d+)\.(\d+)\.(\d+)\.(\d+)',  # 提取信息中的IP地址 或 \d+\.\d+\.\d+\.\d+ (提取IP地址时有用)
            2: '((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))',  # IP地址
            # IP-v4地址
            3: '\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b',
            # 校验IP-v6地址
            4: '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))',
            5: '''((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))''',  # 子网掩码
            6: "[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?",  # 域名
        }
        return re_gu.get(re_type)

    def xml_rules(self, re_type, m='', n='', ):
        re_gu = {
            1: '^([a-zA-Z]+-?)+[a-zA-Z0-9]+\\.[x|X][m|M][l|L]$',  # xml文件：
        }
        return re_gu.get(re_type)

    def sql_rules(self, re_type, m='', n='', ):
        re_gu = {
            1: '^(select|drop|delete|create|update|insert).*$',  # sql语句
        }
        return re_gu.get(re_type)

    def str_rules(self, re_type, m='', n='', ):
        re_gu = {
            1: '^[A-Za-z]+$',  # 英文字符串 由26个英文字母组成的字符串
            2: '^[A-Z]+$',  # 英文大写串  由26个大写英文字母组成的字符串
            3: '^[a-z]+$',  # 英文小写串 由26个小写英文字母组成的字符串
            4: '^[A-Za-z0-9]+$',  # 英文字符数字串
            5: '^\w+$',  # 英数字加下划线串
            6: '^[A-Za-z0-9]+$',  # 英文和数字/由数字和26个英文字母组成的字符串：^[A-Za-z0-9]+$ 或 ^[A-Za-z0-9]{4,40}$
            7: '^\w+$',  # 由数字、26个英文字母或者下划线组成的字符串：^\w+$ 或 ^\w{3,20}
            8: '^[\u4E00-\u9FA5A-Za-z0-9]+$',  # 中文、英文、数字但不包括下划线等符号 或 ^[\u4E00-\u9FA5A-Za-z0-9]{2,20}$
            9: '^[\u4E00-\u9FA5A-Za-z0-9_]+$',  # 中文、英文、数字包括下划线： 或^[\u4e00-\u9fa5_a-zA-Z0-9]+$'
            10: '^[a-zA-Z][a-zA-Z0-9_]{4,15}$',  # 帐号(字母开头，允许5-16字节，允许字母数字下划线)
            11: '^[\u0391-\uFFE5]+$',  # 中文
            12: '^[\u4e00-\u9fa5]{0,%s}$' % (n),  # 汉字：^[\u4e00-\u9fa5]{0,}$ 0-n个汉字
            13: '[\u4e00-\u9fa5]',  # 匹配中文字符的正则表达式
            14: '[\uFF00-\uFFFF]',  # 全角符号
            15: '[\u0000-\u00FF]',  # 半角符号
            16: '^\x00-\xff',  # 匹配双字节字符(包括汉字在内，可以用来计算字符串的长度(一个双字节字符长度计2，ASCII字符计1))'[^\x00-\xff]'
            17: r'\\x[a-fA-F0-9]{2}',  # 找到所有的16进制转义字符 \xxx
            18: r'\\u[0-9a-fA-F]{4}',  # 找到所有的un进制转义字符  \uxxx
            19: r'(\\u[0-9a-fA-F]{4}|\\x[0-9a-fA-F]{2})',  # 找到所有的 \xxx \uxxx
        }
        return re_gu.get(re_type)

    def rule(self, re_type, n='', m=''):
        re_gu = {
            1: '^.{%s,%s}$' % (m, n),  # 长度为3-20的所有字符：^.{3,20}$
            2: '[1-9]{1}(\d+){5}',  # 提取信息中的中国邮政编码 '^[1-9]\d{5}$', [1-9]\d{5}(?!\d) (中国邮政编码为6位数字)
            # E-匹配Email地址的正则表达式 或者^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
            3: '^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$',
            4: '^[1-9]*[1-9][0-9]*$',  # 腾讯QQ号 或 [1-9][0-9]{4,} (腾讯QQ号从10000开始)
            5: '^\d{15}|\d{18}$',  # 身份证号(15位、18位数字)
            6: '^([0-9]){7,18}(x|X)?$',  # 短身份证号码(数字、字母x结尾)： 或 ^\d{8,18}|[0-9x]{8,18}|[0-9X]{8,18}?$
            7: '^[a-zA-Z][a-zA-Z0-9_]{4,15}$',  # 帐号是否合法(字母开头，允许5-16字节，允许字母数字下划线)：
            8: '^[a-zA-Z]\w{5,17}$',  # 密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)：
            9: '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$',  # 强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-10之间)
            10: "[^%&',;=?$\x22]+",  # 可以输入含有^%&',;=?$\"等字符：[^%&',;=?$\x22]+
            11: "[^~\x22]+",  # 禁止输入含有~的字符
            # 匹配首尾空格/首尾空白字符的正则表达式^\s*|\s*$或(^\s*)|(\s*$)
            # （像vbscript那样的trim函数）(可以用来删除行首行尾的空白字符(包括空格、制表符、换页符等等)，非常有用的表达式)
            12: '(^\s*)|(\s*$)',
            13: '<!--(.*?)-->',  # 抽取注释
            14: '\n[\s| ]*\r',  # 匹配空行的正则表达式(可以用来删除空白行)  或者 '\n\s*\r',
            15: '''^([a-zA-Z]\\:|\\\\)\\\\([^\\\\]+\\\\)*[^\\/:*?"<>|]+\\.txt(l)?$''',  # 文件扩展名效验
            16: '''^.*MSIE [5-8](?:\\.[0-9]+)?(?!.*Trident\\/[5-9]\\.0).*$''',  # 判断IE版本
        }
        return re_gu.get(re_type)

    def get_text_compile(self, rule):
        pattern = re.compile(rule)
        return pattern

    def get_text_findall(self, rule, message):
        pattern = self.get_text_compile(rule)
        return pattern.findall(message)

    def get_text_match(self, rule, message, location=False):
        """可返回一个class、str、tuple。但是一定需要注意match()，从位置0开始匹配，匹配不到会返回None，
        返回None的时候就没有span/group属性了，并且与group使用，返回一个单词‘Hello’后匹配就会结束.
        """
        pattern = self.get_text_compile(rule)
        match = pattern.match(message)
        if match:
            if location:
                return match.span()
            else:
                return match.group()
        return False

    def get_text_search(self, rule, message, location=False):
        """
        但是不同的是search(), 可以不从位置0开始匹配。但是匹配一个单词之后，匹配和match()一样，匹配就会结束。
        """
        pattern = self.get_text_compile(rule)
        search = pattern.search(message)
        if search:
            if location:
                return search.span()
            else:
                return search.group()
        return False

    # 替换
    def sub(self, pattern, text):
        """
        :param pattern: r"(\\u[0-9a-fA-F]{4}|\\x[0-9a-fA-F]{2})"
        :param text: r"This string contains \u1234 and \x99 unicode characters."
        :return: This string contains  and  unicode characters.
        """
        return re.sub(pattern, '', text)
