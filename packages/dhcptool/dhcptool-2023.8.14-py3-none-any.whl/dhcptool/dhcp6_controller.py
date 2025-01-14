# -*- coding: utf-8 -*-
# @Time    : 2022/10/23 19:06
# @Author  : mf.liang
# @File    : dhcp6_controller.py
# @Software: PyCharm
# @desc    :
from queue import Empty
from scapy.layers.dhcp6 import dhcp6types
from dhcptool.dhcp_pkt import Dhcp6Pkt
from dhcptool.env_args import summary_result, logs, pkt_result, global_var
from dhcptool.tools import Tools


class Dhcp6Controller(Dhcp6Pkt):

    def __init__(self, args):
        super(Dhcp6Controller, self).__init__(args)
        self.args = args

    def run(self):
        """
        执行 发包测试入口
        :return:
        """
        for i in dhcp6types.values():
            summary_result[i] = 0
        for i in range(int(self.args.num)):
            global_var['tag'] = i
            try:
                send_pkts = {
                    self.args.renew: self.send_renew if self.args.single
                    else self.send_solicit_advertise_request_reply_renew,

                    self.args.release: self.send_release if self.args.single
                    else self.send_solicit_advertise_request_reply_release,

                    self.args.decline: self.send_decline if self.args.single
                    else self.send_solicit_advertise_request_reply_decline,

                    self.args.solicit: self.send_solicit,
                }
                send_pkts.get(True, self.send_solicit_advertise_request_reply)()
            except Empty as ex:
                logs.info('没有接收到返回包！')
            except AssertionError as ex:
                logs.info('返回包未包含分配ip！')
            print('-' * 60)
            pkt_result.get('dhcp6_reply').queue.clear()
        str_summary_result = str(summary_result).replace('{', '').replace('}', '').replace("'", '')
        logs.info(str_summary_result)

    def send_solicit_advertise_request_reply(self):
        """
        发送  dhcp6 完整分配流程
        :return:
        """
        self.__init__(self.args)
        solicit_pkt = self.dhcp6_solicit()
        res = self.send_dhcp6_pkt(solicit_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)
        request_pkt = self.dhcp6_request()
        res = self.send_dhcp6_pkt(request_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_solicit_advertise_request_reply_renew(self):
        """
        分配完地址后进行 更新租约
        :return:
        """
        self.send_solicit_advertise_request_reply()
        renew_pkt = self.dhcp6_renew()
        Tools.rate_print('租约更新', self.args.sleep_time)
        res = self.send_dhcp6_pkt(renew_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_solicit_advertise_request_reply_release(self):
        """
        分配完地址后进行 释放地址
        :return:
        """
        self.send_solicit_advertise_request_reply()
        release_pkt = self.dhcp6_release()
        Tools.rate_print('租约释放', self.args.sleep_time)
        res = self.send_dhcp6_pkt(release_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_solicit_advertise_request_reply_decline(self):
        """
        分配完地址后进行 释放地址
        :return:
        """
        self.send_solicit_advertise_request_reply()
        decline_pkt = self.dhcp6_decline()
        Tools.rate_print('模拟冲突', self.args.sleep_time)
        res = self.send_dhcp6_pkt(decline_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_solicit(self):
        """
        单独的solicit包
        :return:
        """
        discover_pkt = self.dhcp6_solicit()
        res = self.send_dhcp6_pkt(discover_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_renew(self):
        """
        单独的renew包
        :return:
        """
        renew_pkt = self.dhcp6_renew()
        res = self.send_dhcp6_pkt(renew_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_decline(self):
        """
        单独的decline包
        :return:
        """
        decline_pkt = self.dhcp6_decline()
        res = self.send_dhcp6_pkt(decline_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_release(self):
        """
        单独的release包
        :return:
        """
        release_pkt = self.dhcp6_release()
        res = self.send_dhcp6_pkt(release_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

