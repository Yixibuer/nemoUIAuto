import os
import sys
import pytest
import subprocess
from data.cfg import ENV

# cur = os.path.realpath(__file__)
# print(cur)
#
# cur_path = os.path.dirname(os.path.realpath(__file__))
# print(cur_path)
#
# print(sys.path)
#
# print(sys.path[0])
#
# repath = sys.path[0] + r"\report\xml"
# print(repath)

if __name__ == '__main__':
    # 运行全部test用例
    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹(report文件夹为空时会报错，到时候注释掉即可)
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    pytest.main(["--tb=line", "--alluredir", path_xml])
    # pytest.main(["--ff", "--alluredir", path_xml])
    # 可在path_html目录里使用python -m http.server命令供他人访问报告
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    # 设置allure环境变量参数，要在报告生成前，把environment.properties文件放到报告的xml文件夹里
    file_name = 'environment.properties'
    path_report_env = os.path.join(path_xml, file_name)
    with open(path_report_env, 'w') as file_obj:
        file_obj.write("Environment={}\n".format(ENV))
        file_obj.write("PackageName=com.codemao.nemo\n")
        file_obj.write("ActivityName=com.codemao.nemo.MainActivityV2")
    # 生成报告前把categories.json放到报告的xml文件夹里（通过复制）
    # sys.path[n]在不同环境下可能不同
    path_categories_filename = os.path.join(sys.path[2], r"categories.json")
    subprocess.run(r'copy ' + path_categories_filename + ' ' + path_xml, shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
