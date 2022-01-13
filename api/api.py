from httpReq.http import Http


class XueQiu:
    def __init__(self) -> None:
        self.base_url = "https://xueqiu.com/"
        self.reqest = Http()
        self.cookie = {}

    def get_token(self):
        resp = self.reqest.get(self.base_url)
        token = resp.cookies.get("xq_a_token","")
        self.cookie={"xq_a_token": token}
        return token

    def get_stock(self,code):
            url = "https://stock.xueqiu.com/v5/stock/realtime/quotec.json?symbol={}".format(code)
            resp = self.reqest.get(url,cookie= self.cookie)
            return resp.json()

