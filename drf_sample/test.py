#!/usr/bin/env python3
import sys

sys.path.append('/fan/')

from fan.contrib.kazoo.discovery import KazooDiscovery
from fan.transport import HTTPTransport

kd = KazooDiscovery('zk')
kd.on_start()
print('CHILDS: {}'.format(kd.zk.get_children('/endpoints/app/author/1.0.0/')))

kd.transport_classes = {
    'http': HTTPTransport,
}

ep = kd.find_endpoint('app.author', None)
ctx = None
print('EP: {}'.format(ep))

cr = ep.perform_call(ctx, 'create', name='lol')
print('create: {}'.format(cr))

lst = ep.perform_call(ctx, 'list')
print('Lst: {}'.format(lst))

u = lst[0]
u['name'] = 'new name'
up = ep.perform_call(ctx, 'update', **u)

print('Update: {}'.format(up))

for l in lst:
    dl = ep.perform_call(ctx, 'delete', **l)
    print('Dl: {}'.format(dl))
