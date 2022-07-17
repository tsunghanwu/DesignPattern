## An example of log in anomaly notice 

import time
from abc import ABCMeta, abstractmethod
from p1_2 import Observer, Observable

class Account(Observable):
    def __init__(self):
        super().__init__()
        self._latest_ip = {}
        self._latest_region = {}

    def login(self, name, ip, time):
        region = self._get_region(ip)
        if self._is_long_distance(name, region):
            self.notify_observers(
                    {'name': name, 'ip':ip, 'region':region, 'time':time}
                    )
        self._latest_region[name] = region
        self._latest_ip[name] = ip

    def _get_region(self, ip):
        ## Get region from ip
        ip_region = {
                '101.47.18.9': 'City A',
                '67.218.147.69': 'City B'
                }
        region = ip_region.get(ip)
        if region is None:
            return ''
        else:
            return region

    def _is_long_distance(self, name, region):
        latest_region = self._latest_region.get(name)
        return latest_region is not None and latest_region != region

class SmsSender(Observer):
    def update(self, observable, object):
        print('[Message] ' + 'Hello {}, '.format(object['name']) + 'abnormal log-in activity detected')
        print('Recent log-in region: {}'.format(object['region']))
        print('IP: {}'.format(object['ip']))
        print('Login time: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(object['time']))))

class MailSender(Observer):
    def update(self, observable, object):
        print('[Mail] ' + 'Hello {}, '.format(object['name']) + 'abnormal log-in activity detected')
        print('Recent log-in region: {}'.format(object['region']))
        print('IP: {}'.format(object['ip']))
        print('Login time: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(object['time']))))

def test_login():
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(MailSender())
    account.login('Tony', '101.47.18.9', time.time())
    account.login('Tony', '67.218.147.69', time.time())


if __name__ == '__main__':
    test_login()
