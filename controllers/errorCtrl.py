#coding=utf-8

class ErrorCtrl(object):
    """docstring for ErrorCtrl"""
    @classmethod
    def get_error(cls,error_num):
        
        res = {
            'errno' : error_num
        }
        return res
