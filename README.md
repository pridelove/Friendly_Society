本程序是用于批量管理你自己的小号,自动化进行每日友爱社任务的自动完成,本程序只供学习使用,请勿使用于违法途径

Batch_consent.py是24小时 自动帮你审核通过其他小伙伴申请加入你的友爱社,避免他们过长的等待,需要副会长或者会长的Cookie

Fridendly_society.py 是友爱社日常任务的主模块,实现日常功能

Friendly_society_main.py 运行程序

使用方法:

	1.如果自己是副会,可以获得自己电脑端的Cookie,要问如何获取?F12大法,把获取的Cookie放入 Batch_consent.py Ck=''中,然后运行
	
	2.如果有多个账号需要管理,获取每个账号的App端和Pc端的Cookie进行存放
	格式例	如:access_token=1cee75d1e4abdac5990994fcba8e3b21;refresh_token=37924c4ae79d352f8f9ca469bc032721;bili_jct=fd584f9081e2503a65fcaddbf36954b9;DedeUserID=471433885;DedeUserID__ckMd5=74625122ffdbe521;sid=a6iwqb41;SESSDATA=33c3006f%2C1584951691%2C5a382921
	按照每行存在在cookies.txt
	
	3.获取你自己的友爱社id,需要一点的抓包知识,用自己的其他账号加入友爱社,然后看参数,union的参数就是友爱社id,然后在Friendly_Society.py中 的union_id=中填入你的友爱社id
	
	4.设置多账号一次进入友爱社的数量,在Friendly_society_main.py中开头的num中填入数字,然后双击运行即可
	基本都有些注释~直接看注释也直观明了~
