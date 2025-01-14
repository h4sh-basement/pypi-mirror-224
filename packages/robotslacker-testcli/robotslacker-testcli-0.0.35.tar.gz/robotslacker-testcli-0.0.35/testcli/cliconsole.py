# -*- coding: utf-8 -*-
import os
import sys
import traceback
import click
import pytest
import platform
import signal
from .__init__ import __version__
from .testcli import TestCli
from .testcliexception import TestCliException


# 信号处理程序
def abortSignalHandler(signum, frame):
    click.secho("Got signal [" + str(signum) + "]. Quit application.", err=True, fg="red")
    if frame:
        pass
    # 直接退出
    sys.exit(255)


@click.command()
@click.option("--version", is_flag=True, help="Show TestCli version.")
@click.option("--logon", type=str, help="SQL logon user name and password. user/pass",)
@click.option("--logfile", type=str, help="Log every command and its results to file.",)
@click.option("--execute", type=str, help="Execute command script.")
@click.option("--commandmap", type=str, help="Command mapping file.")
@click.option("--nologo", is_flag=True, help="Execute with no-logo mode.")
@click.option("--xlog", type=str, help="Save command extended log.")
@click.option("--xlogoverwrite", is_flag=True, help="Overwrite extended log if old file exists. Default is false.")
@click.option("--clientcharset", type=str, help="Set client charset. Default is UTF-8.")
@click.option("--resultcharset", type=str, help="Set result charset. Default is same to clientCharset.")
@click.option("--profile", type=str, help="Startup profile. Default is none.")
@click.option("--scripttimeout", type=int, help="Script timeout(seconds). Default is -1, means no limit.")
@click.option("--namespace", type=str, help="Command default name space(SQL|API). Default is depend on file suffix.")
@click.option("--selftest", is_flag=True, help="Run self test and exit.")
@click.option("--suitename", type=str, help="Test suite name.")
@click.option("--casename", type=str, help="Test case name.")
@click.option("--silent", is_flag=True, help="Run script in silent mode, no console output. Default is false.")
@click.option("--daemon", is_flag=True, help="Run script in daemon mode. Default is false.")
@click.option("--pidfile", type=str, help="Set pid file path and filename. Default is no pid control.")
@click.option("--debug", is_flag=True, help="Run in debug mode. Default is False.")
def cli(
        version,
        logon,
        logfile,
        execute,
        commandmap,
        nologo,
        xlog,
        xlogoverwrite,
        clientcharset,
        resultcharset,
        profile,
        scripttimeout,
        namespace,
        selftest,
        suitename,
        casename,
        silent,
        daemon,
        pidfile,
        debug
):
    # 程序的返回值，默认是0
    appExitValue = 0

    # 捕捉信号，处理服务中断的情况
    if platform.system().upper() in ["LINUX", "DARWIN"]:
        # 通信管道中断，不处理中断信息，放弃后续数据
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
        # 被操作系统KILL
        signal.signal(signal.SIGTERM, abortSignalHandler)

    # 如果没有标准输出和标准错误输出，则不输出。不报错
    if not sys.stdout.isatty():
        sys.stdout = open(os.devnull, mode="w")
    if not sys.stderr.isatty():
        sys.stderr = open(os.devnull, mode="w")

    try:
        # 如果需要运行在Daemon模式，则直接运行到后台
        if daemon:
            if platform.system().upper() in ["LINUX", "DARWIN"]:
                # fork子进程
                currentPwd = os.getcwd()
                try:
                    pid = os.fork()
                    if pid > 0:
                        # 关闭输入输出，抑制dameon系统回调的屏幕显示
                        with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
                            os.dup2(read_null.fileno(), sys.stdin.fileno())
                            os.dup2(write_null.fileno(), sys.stdout.fileno())
                            os.dup2(write_null.fileno(), sys.stderr.fileno())
                        sys.exit(0)
                except OSError as oe:
                    click.secho(repr(oe), err=True, fg="red")
                    sys.exit(255)

                # 修改子进程工作目录
                os.chdir(currentPwd)
                os.setsid()
                os.umask(0)

                # 创建孙子进程，而后子进程退出
                try:
                    pid = os.fork()
                    if pid > 0:
                        # 关闭输入输出，抑制dameon系统回调的屏幕显示
                        with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
                            os.dup2(read_null.fileno(), sys.stdin.fileno())
                            os.dup2(write_null.fileno(), sys.stdout.fileno())
                            os.dup2(write_null.fileno(), sys.stderr.fileno())
                        sys.exit(0)
                except OSError as oe:
                    click.secho(repr(oe), err=True, fg="red")
                    sys.exit(255)

                # 不再保留当前终端的文件描述符
                sys.stdout.flush()
                sys.stderr.flush()
                with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
                    os.dup2(read_null.fileno(), sys.stdin.fileno())
                    os.dup2(write_null.fileno(), sys.stdout.fileno())
                    os.dup2(write_null.fileno(), sys.stderr.fileno())
            else:
                # 非Linux平台不支持daemon模式运行, 即使设置了Daemon参数，也会忽略
                click.secho(
                    "[WARN] Current platform [" + platform.system().upper() + "] does not support daemon mode.",
                    fg="yellow")
                pass

        # 打印版本信息
        if version:
            click.secho("Version: " + __version__)
            return

        # 程序处于调试状态
        if debug:
            os.environ["TESTCLI_DEBUG"] = "1"

        # 程序自检
        if selftest:
            testpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "test", "testcliunittest.py"))
            pytest.main(
                args=[
                    "-vs",
                    testpath,
                ],
            )
            return

        # 程序脚本超时时间设置
        if not scripttimeout:
            scripttimeout = -1

        # 如果需要的话，写入PID文件
        if pidfile:
            try:
                with open(file=pidfile, mode="w") as fp:
                    fp.write(str(os.getpid()))
            except OSError as oe:
                click.secho(
                    "pid file [" + pidfile + "] create failed." + repr(oe),
                    err=True,
                    fg="red"
                )
                sys.exit(1)

        # 运行主程序
        appHandler = TestCli(
            logfilename=logfile,
            logon=logon,
            script=execute,
            commandMap=commandmap,
            nologo=nologo,
            xlog=xlog,
            xlogoverwrite=xlogoverwrite,
            clientCharset=clientcharset,
            resultCharset=resultcharset,
            profile=profile,
            scripttimeout=scripttimeout,
            namespace=namespace,
            suitename=suitename,
            casename=casename,
            headlessMode=silent
        )

        # 运行主程序
        appExitValue = appHandler.run_cli()
    except SystemExit as se:
        click.secho(repr(se), err=True, fg="red")
        sys.exit(int(appExitValue))
    except TestCliException as se:
        click.secho(se.message, err=True, fg="red")
        sys.exit(255)
    except Exception as ge:
        if "TESTCLI_DEBUG" in os.environ:
            print('traceback.print_exc():\n%s' % traceback.print_exc())
            print('traceback.format_exc():\n%s' % traceback.format_exc())
        click.secho(repr(ge), err=True, fg="red")
        sys.exit(255)


# 主程序
if __name__ == "__main__":
    cli()
