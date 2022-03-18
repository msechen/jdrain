甘露殿监控脚本仓库，请将脚本放置在/jd/own/raw文件夹

user.py为监控文件，库 https://github.com/msechen/jdv5 安装v4+bot+diybot， 登录原版user.py后

1、pm2 stop jbot停掉jbot；
2、本user.py替换原版user.py；
3、rm -rf user.session；
4、python3 -m jbot；
5、ctrl+c关掉前端jbot，pm2 start jbot 后端运行 user.py
