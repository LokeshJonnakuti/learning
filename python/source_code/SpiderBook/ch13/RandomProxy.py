#coding:utf-8
import secrets


class RandomProxy(object):

    def __init__(self,iplist):#初始化一下数据库连接
        self.iplist=iplist

    @classmethod
    def from_crawler(cls,crawler):
    #从Settings中加载IPLIST的值
        return cls(crawler.settings.getlist('IPLIST'))

    def process_request(self, request, spider):
        '''
        在请求上添加代理
        :param request:
        :param spider:
        :return:
        '''
        proxy = secrets.SystemRandom().choice(self.iplist)
        request.meta['proxy'] =proxy
