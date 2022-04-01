甘露殿监控脚本仓库 

频道:https://t.me/jdredrain 

库 https://github.com/msechen/jdv5 已经更新安装方式，安装之前确保清空之前映射的文件夹，或者删除重新建立文件夹，包括安装v4bot+jbot-diy,和拉取本库监控脚本，登录后自动监控上面甘露殿频道


监控关键字-----------监控活动名称-----------监控脚本                    
computer_activityId---电脑配件---jd_computer.js \
comm_activityIDList---jdjoy_open通用ID任务---jd_joyjd_open.js \
jd_mhurlList---盲盒任务抽京豆---jd_mhtask.js \
jd_nzmhurl---女装盲盒抽京豆---jd_nzmh.js \
wish_appIdArrList---许愿池抽奖机---jd_wish.js \
jd_redrain_url---整点京豆雨---jd_redrain.js \
jd_redrain_half_url---半点京豆雨---jd_redrain_half.js \
M_WX_COLLECT_CARD_URL---集卡任务---m_jd_wx_collectCard.js \
jd_cjhy_activityId---cj组队瓜分---jd_cjzdgf.js \
jd_zdjr_activityId---lz组队瓜分---jd_zdjr.js \
VENDER_ID---入会开卡领豆---jd_OpenCard_Force.js \
WXGAME_ACT_ID---打豆豆游戏---jd_doudou.js \
SHARE_ACTIVITY_ID---分享有礼---jd_share.js \
welfare---联合关注+加购+分享领豆---fav_and_addcart.js \
M_FOLLOW_SHOP_ARGV---M关注有礼---m_jd_follow_shop.js \
M_WX_LUCK_DRAW_URL---M幸运抽奖---m_jd_wx_luckDraw.js \
M_WX_ADD_CART_URL---M加购有礼---m_jd_wx_addCart.js



==========全新安装上述v4bot+jbot-diy忽略以下步骤==========

请将脚本放置在/jd/own/raw文件夹，依赖文件magic.js放在/jd/scripts文件夹 

user.py为监控文件，库 https://github.com/msechen/jdv5 安装v4+bot+diybot， 登录原版user.py后

1、pm2 stop jbot停掉jbot \
2、本user.py替换原版user.py \
3、rm -rf user.session \
4、python3 -m jbot \
5、ctrl+c关掉前端jbot，pm2 start jbot 后端运行 user.py
