#!/usr/bin/env python3
"""
rusda 二进制层去特征补丁器（移植自 taisuii/rusda topatch.py 的等长反转/替换）
用法: python3 rusda_patch.py <in.so> <out.so>
不依赖 lief，纯字节等长替换，不动 ELF 布局。
"""
import sys

MAP = [
    (b'FridaScriptEngine', b'enignEtpircSadirF'),
    (b'GLib-GIO',          b'OIG-biLG'),
    (b'GDBusProxy',        b'yxorPsuBDG'),
    (b'GumScript',         b'tpircSmuG'),
    (b'gum-js-loop',       b'russellloop'),
    (b'gmain',             b'rmain'),
    (b'gdbus',             b'rubus'),
]

def main():
    src, dst = sys.argv[1], sys.argv[2]
    d = bytearray(open(src, 'rb').read())
    total = 0
    for a, b in MAP:
        assert len(a) == len(b)
        n = d.count(a)
        d = d.replace(a, b)
        total += n
        print('%-20s -> %-20s %d' % (a.decode(), b.decode(), n))
    open(dst, 'wb').write(d)
    print('total', total, 'size', len(d))

if __name__ == '__main__':
    main()
