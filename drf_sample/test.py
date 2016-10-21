#!/usr/bin/env python3
import sys
sys.path.append('/fan/')

from fan.sync import get_context  # noqa

ctx = get_context()

author = ctx.rpc.app.author

cr = author.create(name='lol')
print('create: {}'.format(cr))

lst = ctx.rpc.app.author.list()
print('list: {}'.format(lst))

u = lst[0]
u['name'] = 'new name'

up = author.update(**u)
print('update: {}'.format(up))

lst = ctx.rpc.app.author.list()
print('list2: {}'.format(lst))

for l in lst:
    dl = author.delete(**l)
    print('delete: {} => {}'.format(l, dl))


def print_span(span):
    ctx = span.context
    ctx_row = [ctx.trace_id, ctx.span_id, ctx.sampled]
    print('Span: {} {}'.format(ctx_row, span.parent_id))

recorder = ctx.discovery.tracer.recorder
for span in recorder.get_spans():
    print_span(span)
