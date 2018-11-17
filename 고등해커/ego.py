import hashlib
i = input().strip()
k = hashlib.new('md5')
k.update(i.encode())
if i.split('_') == ['Sunrin{this', 'is', 'flag', '', 'lool', '', '}'] and k.digest() == 'Y\xa8\x07-P$\xdc\xcc\x02C\x1a#\xf5\xc4\xd1\x97':
    print('OK')
else:
    print('NOPE')
# okay decompiling Ego.pyc

#Sunrin{this_is_flag__lool__}