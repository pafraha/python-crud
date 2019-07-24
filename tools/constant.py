# -*- coding:utf-8 -*-
__author__ = "qq"
__date__ = "2019.1.2"
__doc__ = "通用常数"

NOT_AUTH_API = ('/', '/auth/login', '/auth/type', '/login', '/login/', '/logout', '/logout/', '/static')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bmp'}
ALLOWED_STATUS = (100, 200, 201, 202, 300, 301, 302, 400, 401, 402, 500, 501, 502, 503)

OK = 1000
DB_ERR = 1001  # DB 错误
LOGIN_FAIL = 1002  # 登录错误
SERVER_ERR = 1003  # 服务器错误
AUTH_FAIL = 1004
NO_TOKEN = 1005
NO_USER = 1006
USER_EXISTS = 1007
PARAM_ERR = 1008
FILE_ILLEGAL = 1009
