import sys
sys.path.append('./')
sys.path.append('../')

from api.api import XueQiu

xq = XueQiu()
xq.get_token()
xq.get_stock("SH603123")