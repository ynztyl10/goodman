#coding=utf-8

SUCCESS = 0    #请求成功

# 通用错误
PARAMS_NULL = 9001  #参数错误
UNKNOW_ERROR = 9999 #未知错误
DATA_SEPERATOR = '|'
# 用户方面错误1xxx
USERNAME_ERROR = 1000    #用户名错误
PASSWORD_ERROR = 1001    #用户密码错误


#配置错误2xxx
ENGINE_NOT_SUPPORT = 2000    #不支持的引擎
#RESOURCE_NOTFOUND = 2001    #资源不存在