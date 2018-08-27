from selenium import webdriver
from lxml import etree
from bs4 import BeautifulSoup
import time
import logging
import io
import os
import ast
import sys
import requests
import json
from userlogin import user_data
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
logging.basicConfig(filename='error.log', level=logging.INFO)



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
        self.click_button = self.driver.find_elements_by_tag_name("a")
        for button_url in self.click_button:
            if "javascript:" in button_url.get_attribute("href") and "javascript:;" not in button_url.get_attribute("href"):
                button_url.click()
        time.sleep(20)

        u = self.driver.current_url

        if s in u or ba in u:
            user_d = {"username": self.username, "passwd": self.passwd}
            with open("not_code.txt", "a", encoding="utf8") as f:
                f.write(str(user_d)+str("!"))
            f.close()
            self.driver.quit()
        else:
            self.article()

    def article(self):
        # time.sleep(5)
        data = str(self.driver.page_source)
        html = etree.HTML(data)
        title_data = html.xpath("//div[@class='weui-desktop-mass-appmsg__bd']/a[@class='weui-desktop-mass-appmsg__title']/text()")
        # print(title_data)
        title_list = []
        for title in title_data:
            new_title = str(title).strip()
            if new_title:
                title_list.append(new_title)
        read_number_data = html.xpath("//li[@class='weui-desktop-mass-media__data appmsg-view']/span[@class='weui-desktop-mass-media__data__inner']/text()")
        read_list = []
        for read in read_number_data:
            new_read_number = read.strip()
            if new_read_number:
                read_list.append(new_read_number)
        like_number_data = html.xpath("//li[@class='weui-desktop-mass-media__data appmsg-like']/span[@class='weui-desktop-mass-media__data__inner']/text()")
        like_list = []
        for like in like_number_data:
            new_like_number = str(like).strip()
            if new_like_number:
                like_list.append(new_like_number)
        d = map(list, zip(title_list, read_list, like_list))
        new_dict = []
        for item in d:
            new_dict = dict(zip(['title', 'read_number', 'like_number'], item))
            self.other_list.append(new_dict)

        for other in self.other_list:
            other["read_number"] = int(other.get("read_number"))
            other["like_number"] = int(other.get("like_number"))

        # print(self.other_list)
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
                # print(new_traffic_url)
                self.url_list['new_traffic_url'] = new_traffic_url

            elif key_word in traffic_url.get_attribute("href"):
                useranalysis = traffic_url.get_attribute("href")
                self.url_list['useranalysis'] = useranalysis

            elif gongzhonghao in traffic_url.get_attribute("href"):
                set_up = traffic_url.get_attribute("href")
                self.url_list['gzhao_url'] = set_up

        self.traffic_analysis_data()

    def traffic_analysis_data(self):
        time.sleep(2)
        self.driver.get(self.url_list.get("new_traffic_url"))
        # print(self.url_list)
        time.sleep(2)
        count_number = etree.HTML(str(self.driver.page_source))
        h = count_number.xpath("//div[@class='DataColumn__itemAlignCenter-3kdmM DataColumn__numberPositionTop-3m8zi']/div[@class='DataColumn__num-1iBxl']/text()")
        if len(h) != 0:
            self.count_num = h[1]
            time.sleep(5)
            self.data_report_url = self.driver.find_elements_by_tag_name("a")
            host_type = "publisher/publisher_report&token="
            for report_url in self.data_report_url:
                if host_type in report_url.get_attribute("href"):
                    self.host_pay_url = report_url.get_attribute("href")
                    self.driver.get(self.host_pay_url)
                    time.sleep(5)
                    host_str_data = str(self.driver.page_source)
                    self.host_url_data(host_str_data)
                    break
        else:
            self.host_data_conunt = []
            self.host_data_conunt.append({
                "date_time": "date_time",
                "income_number": 0,
            })
            self.graphic_analysis_data()

    def host_url_data(self, host_str_data):
        time.sleep(1)
        self.host_data_conunt = []
        soup = BeautifulSoup(host_str_data, "html.parser")
        for idx, tr in enumerate(soup.find_all('tr')):
            if idx != 0:
                tds = tr.find_all('td')
                d = str(tds[0].contents[0]).split("div>")[1]
                date_time = d.split("</")[0]
                n = str(tds[4].contents[0]).split("div>")[1]
                income_number = n.split("</")[0]
                self.host_data_conunt.insert(0,{
                    "date_time": date_time,
                    "income_number": income_number
                })
                # print(date_time,income_number)
        self.graphic_analysis_data()

    def graphic_analysis_data(self):
        time.sleep(1)
        fans_list = []
        self.driver.get(self.url_list.get("useranalysis"))
        i = 0
        while i < 7:
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

    def date_summary(self, fans_list):
        wechatdata = {
            "fans_data": fans_list,
            "other_data": self.other_list
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

    def sql_conn(self, wechdata):

        w = wechdata.get("username")
        gh_name = wechdata.get("gh_name")
        gongzhonghao = wechdata.get("gongzhonghao_name")
        fans = wechdata.get("fans_data")
        other_data = wechdata.get("other_data")
        d_time = fans[6].get("date_time")

        if len(self.host_data_conunt) != 1:
            count_s = str(self.count_num)
            float_count = float(count_s)

            for ho in reversed(self.host_data_conunt):
                ho["income_count_number"] = float('%.2f' % float_count)
                float_count = float('%.2f' % float_count) - float(ho.get("income_number"))

            i = 1
            k = 1
            lll = []
            for host_data in self.host_data_conunt:
                for f in fans:
                    if host_data.get("date_time").replace("-", "", 2) == f.get("date_time"):
                        f["income_number"] = host_data.get("income_number")
                        f["income_count_number"] = host_data.get("income_count_number")

        else:
            for f in fans:
                f["income_number"] = "0"
                f["income_count_number"] = "0"
        self.close_browser(wechdata)

    def close_browser(self, wechdata):
        # close browser
        if self.driver:
            # time.sleep(5)
            self.driver.quit()
        logging.exception("spider sucess")
        url = "https://wq.benmingfo.com.cn/app/index.php?i=5&c=entry&do=alljson&m=wxlm_statistics"
        q = requests.post(url, data = json.dumps(wechdata), )
        print("爬取完成")


if __name__ =="__main__":
    for k, v in enumerate(user_data):
        wc = WeChatSpider(browser="F:\py\Google\Chrome\Application\chromedriver", url="https://mp.weixin.qq.com/", username=v.get("username"), passwd=v.get("passwd"),)

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
