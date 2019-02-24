import asyncio
import aiohttp
import json
import csv
import time


# url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=dm&st=desc&sd=2018-02-14&ed=2019-02-20&qdii=&tabSubtype=,,,,,&pi=' + offset + '&pn=50&dx=1&v=0.13549086251577092'


def get_data(html):
    data = html[html.find('{'):html.find(']')+1] + '}'
    fund_data = data.replace('datas', '\"datas\"')
    fund = json.loads(fund_data)
    fund_value = fund.values()
    return fund_value


def save_csv(values):
    fund_info = ['Code', 'Name', 'Pinyin', 'Current_date', 'Net_value', 'Gross_value', 'Day_rate', 'One_week', 'One_month', 'Three_month', 'Six_month', 'One_year',
                 'Two_year', 'Three_year', 'From_this_y', 'From_establish', 'Establish_date', '', '', 'Management_rate',
                 'Discounted_m_r', '', 'Discounted_m_r', '', '']
    with open('fund_20190223.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fund_info)
        for value in values:
            for v in value:
                for i in v:
                    writer.writerow(i.split(','))


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(offsets):
    urls = ['http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=dm&st=desc&sd=2018-02-20&ed=2019-02-20&qdii=&tabSubtype=,,,,,&pi= {0} &pn=50&dx=1'.format(offset) for offset in offsets]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        page_list = await asyncio.gather(*tasks)
        page_list_data = []
        for page in page_list:
            data = get_data(page)
            page_list_data.append(data)
        print(len(page_list_data))
        save_csv(page_list_data)


if __name__ == '__main__':
    s = time.time()
    total_page = list(x for x in range(1, 94))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(total_page))
    print("It takes {} seconds".format(time.time() - s))
