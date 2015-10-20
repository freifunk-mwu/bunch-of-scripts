#!/usr/bin/env python3

from common import pinit


def update_tinc_conf():
    photon, settings = pinit('update_tinc_conf', verbose=True)

    photon.git_handler(
        settings['icvpn']['tinc']['local'],
        remote_url=settings['icvpn']['tinc']['remote']
    )._pull()

if __name__ == '__main__':
    update_tinc_conf()
