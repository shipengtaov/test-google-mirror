#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time
import multiprocessing

import requests

from mirrors import mirrors


def test_url(url):
    try:
        res = None
        start = time.time()
        res = requests.get(url, timeout=5)
        time_cost = time.time() - start
        assert res.ok
        assert '<title>Google</title>' in res.text
        assert '<form' in res.text
        assert '<input' in res.text
        assert 'Google' in res.text
    except:
        pass
    else:
        if res.history:
            msg = []
            for h in res.history + [res]:
                msg.append(h.url)
            msg.append('%fs\n' % time_cost)
            print('  -->  '.join(msg))
        else:
            print('%s  -->  %fs\n' % (url, time_cost))


def main():
    pool = multiprocessing.Pool(multiprocessing.cpu_count()*2)
    pool.map(test_url, mirrors)

if __name__ == '__main__':
    main()
