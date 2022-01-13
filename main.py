from util.emailUtil import send
from api.api import XueQiu
from util import fileDeal
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date
import sys

sys.path.append('./')
sys.path.append('../')

xq = XueQiu()
xq.get_token()


def run(sendFlag=False):
    msg = ""
    stocks = fileDeal.get_stocks()
    for stock in stocks.get("stock", []):
        stock_code = set(stock.keys()).pop()
        stock_dict = stock.get(stock_code)
        resp = xq.get_stock(stock_code)
        datas = resp.get("data", [])
        for data in datas:
            stock_dict.update(data)
            if data["current"] >= stock_dict["sellNotify"]:
                stock_dict["trade"] = "卖出"
                sendFlag = True
            if data["current"] <= stock_dict["buyNotify"]:
                sendFlag = True
                stock_dict["trade"] = "买入"
            profit = data["current"] - stock_dict["costPrice"]
            if profit >= 0:
                stock_dict["profit"] = "盈利"
            else:
                stock_dict["profit"] = "亏本"
            stock_dict["today_profit"] = (
                data["current"] - data["last_close"])*stock_dict["number"]
            print(stock_dict)
            for k, v in stock_dict.items():
                msg += f"{k}:{v}\n"
        print(msg)
        if sendFlag:
            send(msg)


sched = BlockingScheduler()

# The job will be executed on November 6th, 2009
# sched.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
sched.add_job(run, 'cron', second="*/30", hour="9-16")
sched.add_job(run, 'cron', hour="16", args=[True])

sched.start()
