#!/usr/bin/env  python
# -*- coding:utf-8 -*-

# @Create_time     :2020/8/9 21:42
# @Author          :wuweihong6
# @e-mail          :1454565178@qq.com
# @File            :git_multisite.py
# @software        :PyCharm
# @description     :

from collections import namedtuple

GIT_MULTISITE_VER = "V1.3.1 build "
GIT_MULTISITE_DEF_SRV_PORT = 1988
GIT_MULTISITE_LISTEN_QU_LEN = 8
GIT_MULTISITE_LOCK = "GIT_multisite.lock"
GIT_MULTISITE_LOG_PATH = "/var/log/GIT_multisite"
GIT_MULTISITE_YNC_LOCK_TIME_OUT = 36000
GIT_MULTISITE_TXN_TIMEOUT = 1200
TIMEOUT = 60  # 设置超时时间为30秒
GIT_MULTISITE_LINE_END = "\r\n"
GIT_MULTISITE_VER = "V1.3.1 build"
CMFTPD_DB_NAME = "GITadmin"

GIT_MULTISITE_OK = 0
GIT_MULTISITE_ERR = -1
GIT_MULTISITE_YNC_ERR = 1

LOCKFILE_NET = "/var/run/git_multisite_net.pid"
LOCKFILE_MONITOR = "/var/run/git_multisite_monitor.pid"
LOCKFILE_REPAIR = "/var/run/git_multisite_repair.pid"

# TCP socket options 
TCP_NODELAY = 1       # Turn off Nagle's algorithm. 
TCP_MAXSEG = 2       # Limit MSS 
TCP_CORK = 3       # Never send partially complete segments 
TCP_KEEPIDLE = 4       # Start keeplives after this period 
TCP_KEEPINTVL = 5       # Interval between keepalives 
TCP_KEEPCNT = 6       # Number of keepalives before death 
TCP_SYNCNT = 7       # Number of SYN retransmits 
TCP_LINGER2 = 8       # Life time of orphaned FIN-WAIT-2 state 
TCP_DEFER_ACCEPT = 9       # Wake up listener only when data arrive 
TCP_WINDOW_CLAMP = 10      # Bound advertised window 
TCP_INFO = 11      # Information about this connection. 
TCP_QUICKACK = 12      # Block/reenable quick acks 
TCP_CONGESTION = 13      # Congestion control algorithm 
TCP_MD5SIG = 14      # TCP MD5 Signature (RFC2385) 
TCP_THIN_LINEAR_TIMEOUTS = 16      # Use linear timeouts for thin streams
TCP_THIN_DUPACK = 17      # Fast retrans. after 1 dupack

REPOS_YNC = 1
LISTEN_MODE = 2
REPOS_CHECK = 3
REPOS_SET_LOCK = 4
MULTISITE_MOD = 5
MULTISITE_STOP = 6

mysql_connection = namedtuple('mysql_connection', "host user passwd port")
git_multisite_connection = mysql_connection("10.1.24.56", "root", "hikvision@1", 3306)


class CmftpdUser:
    source_repos_id = 0
    target_repos_id = 0
    repos_path = ""
    branch = "master"
    repos_workspace = ""
    version = "0" * 40
    err = 0


class ReposInfo:
    repos_id = 0
    version = "0" * 40
    multisite_id = 0
    ismaster = 0
    repos_current = ""


repos_id_pool = {}


#  local functions
def git_multisite_do_port():
    pass


def git_multisite_do_pasv():
    pass


def git_multisite_do_stor():
    pass


def git_multisite_do_quit():
    pass


def git_multisite_do_sync():
    pass


def git_multisite_do_gotoync():
    pass


def git_multisite_do_rev_done():
    pass


def git_multisite_do_yncdata_transfer():
    pass


def git_multisite_do_yncdata():
    pass


def git_multisite_get_keyword():
    pass


def git_multisite_send_set_rev_retry():
    pass


def git_multisite_do_set_rev_retry():
    pass


def git_multisite_send_local_control():
    pass


def git_multisite_set_uid():
    pass


# global variables
git_multisite_debug_on = 0
git_multisite_srv_port = GIT_MULTISITE_DEF_SRV_PORT
git_multisite_quit_flag = 0
git_multisite_safe_mode = 0
git_multisite_pasv_fd = None
git_multisite_pasv_connfd = None
git_multisite_port_connfd = None
client_ip = ""
server_ip = ""
repos_name = ""
multisite_name = ""
mod_type = ""
exec_user = ""
work_sign = 0
rev_no = "0" * 40
client_sign = ""


git_multisite_cmds = {
        "PORT": git_multisite_do_port,
        "PASV": git_multisite_do_pasv,
        "STOR": git_multisite_do_stor,
        "QUIT": git_multisite_do_quit,
        "SYNC": git_multisite_do_sync,
        "GYNC": git_multisite_do_gotoync,
        "SREV": git_multisite_do_set_rev_retry,
        "DONE": git_multisite_do_rev_done,
}

git_multisite_srv_resps = {
        "150 Begin transfer{}".format(GIT_MULTISITE_LINE_END),
        "200 OK{}".format(GIT_MULTISITE_LINE_END),
        "213 %d{}".format(GIT_MULTISITE_LINE_END),
        "215 UNIX Type: L8{}".format(GIT_MULTISITE_LINE_END),
        "220 git_multisite " + GIT_MULTISITE_VER + " server{}".format(GIT_MULTISITE_LINE_END),
        "221 Goodbye{}".format(GIT_MULTISITE_LINE_END),
        "226 Transfer complete{}".format(GIT_MULTISITE_LINE_END),
        "227 Entering Passive Mode (%d,%d,%d,%d,%d,%d){}".format(GIT_MULTISITE_LINE_END),
        "230 User %s logged in{}".format(GIT_MULTISITE_LINE_END),
        "272 Error :  %s %s %s{}".format(GIT_MULTISITE_LINE_END),
        "405 Wrong version {}".format(GIT_MULTISITE_LINE_END),
        "500 Unsupport command %s{}".format(GIT_MULTISITE_LINE_END),
        "505 MD5 check failed {}".format(GIT_MULTISITE_LINE_END),
        "506 Access denied {}".format(GIT_MULTISITE_LINE_END),
        "530 Login %s{}".format(GIT_MULTISITE_LINE_END),
        "531 Error : %s %s %s{}".format(GIT_MULTISITE_LINE_END),
        "532 ync %s{}".format(GIT_MULTISITE_LINE_END),
        "550 Error{}".format(GIT_MULTISITE_LINE_END),
}


def git_multisite_usage():
    print("\nGIT Multisite " + GIT_MULTISITE_VER + " usage:\n")
    help_information = """
    \n\
    1、后台监听模式\n\
       -l \n\
       -w  服务器容易断电的区域建议使用该参数，确保所有缓存数据已经写入磁盘\n\
       说明:后台监听将启动2个进程:socket监听定时版本检查. \n\
       \n\
    2、版本提交前建锁(传输锁)\n\
       -c \n\
       -p  需要建立锁的版本库名称\n\
       说明:传输锁为pre-commit末段执行。Return:0 success 1 failed -1 error.\n\
       \n\
    3、版本提交后建锁(提交锁)\n\
       -s \n\
       -p  需要建立锁的版本库名称\n\
       -r  完成提交的版本号\n\
       说明:提交锁为post-commit首段执行。Return:0 success 1 failed -1 error. \n\
       \n\
    4、版本同步\n\
       -y \n\
       -p  同步的版本库名称\n\
       -r  同步的版本号\n\
       说明:同步为完成提交锁后执行。slave => master master => slave. \n\
       \n\
    5、修改Mulitiste关系(管理员功能)\n\
       -m \n\
       -n  Multisite名称\n\
       -p  待修改的版本库名称\n\
       -r  修改的版本库的版本号(该参数仅在mod下有效)\n\
       -a  操作方法:create(创建)、add(加入组)、master(设置master)、del(删除)、mod(修改版本).\n\
       说明:需先创建multisite(名称需唯一)，非master可以可设置master和解除同步关系 \n\
       \n\
    6、其他说明 \n\
       -q  退出操作，关闭Multisite的监听进程\n\
       \n\
    """
    print(help_information)


def git_multisite_parse_args():
    err = 0
    global git_multisite_debug_on
    global svn_multisite_safe_mode
    global server_ip
    global mod_type
    global repos_name
    global multisite_name
    global rev_no
    global work_sign
    global exec_user
    #  todo 解析参数


def already_running(filename):
    # todo 定义锁文件操作
    pass


def svn_multisite_setsockopt(socket_obj):
    # todo 定义套接字的属性
    pass


def svn_multisite_debug():
    # todo 定义日志函数
    pass


def svn_multisite_sigchild():
    # todo 定义主进程回收僵尸进程
    pass


def svn_multisite_do_get_command():
    # todo
    pass


def svn_multisite_init():
    # 程序初始化
    pass


def svn_multisite_create_srv():
    #  todo 创建服务端监听套接字
    pass


def svn_multisite_srv_resp_num2msg():
    # todo
    pass


def svn_multisite_send_msg(socket_obj, msg):
    # todo 定义发送信息函数
    pass


def svn_multisite_recv_msg(socket_obj):
    # todo 定义接受消息函数
    pass


def svn_multisite_send_resp(socket_obj, num):
    pass


def svn_multisite_get_connfd():
    pass


def svn_multisite_close_all_fd():
    pass


def svn_multisite_do_request():
    pass


def svn_multisite_ctrl_conn_handler():
    pass


def svn_multisite_do_loop():
    pass


def svn_multisite_get_recv(socket_obj):
    pass


def svn_multisite_get_md5sum(socket_obj):
    pass


def svn_multisite_check_repos_ync_done(socket_obj):
    pass


def svn_multisite_ctrl_ync_conn():
    pass


def svn_multisite_get_repos_info():
    # todo 获取接收到的数据信息
    pass


def svn_multisite_repair_monitor():
    # 主动修复进程，用于判断一些情况下hooks异常，导致版本库更新后，数据库没有更新的情况
    # 这种修复一般在自动监控或者写入锁校验失败的情况下介入
    pass


def svn_multisite_version_check_monitor():
    # 监控进程，用于判断是否有版本库没有完成同步，如果出现没有完成同步的，启动同步进程
    # 同步的模式为主动推送，即我的版本高于其他，我主动推动给其他对象
    pass


def svn_multisite_set_uid(username):
    # 设置程序运行的uid
    pass


def main():
    pass


if __name__=="__main__":
    main()
