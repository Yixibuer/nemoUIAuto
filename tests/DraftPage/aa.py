import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog
from time import sleep
from tests.hzj.read_excel import read_excel

test_datas=list(read_excel('从模板创作.xlsx','data'))
logger = MyLog().getlog()


def test_env_draft_twelve():
    '''
    登录成功后，通过‘从模板创作’创建‘丛林爬爬’可以成功
    '''
    d = u2.connect(f"{udid}")

    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    for test_num in test_datas:
        j = test_num['num']
        index =test_num['index']
        tv_name = test_num['name']
        tv_content = test_num['content']

        with allure.step("点击+进入创作页面"):
            logger.info('点击+按钮')
            d(resourceId="com.codemao.nemo:id/createBtn").click()
        with allure.step("选择边学边做"):
            sleep(3)
            logger.info('选择“从模板创建”')
            d(resourceId="com.codemao.nemo:id/item2_name").click()

        with allure.step('进入从模板创作页面'):
            logger.info('从模板创做‘{}’'.format(tv_name))
            for i in range(0,j-1):
                d.swipe_ext("left", scale=0.8)
                sleep(3)
            logger.info('右滑{}次'.format(j))
            print(d(resourceId='com.codemao.nemo:id/index').get_text(), index)
            print(d(resourceId='com.codemao.nemo:id/tv_name').get_text(), tv_name)
            print(d(resourceId='com.codemao.nemo:id/tv_content').get_text(), tv_content)
            assert d(resourceId='com.codemao.nemo:id/index').get_text() == index
            assert d(resourceId='com.codemao.nemo:id/tv_name').get_text() == tv_name
            assert d(resourceId='com.codemao.nemo:id/tv_content').get_text() == tv_content
            logger.info('点击“立即创作”')
            d(resourceId="com.codemao.nemo:id/tv_enter").click()
            sleep(5)
            logger.info('点击“菜单”')
            d(resourceId="com.codemao.nemo:id/menu").click()
            sleep(2)
            logger.info('点击“退出”')
            d(resourceId="com.codemao.nemo:id/tv_quit").click()
            sleep(2)
            logger.info('点击“好的”')
            d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        draft_id = d.xpath('//*[@text="{}-副本"]'.format(tv_name))
        assert draft_id.wait()
        logger.info('{}-副本'.format(tv_name))
        assert draft_id.get_text() == "{}-副本".format(tv_name)
        print('aa')


a=test_env_draft_twelve()
