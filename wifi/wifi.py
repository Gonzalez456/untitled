import pywifi
from pywifi import const

self.file = open(path, "r", errors="ignore")
wifi = pywifi.PyWiFi()  # 抓取网卡接口
self.iface = wifi.interfaces()[0]  # 抓取第一个无限网卡
self.iface.disconnect()  # 测试链接断开所有链接
