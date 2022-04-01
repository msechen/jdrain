甘露殿监控脚本仓库 

频道:https://t.me/jdredrain 

库 https://github.com/msechen/jdv5 已经更新安装方式，安装之前确保清空之前映射的文件夹，或者删除重新建立文件夹，包括安装v4bot+jbot-diy,和拉取本库监控脚本，登录后自动监控上面甘露殿频道



===================全新安装上述v4bot+jbot-diy忽略以下步骤=================================

请将脚本放置在/jd/own/raw文件夹，依赖文件magic.js放在/jd/scripts文件夹 

user.py为监控文件，库 https://github.com/msechen/jdv5 安装v4+bot+diybot， 登录原版user.py后

1、pm2 stop jbot停掉jbot \
2、本user.py替换原版user.py \
3、rm -rf user.session \
4、python3 -m jbot \
5、ctrl+c关掉前端jbot，pm2 start jbot 后端运行 user.py
