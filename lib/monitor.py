#coding:utf-8

import memcache

ips = ['10.32.39.142:11218']

client = memcache.Client(ips)

print client.get_stats()
