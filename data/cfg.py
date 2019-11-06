import subprocess


'''
未被注释的即为当前环境
'''
# ENV = 'dev'
ENV = 'test'
# ENV = 'staging'
# ENV = 'release'


if ENV == 'dev':
    mao = 'backend-dev.codemao.cn'   #dev环境
    AdminMao = 'dev-backstage-nemo.codemao.cn'   #dev环境
elif ENV == 'test':
    mao = 'test-api.codemao.cn'     #test环境
    AdminMao = 'test-backstage-nemo.codemao.cn'     #test环境
elif ENV == 'staging':
    mao = 'backend-test.codemao.cn'  #staging环境
    AdminMao = 'staging-backstage-nemo.codemao.cn'  #staging环境
elif ENV == 'release':
    mao = 'api.codemao.cn'      #release环境
    AdminMao = 'backstage-nemo.codemao.cn'      #release环境

# mao = 'test-api.codemao.cn'     #test环境
# mao = 'backend-dev.codemao.cn'   #dev环境
# mao = 'backend-test.codemao.cn'  #staging环境
# mao = 'api.codemao.cn'      #release环境

# AdminMao = 'test-backstage-nemo.codemao.cn'     #test环境
# AdminMao = 'dev-backstage-nemo.codemao.cn'   #dev环境
# AdminMao = 'staging-backstage-nemo.codemao.cn'  #staging环境
# AdminMao = 'backstage-nemo.codemao.cn'      #release环境


username166 = "16675197301"
password166 = "123456"
pid = "T5qx9_w0"

username183 = "18319138088"
password183 = "123456"

username183001 = "18319138088001"
password183001 = "123456"

#运营token
adminToken = "Bearer {}".format("eyJhbGciOiJIUzI1NiIsInR5cCI6Ik"
                                    "pXVCJ9.eyJ1c2VyX2lkIjoxMzYsInVzZXJfdHlwZSI6ImFkbWluIiwi"
                                    "anRpIjoiNDNkMjEyMWUtM2JkYy00YWJjLTkwOTYtYzMzMDg0OGRlZWEwIiw"
                                    "iaWF0IjoxNTM3MjU2MTMzfQ.mXgihczgjH3K1yLAu-ESFB8Ou0Oc7GBDV3zBe7dCqEk")

'''
获取连接电脑的UDID，注意只能获取排名第一的那个机器的udid，如有多个手机一起连接电脑时
'''

pudid = subprocess.getstatusoutput("adb devices")
pudid = list(pudid)
# print(pudid[1].split('\n')[1].split(' ')[0].split('\t')[0])
# print(pudid[1].split('\t')[0].split('\n')[1])

udid = pudid[1].split('\t')[0].split('\n')[1]