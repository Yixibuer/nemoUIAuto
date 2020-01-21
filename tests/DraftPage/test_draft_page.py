import uiautomator2 as u2
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog
import time

# 调用日志模块
logger = MyLog().getlog()



import re
@allure.tag(f"environment:{ENV}", "P0", "TC2001")
@allure.feature('草稿箱测试')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.run(order=1)
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_login_tc2001(login_and_logout190):
    '''
      启动App
    点击切换环境按钮
    选择test环境并等待0.5s
    清空编程猫的app信息
    选择编程猫账号登录
    登录后草稿箱数目为0
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击物品的，进入草稿箱'):
        logger.info('进入我的页面')
        d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
        draft_id = d(text="草稿箱(0)")
        assert draft_id.wait()
        assert draft_id.get_text() == "草稿箱(0)"
        logger.info('草稿箱数目为0')
        a1 = int(re.findall("\d+", d.xpath("//*[contains(@text, '草稿箱')]").get_text())[0])
        assert a1 ==0

@allure.tag(f"environment:{ENV}", "P0", "TC2002")
@allure.feature('草稿箱测试')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_deaft_tc2002(stop_app):
    '''
    登录后点击自由创作后，作品可以新增成功
    新增作品名称为“新的作品”
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    a1 = int(re.findall("\d+", d.xpath("//*[contains(@text, '草稿箱')]").get_text())[0])
    logger.info('进入我的页面')
    with allure.step('点击创作'):
        d(resourceId="com.codemao.nemo:id/createBtn").click(timeout=10)
        logger.info('全新的作品')
    with allure.step('点击自由创作'):
        d(resourceId="com.codemao.nemo:id/item3_name").click(timeout=10)
        logger.info('点击菜单')
        time.sleep(10)
        d(resourceId="com.codemao.nemo:id/menu").click(timeout=30)
        # d(resourceId="com.codemao.nemo:id/menu").click()
        logger.info('点击退出')
        d(resourceId="com.codemao.nemo:id/tv_quit").click(timeout=10)
    # d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    a2 = int(re.findall("\d+", d.xpath("//*[contains(@text, '草稿箱')]").get_text())[0])
    assert a2==a1+1
    assert '新的作品' in d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()
    logger.info('自由创作创建一个作品成功')




@allure.tag(f"environment:{ENV}", "P0", "TC2003")
@allure.feature('草稿箱测试')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=1,reruns_delay=2)
def test_env_deaft_tc2003(stop_app):
    '''
    登录成功后，通過自由創作可以新增作品可以存储在草稿箱，草稿箱数目变与新增数相同,新增2个作品
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    a1 = int(re.findall("\d+", d.xpath("//*[contains(@text, '草稿箱')]").get_text())[0])
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('自由创作2个作品'):
        for i in  range(0,2):
            with allure.step('进入我的页面'):
                logger.info('自由创作{}个作品'.format(i))
                logger.info('点击“创作”')
                d(resourceId="com.codemao.nemo:id/createBtn").click(timeout=10)
                logger.info('自由创作新的作品')
                d(resourceId="com.codemao.nemo:id/item3_name").click(timeout=10)
                logger.info('点击菜单')
                time.sleep(10)
                d(resourceId="com.codemao.nemo:id/menu").click(timeout=30)
                logger.info('点击退出')
                d(resourceId="com.codemao.nemo:id/tv_quit").click(timeout=10)
    # d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    a2 = int(re.findall("\d+", d.xpath("//*[contains(@text, '草稿箱')]").get_text())[0])
    assert a2==a1+2
    assert '新的作品' in d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()


@allure.tag(f"environment:{ENV}", "P0", "TC2004")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_draft_tc2004(stop_app):
    '''
    登录成功后，通过‘边学边做’可以新增作品成功,新增一个作品
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    a1 = int(re.findall("\d+", d.xpath("//*[contains(@text, '草稿箱')]").get_text())[0])
    with allure.step('进入我的页面'):
        logger.info('边学边做创做1个作品')
        logger.info('点击“创作”')
        d(resourceId="com.codemao.nemo:id/createBtn").click(timeout=10)
    with allure.step("选择边学边做"):
        logger.info('选择“边学边做”')
        d(resourceId="com.codemao.nemo:id/item1_name").click(timeout=10)
        logger.info('点击学习视频')
        d(resourceId="com.codemao.nemo:id/cover").click(timeout=10)
        logger.info('点击：去创造')
        d(text="去创作").click(timeout=10)
    with allure.step('退出创作页面'):
        logger.info('点击菜单')
        time.sleep(10)
        d(resourceId="com.codemao.nemo:id/menu").click(timeout=30)
        d(resourceId="com.codemao.nemo:id/menu").click(timeout=30)
        logger.info('点击退出')
        d(resourceId="com.codemao.nemo:id/tv_quit").click(timeout=10)
    a2 = int(re.findall("\d+", d.xpath("//*[contains(@text, '草稿箱')]").get_text())[0])
    logger.info(f'草稿箱有{a2}个作品')
    assert a2==a1+1
    assert '新的作品' in d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()






test_datas=[{'num': 1, 'index': '1/8', 'name': '地底寻宝', 'content': '跟随编程猫寻找宝藏，了解旋转的奥秘吧'},
            {'num': 2, 'index': '2/8', 'name': '源码画板', 'content': '拿起画笔，成为源码世界的小小艺术家'},
            {'num': 3, 'index': '3/8', 'name': '唱片机', 'content': '播放音乐，唱出欢快乐曲'},
            {'num': 4, 'index': '4/8', 'name': '声控捕鱼', 'content': '大喊轰隆隆，看谁抓的鱼儿多'},
            {'num': 5, 'index': '5/8', 'name': '贪吃猴', 'content': '操控摇杆，帮助雷电猴吃到更多电力吧'},
            {'num': 6, 'index': '6/8', 'name': '飞翔的蓝雀', 'content': '冲破阻碍，向着蓝天自由飞翔吧'},
            {'num': 7, 'index': '7/8', 'name': '躲避弹球', 'content': '左右倾斜，帮助阿短躲避疯狂弹球吧'},
            {'num': 8, 'index': '8/8', 'name': '丛林爬爬', 'content': '丛林爬呀爬，躲避飞镖谁最行'}]


@allure.tag(f"environment:{ENV}", "P0", "TC2005")
@allure.feature('草稿箱测试')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_draft_mould_tc2005(stop_app):
    '''
    登录成功后，通过‘从模板创作’创建作品可以成功
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.wait_timeout = 30.0  # default 20.0
    for test_num in test_datas:
        j = test_num['num']
        index = test_num['index']
        tv_name = test_num['name']
        tv_content = test_num['content']
        with allure.step("点击+进入创作页面"):
            logger.info('点击+按钮')
            d(resourceId="com.codemao.nemo:id/createBtn").click(timeout=10)
        with allure.step("选择边学边做"):
            logger.info('选择“从模板创建”')
            d(resourceId="com.codemao.nemo:id/item2_name").click(timeout=10)
        with allure.step('进入从模板创作：{}'.format(tv_name)):
            logger.info('从模板创做作品‘{}’'.format(tv_name))
            for i in range(0, j - 1):
                d.swipe_ext("left", scale=0.6)
            logger.info('左滑{}次'.format(j - 1))
            logger.info('模板的序号为：{}'.format(d(resourceId='com.codemao.nemo:id/index').get_text()))
            logger.info('模板的名称为：{}'.format(d(resourceId='com.codemao.nemo:id/tv_name').get_text()))
            logger.info('模板的说明为：{}'.format(d(resourceId='com.codemao.nemo:id/tv_content').get_text()))
            assert d(resourceId='com.codemao.nemo:id/index').get_text() == index
            assert d(resourceId='com.codemao.nemo:id/tv_name').get_text() == tv_name
            assert d(resourceId='com.codemao.nemo:id/tv_content').get_text() == tv_content
            logger.info('点击“立即创作”')
            d(resourceId="com.codemao.nemo:id/tv_enter").click(timeout=10)
            logger.info('点击“菜单”')
            time.sleep(10)
            d(resourceId="com.codemao.nemo:id/menu").click(timeout=30)
            logger.info('点击“退出”')
            d(resourceId="com.codemao.nemo:id/tv_quit").click(timeout=10)
            logger.info('点击“好的”')
            d(resourceId="com.codemao.nemo:id/tv_confirm").click(timeout=10)
        draft_id = d.xpath('//*[@text="{}-副本"]'.format(tv_name))
        assert draft_id.wait()
        assert "副本" in draft_id.get_text() == "{}-副本".format(tv_name)
        logger.info('{}-副本，创建成功'.format(tv_name))

@allure.tag(f"environment:{ENV}", "P0", "TC2006")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_draft_tc2006(stop_app):
    '''
    登录成功后：
    1.进入 我的
    2.复制草稿箱内作品
    3.点击上传，作品上传
    4.点击删除，可以删除成功
    以下P0取消
    5.重复复制4次可以复制成功
    6.可以重复删除4次
    7.每次复制后都加编号，第一次复制直接为“副本”，没有编号
    8.复制的时候会检查序号，补充缺失的序号
    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay

    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    with allure.step("点击复制"):
        d(resourceId="com.codemao.nemo:id/copy_iv").click(timeout=10)
        logger.info('点击复制')

    with allure.step("点击上传"):
        d(resourceId="com.codemao.nemo:id/cloud_up_iv").click(timeout=10)
        logger.info('点击上传')
    with allure.step("上传成功上传按钮消失"):
        assert d(resourceId='com.codemao.nemo:id/cloud_up_iv').exists(timeout=10)==0
        logger.info('上传按钮消失')
    with allure.step("点击删除"):
        d(resourceId="com.codemao.nemo:id/remove_iv").click(timeout=10)
        logger.info('点击删除')
        time.sleep(2)
    # with allure.step("删除按钮消失"):
    #     logger.info("确认不删除")
    #     d(resourceId="com.codemao.nemo:id/remove_cancel").click()
    #     logger.info('删除按钮还在')
    #     time.sleep(2)
    #     assert d(resourceId='com.codemao.nemo:id/remove_iv').exists() == 1
    #     logger.info('点击删除')
    #     d(resourceId="com.codemao.nemo:id/remove_iv").click(timeout=10)
    #     logger.info("确认删除")
    #     d(resourceId='com.codemao.nemo:id/remove_confirm').click(timeout=10)
    #     time.sleep(2)
    #     assert d(resourceId='com.codemao.nemo:id/remove_iv').exists()==0
    #     logger.info('删除按钮消失')
    #
    # with allure.step("复制4次，每次检查作品名称后缀"):
    #     d(resourceId="com.codemao.nemo:id/copy_iv").click(timeout=10)
    #     assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()=='声控小火箭-副本'
    #     for i in range(1,5):
    #         d(resourceId="com.codemao.nemo:id/copy_iv").click(timeout=10)
    #         assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()=='声控小火箭-副本{}'.format(i+1)
    #         logger.info('新复制的作品名称为{}'.format(d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()))
    #     logger.info('点击复制')
    # # 删除副本
    # with allure.step("验证删除副本后，新增副本的编号补充删除的编号"):
    #     logger.info("选择删除副本4")
    #     time.sleep(2)
    #     a = d.xpath(
    #         '//*[@resource-id="com.codemao.nemo:id/rvContainer"]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[4]')
    #     a.click(timeout=10)
    #     d(resourceId='com.codemao.nemo:id/remove_confirm').click(timeout=10)
    #     logger.info("删除副本4，新的副本为副本3")
    #     logger.info("复制副本3，新的副本为副本4")
    #     time.sleep(2)
    #     b = d.xpath(
    #         '//*[@resource-id="com.codemao.nemo:id/rvContainer"]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[3]')
    #     b.click(timeout=10)
    #     assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text() == '声控小火箭-副本4'



@allure.tag(f"environment:{ENV}", "P0", "TC2007")
@allure.feature('草稿箱测试')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_draft_tc2007(stop_app):
    '''
    登录成功后：
    进入 我的
    复制草稿箱内作品
    点击编辑按钮，修改作品名称
    清空作品名
    取消重命名作品，作品名称不变
    输入新的名称，确认修改名称
    保存成功后，比较修改后的值与输入值相同
    输入20字以上可以保存成功
    小于20字，输入全英文可以保存成功
    输入小于20字的中英文昏花可以保存成功
    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    with allure.step("点击复制"):
        d(resourceId="com.codemao.nemo:id/copy_iv").click(timeout=10)
        logger.info('点击复制')
    with allure.step("修改作品名称"):
        a=d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()
        logger.info("修改前的作品名为{}".format(a))
        logger.info('点击修改作品名称')
        d(resourceId="com.codemao.nemo:id/iv_edit_name").click(timeout=10)
        d(resourceId="com.codemao.nemo:id/edit_content").click(timeout=10)
        logger.info('清空作品名')
        d.set_fastinput_ime(True)
        d.clear_text()
        logger.info('修改作品名称成功')
        d.send_keys(f"你好，大黄鸭")  # adb广播输入
    with allure.step('清空作评名后，点击X，取消重命名'):
        d(resourceId="com.codemao.nemo:id/iv_close").click(timeout=10)
        assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text() == a
        logger.info("作品名称不变")
    with allure.step('点击确认'):
        logger.info('点击修改作品名称')
        d(resourceId="com.codemao.nemo:id/iv_edit_name").click(timeout=10)
        d(resourceId="com.codemao.nemo:id/edit_content").click(timeout=10)
        logger.info('清空作品名')
        d.clear_text()
        logger.info('修改作品名称成功')
        d.send_keys(f"你好大黄鸭")
        logger.info('切换回正常输入法')
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        logger.info("点击确定")
        d(resourceId="com.codemao.nemo:id/tv_confirm").click(timeout=10)
        assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text() == '你好大黄鸭'



@allure.tag(f"environment:{ENV}", "P0", "TC2008")
@allure.feature('草稿箱测试')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_draft_tc2008(stop_app):
    '''
    登录成功后：
    进入 我的
    复制草稿箱内作品
    点击发布，跳转到发布页面
    点击“发布”，发布成功后进入“最新”页面
    回到我的页面，点击取消发布
    二次确认时，选择“保留发布”，作品没有取消发布
    二次确认时，选择“取消发布”，作品取消发布
    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
    with allure.step("点击复制"):
        time.sleep(2)
        d(resourceId="com.codemao.nemo:id/copy_iv").click(timeout=10)
        logger.info('点击复制')
        time.sleep(2)
    with allure.step("点击发作品"):
        logger.info('点击发布')
        d(resourceId="com.codemao.nemo:id/pub_iv").click(timeout=10)
        logger.info("跳转发布页面")
        d(resourceId="com.codemao.nemo:id/tv_publish").click(timeout=10)


    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')
    with allure.step('校验是否成功登录并进入首页，推荐按钮text校验：{}, 最新按钮text校验：{}'.format(
                recommend.get_text(), newest.get_text())):
        logger.info('校验是否成功登录并进入首页')
        assert recommend.get_text() == "推荐"
        assert newest.get_text() == "最新"
    with allure.step("二次确认是否取消发布"):
        d(resourceId="com.codemao.nemo:id/mine_rb").click(timeout=10)
        d(resourceId="com.codemao.nemo:id/pub_iv").click(timeout=10)
        logger.info("二次确认时点击保留发布")
        assert d(resourceId="com.codemao.nemo:id/tv_content").get_text()=="取消发布作品后他人将无法看到你的作品。"
        d(resourceId="com.codemao.nemo:id/tv_confirm").click(timeout=10)
        logger.info("作品没有取消发布成功")
        logger.info("没有删除按钮")
        assert d(resourceId='com.codemao.nemo:id/remove_iv').exists()==0
        logger.info("点击取消发布")
        d(resourceId="com.codemao.nemo:id/pub_iv").click(timeout=10)
        d(resourceId="com.codemao.nemo:id/tv_cancel").click(timeout=10)
        logger.info("作品取消发布成功")
        logger.info("有删除按钮原生可以定位")
        assert d(resourceId='com.codemao.nemo:id/remove_iv').exists()== 1


if __name__ == '__main__':
    # pytest.main(["-k", "2006"])
    import subprocess
    import sys
    import os

    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    # # pytest.main(["-s", "-q", "--alluredir", path_xml])
    pytest.main(["-s", "-q", "test_draft_page.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)