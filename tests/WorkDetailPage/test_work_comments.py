import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog

'''
作品详情页(评论区)测试用例
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC0016")
@allure.feature('作品详情页')
@allure.story('评论区')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_comments_one(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品内是否可以发表评论
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('点击进入第一个作品详情页'):
        logger.info('点击进入第一个作品详情页')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('对着作品标题左滑切换到评论标签页'):
        logger.info('对着作品标题左滑切换到评论标签页')
        d(resourceId="com.codemao.nemo:id/tv_user_name").swipe("left", steps=10)

    with allure.step('点击发表评论：第一级评论'):
        logger.info('点击发表评论：第一级评论')
        d(resourceId="com.codemao.nemo:id/tv_show_input").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/edit_content").click()
        d.send_keys("第一级评论")  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        time.sleep(0.5)
        d(resourceId="com.codemao.nemo:id/tv_send_reply").click()  # 点击发送评论

    with allure.step('检查第一个评论是否为：第一级评论'):
        logger.info('检查第一个评论是否为：第一级评论')
        content = d(resourceId="com.codemao.nemo:id/tv_comment_content").get_text()
        assert "第一级评论" in content

    with allure.step('点击删除按钮，删除刚刚发表的评论'):
        logger.info('点击删除按钮，删除刚刚发表的评论')
        d(resourceId="com.codemao.nemo:id/iv_comment_more").click()  # 点击"..."
        time.sleep(0.3)
        d(resourceId="com.codemao.nemo:id/tv_delete").click()  # 点击”删除“
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()  # 确认删除

    with allure.step('验证第一条评论已经不包含：第一级评论'):
        logger.info('验证第一条评论已经不包含：第一级评论')
        if d(resourceId="com.codemao.nemo:id/tv_comment_content").exists:  # 先判断此时是否有评论
            content_new = d(resourceId="com.codemao.nemo:id/tv_comment_content").get_text()
            assert "第一级评论" not in content_new
        else:
            content_new = None

    allure.attach("删除前的第一条评论: {}\n"
                  "删除后的第一条评论: {}\n".format(content, content_new), '评论详情', allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0017")
@allure.feature('作品详情页')
@allure.story('评论区')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_comments_two(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品内是否可以发表二、三级评论
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('点击进入第一个作品详情页'):
        logger.info('点击进入第一个作品详情页')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('对着作品标题左滑切换到评论标签页'):
        logger.info('对着作品标题左滑切换到评论标签页')
        d(resourceId="com.codemao.nemo:id/tv_user_name").swipe("left", steps=10)

    with allure.step('点击发表评论：第一级评论'):
        logger.info('点击发表评论：第一级评论')
        d(resourceId="com.codemao.nemo:id/tv_show_input").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/edit_content").click()
        d.send_keys("第一级评论")  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        time.sleep(0.3)
        d(resourceId="com.codemao.nemo:id/tv_send_reply").click()  # 点击发送评论

    with allure.step('检查第一个评论是否为：第一级评论'):
        logger.info('检查第一个评论是否为：第一级评论')
        content = d(resourceId="com.codemao.nemo:id/tv_comment_content").get_text()
        assert "第一级评论" in content

    with allure.step('点击第一个评论，发布第二个评论：第二级评论'):
        logger.info('点击第一个评论，发布第二个评论：第二级评论')
        d(resourceId="com.codemao.nemo:id/tv_comment_content").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/edit_content").click()
        d.send_keys("第二级评论")  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        time.sleep(0.3)
        d(resourceId="com.codemao.nemo:id/tv_send_reply").click()  # 点击发送评论

    with allure.step('检查第二个评论是否为：第二级评论'):
        logger.info('检查第二个评论是否为：第二级评论')
        content_second = d(resourceId="com.codemao.nemo:id/tv_comment_content")[1].get_text()
        assert "第二级评论" in content_second

    with allure.step('点击第二个评论，来到二级评论页'):
        logger.info('点击第二个评论，来到二级评论页')
        d(resourceId="com.codemao.nemo:id/tv_comment_content")[1].click()

    with allure.step('检查页面标题是否为：1条回复'):
        logger.info('检查页面标题是否为：1条回复')
        reply_num = d(resourceId="com.codemao.nemo:id/tv_reply_num").get_text()
        assert "1条回复" in reply_num

    with allure.step('再次点击第二个评论，发布第二个评论：第三级评论'):
        logger.info('再次点击第二个评论，发布第二个评论：第三级评论')
        d(resourceId="com.codemao.nemo:id/tv_comment_content")[1].click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/edit_content").click()
        d.send_keys("第三级评论")  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        time.sleep(0.3)
        d(resourceId="com.codemao.nemo:id/tv_send_reply").click()  # 点击发送评论

    with allure.step('检查当前页第三个评论是：第三级评论'):
        logger.info('检查当前页第三个评论是：第三级评论')
        content_third = d(resourceId="com.codemao.nemo:id/tv_comment_content")[2].get_text()
        assert "第三级评论" in content_third

    with allure.step('点击删除按钮，删除刚刚发表的一级评论，连带删除所有评论'):
        logger.info('点击删除按钮，删除刚刚发表的一级评论，连带删除所有评论')
        d(resourceId="com.codemao.nemo:id/iv_comment_more").click()  # 点击"..."
        time.sleep(0.3)
        d(resourceId="com.codemao.nemo:id/tv_delete").click()  # 点击”删除“
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()  # 确认删除

    with allure.step('验证第一条评论已经不包含：第一级评论'):
        logger.info('验证第一条评论已经不包含：第一级评论')
        if d(resourceId="com.codemao.nemo:id/tv_comment_content").exists:  # 先判断此时是否有评论
            content_new = d(resourceId="com.codemao.nemo:id/tv_comment_content").get_text()
            assert "第一级评论" not in content_new
        else:
            content_new = None

    allure.attach("content: {}\n"
                  "content_second: {}\n"
                  "content_third: {}\n"
                  "reply_num: {}\n".format(content, content_second, content_third, reply_num), '评论详情',
                  allure.attachment_type.TEXT)


if __name__ == '__main__':
    import subprocess
    import sys
    import os

    # pytest.main(["-v", "test_ban_and_recover_login.py"])
    # pytest.main(["-v", "-s", "test_ban_and_recover_login.py"])
    # pytest.main(["-v", "--setup-show", "test_ban_and_recover_login.py"])
    # 运行全部test用例
    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    # # pytest.main(["-s", "-q", "--alluredir", path_xml])
    pytest.main(["-s", "-q", "test_work_comments.py", "--alluredir", path_xml])
    # pytest.main(["--lf", "-v", "test_cloud.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)