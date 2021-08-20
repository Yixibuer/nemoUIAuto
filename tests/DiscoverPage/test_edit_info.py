import pytest
import uiautomator2 as u2
from data.cfg import udid
from logs.my_logger import MyLog
from data.cfg import ENV, username183, password183
import allure

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC3017")
@allure.feature('发现-作品详情页')
@allure.story('验证在作品详情页可使用编辑信息功能修改封面')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_change_cover_one(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“+”选择从模板创建新作品'):
        logger.info('点击“+”选择从模板创建新作品')
        d(resourceId="com.codemao.nemo:id/createBtn").click()
        d(text="从模板创建").click()
        d(resourceId="com.codemao.nemo:id/tv_enter").click()

    with allure.step('保存作品，命名为“testeditinfo123'):
        logger.info('保存作品，命名为“testeditinfo123')
        d(resourceId="com.codemao.nemo:id/menu").click()
        d(resourceId="com.codemao.nemo:id/tv_quit").click()
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        d.xpath(
            '//*[@resource-id="com.codemao.nemo:id/rvContainer"]/android.widget.FrameLayout[1]'
            '/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
            ).click()
        d(resourceId="com.codemao.nemo:id/edit_content").clear_text()
        test_work_name = "testeditinfo123"
        d(resourceId="com.codemao.nemo:id/edit_content").send_keys(test_work_name)
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('发布作品'):
        logger.info('发布作品')
        d(resourceId="com.codemao.nemo:id/pub_iv").click()
        d(resourceId="com.codemao.nemo:id/tv_publish").click()

    with allure.step('验证来到“最新”页面'):
        logger.info('验证来到“最新”页面')
        if d(text="最新").exists():
            pass
        else:
            return False

    with allure.step('搜索刚刚发布的作品，并点击'):
        logger.info('搜索刚刚发布的作品，并点击')
        d(resourceId="com.codemao.nemo:id/iv_search").click()
        while True:
            if d(resourceId="com.codemao.nemo:id/tv_work_name").get_text() == test_work_name:
                break
            else:
                d.swipe_ext("up", scale=0.09)
                continue
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('点击右上角“...”'):
        logger.info('点击右上角“...”')
        d(resourceId="com.codemao.nemo:id/iv_more").click()
        logger.info('点击“编辑信息”')
        d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()

    with allure.step('验证进入发布作品页'):
        logger.info('验证进入发布作品页')
        if d(resourceId="com.codemao.nemo:id/tv_title").get_text() == "发布作品":
            pass
        else:
            return False

    with allure.step('点击“作品封面”按钮'):
        logger.info('点击“作品封面”按钮')
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()

    with allure.step('点击“取消”'):
        logger.info('点击“取消”')
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()

    with allure.step('验证进入发布作品页'):
        logger.info('验证进入发布作品页')
        assert d(resourceId="com.codemao.nemo:id/tv_title").get_text() == "发布作品"

    with allure.step('点击“作品封面”按钮'):
        logger.info('点击“作品封面”按钮')
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()

    with allure.step('点击“上传图片”'):
        logger.info('点击“上传图片”')
        d(resourceId="com.codemao.nemo:id/tv_edit_local_cover").click()

    with allure.step('选择第二张图片并上传'):
        logger.info('选择第二张图片并上传')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').click()
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('验证进入发布作品页'):
        logger.info('验证进入发布作品页')
        assert d(resourceId="com.codemao.nemo:id/tv_title").get_text() == "发布作品"

    with allure.step('截图上传，后续检查是否上传成功'):
        logger.info('截图上传，后续检查是否上传成功')
        d.screenshot()

    with allure.step('直接点击作品封面'):
        logger.info('直接点击作品封面')
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()

    with allure.step('点击“取消”'):
        logger.info('点击“取消”')
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()

    with allure.step('验证进入发布作品页'):
        logger.info('验证进入发布作品页')
        assert d(resourceId="com.codemao.nemo:id/tv_title").get_text() == "发布作品"

    with allure.step('直接点击作品封面'):
        logger.info('直接点击作品封面')
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()

    with allure.step('点击“上传图片”'):
        logger.info('点击“上传图片”')
        d(resourceId="com.codemao.nemo:id/tv_edit_local_cover").click()

    with allure.step('选择第三张图片并上传'):
        logger.info('选择第三张图片并上传')
        d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[3]').click()
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()

    with allure.step('验证进入发布作品页'):
        logger.info('验证进入发布作品页')
        assert d(resourceId="com.codemao.nemo:id/tv_title").get_text() == "发布作品"

    with allure.step('再次截图上传，后续检查是否上传成功'):
        logger.info('再次截图上传，后续检查是否上传成功')
        d.screenshot()


@allure.tag(f"environment:{ENV}", "TC3018")
@allure.feature('发现-作品详情页')
@allure.story('验证在作品详情页可使用编辑信息功能修改作品名')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_change_work_name_one(login_and_logout183_module, stop_and_run_nemo):
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('搜索新发布的作品'):
        logger.info('搜索新发布的作品')
        ######################################

    with allure.step('点击右上角“...”'):
        logger.info('点击右上角“...”')
        d(resourceId="com.codemao.nemo:id/iv_more").click()
        logger.info('点击“编辑信息”')
        d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()

    with allure.step('验证进入发布作品页'):
        logger.info('验证进入发布作品页')
        if d(resourceId="com.codemao.nemo:id/tv_title").get_text() == "发布作品":
            pass
        else:
            return False



