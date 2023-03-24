import os
import getpass

# 宽带连接名称
connection_name = "宽带连接"

# 尝试从文件中读取用户账号和密码
try:
    with open("pppoe.txt", "r") as f:
        username, password = f.readline().strip().split(",")
except FileNotFoundError:
    username, password = "", ""

# 如果未保存用户账号和密码，则提示用户输入
if not username:
    username = input("请输入宽带账号：")
if not password:
    password = getpass.getpass("请输入宽带密码：")

# 创建 PPPoE 连接
os.system("rasdial {} /disconnect".format(connection_name))
os.system("rasdial {} {} {}".format(connection_name, username, password))

# 保存用户账号和密码
with open("pppoe.txt", "w") as f:
    f.write("{},{}".format(username, password))
