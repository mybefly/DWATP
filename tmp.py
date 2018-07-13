import json
def cmp_dict(src_data,dst_data):
    assert type(src_data) == type(dst_data),"type: '{}' != '{}'".format(type(src_data), type(dst_data))
    if isinstance(src_data,dict):
        assert len(src_data) == len(dst_data),"dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for key in src_data:
            assert dst_data.has_key(key)
            cmp_dict(src_data[key],dst_data[key])
    elif isinstance(src_data,list):
        assert len(src_data) == len(dst_data),"list len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            cmp_dict(src_list, dst_list)
    else:
        assert src_data == dst_data,"value '{}' != '{}'".format(src_data, dst_data)
a = {'data': {'notification_id': '88'}, 'errcode': 1000, 'errmsg': 'ok', 'ret': 0}
# b = {'data': {'notification_id': '88'}, 'errcode': 1000, 'errmsg': 'ok', 'ret': 0}
print(a.has_key("ret"))
# print(cmp_dict(a,b))