import pytest
import uiautomator2 as u2
from data.cfg import udid
from logs.my_logger import MyLog
from data.cfg import ENV, username183, password183
import allure

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC3001")
@allure.feature('个人中心')
@allure.story('验证可进入个人资料页面')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_enter_personal_info_one(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(text="我的").click()

    with allure.step('点击头像、昵称等范围内的可点击区域'):
        logger.info('点击头像、昵称等范围内的可点击区域')
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    # 检查是否已进入头像编辑页面：验证页面上出现“训练师编号”
    with allure.step('验证是否进入个人资料页面'):
        logger.info('验证是否进入个人资料页面')
        assert "训练师编号" in d(resourceId="com.codemao.nemo:id/tv_user_id").get_text()


@allure.tag(f"environment:{ENV}", "TC3002")
@allure.feature('个人中心')
@allure.story('验证点击头像进行修改头像正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_change_avatar_two(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('点击头像'):
        logger.info('点击头像')
        d(resourceId="com.codemao.nemo:id/iv_user_avatar").click()

    with allure.step('验证进入用户头像页'):
        logger.info('验证进入用户头像页')
        if d(text='用户头像').exists():
            logger.info('已进入用户头像页')
        else:
            logger.info('未进入用户头像页')
            return 'unknown error'

    with allure.step('点击第三个头像'):
        logger.info('点击第三个头像')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[3]').click()

    with allure.step('验证修改成功'):
        message = d.toast.get_message()
        assert "修改头像成功" in message and "训练师编号" in d(resourceId="com.codemao.nemo:id/tv_user_id").get_text()

    with allure.step('点击头像'):
        logger.info('点击头像')
        d(resourceId="com.codemao.nemo:id/iv_user_avatar").click()

    with allure.step('点击加号,如果有权限提示，选择开启权限'):
        logger.info('点击加号，如果有权限提示，选择开启权限')
        d(resourceId="com.codemao.nemo:id/iv_add").click()
        if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
            d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
        if d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').exists:
            logger.info('已进入手机相册')
        else:
            return "unknown error"

    with allure.step('选择照片并点击确认'):
        logger.info('选择照片并点击确认')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').click()
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('验证修改成功'):
        message = d.toast.get_message()
        assert "修改头像成功" in message and "训练师编号" in d(resourceId="com.codemao.nemo:id/tv_user_id").get_text()

    # with allure.step('点击头像'):
    #     logger.info('点击头像')
    #     d(resourceId="com.codemao.nemo:id/iv_user_avatar").click()
    #
    # with allure.step('点击加号,如果有权限提示，选择开启权限'):
    #     logger.info('点击加号，如果有权限提示，选择开启权限')
    #     d(resourceId="com.codemao.nemo:id/iv_add").click()
    #     if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
    #         d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
    #     if d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').exists:
    #         logger.info('已进入手机相册')
    #     else:
    #         return "unknown error"
    #
    # with allure.step('点击“拍摄照片”,如果有权限提示，选择开启权限'):
    #     logger.info('点击“拍摄照片”,如果有权限提示，选择开启权限')
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[1]').click()
    #     d.wait_timeout = 30.0
    #     if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
    #         d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
    #
    # with allure.step('点击拍照按钮'):
    #     logger.info('点击拍照按钮')
    #     d(resourceId="com.huawei.camera:id/shutter_button").click()
    #
    # with allure.step('点击确认'):
    #     logger.info('点击确认')
    #     d(resourceId="com.huawei.camera:id/btn_done").click()
    #     d(resourceId="com.codemao.nemo:id/tv_confirm").click()
    #
    # with allure.step('验证修改成功'):
    #     message = d.toast.get_message()
    #     assert "修改头像成功" in message and "训练师编号" in d(resourceId="com.codemao.nemo:id/tv_user_id").get_text()

    with allure.step('恢复默认头像'):
        logger.info('恢复默认头像')
        d(resourceId="com.codemao.nemo:id/iv_user_avatar").click()
        d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[3]').click()


@allure.tag(f"environment:{ENV}", "TC3003")
@allure.feature('个人中心')
@allure.story('验证点击封面进行修改封面正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_change_cover_three(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('点击封面'):
        logger.info('点击封面')
        d(resourceId="com.codemao.nemo:id/iv_user_cover").click()

    with allure.step('验证进入修改封面页'):
        logger.info('验证进入修改封面页')
        if d(text='修改封面').exists():
            logger.info('已进入修改封面页')
        else:
            logger.info('未进入修改封面页')
            return 'unknown error'

    with allure.step('点击第二个封面'):
        logger.info('点击第二个封面')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]').click()

    with allure.step('验证封面上传成功'):
        logger.info('验证封面上传成功')
        message = d.toast.get_message()
        assert "封面上传成功" in message and "训练师编号" in d(resourceId="com.codemao.nemo:id/tv_user_id").get_text()

    with allure.step('点击封面'):
        logger.info('点击封面')
        d(resourceId="com.codemao.nemo:id/iv_user_cover").click()

    with allure.step('点击加号,如果有权限提示，选择开启权限'):
        logger.info('点击加号，如果有权限提示，选择开启权限')
        d(resourceId="com.codemao.nemo:id/iv_add").click()
        if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
            d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
        if d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').exists:
            logger.info('已进入手机相册')
        else:
            return "unknown error"

    with allure.step('选择照片并点击确认'):
        logger.info('选择照片并点击确认')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').click()
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('验证封面上传成功'):
        logger.info('验证封面上传成功')
        message = d.toast.get_message()
        assert "封面上传成功" in message and "训练师编号" in d(resourceId="com.codemao.nemo:id/tv_user_id").get_text()

    # with allure.step('点击封面'):
    #     logger.info('点击封面')
    #     d(resourceId="com.codemao.nemo:id/iv_user_cover").click()
    #
    # with allure.step('点击加号,如果有权限提示，选择开启权限'):
    #     logger.info('点击加号，如果有权限提示，选择开启权限')
    #     d(resourceId="com.codemao.nemo:id/iv_add").click()
    #     if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
    #         d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
    #     if d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').exists:
    #         logger.info('已进入手机相册')
    #     else:
    #         return "unknown error"
    #
    # with allure.step('点击“拍摄照片”,如果有权限提示，选择开启权限'):
    #     logger.info('点击“拍摄照片”,如果有权限提示，选择开启权限')
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[1]').click()
    #     d.wait_timeout = 30.0
    #     if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
    #         d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
    #
    # with allure.step('点击拍照按钮'):
    #     logger.info('点击拍照按钮')
    #     d(resourceId="com.huawei.camera:id/shutter_button").click()
    #
    # with allure.step('点击确认'):
    #     logger.info('点击确认')
    #     d(resourceId="com.huawei.camera:id/btn_done").click()
    #     d(resourceId="com.codemao.nemo:id/tv_confirm").click()
    #
    # with allure.step('验证封面上传成功'):
    #     logger.info('验证封面上传成功')
    #     message = d.toast.get_message()
    #     assert "封面上传成功" in message and "训练师编号" in d(resourceId="com.codemao.nemo:id/tv_user_id").get_text()

    with allure.step('恢复默认封面'):
        logger.info('恢复默认封面')
        d(resourceId="com.codemao.nemo:id/iv_user_cover").click()
        d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]').click()


@allure.tag(f"environment:{ENV}", "TC3004")
@allure.feature('个人中心')
@allure.story('验证编辑页面修改用户头像正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_edit_page_change_avatar_four(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('点击“编辑”'):
        logger.info('点击“编辑”')
        d(resourceId="com.codemao.nemo:id/tv_follow_or_edit").click()

    with allure.step('验证进入个人资料编辑页'):
        logger.info('验证进入个人资料编辑页')
        if d(text='个人资料').exists():
            logger.info('已进入个人资料编辑页')
        else:
            logger.info('未进入个人资料编辑页')
            return 'unknown error'

    with allure.step('点击用户头像栏'):
        logger.info('点击用户头像栏')
        d(resourceId="com.codemao.nemo:id/rl_user_avatar").click()

    with allure.step('点击第三个头像'):
        logger.info('点击第三个头像')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[3]').click()

    with allure.step('验证修改成功'):
        message = d.toast.get_message()
        assert "修改头像成功" in message and d(text='个人资料').exists()
        if d(text='个人资料').exists():
            logger.info('已返回个人资料编辑页')
            logger.info('修改头像成功')
        else:
            logger.info('未返回个人资料编辑页')
            return 'unknown error'

    with allure.step('点击用户头像栏'):
        logger.info('点击用户头像栏')
        d(resourceId="com.codemao.nemo:id/rl_user_avatar").click()

    with allure.step('点击加号,如果有权限提示，选择开启权限'):
        logger.info('点击加号，如果有权限提示，选择开启权限')
        d(resourceId="com.codemao.nemo:id/iv_add").click()
        if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
            d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
        if d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').exists:
            logger.info('已进入手机相册')
        else:
            return "unknown error"

    with allure.step('选择照片并点击确认'):
        logger.info('选择照片并点击确认')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').click()
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('验证修改成功'):
        d.wait_timeout = 50.0
        message = d.toast.get_message()
        assert "修改头像成功" in message
        d.wait_timeout = 50.0
        # assert d(text='个人资料').exists()
        if d(text='个人资料').exists():
            logger.info('已返回个人资料编辑页')
            logger.info('修改头像成功')
        else:
            logger.info('未返回个人资料编辑页')
            return 'unknown error'

    # with allure.step('点击用户头像栏'):
    #     logger.info('点击用户头像栏')
    #     d(resourceId="com.codemao.nemo:id/rl_user_avatar").click()
    #
    # with allure.step('点击加号,如果有权限提示，选择开启权限'):
    #     logger.info('点击加号，如果有权限提示，选择开启权限')
    #     d(resourceId="com.codemao.nemo:id/iv_add").click()
    #     if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
    #         d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
    #     if d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').exists:
    #         logger.info('已进入手机相册')
    #     else:
    #         return "unknown error"
    #
    # with allure.step('点击“拍摄照片”,如果有权限提示，选择开启权限'):
    #     logger.info('点击“拍摄照片”,如果有权限提示，选择开启权限')
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[1]').click()
    #     if d(resourceId="com.android.packageinstaller:id/permission_message").exists():
    #         d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
    #
    # with allure.step('点击拍照按钮'):
    #     logger.info('点击拍照按钮')
    #     d(resourceId="com.huawei.camera:id/shutter_button").click()
    #
    # with allure.step('点击确认'):
    #     logger.info('点击确认')
    #     d(resourceId="com.huawei.camera:id/btn_done").click()
    #     d(resourceId="com.codemao.nemo:id/tv_confirm").click()
    #
    # with allure.step('验证修改成功'):
    #     message = d.toast.get_message()
    #     assert "修改头像成功" in message and d(text='个人资料').exists()
    #     if d(text='个人资料').exists():
    #         logger.info('已返回个人资料编辑页')
    #         logger.info('修改头像成功')
    #     else:
    #         logger.info('未返回个人资料编辑页')
    #         return 'unknown error'

    with allure.step('恢复默认头像'):
        logger.info('恢复默认头像')
        d(resourceId="com.codemao.nemo:id/rl_user_avatar").click()
        d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[3]').click()


@allure.tag(f"environment:{ENV}", "TC3005")
@allure.feature('个人中心')
@allure.story('验证编辑页面修改昵称正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_edit_page_change_nickname_five(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('点击“编辑”'):
        logger.info('点击“编辑”')
        d(resourceId="com.codemao.nemo:id/tv_follow_or_edit").click()

    with allure.step('验证进入个人资料编辑页'):
        logger.info('验证进入个人资料编辑页')
        if d(text='个人资料').exists():
            logger.info('已进入个人资料编辑页')
        else:
            logger.info('未进入个人资料编辑页')
            return 'unknown error'

    with allure.step('点击昵称栏'):
        logger.info('点击昵称栏')
        d(resourceId="com.codemao.nemo:id/rl_user_nick_name").click()

    with allure.step('验证进入昵称栏'):
        logger.info('验证进入昵称栏')
        if d(text='昵称').exists() and d(resourceId="android:id/inputArea").exists():
            logger.info('已进入昵称编辑页, 键盘弹起')
        else:
            logger.info('未进入昵称编辑页')
            return 'unknown error'

    with allure.step("获取初始昵称"):
        logger.info('获取初始昵称')
        initial_nick_name = d(resourceId="com.codemao.nemo:id/edit_content").get_text()

    with allure.step('修改昵称并点击返回'):
        logger.info('修改昵称并点击返回')
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        logger.info("获取当前昵称")
        current_nick_name = d(resourceId="com.codemao.nemo:id/tv_user_nickname").get_text()
        if d(text='个人资料').exists():
            assert initial_nick_name == current_nick_name
        else:
            logger.info('未回到个人资料页')
            return 'unknown error'

    with allure.step('修改昵称并点击保存'):
        logger.info('点击昵称栏')
        d(resourceId="com.codemao.nemo:id/rl_user_nick_name").click()
        logger.info('修改为格式正确的昵称并保存')
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        correct_nick_name = '一希test_8'
        d(resourceId="com.codemao.nemo:id/edit_content").send_keys(correct_nick_name)
        d(resourceId="com.codemao.nemo:id/tv_save").click()
        logger.info("获取当前昵称")
        current_nick_name = d(resourceId="com.codemao.nemo:id/tv_user_nickname").get_text()
        if d(text='个人资料').exists():
            message = d.toast.get_message()
            assert "昵称修改成功" in message and correct_nick_name == current_nick_name
        else:
            logger.info('未回到个人资料页')
            return 'unknown error'
        logger.info('点击昵称栏')
        d(resourceId="com.codemao.nemo:id/rl_user_nick_name").click()
        logger.info('修改为重名的昵称并保存')
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        same_nick_name = '热情的超能鸭eOwT'
        d(resourceId="com.codemao.nemo:id/edit_content").send_keys(same_nick_name)
        d(resourceId="com.codemao.nemo:id/tv_save").click()
        assert d(text='昵称').exists() and d(resourceId="com.codemao.nemo:id/tv_name_used").exists()
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        if d(text='个人资料').exists():
            assert correct_nick_name == current_nick_name
        else:
            logger.info('未回到个人资料页')
            return 'unknown error'
        # logger.info('修改为格式错误的昵称并点击保存')

    with allure.step('检查个人中心页的昵称显示已改'):
        logger.info('检查个人中心页的昵称显示已改')
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        current_personal_center_user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
        assert current_personal_center_user_name == current_nick_name

    with allure.step('检查"我的"页面昵称显示已改'):
        logger.info('检查"我的"页面昵称显示已改')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        current_my_user_name = d(resourceId="com.codemao.nemo:id/author_name_tv").get_text()
        assert current_my_user_name == current_nick_name

    with allure.step('进入我的任意作品详情页，检查昵称显示已改'):
        logger.info('进入我的任意作品详情页，检查昵称显示已改')
        d.xpath("//*[contains(@text, '已发布')]").click()
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        current_author_user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
        assert current_author_user_name == current_nick_name

    with allure.step('还原昵称'):
        logger.info('还原昵称')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        logger.info('返回个人中心页')
        d(resourceId="com.codemao.nemo:id/author_click_area").click()
        logger.info('点击“编辑”')
        d(resourceId="com.codemao.nemo:id/tv_follow_or_edit").click()
        logger.info('点击昵称栏，还原初始昵称')
        d(resourceId="com.codemao.nemo:id/rl_user_nick_name").click()
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        d(resourceId="com.codemao.nemo:id/edit_content").send_keys(initial_nick_name)
        d(resourceId="com.codemao.nemo:id/tv_save").click()


@allure.tag(f"environment:{ENV}", "TC3006")
@allure.feature('个人中心')
@allure.story('验证编辑页面修改签名正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_edit_page_change_sign_six(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('点击“编辑”'):
        logger.info('点击“编辑”')
        d(resourceId="com.codemao.nemo:id/tv_follow_or_edit").click()

    with allure.step('验证进入个人资料编辑页'):
        logger.info('验证进入个人资料编辑页')
        if d(text='个人资料').exists():
            logger.info('已进入个人资料编辑页')
        else:
            logger.info('未进入个人资料编辑页')
            return 'unknown error'

    with allure.step('点击签名栏'):
        logger.info('点击签名栏')
        d(resourceId="com.codemao.nemo:id/rl_user_sign").click()

    with allure.step('验证进入签名栏'):
        logger.info('验证进入签名栏')
        if d(text='签名').exists() and d(resourceId="android:id/inputArea").exists():
            logger.info('已进入签名编辑页, 键盘弹起')
        else:
            logger.info('未进入签名编辑页')
            return 'unknown error'

    with allure.step("获取初始签名"):
        logger.info('获取初始签名')
        initial_sign = d(resourceId="com.codemao.nemo:id/edit_content").get_text()

    with allure.step('检查还可输入字符数=50-已输入字符数'):
        input_text_len = len(d(resourceId="com.codemao.nemo:id/edit_content").get_text())
        logger.info('已输入字符数为%s' % input_text_len)
        # print(input_text_len)
        remain_text_len_filter = filter(str.isdigit, d(resourceId="com.codemao.nemo:id/tv_count_limit").get_text())
        remain_text_len = int(''.join(list(remain_text_len_filter)))
        logger.info('还可输入字符数为%s' % remain_text_len)
        logger.info("还可输入字符数=50-已输入字符数")
        assert remain_text_len == 50 - int(input_text_len)

    with allure.step('修改签名并点击返回'):
        logger.info('修改签名并点击返回')
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        if d(resourceId="com.codemao.nemo:id/tv_content").exists():
            d(resourceId="com.codemao.nemo:id/tv_cancel").click()
        current_sign = d(resourceId="com.codemao.nemo:id/tv_user_sign").get_text()
        if d(text='个人资料').exists():
            assert initial_sign == current_sign
        else:
            logger.info('未回到个人资料页')
            return 'unknown error'

    with allure.step('修改签名，并点击返回'):
        logger.info('点击签名栏')
        d(resourceId="com.codemao.nemo:id/rl_user_sign").click()
        logger.info('修改为格式正确的签名并保存')
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        correct_sign = 'this is for test,!@#$%^&*()123456789_    '
        d(resourceId="com.codemao.nemo:id/edit_content").send_keys(correct_sign)
        d(resourceId="com.codemao.nemo:id/tv_save").click()
        logger.info("获取当前签名")
        current_sign = d(resourceId="com.codemao.nemo:id/tv_user_sign").get_text()
        if d(text='个人资料').exists():
            message = d.toast.get_message()
            assert "签名修改成功" in message and correct_sign == current_sign
        else:
            logger.info('未回到个人资料页')
            return 'unknown error'

    with allure.step('检查个人中心页的签名显示已改'):
        logger.info('检查个人中心页的签名显示已改')
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        current_personal_center_sign = d(resourceId="com.codemao.nemo:id/tv_user_sign").get_text()
        assert current_personal_center_sign == current_sign

    with allure.step('还原签名'):
        logger.info('还原签名')
        logger.info('点击“编辑”')
        d(resourceId="com.codemao.nemo:id/tv_follow_or_edit").click()
        logger.info('点击昵称栏，还原初始昵称')
        d(resourceId="com.codemao.nemo:id/rl_user_sign").click()
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        d(resourceId="com.codemao.nemo:id/edit_content").send_keys(initial_sign)
        d(resourceId="com.codemao.nemo:id/tv_save").click()


@allure.tag(f"environment:{ENV}", "TC3007")
@allure.feature('个人中心')
@allure.story('验证关注列表显示正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_follow_list_seven(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('获取自己昵称'):
        logger.info('获取自己昵称')
        my_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()

    with allure.step('获取初始关注数'):
        logger.info('获取初始关注数')
        d.wait_timeout = 50.0
        initial_follow_num = int(d(resourceId='com.codemao.nemo:id/tv_flow_num').get_text())
        logger.info('初始关注数为：%s' % initial_follow_num)

    with allure.step('点击关注'):
        logger.info('点击关注')
        d(text='关注').click()

    with allure.step('验证进入"我的关注"页面'):
        logger.info('验证进入"我的关注"页面')
        if "我的关注" in d(resourceId='com.codemao.nemo:id/tv_title').get_text():
            logger.info('已进入"我的关注"页面')
        else:
            logger.info('未进入"我的关注"页面')
            return 'unknown error'

    with allure.step('检查头像、昵称、作品数、点赞数、关注按钮均有显示'):
        logger.info('检查头像、昵称、作品数、点赞数、关注按钮均有显示')
        assert d(resourceId='com.codemao.nemo:id/iv_user_avatar').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_user_name').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_work_num').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_praise_num').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_follow').exists()

    with allure.step('在发现-推荐页面内关注一名训练师'):
        logger.info('在发现-推荐页面内关注一名训练师')
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        d(resourceId="com.codemao.nemo:id/discover_rb").click()
        d.swipe_ext("up", scale=0.2)
        d(resourceId="com.codemao.nemo:id/tv_user_name").click()
        while True:
            d(resourceId="com.codemao.nemo:id/tv_user_name").click()
            d(resourceId="com.codemao.nemo:id/tv_user_name").click()
            if d(resourceId="com.codemao.nemo:id/tv_follow_or_edit").get_text() == "关注":
                d(resourceId="com.codemao.nemo:id/tv_follow_or_edit").click()
                logger.info('关注该训练师')
                new_follow_user = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
                logger.info('记录新关注的训练师名字:%s' % new_follow_user)
                break
            else:
                logger.info('该训练师已被关注，重新选择')
                d(resourceId="com.codemao.nemo:id/iv_back").click()
                d.swipe_ext("up", scale=0.4)
                continue

    with allure.step('回到个人中心页面，检查关注数'):
        logger.info('回到个人中心页面，检查关注数')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        d(resourceId="com.codemao.nemo:id/mine_rb").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()
        new_follow_num = int(d(resourceId='com.codemao.nemo:id/tv_flow_num').get_text())
        d.wait_timeout = 10.0
        logger.info('获取新的关注数为：%s' % new_follow_num)
        assert new_follow_num == initial_follow_num + 1

    with allure.step('进入关注列表'):
        logger.info('进入关注列表')
        d(text="关注").click()

    with allure.step('验证列表中有该训练师,并点击‘已关注’'):
        logger.info('验证列表中有该训练师,并点击‘已关注’')
        while True:
            logger.info('检查关注列表')
            d.wait_timeout = 50.0
            if not d(resourceId="com.codemao.nemo:id/tv_user_name").exists():
                logger.info('关注列表为空')
                break
            user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
            if user_name == new_follow_user:
                logger.info('已找到该训练师')
                d.wait_timeout = 50.0
                d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]/android.widget.TextView[2]').click()
                logger.info('点击"已关注"，验证按钮变为‘关注’')
                d.wait_timeout = 100.0
                assert d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]/android.widget.TextView[2]').get_text() == "关注"
                break
            elif user_name != new_follow_user:
                d.swipe_ext("up", scale=0.09)
                if d(text="喵~已经到最后啦！").exists():
                    for i in d(resourceId="com.codemao.nemo:id/tv_user_name"):
                        if i.get_text() == new_follow_user:
                            logger.info('已找到该训练师')
                            d.wait_timeout = 50.0
                            d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]/android.widget.TextView[2]').click()
                            logger.info('点击"已关注"，验证按钮变为‘关注’')
                            d.wait_timeout = 100.0
                            assert d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]/android.widget.TextView[2]').get_text() == "关注"
                            break
                    raise Exception()

    with allure.step('返回一步，检查关注数'):
        logger.info('返回一步，检查关注数')
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        current_follow_num = int(d(resourceId='com.codemao.nemo:id/tv_flow_num').get_text())
        logger.info('当前关注数为：%s' % current_follow_num)
        assert current_follow_num == initial_follow_num

    # with allure.step('记录第一个训练师名字'):
    #     logger.info('记录第一个训练师名字')
    #     first_follow_name = d(resourceId='com.codemao.nemo:id/tv_user_name').get_text()
    #
    # with allure.step('点击进入第一个训练师首页'):
    #     logger.info('点击进入第一个训练师首页')
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[1]').click()
    #     logger.info('检查页面显示“已关注”')
    #     assert d(resourceId='com.codemao.nemo:id/tv_follow_or_edit').get_text() == "已关注"
    #
    # with allure.step('点击"粉丝"'):
    #     logger.info('点击"粉丝"')
    #     d(text="粉丝").click()
    #
    # with allure.step('检查"我"在粉丝列表中'):
    #     logger.info('检查"我"在粉丝列表中')
    #     while True:
    #         logger.info('检查粉丝列表')
    #         if not d(resourceId="com.codemao.nemo:id/tv_user_name").exists():
    #             logger.info('粉丝列表为空')
    #             break
    #         user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
    #         if user_name != my_name:
    #             d.swipe_ext("up", scale=0.1)
    #             if d(text="喵~已经到最后啦！").exists():
    #                 for view in d(resourceId="com.codemao.nemo:id/tv_user_name"):
    #                     if view.get_text() == my_name:
    #                         logger.info('已找到我的名字')
    #                         break
    #                 raise Exception("我的名字不在粉丝列表中")
    #         elif user_name == my_name:
    #             logger.info('已找到我的名字')
    #             break
    #         else:
    #             raise Exception("未知错误")
    #
    # with allure.step('返回“我的关注”页并点击“已关注”按钮'):
    #     logger.info('返回“我的关注”页并点击“已关注”按钮')
    #     d.press("back")
    #     d.press("back")
    #     d(text="已关注").click()
    #
    # with allure.step('检查按钮内容变为"关注"'):
    #     assert d(resourceId='com.codemao.nemo:id/tv_follow').get_text() == "关注"
    #
    # with allure.step('再次进入训练师首页'):
    #     logger.info('再次进入训练师首页')
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[1]').click()
    #     logger.info('检查页面显示变为"关注"')
    #     assert d(resourceId='com.codemao.nemo:id/tv_follow_or_edit').get_text() == "关注"
    #
    # with allure.step('点击"粉丝"'):
    #     logger.info('点击"粉丝"')
    #     d(text="粉丝").click()
    #
    # with allure.step('查看粉丝列表应该没有我的名字'):
    #     logger.info('查看粉丝列表应该没有我的名字')
    #     while True:
    #         logger.info('找寻粉丝列表')
    #         # 自动匹配第一个，即使有多个元素拥有此ID
    #         user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
    #         if user_name != my_name:
    #             d.swipe_ext("up", scale=0.1)
    #             if d(text="喵~已经到最后啦！").exists():
    #                 for view in d(resourceId="com.codemao.nemo:id/tv_user_name"):
    #                     if view.get_text() == my_name:
    #                         logger.info('已找到我的名字')
    #                         raise Exception("我的名字还在粉丝列表中")
    #                 break
    #         elif user_name == my_name:
    #             logger.info('已找到我的名字')
    #             raise Exception("我的名字还在粉丝列表中")
    #         else:
    #             raise Exception("未知错误")
    #
    # with allure.step('回到个人资料页面，检查关注数'):
    #     logger.info('回到个人资料页面，检查关注数')
    #     d(resourceId="com.codemao.nemo:id/iv_close").click()
    #     d(resourceId="com.codemao.nemo:id/iv_back").click()
    #     d(resourceId="com.codemao.nemo:id/iv_close").click()
    #     current_follow_num = int(d(resourceId="com.codemao.nemo:id/tv_flow_num").get_text())
    #     logger.info('判断当前关注数=初始关注数-1')
    #     assert current_follow_num == initial_follow_num - 1
    #
    # with allure.step('进入发现页面，重新关注该训练师'):
    #     logger.info('进入发现页面，重新关注该训练师')
    #     d(resourceId="com.codemao.nemo:id/iv_back").click()
    #     d(resourceId="com.codemao.nemo:id/discover_rb").click()
    #     d(resourceId="com.codemao.nemo:id/iv_search").click()
    #     d(resourceId="com.codemao.nemo:id/animRoot").send_keys(first_follow_name)
    #     d.send_action("search")
    #     d(text="用户").click()
    #     # 找到符合名字的训练师，并点击关注
    #
    # with allure.step('返回个人资料页,检查关注数'):
    #     logger.info('返回个人资料页,检查关注数')
    #     d(resourceId="com.codemao.nemo:id/cancel_tv").click()
    #     d(resourceId="com.codemao.nemo:id/mine_rb").click()
    #     d(resourceId="com.codemao.nemo:id/author_click_area").click()
    #     logger.info('判断新的关注数=初始关注数')
    #     new_follow_num = int(d(resourceId="com.codemao.nemo:id/tv_flow_num").get_text())
    #     assert new_follow_num == initial_follow_num

    # 进入我的关注，检查该训练师在我的关注列表中，进入其首页，检查我在其粉丝列表中


@allure.tag(f"environment:{ENV}", "TC3008")
@allure.feature('个人中心')
@allure.story('验证粉丝列表显示正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_fun_list_eight(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    # with allure.step('获取自己昵称'):
    #     logger.info('获取自己昵称')
    #     my_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()

    with allure.step('获取初始关注数'):
        logger.info('获取初始关注数')
        initial_follow_num = int(d(resourceId='com.codemao.nemo:id/tv_flow_num').get_text())
        logger.info('初始关注数为：%s' % initial_follow_num)

    with allure.step('点击粉丝'):
        logger.info('点击粉丝')
        d(text="粉丝").click()

    with allure.step('验证进入"我的粉丝"页面'):
        logger.info('验证进入"我的粉丝"页面')
        if "我的粉丝" in d(resourceId='com.codemao.nemo:id/tv_title').get_text():
            logger.info('已进入"我的粉丝"页面')
        else:
            logger.info('未进入"我的粉丝"页面')
            return 'unknown error'

    with allure.step('检查头像、昵称、作品数、点赞数、关注按钮均有显示'):
        logger.info('检查头像、昵称、作品数、点赞数、关注按钮均有显示')
        assert d(resourceId='com.codemao.nemo:id/iv_user_avatar').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_user_name').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_work_num').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_praise_num').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_follow').exists()

    # with allure.step('点击进入第一个训练师首页'):
    #     logger.info('点击进入第一个训练师首页')
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[1]').click()
    with allure.step('找到未关注的训练师，点击关注'):
        logger.info('找到未关注的训练师，点击关注')
        while True:
            follow_text = d(resourceId='com.codemao.nemo:id/tv_follow').get_text()
            if follow_text == "关注":
                logger.info('暂未关注该用户')
                d.wait_timeout = 30.0
                follow_name = d(resourceId='com.codemao.nemo:id/tv_user_name').get_text()
                logger.info('将关注的训练师名字为：%s' % follow_name)
                logger.info('点击关注')
                d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]/android.widget.TextView[2]').click()
                d.wait_timeout = 30.0
                follow_text = d(resourceId='com.codemao.nemo:id/tv_follow').get_text()
                assert follow_text == '已关注'
                break
            else:
                logger.info('已关注该用户')
                d.swipe_ext("up", scale=0.09)
                continue

    with allure.step('返回一步，验证关注数'):
        logger.info('返回一步，验证关注数')
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        new_follow_num = int(d(resourceId='com.codemao.nemo:id/tv_flow_num').get_text())
        logger.info('新的关注数为：%s' % new_follow_num)
        assert new_follow_num == initial_follow_num + 1

    with allure.step('点击粉丝'):
        logger.info('点击粉丝')
        d(text="粉丝").click()

    with allure.step('找到刚刚关注的训练师，点击“已关注”'):
        logger.info('找到刚刚关注的训练师，点击“已关注”')
        while True:
            current_name = d(resourceId='com.codemao.nemo:id/tv_user_name').get_text()
            if current_name == follow_name:
                logger.info('已找到该训练师')
                d.wait_timeout = 50.0
                d.xpath('//*[@resource-id="com.codemao.nemo:id/swipe_target"]/android.widget.RelativeLayout[2]/android.widget.TextView[2]').click()
                logger.info('点击已关注')
                d.wait_timeout = 50.0
                follow_text = d(resourceId='com.codemao.nemo:id/tv_follow').get_text()
                assert follow_text == '关注'
                break
            else:
                logger.info('暂未找到该训练师')
                d.swipe_ext("up", scale=0.09)
                continue

    with allure.step('返回一步，验证关注数'):
        logger.info('返回一步，验证关注数')
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        d.wait_timeout = 50.0
        new_follow_num = int(d(resourceId='com.codemao.nemo:id/tv_flow_num').get_text())
        logger.info('新的关注数为：%s' % new_follow_num)
        assert new_follow_num == initial_follow_num


@allure.tag(f"environment:{ENV}", "TC3009")
@allure.feature('个人中心')
@allure.story('验证收藏列表显示正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_collect_list_nine(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('记录初始收藏总数'):
        logger.info('记录初始收藏总数')
        initial_collect_num = int(d(resourceId="com.codemao.nemo:id/tv_collect_num").get_text())

    with allure.step('点击收藏'):
        logger.info('点击收藏')
        d(text="收藏").click()

    with allure.step('验证进入"我的收藏"页面'):
        logger.info('验证进入"我的收藏"页面')
        if "我的收藏" in d(resourceId="com.codemao.nemo:id/mid_view").get_text():
            logger.info('已进入"我的收藏"页面')
        else:
            logger.info('未进入"我的收藏"页面')
            return 'unknown error'

    with allure.step('检查作品名称、创作人、查看数、点赞数、收藏数均有显示'):
        logger.info('检查作品名称、创作人、查看数、点赞数、收藏数均有显示')
        d.wait_timeout = 30.0
        assert d(resourceId='com.codemao.nemo:id/tv_work_name').exists()
        assert d(resourceId='com.codemao.nemo:id/iv_user_avatar').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_user_name').exists()
        assert d(resourceId="com.codemao.nemo:id/tv_view_num").exists()
        assert d(resourceId='com.codemao.nemo:id/tv_praise_num').exists()
        assert d(resourceId='com.codemao.nemo:id/tv_collect_num').exists()
        assert d(resourceId='com.codemao.nemo:id/iv_remove').exists()

    with allure.step('记录第一个收藏的作品名'):
        logger.info('记录第一个收藏的作品名')
        initial_first_work_name = d(resourceId='com.codemao.nemo:id/tv_work_name').get_text()

    with allure.step('选择第一个收藏的作品，点击删除并点击取消'):
        logger.info('选择第一个收藏的作品，点击删除并点击取消')
        d(resourceId='com.codemao.nemo:id/iv_remove').click()
        d(resourceId="com.codemao.nemo:id/remove_cancel").click()

    with allure.step('取消删除，验证作品仍然存在'):
        logger.info('取消删除，验证作品仍然存在')
        current_first_work_name = d(resourceId='com.codemao.nemo:id/tv_work_name').get_text()
        assert current_first_work_name == initial_first_work_name

    with allure.step('选择第一个收藏的作品，点击删除并点击确定'):
        logger.info('选择第一个收藏的作品，点击删除并点击确定')
        d(resourceId='com.codemao.nemo:id/iv_remove').click()
        d(resourceId="com.codemao.nemo:id/remove_confirm").click()

    with allure.step('回到个人资料页面，检查收藏数'):
        logger.info('回到个人资料页面，检查收藏数')
        d(resourceId="com.codemao.nemo:id/left_view").click()
        current_collect_num = int(d(resourceId="com.codemao.nemo:id/tv_collect_num").get_text())
        logger.info('判断当前收藏数=初始收藏数-1')
        assert current_collect_num == initial_collect_num - 1

    with allure.step('进入发现页面，搜索该作品，重新收藏'):
        logger.info('进入发现页面，搜索该作品，重新收藏')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        d(resourceId="com.codemao.nemo:id/discover_rb").click()
        d(resourceId="com.codemao.nemo:id/iv_search").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/animRoot").click()
        d.send_keys(initial_first_work_name)
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        d.send_action("search")
        while True:
            if initial_first_work_name == d(resourceId="com.codemao.nemo:id/tv_work_name").get_text():
                d(resourceId="com.codemao.nemo:id/tv_work_name").click()
                logger.info('点击收藏')
                d(resourceId="com.codemao.nemo:id/iv_collect").click()
                break
            elif initial_first_work_name != d(resourceId="com.codemao.nemo:id/tv_work_name").get_text():
                d.swipe_ext("up", scale=0.09)
                continue
            else:
                logger.info('未找到指定作品')
                return "unknown error"

    with allure.step('回到个人资料页面，检查收藏数'):
        logger.info('回到个人资料页面，检查收藏数')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        d(resourceId="com.codemao.nemo:id/cancel_tv").click()
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()
        current_collect_num = int(d(resourceId="com.codemao.nemo:id/tv_collect_num").get_text())
        logger.info('判断当前收藏数=初始收藏数')
        assert current_collect_num == initial_collect_num

    with allure.step('进入“我的收藏”页面,检查该作品出现在“我的收藏”列表中'):
        logger.info('进入“我的收藏”页面,检查该作品出现在“我的收藏”列表中')
        d(text="收藏").click()
        current_first_work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
        assert current_first_work_name == initial_first_work_name


@allure.tag(f"environment:{ENV}", "TC3010")
@allure.feature('个人中心')
@allure.story('验证作品列表显示正常')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_list_ten(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入个人资料页面'):
        logger.info('进入个人资料页面')
        d(text="我的").click()
        d(resourceId="com.codemao.nemo:id/author_click_area").click()

    with allure.step('检查作品总数显示正常'):
        logger.info('检查作品总数显示正常')
        works_num_filter = filter(str.isdigit, d(resourceId="com.codemao.nemo:id/tv_works_num").get_text())
        works_num = int(''.join(list(works_num_filter)))
        print('works_num is %s' % works_num)
    #     如何验证作品总数显示的数值准确???????????????????????????????????????

    with allure.step('检查作品查看数显示正确'):
        logger.info('检查作品查看数显示正确')
        logger.info('向上滑动')
        d.swipe_ext("up", scale=0.3)
        initial_view_num = int(d(resourceId="com.codemao.nemo:id/tv_view_num").get_text())
        logger.info('第一个作品的初始查看数为：%s' % initial_view_num)
        logger.info('点击该作品')
        d(resourceId="com.codemao.nemo:id/rl_normal").click()
        logger.info('记录该作品现查看数')
        current_view_num = int(d(resourceId="com.codemao.nemo:id/tv_browse_num").get_text())
        assert current_view_num == initial_view_num + 1
        logger.info('退出作品，再次检查作品查看数')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        new_view_num = int(d(resourceId="com.codemao.nemo:id/tv_view_num").get_text())
        print(new_view_num)
        assert new_view_num == current_view_num + 1

    with allure.step('检查作品点赞数显示正确'):
        logger.info('检查作品点赞数显示正确')
        initial_like_num = int(d(resourceId="com.codemao.nemo:id/tv_praise_num").get_text())
        logger.info('第一个作品的点赞数为：%s' % initial_like_num)
        logger.info('点击该作品')
        d(resourceId="com.codemao.nemo:id/rl_normal").click()
        logger.info('给作品点赞')
        d(resourceId="com.codemao.nemo:id/iv_praise").click()
        logger.info('返回检查现点赞数')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        d.wait_timeout = 30.0
        current_like_num = int(d(resourceId="com.codemao.nemo:id/tv_praise_num").get_text())
        logger.info('现点赞数为%s' % current_like_num)
        assert current_like_num == initial_like_num + 1

    with allure.step('恢复作品点赞数'):
        logger.info('恢复作品点赞数')
        logger.info('再次点击该作品')
        d(resourceId="com.codemao.nemo:id/rl_normal").click()
        logger.info('再次点击点赞按钮，取消给作品点赞')
        d(resourceId="com.codemao.nemo:id/iv_praise").click()
        logger.info('返回检查现点赞数')
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        d.wait_timeout = 30.0
        current_new_like_num = int(d(resourceId="com.codemao.nemo:id/tv_praise_num").get_text())
        logger.info('现点赞数为%s' % current_new_like_num)
        assert current_new_like_num == initial_like_num

    with allure.step('记录作品收藏数'):
        logger.info('记录作品收藏数')
        initial_collect_num = int(d(resourceId="com.codemao.nemo:id/tv_collect_num").get_text())

    with allure.step('检查作品收藏数显示正确'):
        logger.info('检查作品收藏数显示正确')
        logger.info('点击该作品')
        d(resourceId="com.codemao.nemo:id/rl_normal").click()
        logger.info('点击收藏')
        d(resourceId="com.codemao.nemo:id/iv_collect").click()
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        logger.info('返回检查当前收藏数')
        d.wait_timeout = 50.0
        current_collect_num = int(d(resourceId="com.codemao.nemo:id/tv_collect_num").get_text())
        logger.info('现收藏数为%s' % current_collect_num)
        assert current_collect_num == initial_collect_num + 1

    with allure.step('恢复原收藏数'):
        logger.info('点击该作品')
        d(resourceId="com.codemao.nemo:id/rl_normal").click()
        logger.info('再次点击取消收藏')
        d(resourceId="com.codemao.nemo:id/iv_collect").click()
        d(resourceId="com.codemao.nemo:id/iv_back").click()
        logger.info('返回检查新的收藏数')
        d.wait_timeout = 30.0
        current_new_collect_num = int(d(resourceId="com.codemao.nemo:id/tv_collect_num").get_text())
        assert current_new_collect_num == initial_collect_num

    with allure.step('点击"最热"'):
        logger.info('点击"最热"')
        d(resourceId="com.codemao.nemo:id/tv_hotest").click()

    with allure.step('验证作品点赞数按倒叙排列'):
        logger.info('验证作品点赞数按倒叙排列')
        like_list = []
        while True:
            if len(like_list) < 5:
                like_num = d(resourceId="com.codemao.nemo:id/tv_praise_num").get_text()
                like_list.append(like_num)
                d.swipe_ext("up", scale=0.4)
                continue
            else:
                print(like_list)
                like_list_new = like_list
                break
        like_list.sort()
        print(like_list)
        like_list.reverse()
        # print(like_list)
        # print(like_list_new)
        assert like_list == like_list_new

    with allure.step('点击"最新"'):
        logger.info('点击"最新"')
        d(scrollable=True).scroll.toBeginning()
        d.wait_timeout = 200.0
        d(text="最新").click()
        d(text="最新").click()
        d.swipe_ext("up", scale=0.3)

    with allure.step('验证作品时间按倒叙排列'):
        logger.info('验证作品时间按倒叙排列')
        publish_time_list = []
        while True:
            if len(publish_time_list) < 5:
                logger.info('记录作品发布时间')
                publish_time = d(resourceId='com.codemao.nemo:id/tv_publish_time').get_text()
                publish_time_list.append(publish_time)
                d.swipe_ext("up", scale=0.4)
                continue
            else:
                print(publish_time_list)
                publish_time_list_new = publish_time_list
                break
        publish_time_list.sort()
        print(publish_time_list)
        publish_time_list.reverse()
        # print(publish_time_list)
        # print(publish_time_list_new)
        assert publish_time_list == publish_time_list_new


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

