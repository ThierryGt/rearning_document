# coding: utf-8
from selenium import webdriver
from lxml import etree
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import logging
import io
import os
import operator
import ast
import sys
import requests
import pymysql
import json
from userlogin import user_data
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
logging.basicConfig(filename='error.log', level=logging.INFO)

# wait = WebDriverWait(browser, 10)

class WeChatSpider(object):
    def __init__(self, browser, url, username, passwd,):
        self.other_list = []
        self.browser = browser
        self.url = url
        self.username = username
        self.passwd = passwd
        self.browser_create()

    # request url
    def browser_create(self):
        self.driver = webdriver.Chrome(executable_path=self.browser)
        self.driver.get(self.url)
        # Fill in the username
        time.sleep(1)
        self.driver.find_element_by_name("account").send_keys(self.username)
        # Fill in the passwd
        time.sleep(1)
        self.driver.find_element_by_name("password").send_keys(self.passwd)
        self.user_login()

    # click login button
    def user_login(self):
        s = "bizlogin"
        ba = "ban"
        self.click_button = self.driver.find_element_by_class_name("btn_login")
        self.click_button.click()
        time.sleep(10)

        u = self.driver.current_url

        if s in u or ba in u or u == "https://mp.weixin.qq.com/":
            user_d = {"username": self.username, "passwd": self.passwd}
            with open("not_code.txt", "a", encoding="utf8") as f:
                f.write(str(user_d)+str("!"))
            f.close()
            self.driver.quit()
        else:
            self.article()

    # FIXME ARTICLE SPIDER
    def article(self):
        title_list = []
        like_list = []
        read_list = []
        self.affiliated_message = []
        try:
            time.sleep(5)
            data = str(self.driver.page_source)
            html = etree.HTML(data)
            the_header = html.xpath('//div[@class="weui-desktop-pagination"]/span[@class="weui-desktop-pagination__nav"]/span[@class="weui-desktop-pagination__num__wrp"]/label[@class="weui-desktop-pagination__num"]/text()')
            the_header_number = int(the_header[0])
            the_header_tail = int(the_header[1])
            while the_header_number < the_header_tail:
                data = str(self.driver.page_source)
                html = etree.HTML(data)
                affiliated_message_data = html.xpath('//div[@class="weui-desktop-panel__bd"]/ul[@class="weui-desktop-mass"]/li[@class="weui-desktop-mass__item"]//text()')
                if affiliated_message_data:
                    i = 1
                    while i < 10:
                        # s = '//div[@class="weui-desktop-panel__bd"]/ul[@class="weui-desktop-mass"]/li[@class="weui-desktop-mass__item"][%d]//text()'%i
                        d = html.xpath('//div[@class="weui-desktop-panel__bd"]/ul[@class="weui-desktop-mass"]/li[@class="weui-desktop-mass__item"][%d]//text()'%i)
                        i+=1
                        self.affiliated_message.append({
                            "d":d,
                        })

                title_data = html.xpath("//div[@class='weui-desktop-mass-appmsg__bd']/a[@class='weui-desktop-mass-appmsg__title']/text()")
                for title in title_data:
                    new_title = str(title).strip()
                    if new_title:
                        title_list.append(new_title)
                read_number_data = html.xpath("//li[@class='weui-desktop-mass-media__data appmsg-view']/span[@class='weui-desktop-mass-media__data__inner']/text()")
                for read in read_number_data:
                    new_read_number = read.strip()
                    if new_read_number:
                        read_list.append(new_read_number)
                like_number_data = html.xpath("//li[@class='weui-desktop-mass-media__data appmsg-like']/span[@class='weui-desktop-mass-media__data__inner']/text()")
                for like in like_number_data:
                    new_like_number = str(like).strip()
                    if new_like_number:
                        like_list.append(new_like_number)

                time.sleep(5)
                self.driver.find_element_by_xpath('//a[text()="下一页"]').click()
                the_header_number += 1
            d = map(list, zip(title_list, read_list, like_list))
            new_dict = []
            for item in d:
                new_dict = dict(zip(['title', 'read_number', 'like_number'], item))
                self.other_list.append(new_dict)

            for other in self.other_list:
                other["read_number"] = int(other.get("read_number"))
                other["like_number"] = int(other.get("like_number"))

        except Exception as e:
            logging.exception("error"+str(e))

        finally:
            print(self.other_list)
            print(self.affiliated_message)
        self.traffic()

    def traffic(self):
        # 流量主
        traffic_type = "publisher/publisher_index"
        # 用户分析
        key_word = "useranalysis"
        # 公众号
        gongzhonghao = "/cgi-bin/settingpage?t=setting/index&"
        self.url_list = {
            "new_traffic_url": "",
            "useranalysis": "",
            "gzhao_url": "",
        }
        time.sleep(1)
        self.traffic_button = self.driver.find_elements_by_tag_name("a")
        for traffic_url in self.traffic_button:
            if traffic_type in traffic_url.get_attribute("href"):
                new_traffic_url = traffic_url.get_attribute("href")
                self.url_list['new_traffic_url'] = new_traffic_url

            elif key_word in traffic_url.get_attribute("href"):
                useranalysis = traffic_url.get_attribute("href")
                self.url_list['useranalysis'] = useranalysis

            elif gongzhonghao in traffic_url.get_attribute("href"):
                set_up = traffic_url.get_attribute("href")
                self.url_list['gzhao_url'] = set_up

        # self.traffic_analysis_data()
        # todo: 处理财务管理
        self.financial_management()

    # 处理财务管理
    # financial_url
    def financial_management(self):
        judge_type = 0
        li = []
        self.driver.get(self.url_list.get("new_traffic_url"))
        time.sleep(5)
        count_number = etree.HTML(str(self.driver.page_source))
        h = count_number.xpath("//div[@class='DataColumn__itemAlignCenter-3kdmM DataColumn__numberPositionTop-3m8zi']/div[@class='DataColumn__num-1iBxl']/text()")
        # return ['4.87', 'l']
        # print(h)
        time.sleep(2)
        if len(h) != 0:
            try:
                financial_keyword = "publisher/publisher_recharge&token"
                time.sleep(2)
                all_a = self.driver.find_elements_by_tag_name("a")
                for financial_url in all_a:
                    if financial_keyword in financial_url.get_attribute("href"):
                        self.driver.get(financial_url.get_attribute("href"))
                        break
                time.sleep(5)
                k = 1
                while k < 4:
                    time.sleep(2)
                    data = str(self.driver.page_source)
                    html = etree.HTML(data)
                    d = html.xpath('//div[@class="Table_new__outer-2fbBb Table_new__insideDialog-2GC3P style__grayTableTh-Hx4F4"]//tbody//text()')
                    li.append(d)
                    time.sleep(2)
                    jump_data = html.xpath('//div[@class="ui-flex-center ui-flex_align-justify"]//text()')
                    if jump_data:
                        # FIXME BUTTON NEXT PAGE .send_keys(Keys.ENTER)
                        self.driver.find_element_by_xpath('//span[@class="Pagination__jumper-2jLLc"]/input').send_keys(str(k + 1))
                        time.sleep(2)
                        self.driver.find_element_by_xpath('//button[@class="Button_new__base-1H7bt Button_new__default-3C02p Button_new__mini-catyW"]/span[text()="跳转"]').click()
                        k += 1
                        time.sleep(5)
                n = 1
                while n < 4:
                    # 先打开选择器
                    self.driver.find_element_by_class_name("el-input__inner").click()
                    time.sleep(2)
                    if judge_type == 0:
                        print("HelloWorld")
                    else:
                        self.driver.find_element_by_xpath('//button[@class="el-picker-panel__icon-btn el-icon-arrow-left"]').click()
                    # 月份翻页
                    time.sleep(2)
                    # 选择左边table月份的一号
                    self.driver.find_element_by_xpath('//div[@class="el-picker-panel__content el-date-range-picker__content is-left"]/table[@class="el-date-table"]/tbody/tr[@class="el-date-table__row"]/td[text()="1"]').click()
                    time.sleep(2)
                    # 选择右边table月份的一号
                    self.driver.find_element_by_xpath('//div[@class="el-picker-panel__content el-date-range-picker__content is-right"]/table[@class="el-date-table"]/tbody/tr[@class="el-date-table__row"]/td[text()="1"]').click()
                    time.sleep(2)
                    judge_type = 1
                    data = str(self.driver.page_source)
                    html = etree.HTML(data)
                    No_data = html.xpath('//div[@class="Table_new__wrapper-3l9iP Table_new__empty-1AjHZ Table_new__insideDialog-2GC3P"]//div[@class="Table_new__loading-PVDQT"]/div/text()')
                    if No_data:
                        # return ["暂无数据"]
                        # print(No_data)
                        break
                    else:
                        i = 0
                        while i < 4:
                            time.sleep(2)
                            data = str(self.driver.page_source)
                            html = etree.HTML(data)
                            d = html.xpath('//div[@class="Table_new__outer-2fbBb Table_new__insideDialog-2GC3P style__grayTableTh-Hx4F4"]//tbody//text()')
                            li.append(d)
                            time.sleep(2)
                            jump_data = html.xpath('//div[@class="ui-flex-center ui-flex_align-justify"]//text()')
                            if jump_data:
                                # FIXME BUTTON NEXT PAGE .send_keys(Keys.ENTER)
                                self.driver.find_element_by_xpath('//span[@class="Pagination__jumper-2jLLc"]/input').send_keys(str(i+1))
                                time.sleep(2)
                                self.driver.find_element_by_xpath('//button[@class="Button_new__base-1H7bt Button_new__default-3C02p Button_new__mini-catyW"]/span[text()="跳转"]').click()
                                i += 1
                                time.sleep(5)
                        n += 1
                self.financial_management_cleaning(li,h)
            except Exception as e:
                logging.exception("error" + str(e))
        else:
            self.host_data_conunt = []
            self.host_data_conunt.append({
                "date_time": "date_time",
                "income_number": 0,
                "income_count_number": 0,
            })
            self.graphic_analysis_data()

    # TODO DATA SET
    def financial_management_cleaning(self, li, h):
        li_data = []
        new_lidata = []
        initial_price = float(h[1])
        self.host_data_conunt=[]
        for i in li:
            k = 0
            j = 0
            while k < len(i) / 2:
                li_data.insert(0, {
                    "data_time": i[j],
                    "money": i[j + 1]
                })
                j += 2
                k += 1

        for clean_data in li_data:
            if clean_data not in self.host_data_conunt:
                self.host_data_conunt.insert(0,{
                "data_time": clean_data.get("data_time").replace("-", ""),
                "income_number": float(clean_data.get("money"))
                })

        sorted_x = sorted(self.host_data_conunt, key=operator.itemgetter('data_time'), reverse=True)
        for x in sorted_x:
            x["income_number"] = float(x.get("income_number"))
            x["income_count_number"] = float('%.2f' % initial_price)
            initial_price = float('%.2f' % initial_price) - float(x.get("income_number"))
        self.graphic_analysis_data()

    def graphic_analysis_data(self):
        time.sleep(1)
        fans_list = []
        self.driver.get(self.url_list.get("useranalysis"))
        i = 0
        while i < 10:
            # time.sleep(10)
            table = self.driver.find_element_by_id('js_detail')
            # table的总行数，包含标题
            table_rows = table.find_elements_by_tag_name('tr')
            # print(table_rows)
            date_time = table_rows[i].find_elements_by_tag_name('td')[0].text
            date_time = date_time.replace("-", "", 2)
            # print("时间",date_time)
            # 获取某单元格的text:获取第一行第二列的text,[不算标题行]
            new_number = table_rows[i].find_elements_by_tag_name('td')[1].text
            # print("新关注数:",new_number)
            cancel_number = table_rows[i].find_elements_by_tag_name('td')[2].text
            # print("取消关注人数",cancel_number)
            net_number = table_rows[i].find_elements_by_tag_name('td')[3].text
            # print("净增关注人数",net_number)
            cumulative_number = table_rows[i].find_elements_by_tag_name('td')[4].text
            # print("累积关注人数",cumulative_number)
            date = {
                "date_time": date_time,
                "new_number": int(new_number),
                "cancel_number": int(cancel_number),
                "net_number": int(net_number),
                "cumulative_number": int(cumulative_number),
            }
            fans_list.insert(0,date)
            i += 1
        self.date_summary(fans_list)

    # FIXME self.other_list self.affiliated_message
    def date_summary(self,fans_list):
        i = 0
        new_article_list = []
        self.article_data_list = []
        while i < len(self.affiliated_message):
            for all_article_data in set(self.affiliated_message[i].get("d")):
                for article_data in self.other_list:
                    if all_article_data.strip() == article_data.get("title"):
                        new_article_list.append({
                            "d": set(self.affiliated_message[i].get("d")),
                            "da": article_data,
                        })
                        break
            i += 1
        for j in new_article_list:
            for k in j.get("d"):
                if "月" in k and "日" in k:
                    self.article_data_list.append({
                        "data_time": k,
                        "data": j.get("da")
                    })

        wechatdata = {
            "fans_data": fans_list,
            "other_data": self.article_data_list,
            "liuliangzhu": self.host_data_conunt,
        }
        self.gonghao(wechatdata)

    def gonghao(self,wechatdata):
        time.sleep(1)
        self.driver.get(self.url_list.get("gzhao_url"))
        time.sleep(3)
        gongzhonghao_data = str(self.driver.page_source)
        html = etree.HTML(gongzhonghao_data)
        html_data = html.xpath('//div/span[@class="weui-desktop-setting__item__info"]/text()')
        gongzhonghao_name = str(html_data[0]).strip()
        gh_name = str(html_data[-1]).strip()
        uname = html.xpath("//div[@class='weui-desktop-setting__item__main']/div[@class='weui-desktop-setting__item__info']/text()")
        username = str(uname[-1]).strip()
        wechatdata["gongzhonghao_name"] = gongzhonghao_name
        wechatdata["gh_name"] = gh_name
        wechatdata["username"] = username
        self.sql_conn(wechatdata)

    # TODO DATA SUMMARY
    def sql_conn(self, wechdata):
        print(wechdata)
        self.close_browser(wechdata)


    def close_browser(self, wechdata):
        # close browser
        if self.driver:
            # time.sleep(5)
            self.driver.quit()
        url = ""
        q = requests.post(url, data = json.dumps(wechdata), )
        print("爬取完成")
        print(q.text)


if __name__ =="__main__":

    for k, v in enumerate(user_data):
        wc = WeChatSpider(browser="F:\py\Google\Chrome\Application\chromedriver", url="https://mp.weixin.qq.com/", username=v.get("username"), passwd=v.get("passwd"),)
        logging.exception("error")

    while True:
        with open("not_code.txt", "r+") as f:
            try:
                da = f.read()
                f.seek(0)
                f.truncate()
            except Exception as e:
                logging.exception("error"+str(e))
            finally:
                if f:
                    f.close()

        if da:
            s = da.split("!")
            s.pop(-1)
            for ss in s:
                sss = ast.literal_eval(str(ss))
                wc = WeChatSpider(browser="F:\py\Google\Chrome\Application\chromedriver", url="https://mp.weixin.qq.com/",username=sss.get("username"), passwd=sss.get("passwd"), )
        else:
            break
