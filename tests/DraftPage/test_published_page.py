# @Author　 :hzj
# @Time　　 :2019/12/23   14:04
#@ File　　 :test_published_page.py
#@Projec    :nemo_ui
#@Description   :测试已发布作品


import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog
from time import sleep



'''
测试草稿箱页面
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "P0", "TC2009")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj
def test_env_login_tc2009(login_and_logout183):
    '''
    修改作品名称、说明、封面可以成功
    启动App
    点击切换环境按钮
    选择test环境并等待0.5s
    清空编程猫的app信息
    选择编程猫账号登录
    登录后修改已发布作品的信息
    点击进入已发布作品
    点击“编辑信息”，进入编辑页面，确认已进入编辑页面
    清空原作品名称，分别输入20个以上汉字、20个以上英文、20字以上中英混和
    校验20字以后的数据不饿\能输入
    清空作品简介，校验默认的说明信息
    输入200字以上字符，校验200字以上不能输入成功
    更新封面：确认更新、取消更新；二次取消选择土拍你，二次确认更新
    点击发布
    '''
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    sleep(5)
    d.click(0.425, 0.309)
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        sleep(5)
        logger.info("点击右上角...")
        d(resourceId="com.codemao.nemo:id/iv_more").click()
        sleep(5)
        logger.info("点击编辑信息")
        d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
    with allure.step("修改作品名称"):
        logger.info("修改作品名称")
        d(resourceId="com.codemao.nemo:id/et_work_name").click()
        d.set_fastinput_ime(True)  # 切换成正常的输入法
        d.clear_text()
        logger.info("输入20字以上的数字")
        d.send_keys("12345678901234567890123")
        logger.info("校验20字后的输入不成功")
        assert d(resourceId="com.codemao.nemo:id/et_work_name").get_text()=="12345678901234567890"
        logger.info("输入20字以上的汉字")
        d.clear_text()
        d.send_keys("一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十")
        logger.info("校验20字后的输入不成功")
        assert d(resourceId="com.codemao.nemo:id/et_work_name").get_text() == "一二三四五六七八九十一二三四五六七八九十"
    with allure.step("修改封面"):
        logger.info("点击作品封面")
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()
        logger.info("点击取消")
        sleep(2)
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()
        sleep(2)
        logger.info("点击作品封面")
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()
        logger.info("点击上传图片")
        d(resourceId="com.codemao.nemo:id/tv_edit_local_cover").click()
        sleep(5)
        logger.info("选择第一张图片")
        d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').click()
        sleep(2)
    with allure.step("确认选择图片页面验证"):
        logger.info("勾选图片后，点击 ✔")
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        sleep(2)
        logger.info("二次确认页面校验——选择取消")
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()
        sleep(2)
        logger.info("返回相册页面，上一次图片处于选定状态")
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        sleep(2)
        logger.info("二次确认页面校验——选择选取")
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        sleep(5)
    with allure.step("修改作品秒速"):
        d(resourceId="com.codemao.nemo:id/et_work_description").click()
        d.clear_text()
        logger.info("校验默认值")
        sleep(5)
        assert d(resourceId="com.codemao.nemo:id/et_work_description").get_text()=="向大家介绍你的作品，并教大家如何操作吧！如果你的作品是基于他人作品再创作，或者从他人作品中得到灵感，别忘记感谢原作者哦~"
        logger.info("输入200字一下字符")
        d.send_keys("我在测试：向大家介绍你的作品，https://www.tapd.cn/56872519/documents/view/1156872519001001820?file_type=mindmap&file_ext=xmind并教大家如何操作吧！如果你的作品向大家介绍你的作品，并教大家如何操作吧！如果你的作品向大家介绍你的作品，并教大家如何操作吧！如果你的作品向大家介绍你的作品，并教大家如何操作吧！如果你的作品")
        sleep(3)
        logger.info("切换输入法")
        d.set_fastinput_ime(False)
    with allure.step("点击发布"):
        logger.info("点击发布")
        d(resourceId="com.codemao.nemo:id/tv_publish").click()
        sleep(5)
    with allure.step("校验作品名、作品秒速修改成功"):
        logger.info("校验作品名")
        assert d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()=="一二三四五六七八九十一二三四五六七八九十"
        logger.info("校验作品描述,暂时没有做")
        logger.info("封面更换成功，暂时没有做校验")


@allure.tag(f"environment:{ENV}", "P0", "TC2010")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj
def test_env_login_tc2010(login_and_logout183):
    '''
    修改作品信息=不影响作评的开源状态
    启动App
    登录后修改已发布作品的信息
    点击进入已发布作品
    已发布作评默认为——开放开源代码
    已发布作评默认为——关闭开源代码——发布后，没有开源按钮
    已发布作评默认为——打开开源代码——发布后，有开源按钮
    '''
    a="测试"+time.strftime("%Y-%m-%d_%H%M%S")
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    sleep(5)
    d.click(0.425, 0.309)
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        sleep(5)
        with allure.step("如果第一个作评为不开源，则把它改为开源"):
            if d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 0:
                logger.info("第一个作评为不开源，把它改为开源")
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                sleep(5)
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                d.click(0.472, 0.841)
                sleep(2)
                logger.info("点击发布")
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
                sleep(5)
            else:
                logger.info("第一个作评为开源，无需操作")
            logger.info("点击右上角...")
            d(resourceId="com.codemao.nemo:id/iv_more").click()
            sleep(5)
            logger.info("点击编辑信息")
            d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
            with allure.step("修改作品名称，不会使开源作品变为不开源"):
                logger.info("修改作品名称")
                d(resourceId="com.codemao.nemo:id/et_work_name").click()
                d.set_fastinput_ime(True)  # 切换成正常的输入法
                d.clear_text()
                d.send_keys(a)
                d(resourceId="com.codemao.nemo:id/et_work_description").click()
                d.set_fastinput_ime(False)
            with allure.step("点击发布"):
                logger.info("点击发布")
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
                sleep(5)
            with allure.step("校验开源按钮"):
                logger.info("校验作品名")
                print(d(resourceId="com.codemao.nemo:id/tv_work_name").get_text())
                print(a)
                logger.info("校验开源按钮还在")
                assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists()==1
                # assert d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()==a
            with allure.step("关闭开源按钮"):
                logger.info("校验作品名")
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                sleep(5)
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                sleep(5)
                logger.info("点击开源代码——关闭")
                d.click(0.472, 0.841)
                sleep(2)
                logger.info("点击发布")
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
                sleep(5)
                logger.info("校验开源按钮消失")
                assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 0
                sleep(5)
            with allure.step("打开开源按钮"):
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                sleep(5)
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                sleep(2)
                logger.info("点击开源代码——关闭")
                d.click(0.472, 0.841)
                sleep(2)
                logger.info("点击发布")
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
                sleep(5)
                logger.info("校验开源按钮显示")
                assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 1


@allure.tag(f"environment:{ENV}", "P0", "TC2011")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj
def test_env_login_tc2011(login_and_logout183):
    '''
    编辑积木————不影响作品的开源状态
    启动App
    登录后修改已发布作品的信息
    点击进入已发布作品
    如果第一个作品为不开源作品，则修改为开源作品
    已发布作品评默认为——开放开源代码
    已发布作品评默认为——关闭开源代码——发布后，没有开源按钮
    已发布作品评默认为——打开开源代码——发布后，有开源按钮
    '''
    pass
def test():
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    sleep(5)
    d.click(0.425, 0.309)
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        sleep(5)
        with allure.step("如果第一个作评为不开源，则把它改为开源"):
            if d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 0:
                logger.info("第一个作评为不开源，把它改为开源")
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                sleep(5)
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                d.click(0.472, 0.841)
                sleep(2)
                logger.info("点击发布")
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
                sleep(5)
            else:
                logger.info("第一个作评为开源，无需操作")
            logger.info("点击右上角...")
            d(resourceId="com.codemao.nemo:id/iv_more").click()
            sleep(5)
            logger.info("点击编辑积木信息")
            d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑积木").click()
            with allure.step("修改积木信息，不会使开源作品变为不开源"):
                sleep(10)
                logger.info("进入修改作评信息后后，点击发布")
                d(resourceId="com.codemao.nemo:id/menu").click()
                sleep(3)
                d(resourceId="com.codemao.nemo:id/iv_upload").click()
                sleep(15)
            with allure.step("点击发布"):
                logger.info("点击发布,这里变成了非dom结构，所以使用了坐标定位")
                # d(resourceId="com.codemao.nemo:id/tv_publish").click()
                d.click(0.956, 0.059)
                sleep(5)
            with allure.step("校验开源按钮"):
                d(resourceId="com.codemao.nemo:id/mine_rb").click()
                sleep(5)
                d.click(0.425, 0.309)
                sleep(2)
                d(resourceId="com.codemao.nemo:id/rl_cover").click()
                logger.info("校验开源按钮还在")
                sleep(5)
                assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists()==1
            with allure.step("关闭开源按钮"):
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                sleep(5)
                logger.info("点击编辑积木信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑积木").click()
                sleep(10)
                logger.info("进入修改作评页后，点击发布")
                d(resourceId="com.codemao.nemo:id/menu").click()
                sleep(3)
                d(resourceId="com.codemao.nemo:id/iv_upload").click()
                sleep(10)
                logger.info("点击开源代码——关闭")
                d.click(0.472, 0.841)
                sleep(2)
                logger.info("点击发布")
                # d(resourceId="com.codemao.nemo:id/tv_publish").click()
                logger.info("这里发布按钮又变成了非原生，所以采用相对坐标定位")
                d.click(0.892, 0.059)
                sleep(5)
                d(resourceId="com.codemao.nemo:id/mine_rb").click()
                sleep(5)
                d.click(0.425, 0.309)
                sleep(2)
                d(resourceId="com.codemao.nemo:id/rl_cover").click()
                logger.info("校验开源按钮消失")
                sleep(5)
                assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 0
                sleep(5)
            with allure.step("打开开源按钮"):
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                sleep(5)
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                sleep(2)
                logger.info("点击开源代码——关闭")
                d.click(0.472, 0.841)
                sleep(2)
                logger.info("点击发布")
                # d(resourceId="com.codemao.nemo:id/tv_publish").click()
                logger.info("这里发布按钮又变成了非原生，所以采用相对坐标定位")
                d.click(0.892, 0.059)
                sleep(5)
                logger.info("校验开源按钮显示")
                assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 1



a=test()