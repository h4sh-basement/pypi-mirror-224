#!/usr/bin/python
"""
@Author  :  Lijiawei
@Date    :  8/24/2021 1:35 PM
@Desc    :  Scaffold Generator.
"""
import os
import platform
import sys

from loguru import logger

from utx.core.utils.tools import decryption


class ExtraArgument:
    create_venv = False


def init_parser_install(parsers):
    install_parser = parsers.add_parser(
        "install", help="install iOS app (.ipa) from filepath_or_url."
    )
    install_parser.add_argument(
        "filepath_or_url", type=str, nargs="?", help="local filepath or url."
    )

    return install_parser


def creat_install(filepath_or_url):
    if filepath_or_url is None:
        logger.error(
            "UTX install: error: the following arguments are required: filepath_or_url"
        )
        return 1
    elif filepath_or_url.endswith(".ipa"):
        os.system("{} install {}".format(decryption(b"dGlkZXZpY2U="), filepath_or_url))
    elif filepath_or_url.startswith("http"):
        os.system("{} install {}".format(decryption(b"dGlkZXZpY2U="), filepath_or_url))
    else:
        logger.error(
            "UTX install: error: the following arguments are required: filepath_or_url"
        )
        return 1


def main_install(args):
    sys.exit(creat_install(args.filepath_or_url))


def init_parser_uninstall(parsers):
    uninstall_parser = parsers.add_parser(
        "uninstall", help="uninstall iOS app (.ipa) from bundle_id."
    )
    uninstall_parser.add_argument(
        "bundle_id", type=str, nargs="?", help="bundle_id of application."
    )

    return uninstall_parser


def creat_uninstall(bundle_id):
    if bundle_id is None:
        logger.error(
            "UTX uninstall: error: the following arguments are required: bundle_id"
        )
        return 1
    elif bundle_id.replace(".", "").isalnum():
        os.system("{} uninstall {}".format(decryption(b"dGlkZXZpY2U="), bundle_id))
    else:
        logger.error(
            "UTX uninstall: error: the following arguments are required: bundle_id"
        )
        return 1


def main_uninstall(args):
    sys.exit(creat_uninstall(args.bundle_id))


def init_parser_scaffold(subparsers):
    sub_parser_scaffold = subparsers.add_parser(
        "startproject", help="create a new app project with template structure."
    )
    sub_parser_scaffold.add_argument(
        "project_name", type=str, nargs="?", help="Specify new project name."
    )
    sub_parser_scaffold.add_argument(
        "-venv",
        dest="create_venv",
        action="store_true",
        help="create virtual environment in the project, and install utx.",
    )
    return sub_parser_scaffold


def create_scaffold(project_name):
    """Create scaffold with specified project name."""
    if os.path.isdir(project_name):
        logger.warning(
            f"Project folder {project_name} exists, please specify a new project name."
        )
        return 1
    elif os.path.isfile(project_name):
        logger.warning(
            f"Project name {project_name} conflicts with existed file, please specify a new one."
        )
        return 1

    logger.info(f"Create new project: {project_name}")
    print(f"Project root dir: {os.path.join(os.getcwd(), project_name)}\n")

    def create_folder(path):
        os.makedirs(path)
        msg = f"Created folder: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"Created file: {path}"
        print(msg)

    create_folder(project_name)
    create_folder(os.path.join(project_name, "config"))
    create_folder(os.path.join(project_name, "logs"))
    create_folder(os.path.join(project_name, "packages"))
    create_folder(os.path.join(project_name, "report/airtest"))
    create_folder(os.path.join(project_name, "tests"))
    create_folder(os.path.join(project_name, "suites"))

    content = """venv
.idea/
.pytest_cache
*/*__pycache__/
report
debug
*.pyc
"""
    create_file(os.path.join(project_name, ".gitignore"), content)

    content = """# UTX
![PyPI](https://img.shields.io/pypi/v/utx) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/utx) [![Downloads](https://static.pepy.tech/personalized-badge/utx?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads/total)](https://pepy.tech/project/utx) ![GitHub top language](https://img.shields.io/github/languages/top/openutx/utx) ![GitHub stars](https://img.shields.io/github/stars/openutx/utx?style=social) ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange)

## logo
![](https://cdn.jsdelivr.net/gh/openutx/static/image/utx.png)
## 安装
- 命令行执行
```
pip install -U utx
```


## 设计理念

很大程度上借鉴了HttpRunner（优秀的框架）。不同的是，utx更着重写python，而不是写yaml文件。

- 简单是更好的
- 每个人都能用python写自动化
- UI自动化跟的上冲刺迭代和UI变更


这就是utx的设计理念。


## 项目结构
![](https://cdn.jsdelivr.net/gh/openutx/static/image/jg.png)

- utx提供了快速创建项目的能力，也就是脚手架。
- 【app脚手架】
```shell
utx startproject project_name
```
- 【web脚手架】
```shell
utx startproject-web project_name
```
```text
$ utx startproject demo
2021-09-01 12:39:16.491 | INFO     | utx.cli.scaffold:create_scaffold:51 - Create new project: demo
Project root dir: /PycharmProjects/demo

Created folder: demo
Created folder: demo/config
Created folder: demo/logs
Created folder: demo/packages
Created folder: demo/report/airtest
Created folder: demo/tests
Created folder: demo/suites
Created file: demo/.gitignore
Created file: demo/conftest.py
Created file: demo/pytest.ini
Created file: demo/run.py
Created file: demo/requirements.txt
Created file: demo/config/conf.py
Created file: demo/config/config.ini
Created file: demo/config/__init__.py
Created file: demo/tests/test_devices.py
Created file: demo/tests/__init__.py
Created file: demo/report/summary_template.html

```
## 调用流程图

![](https://cdn.jsdelivr.net/gh/openutx/static/image/lc.png)


## 专注于写脚本

- 项目结构很清晰。在conftest.py进行一些初始化/参数化/清理工作，在suites/写测试脚本。
>在AirtestIDE中写好.air脚本，然后将文件放到suites文件中。
- 更注重平铺写脚本的方式，这样就离“每个人都能用python写自动化”更近一步。毕竟封装之后看着容易晕，我也晕。
- 去除掉框架的约束，给每个人写python的自由，在测试脚本里你可以尽情发挥你的代码风格，代码能力，千人千面。代价呢，就是代码质量参差不齐。

大胆写，能写，写出来，跑通，就已经是在写自动化，就已经是在创造价值了！


## 轻封装

utx尊重原生用法。

airtest的封装只通过装饰器进行了运行方式的调整，没有做任何其他的冗余修改。

- faker，造数据工具
- pytest，测试框架
- airtest，自动化测试工具
- tidevice，iOS设备管理工具
- pandas、numpy，数据处理工具

安装utx，自动就把这些开源利器安装上了，无需单独安装。未来会集成更多实用工具到utx中。

utx本身是很轻的。

## 核心价值

- 上手 0 门槛，iOS/Android 设备均实现即插即用，随写随调
- 测试用例可读性高，编写成本低，支持python语法，便于公共操作抽象，进一步提高用例可维护性
- 用例执行高鲁棒性，多设备机型切换无需更改用例适配
- 执行集创建简单，支持智能并发、分组单模块执行，更高效更灵活

## 功能介绍

1. 支持android,ios,web 平台的自动化测试框架
2. 脚本批量执行
3. 每个脚本执行日志分开存放
4. 每个脚本单独生成一个html报告并在父文件夹生成一个聚合报告
5. 自定义的聚合报告，详细展示运行结果
6. 重试机制，运行失败自动重跑，可自定义重跑次数
7. 自定义脚本运行，可选择部分模块单独运行
8. 自带脚手架工具可以快速生成框架目录


## app使用说明

- 只需在配置文件中填好相关内容，即可运行！
```ini
[device_info]
;设备远程链接URL 设备ip+端口或者设备唯一标识id，多个设备以,分割；例如 设备1,设备2,设备3
device = 127.0.0.1:5555
;设备平台iOS或者Android
platform = android
;ios设备驱动包名，仅测试iOS时需要
wda = com.facebook.WebDriverAgentRunner.utx.xctrunner
;是否执行安装卸载操作 True/False
init = False

[app_info]
;app包名
package = com.wx.mp.test
;apk或者ipa文件名
filename = app_test.apk

[reruns]
;失败后再次运行次数，默认1次
times = 1

[paths]
;自定义执行case目录层级，文件夹名称（例如：smoke），默认为空
name = 

[mode]
;False 表示 运行[suites][cases]选择的用例，True表示运行全部用例
is_all = True
;是否录制视频 True/False
record = False

[suites]
;填写用例的关键字
cases = test.air
```

- app启动命令
1. 普通启动
```shell
python run.py
```
2. 参数化启动
```shell
# Android
python run.py --platform=Android --device=127.0.0.1:5555 --init=True
# iOS
python run.py --platform=iOS --wda=com.facebook.WebDriverAgentRunner.utx.xctrunner --init=True
```
>参数优先级大于配置文件
> >多个设备以,分割; 例如 python run.py --platform=Android --device=设备1,设备2,设备3 --init=True

## web使用说明

- 下载好chrome浏览器对应的驱动，放到driver文件夹中
> 注意：文件名规范 【Linux/Mac：chromedriver】【Windows：chromedriver.exe】
- 只需在配置文件中填好相关内容，即可运行！
```ini
[web_info]
;被测的主页url
url = https://www.baidu.com/
;是否无界面运行
headless = False

[reruns]
;失败后再次运行次数，默认1次
times = 1

[paths]
;自定义执行case目录层级，文件夹名称（例如：smoke），默认为空
name = 

[mode]
;False 表示 运行[suites][cases]选择的用例，True表示运行全部用例
is_all = True
;是否录制视频 True/False
record = False

[suites]
;填写用例的关键字
cases = chrome

```

- web启动命令
1. 普通启动
```shell
python run.py
```
2. 参数化启动
```shell
python run.py --headless=True --driver=/Users/admin/driverpath
```
>参数优先级大于配置文件

## 运行结果
- 报告展示

![](https://cdn.jsdelivr.net/gh/openutx/static/image/bg.png)

"""

    create_file(os.path.join(project_name, "README.md"), content)

    content = """#!/usr/bin/python
# encoding=utf-8

\"\"\" Can only be modified by the administrator. Only fixtures are provided.
\"\"\"

import pytest

from logging import getLogger
from airtest.core.helper import ST
from utx.core.utils.hook import app_fixture, app_info
from config.conf import *
from run import cli_device, cli_platform, cli_wda, cli_init

logger = getLogger(__name__)
logger.info("Get PROJECT_ROOT: {}".format(ST.PROJECT_ROOT))
app_filepath = PACKAGES_PATH + '/' + ini.getvalue('app_info', 'filename')
app_name = ini.getvalue('app_info', 'package')

device_uri, device_idx, is_init = app_info(cli_platform=cli_platform, cli_device=cli_device, cli_wda=cli_wda,
                                           cli_init=cli_init,
                                           ini_platform=ini.getvalue('device_info', 'platform'),
                                           ini_device=ini.getvalue('device_info', 'device'),
                                           ini_wda=ini.getvalue('device_info', 'wda'),
                                           ini_init=ini.getvalue('device_info', 'init'))


@pytest.fixture(scope="session", autouse=True)
def app_init(request):
    app_fixture(request, device_uri=device_uri, app_filepath=app_filepath, app_name=app_name, device_idx=device_idx,
                init=is_init)
"""
    create_file(os.path.join(project_name, "conftest.py"), content)

    content = """[pytest]
xfail_strict=true
log_cli=true
log_cli_level=INFO
log_format = %(asctime)s [%(levelname)-5s] %(name)s %(funcName)s : %(message)s
log_date_format = %Y-%m-%d %H:%M:%S

# show all extra test summary info
addopts = -ra
testpaths = tests
python_files = test_devices.py
"""
    create_file(os.path.join(project_name, "pytest.ini"), content)

    content = """#!/usr/bin/python
# encoding=utf-8
\"\"\" Can only be modified by the administrator. Only Runner are provided.
\"\"\"
import os
import pytest
from utx.cli.cli import cli_env

from config.conf import ALLURE_REPORT_PATH
from utx.core.utils.tools import allure_report

cli_device, cli_platform, cli_wda, cli_init = cli_env()

if __name__ == '__main__':
    report_path = ALLURE_REPORT_PATH + os.sep + "result"
    report_html_path = ALLURE_REPORT_PATH + os.sep + "html"
    pytest.main(["-s", "--alluredir", report_path, "--clean-alluredir"])
    allure_report(report_path, report_html_path)
"""

    create_file(os.path.join(project_name, "run.py"), content)

    content = """# Customize third-parties
# pip install --default-timeout=6000 -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
utx
"""
    create_file(os.path.join(project_name, "requirements.txt"), content)

    content = """#!/usr/bin/python
# encoding=utf-8
\"\"\" Can only be modified by the administrator. Only Path are provided.
\"\"\"
import os

# 项目目录
from utx.core.utils.tools import ReadConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

ini = ReadConfig(INI_PATH)

# 测试用例目录
CASE_PATH = os.path.join(BASE_DIR, 'suites', ini.getvalue('paths', 'name'))
if not os.path.exists(CASE_PATH):
    os.mkdir(CASE_PATH)
# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
# 安装包目录
PACKAGES_PATH = os.path.join(BASE_DIR, 'packages')
if not os.path.exists(PACKAGES_PATH):
    os.mkdir(PACKAGES_PATH)
# allure报告目录
ALLURE_REPORT_PATH = os.path.join(BASE_DIR, 'report')
if not os.path.exists(ALLURE_REPORT_PATH):
    os.mkdir(ALLURE_REPORT_PATH)

# airtest报告目录
AIRTEST_REPORT_PATH = os.path.join(BASE_DIR, 'report', 'airtest')
if not os.path.exists(AIRTEST_REPORT_PATH):
    os.mkdir(AIRTEST_REPORT_PATH)

if __name__ == '__main__':
    print(ini.getvalue('app_info', 'package'))
"""

    create_file(os.path.join(project_name, "config", "conf.py"), content)

    content = """[device_info]
;设备远程链接URL 设备ip+端口或者设备唯一标识id
device = 127.0.0.1:5555
;设备平台iOS或者Android
platform = android
;ios设备驱动包名，仅测试iOS时需要
wda = com.facebook.WebDriverAgentRunner.utx.xctrunner
;是否执行安装卸载操作 True/False
init = True

[app_info]
;app包名
package = com.wx.mp.test
;apk或者ipa文件名
filename = app_test.apk

[reruns]
;失败后再次运行次数，默认1次
times = 1

[paths]
;自定义执行case目录层级，文件夹名称（例如：smoke），默认为空
name = 

[mode]
;False 表示 运行[suites][cases]选择的用例，True表示运行全部用例
is_all = True
;是否录制视频 True/False
record = False

[suites]
;填写用例的关键字
cases = test.air
"""
    create_file(os.path.join(project_name, "config", "config.ini"), content)
    create_file(os.path.join(project_name, "config", "__init__.py"))

    content = """#!/usr/bin/python
# encoding=utf-8
\"\"\" Can only be modified by the administrator. Only Cases are provided.
\"\"\"

import allure
import pytest
from utx.core.css.custom_report import gen_report
from utx.core.utils.tools import decryption, selector_v2, str_to_bool

from config.conf import *
from conftest import device_uri
from utx.core.utils.runner import run_air

device_address = device_uri
results = []
result_list = []

status = str_to_bool(ini.getvalue('mode', 'is_all'))
record = str_to_bool(ini.getvalue('mode', 'record'))
flag = ini.getvalue('suites', 'cases')
app_name = ini.getvalue('app_info', 'package')
times = int(ini.getvalue('reruns', 'times'))
cases = selector_v2(path=CASE_PATH, status=status, mark=flag)


@allure.feature("APP automation test")
class TestApp:
    @pytest.mark.flaky(reruns=times)
    @pytest.mark.parametrize("url", device_address)
    @pytest.mark.parametrize("case", cases)
    @allure.story("APP automation test")
    @allure.title("Current device:{url},Running case:{case}")
    @allure.description("APP automation test")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("Smoke testing")
    def test_ui_app(self, url, case):
        device_url = url
        result, dev = run_air(devices=device_url, case=case, app_name=app_name, log_path=LOG_PATH, case_path=CASE_PATH,
                              base_dir=BASE_DIR, record=record,
                              static_dir=decryption('aHR0cHM6Ly9mYXN0bHkuanNkZWxpdnIubmV0L2doL29wZW51dHgvc3RhdGljLw=='))
        result_list.append(result)
        summary_info = {'devices': dev, 'result': result_list}
        results.append(summary_info)
        assert result['result'] is True

    @allure.story("APP automation test")
    @allure.title("Generate test report of running device")
    @allure.description("APP automation test")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("Generate report")
    def test_report(self):
        gen_report(results=results, report_path=AIRTEST_REPORT_PATH)


if __name__ == "__main__":
    pytest.main(["-s", "test_devices.py"])
"""

    create_file(os.path.join(project_name, "tests", "test_devices.py"), content)
    create_file(os.path.join(project_name, "tests", "__init__.py"))

    if ExtraArgument.create_venv:
        os.chdir(project_name)
        print("\nCreating virtual environment")
        os.system("python -m venv venv")
        print("Created virtual environment: venv")

        print("Installing utx")
        if platform.system().lower() == "windows":
            os.chdir("venv")
            os.chdir("Scripts")
            os.system("pip install utx")
        elif platform.system().lower() == "linux":
            os.chdir("venv")
            os.chdir("bin")
            os.system("pip install utx")
        elif platform.system().lower() == "darwin":
            os.chdir("venv")
            os.chdir("bin")
            os.system("pip install utx")


def main_scaffold(args):
    ExtraArgument.create_venv = args.create_venv
    sys.exit(create_scaffold(args.project_name))
