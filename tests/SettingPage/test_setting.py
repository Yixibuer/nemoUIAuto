import pytest
import uiautomator2 as u2
from data.cfg import udid
from logs.my_logger import MyLog
from data.cfg import ENV, username183, password183
import allure

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC3011")
@allure.feature('设置')
@allure.story('验证立即加群')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_enter_group_one(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(text="我的").click()

    with allure.step('点击"设置"图标'):
        logger.info('点击"设置"图标')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    # 检查是否已进入设置页面：验证页面上出现“设置”
    with allure.step('验证是否进入设置页面'):
        logger.info('验证是否进入设置页面')
        if d(text="设置").exists():
            logger.info('已进入设置页面')
        else:
            logger.info('未进入设置页面')
            return 'unknown error'

    with allure.step('点击"立即进群"'):
        logger.info('点击"立即进群"')
        d(resourceId="com.codemao.nemo:id/tv_enter_group").click()

    with allure.step('验证弹出加QQ群提示'):
        logger.info('验证弹出加QQ群提示')
        if "QQ群号" in d(resourceId="com.codemao.nemo:id/tv_content").get_text():
            logger.info('弹出加群提示')
        else:
            logger.info('未弹出加群提示')
            return False

    with allure.step('点击“复制QQ”'):
        logger.info('点击“复制QQ”')
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('验证弹出toast提示“QQ号复制成功”'):
        logger.info('验证弹出toast提示“QQ号复制成功”')
        message = d.toast.get_message()
        assert "QQ号复制成功" in message
        logger.info('验证加群提示框关闭,回到设置页面')
        assert d(text="设置").exists()

    with allure.step('点击"立即进群"，并点击取消'):
        logger.info('点击"立即进群"，并点击取消')
        d(resourceId="com.codemao.nemo:id/tv_enter_group").click()
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()

    with allure.step('验证加群提示框关闭,回到设置页面'):
        logger.info('验证加群提示框关闭,回到设置页面')
        assert d(text="设置").exists()


@allure.tag(f"environment:{ENV}", "TC3012")
@allure.feature('设置')
@allure.story('验证个人资料')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_user_info_two(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(text="我的").click()

    with allure.step('点击"设置"图标'):
        logger.info('点击"设置"图标')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    # 检查是否已进入设置页面：验证页面上出现“设置”
    with allure.step('验证是否进入设置页面'):
        logger.info('验证是否进入设置页面')
        if d(text="设置").exists():
            logger.info('已进入设置页面')
        else:
            logger.info('未进入设置页面')
            return 'unknown error'

    with allure.step('点击"个人资料"'):
        logger.info('点击"个人资料"')
        d(resourceId="com.codemao.nemo:id/rl_user_info").click()

    with allure.step('验证进入个人资料页'):
        logger.info('验证进入个人资料页')
        if d(text='个人资料').exists():
            logger.info('已进入个人资料编辑页')
        else:
            logger.info('未进入个人资料编辑页')
            return 'unknown error'

    with allure.step('返回一步'):
        logger.info('返回一步')
        d(resourceId="com.codemao.nemo:id/iv_close").click()

    with allure.step('验证设置页面'):
        logger.info('验证回到设置页面')
        assert d(text="设置").exists()


@allure.tag(f"environment:{ENV}", "TC3013")
@allure.feature('设置')
@allure.story('验证用户反馈')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_user_feed_three(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(text="我的").click()

    with allure.step('点击"设置"图标'):
        logger.info('点击"设置"图标')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    # 检查是否已进入设置页面：验证页面上出现“设置”
    with allure.step('验证是否进入设置页面'):
        logger.info('验证是否进入设置页面')
        if d(text="设置").exists():
            logger.info('已进入设置页面')
        else:
            logger.info('未进入设置页面')
            return 'unknown error'

    with allure.step('点击"用户反馈"'):
        logger.info('点击"用户反馈"')
        d(resourceId="com.codemao.nemo:id/rl_user_feed").click()

    with allure.step('验证弹出加技术喵QQ提示'):
        logger.info('验证弹出加技术喵QQ提示')
        if "联系技术喵" in d(resourceId="com.codemao.nemo:id/tv_content").get_text():
            logger.info('弹出加群提示')
        else:
            logger.info('未弹出加群提示')
            return False

    with allure.step('点击“复制QQ”'):
        logger.info('点击“复制QQ”')
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('验证弹出toast提示“QQ号复制成功”'):
        logger.info('验证弹出toast提示“QQ号复制成功”')
        message = d.toast.get_message()
        assert "QQ号复制成功" in message
        logger.info('验证加群提示框关闭,回到设置页面')
        assert d(text="设置").exists()

    with allure.step('点击"用户反馈"，并点击取消'):
        logger.info('点击"用户反馈"，并点击取消')
        d(resourceId="com.codemao.nemo:id/rl_user_feed").click()
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()

    with allure.step('验证加群提示框关闭,回到设置页面'):
        logger.info('验证加群提示框关闭,回到设置页面')
        assert d(text="设置").exists()


@allure.tag(f"environment:{ENV}", "TC3014")
@allure.feature('设置')
@allure.story('验证关于')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_about_four(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(text="我的").click()

    with allure.step('点击"设置"图标'):
        logger.info('点击"设置"图标')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    # 检查是否已进入设置页面：验证页面上出现“设置”
    with allure.step('验证是否进入设置页面'):
        logger.info('验证是否进入设置页面')
        if d(text="设置").exists():
            logger.info('已进入设置页面')
        else:
            logger.info('未进入设置页面')
            return 'unknown error'

    with allure.step('点击"关于"'):
        logger.info('点击"关于"')
        d(resourceId="com.codemao.nemo:id/rl_about").click()

    with allure.step('验证进入"关于"页面'):
        logger.info('验证进入"关于"页面')
        if d(text="关于Nemo，关于编程猫").exists():
            logger.info('已进入"关于"页面')
        else:
            logger.info('未进入"关于"页面')
            return 'unknown error'

    with allure.step('验证“版权声明”存在'):
        logger.info('验证“版权声明”存在')
        assert d(text="版权声明").exists()

    with allure.step('验证“隐私及服务条款”存在'):
        logger.info('验证“隐私及服务条款”存在')
        assert d(resourceId="com.codemao.nemo:id/tv_private_provision").exists()

    with allure.step('点击“隐私及服务条款”'):
        logger.info('点击“隐私及服务条款”')
        d(resourceId="com.codemao.nemo:id/tv_private_provision").click()
        d.wait_timeout = 30.0
        assert d.current_app()['package'] == "com.android.browser"
        d.screenshot()
        d.app_stop("com.android.browser")

    with allure.step('返回一步'):
        logger.info('返回一步')
        d(resourceId="com.codemao.nemo:id/iv_close").click()

    with allure.step('验证设置页面'):
        logger.info('验证回到设置页面')
        assert d(text="设置").exists()


@allure.tag(f"environment:{ENV}", "TC3015")
@allure.feature('设置')
@allure.story('验证应用版本')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_version_five(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(text="我的").click()

    with allure.step('点击"设置"图标'):
        logger.info('点击"设置"图标')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    # 检查是否已进入设置页面：验证页面上出现“设置”
    with allure.step('验证是否进入设置页面'):
        logger.info('验证是否进入设置页面')
        if d(text="设置").exists():
            logger.info('已进入设置页面')
        else:
            logger.info('未进入设置页面')
            return 'unknown error'

    with allure.step('上滑到底'):
        logger.info('上滑到底')
        d(scrollable=True).scroll.toEnd()

    with allure.step('验证“版本号”存在'):
        logger.info('验证“版本号”存在')
        assert d(resourceId="com.codemao.nemo:id/tv_version_num").exists()
        version = d(resourceId="com.codemao.nemo:id/tv_version_num").get_text()
        version_number = version[3:]
        print(version_number)


@allure.tag(f"environment:{ENV}", "TC3016")
@allure.feature('设置')
@allure.story('验证退出')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_logout_six(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(text="我的").click()

    with allure.step('点击"设置"图标'):
        logger.info('点击"设置"图标')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    # 检查是否已进入设置页面：验证页面上出现“设置”
    with allure.step('验证是否进入设置页面'):
        logger.info('验证是否进入设置页面')
        if d(text="设置").exists():
            logger.info('已进入设置页面')
        else:
            logger.info('未进入设置页面')
            return 'unknown error'

    with allure.step('上滑到底'):
        logger.info('上滑到底')
        d(scrollable=True).scroll.toEnd()

    with allure.step('点击退出登录'):
        logger.info('点击退出登录')
        d(text="退出当前账号").click()

    with allure.step('验证已退出登录'):
        logger.info('验证已退出登录')
        assert d(resourceId="com.codemao.nemo:id/iv_Login_account").exists()


if __name__ == '__main__':
    import subprocess
    import sys
    import os

    pytest.main(["-v", "test_personal_center.py"])
    # pytest.main(["-v", "-s", "test_ban_and_recover_login.py"])
    # pytest.main(["-v", "--setup-show", "test_ban_and_recover_login.py"])
    # 运行全部test用例
    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    # # pytest.main(["-s", "-q", "--alluredir", path_xml])
    pytest.main(["-s", "-q", "test_work_detail.py", "--alluredir", path_xml])
    # pytest.main(["-lf", "-q", "-s", "test_work_detail.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)

