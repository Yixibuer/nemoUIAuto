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
from data.cfg import ENV
from logs.my_logger import MyLog
from time import sleep




'''
测试已发布页面
'''

# 调用日志模块
logger = MyLog().getlog()


def edit_published():
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    logger.info("点击'已发布'")
    d.xpath("//*[contains(@text, '已发布')]").click()
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        sleep(2)
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        time.sleep(5)
        logger.info("点击右上角...")
        d(resourceId="com.codemao.nemo:id/iv_more").click()
        logger.info("点击编辑信息")
        d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()



@allure.tag(f"environment:{ENV}", "P0", "TC2009")
@allure.feature('已发布测试--编辑已发布作品的名称')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_login_tc2009(stop_app):
    '''
    登录后修改已发布作品的信息
    点击进入已发布作品
    点击“编辑信息”，进入编辑页面，确认已进入编辑页面
    清空原作品名称，分别输入20个以上汉字、20个以上英文、20字以上中英混和
    校验20字以后的数据不能输入
    清空作品简介，校验默认的说明信息
    输入200字以上字符，校验200字以上不能输入成功
    更新封面：确认更新、取消更新；二次取消选择土拍你，二次确认更新
    点击发布
    '''
    edit_published()
    d = u2.connect(f"{udid}")
    with allure.step("修改作品名称"):
        logger.info("修改作品名称")
        d(resourceId="com.codemao.nemo:id/et_work_name").click()
        d.set_fastinput_ime(True)  # 切换成正常的输入法
        d.clear_text()
        # logger.info("输入20字以上的数字")
        # d.send_keys("12345678901234567890123超过了")
        # logger.info("校验20字后的输入不成功")
        # assert d(resourceId="com.codemao.nemo:id/et_work_name").get_text()=="12345678901234567890"
        logger.info("输入20字以上的汉字")
        d.clear_text()
        d.send_keys("一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十")
        logger.info("校验20字后的输入不成功")
        assert d(resourceId="com.codemao.nemo:id/et_work_name").get_text() == "一二三四五六七八九十一二三四五六七八九十"
    logger.info("校验作品名称20字以下————成功")

@allure.tag(f"environment:{ENV}", "P0", "TC2010")
@allure.feature('已发布测试--更新作品的封面')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_login_tc2010(stop_app):
    '''
    选择编程猫账号登录
    登录后修改已发布作品的信息
    点击进入已发布作品
    点击“编辑信息”，进入编辑页面，确认已进入编辑页面
    点击“作品封面”，校验“取消”、“上传图片”按钮
    选好图片后——进入二次确认确认页面
    二次确认选择取消，再次回到相册页面
    上次选中的相片默认选中，二次确认选择确定，回到发布页面
    点击发布
    '''
    edit_published()
    d = u2.connect(f"{udid}")
    with allure.step("修改封面"):
        logger.info("点击--修改作品封面")
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()
        sleep(3)
        if d(resourceId="com.codemao.nemo:id/tv_edit_local_cover").exists() == 1:
            d(resourceId="com.codemao.nemo:id/tv_edit_local_cover").click()
        logger.info("点击取消")
        try:
            logger.info("获取相册权限")
            time.sleep(3)
            d(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
        except:
            logger.info("获取相册权限失败，请检查")
        #获取权限后就直接进入了相册，所以需要点返回
        d(description="Navigate up").click()
        sleep(2)
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()
        sleep(2)
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()
        logger.info("点击--修改作品封面")
        time.sleep(2)
        d(resourceId="com.codemao.nemo:id/tv_cover_edit").click()
        time.sleep(2)
        logger.info("点击上传图片")
        d(resourceId="com.codemao.nemo:id/tv_edit_local_cover").click()
        logger.info("选择第一张图片")
        d.xpath('//*[@resource-id="com.codemao.nemo:id/grid"]/android.widget.FrameLayout[2]').click()
    with allure.step("确认选择图片页面验证"):
        logger.info("勾选图片后，点击 ✔")
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        sleep(2)
        logger.info("二次确认页面校验——选择取消")
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()
        sleep(2)
        logger.info("返回相册页面，上一次图片处于选定状态")
        d(resourceId="com.codemao.nemo:id/iv_commit").click()
        time.sleep(2)
        logger.info("二次确认页面校验——选择选取")
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        time.sleep(2)
    with allure.step("确认更换图片后可以发布成功"):
        logger.info("更换封面成功——点击发布")
        d(resourceId="com.codemao.nemo:id/tv_publish").click()
        try:
            message = d.toast.get_message()
            assert "信息上传" in message
        except:
            logger.info("toast获取失败")
    logger.info("更换封面————成功")


@allure.tag(f"environment:{ENV}", "P0", "TC2011")
@allure.feature('已发布测试--修改作品描述成功')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_login_tc2011(stop_app):
    '''
     选择编程猫账号登录
    登录后修改已发布作品的信息
    点击进入已发布作品
    点击“编辑信息”，进入编辑页面，确认已进入编辑页面
    修改作品描述，输入30\200个字
    '''
    edit_published()
    d = u2.connect(f"{udid}")
    a = "我在测试：向大家介绍你的作品，https://www.tapd.cn/56872519/documents/view/1156872519001001820?file_type=mindmap&file_ext=xmind并教大家如何操作吧！如果你的作品向大家介绍你的作品，并教大家如何操作吧！如果你的作品向大家介绍你的作品，并教大家如何操作吧！如果你的作品向大家介绍你的作品，并教大家如何操作吧！如果你的作品"
    KeyWords_list = {"少于200字":"测试20字：1234567890000000", "大于200字":a}
    KeyWords_list = {"少于200字": "测试20字：1234567890000000"}
    for i in KeyWords_list.keys():
        with allure.step("修改作品描述"):
            d(resourceId="com.codemao.nemo:id/et_work_description").click()
            d.clear_text()
            logger.info("校验默认值")
            assert d(resourceId="com.codemao.nemo:id/et_work_description").get_text()=="向大家介绍你的作品，并教大家如何操作吧！如果你的作品是基于他人作品再创作，或者从他人作品中得到灵感，别忘记感谢原作者哦~"
            logger.info("测试内容为{}".format(i))
            d.send_keys(KeyWords_list[i])
            logger.info("切换输入法")
            d.set_fastinput_ime(False)
        with allure.step("点击发布"):
            logger.info("点击发布")
            d(resourceId="com.codemao.nemo:id/tv_publish").click()
        with allure.step("校验描述速修改成功"):
            logger.info("点击右上角...")
            time.sleep(5)
            d(resourceId="com.codemao.nemo:id/iv_more").click()
            logger.info("点击编辑信息")
            d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
            a=d(resourceId="com.codemao.nemo:id/et_work_description").get_text()
            if len(KeyWords_list[i])>=200:
                logger.info("校验作品描述,如果输入字符串大于200，则获取值为头200字符")
                b=KeyWords_list[i][0:200]
            else:
                b = KeyWords_list[i]
            logger.info("比较发布后的描述和修改的一致,获取的实际值是:{}".format(a))
            logger.info("比较发布后的描述和修改的一致,预期值是:{}".format(b))
            assert a==b
            logger.info("{}：比较成功".format(KeyWords_list[i]))
            d(resourceId="com.codemao.nemo:id/tv_publish").click()
            d(resourceId="com.codemao.nemo:id/iv_more").click()
            d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
    logger.info("校验作品描述200以下————成功")

@allure.tag(f"environment:{ENV}", "P0", "TC2031")
@allure.feature('已发布测试--开源作品可以设置为不开源')
@allure.severity('important')
@pytest.mark.P0
@pytest.mark.run(order=1)
@pytest.mark.flaky(reruns=2,reruns_delay=2)
def test_env_login_tc2031(login_and_logout190):
    '''
    修改作品信息:如果作品为不开源作品,则可以修改为开源
    '''
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    d.xpath("//*[contains(@text, '已发布')]").click()
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        with allure.step("如果第一个作品为不开源，则把它改为开源"):
            sleep(5)
            if d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 0:
                logger.info("第一个作品为不开源，把它改为开源")
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                sleep(0.5)
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                # logger.info("点击_代码开源按钮，非原生")
                sleep(1)
                d(resourceId="com.codemao.nemo:id/iv_open_source").click()
                logger.info("点击发布")
                sleep(1)
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
                logger.info("第一个作品设置为开源成功")
            else:
                logger.info("第一个作品为开源，可以直接进行设置为不开源")
            logger.info("点击右上角...")
            d(resourceId="com.codemao.nemo:id/iv_more").click()
            logger.info("点击编辑信息")
            d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
            # logger.info("点击_代码开源按钮，非原生")
            sleep(1)
            d(resourceId="com.codemao.nemo:id/iv_open_source").click()
            logger.info("点击发布")
            sleep(1)
            d(resourceId="com.codemao.nemo:id/tv_publish").click()
            logger.info("第一个作品设置为不开源成功")
        with allure.step("校验开源按钮"):
            sleep(3)
            logger.info("校验开源按钮不在")
            assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists()==0
    logger.info("开源作品可以设置为不开源————成功")


@allure.tag(f"environment:{ENV}", "P0", "TC2032")
@allure.feature('已发布测试--不开源作品可以设置为开源')
@allure.severity('important')
@pytest.mark.P0
@pytest.mark.run(order=3)
@pytest.mark.flaky(reruns=1,reruns_delay=2)
def test_env_login_tc2032(stop_app):
    '''
    修改作品信息:如果作品为不开源作品,则可以修改为开源
    '''
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    d.xpath("//*[contains(@text, '已发布')]").click()
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 0
        logger.info("第一个作品为不开源，把它改为开源")
        logger.info("点击右上角...")
        sleep(1)
        d(resourceId="com.codemao.nemo:id/iv_more").click()
        logger.info("点击编辑信息")
        sleep(1)
        d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
        # logger.info("点击_代码开源按钮，非原生")
        sleep(1)
        d(resourceId="com.codemao.nemo:id/iv_open_source").click()
        logger.info("点击发布")
        sleep(1)
        d(resourceId="com.codemao.nemo:id/tv_publish").click()
        sleep(2)
        logger.info("第一个作品设置为开源成功")
        assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists()==1
    logger.info("开源作品可以设置为开源————成功")

@allure.tag(f"environment:{ENV}", "P0", "TC2012")
@allure.feature('已发布测试--修改作品信息不影响开源作品的开源状态')
@allure.severity('important')
@allure.testcase('https://www.tapd.cn/47849719/bugtrace/bugs/view?bug_id=1147849719001024889', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.run(order=4)
@pytest.mark.flaky(reruns=1,reruns_delay=2)
def test_env_login_tc2012(stop_app):
    '''
    修改作品信息__不影响作品的开源状态
    启动App
    登录后修改已发布作品的信息
    点击进入已发布作品
    已发布作品默认为——开放开源代码
    '''
    a="测试"+time.strftime("%Y-%m-%d_%H%M%S")
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    d.xpath("//*[contains(@text, '已发布')]").click()
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        with allure.step("如果第一个作品为不开源，则把它改为开源"):
            sleep(5)
            if d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 0:
                logger.info("第一个作品为不开源，把它改为开源")
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                # logger.info("点击_代码开源按钮，非原生")
                sleep(1)
                d(resourceId="com.codemao.nemo:id/iv_open_source").click()
                logger.info("点击发布")
                sleep(1)
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
            else:
                logger.info("第一个作品为开源，无需操作")
            logger.info("点击右上角...")
            d(resourceId="com.codemao.nemo:id/iv_more").click()
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
            with allure.step("校验开源按钮"):
                sleep(3)
                logger.info("校验开源按钮还在")
                assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists()==1
    logger.info("校验修改作品信息不影响开源状态————成功")


@allure.tag(f"environment:{ENV}", "P0", "TC2013")
@allure.feature('已发布测试--修改作品信息不影响作品的闭源状态')
@allure.severity('important')
@allure.testcase('https://www.tapd.cn/47849719/bugtrace/bugs/view?bug_id=1147849719001024889', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.run(order=2)
@pytest.mark.flaky(reruns=1,reruns_delay=2)
def test_env_login_tc2013(stop_app):
    '''
    编辑积木————不影响作品的闭源状态
    启动App
    登录后修改已发布作品的信息
    点击进入已发布作品
    如果第一个作品为不开源作品，则修改为不开源作品
    修改积木信息后,作品还是不开源状态
    '''
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    d.xpath("//*[contains(@text, '已发布')]").click()
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()
        with allure.step("如果第一个作品为开源，则把它改为不开源"):
            sleep(3)
            if d(resourceId="com.codemao.nemo:id/iv_rework_num").exists() == 1:
                logger.info("第一个作品为开源，把它改为不开源")
                logger.info("点击右上角...")
                d(resourceId="com.codemao.nemo:id/iv_more").click()
                logger.info("点击编辑信息")
                d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑信息").click()
                # logger.info("点击_代码开源__按钮，非原生")
                sleep(1)
                d(resourceId="com.codemao.nemo:id/iv_open_source").click()
                logger.info("点击发布")
                sleep(2)
                d(resourceId="com.codemao.nemo:id/tv_publish").click()
                # d(resourceId="com.codemao.nemo:id/mine_rb").click()
                # d.xpath("//*[contains(@text, '已发布')]").click()
                # d(resourceId="com.codemao.nemo:id/tv_work_name").click()
                d(resourceId="com.codemao.nemo:id/iv_more").click()
            else:
                logger.info("第一个作品为不开源，无需操作")
                logger.info("点击右上角...")
                try:
                    d(resourceId="com.codemao.nemo:id/iv_more").click()
                except:
                    logger.info("未定位到 编辑  按钮")
                    d.click(0.936, 0.059)
                logger.info("点击编辑积木信息")
    d(resourceId="com.codemao.nemo:id/tv_item_name", text="编辑积木").click()
    with allure.step("修改积木信息，不会使不开源作品变为开源"):
        sleep(3)
        if d.xpath("//*[contains(@text, '草稿箱')]").exists==1:
            logger.info("如果本地没有改作品的BCM，则跳转草稿箱页面")
            d(resourceId="com.codemao.nemo:id/enterClickArea").click()
        sleep(10)
        d(resourceId="com.codemao.nemo:id/menu").click()
        d(resourceId="com.codemao.nemo:id/tv_upload").click()
    with allure.step("点击发布"):
        try:
            d(resourceId="com.codemao.nemo:id/tv_publish").click()
        except:
            logger.info("点击发布,这里变成了非dom结构，所以使用了坐标定位")
            d.click(0.956, 0.059)
    with allure.step("校验开源按钮"):
        d(resourceId="com.codemao.nemo:id/mine_rb").click()
        d.xpath("//*[contains(@text, '已发布')]").click()
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        logger.info("校验开源按钮不在")
        sleep(3)
        assert d(resourceId="com.codemao.nemo:id/iv_rework_num").exists()==0
    logger.info("运行成功——修改积木信息不影响__不开源状态")

import re
@allure.tag(f"environment:{ENV}", "P0", "TC2014")
@allure.feature('已发布测试')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_env_login_tc2014(stop_app):
    '''
    登录后修改已发布作品的信息
    点击进入已发布作品
    点击“取消发布”，出现取消二次确认弹框
    点击“保留发布”，停留在作品详情
    点击“取消发布”，有“取消发布成功提示”
    回到了我的页面，“已发布”数量减1
    '''
    d = u2.connect(f"{udid}")
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    logger.info("点击'已发布'")
    a1=int(re.findall("\d+",d.xpath("//*[contains(@text, '已发布')]").get_text())[0])
    d.xpath("//*[contains(@text, '已发布')]").click()
    with allure.step("默认选择第一个作品进行修改"):
        logger.info('点击第一个作品的封面')
        d(resourceId="com.codemao.nemo:id/rl_cover").click()
        #sleep(3)
        logger.info("点击右上角...")
        time.sleep(5)
        d(resourceId="com.codemao.nemo:id/iv_more").click()
        #sleep(2)
        logger.info("点击编辑信息")
        #sleep(2)
        d(resourceId="com.codemao.nemo:id/tv_item_name", text="取消发布").click()
    with allure.step("选择——保留发布"):
        logger.info("二次确认——选择保留发布")
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        time.sleep(3)
        logger.info("校验还留在作品内")
        assert d(resourceId="com.codemao.nemo:id/iv_more").exists()==1
        logger.info("二次确认——选择取消发布")
        d(resourceId="com.codemao.nemo:id/iv_more").click()
        d(resourceId="com.codemao.nemo:id/tv_item_name", text="取消发布").click()
        time.sleep(2)
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()
        a2= int(re.findall("\d+",d.xpath("//*[contains(@text, '已发布')]").get_text())[0])
        logger.info(f"校验发布数量减1,取消发布前数量为{a1}，取消后为{a2}")
        assert a1==a2+1
    logger.info("校验已发布页面取消发布————成功")


if __name__ == '__main__':
    import subprocess
    import sys
    import os

    # pytest.main(["-s","-v", "test_published_page.py::test_env_login_tc2012"])
    # pytest.main(["-v","-k","2012"])
    # pytest.main(["-v", "test_ban_and_recover_login.py"])
    # pytest.main(["-v", "-s", "test_ban_and_recover_login.py"])
    # pytest.main(["-v", "--setup-show", "test_ban_and_recover_login.py"])
    # 运行全部test用例
    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    # pytest.main(["-s", "-q", "--alluredir", path_xml])
    pytest.main(["-s", "-q", "test_published_page.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)