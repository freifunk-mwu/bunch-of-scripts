#!/usr/bin/env python3
'''
To create configuration for tinc, a git hook script is used.

**icvpn-tinc-post-merge**

.. literalinclude:: ../../icvpn-tinc-post-merge
    :language: bash
    :linenos:

'''
from common import pinit


def update_tinc_conf():
    '''
    Pulls updates from the
    `freifunk icvpn repo <https://github.com/freifunk/icvpn>`_ for tinc.
    '''
    photon, settings = pinit('update_tinc_conf', verbose=True)

    photon.git_handler(
        settings['icvpn']['tinc']['local'],
        remote_url=settings['icvpn']['tinc']['remote']
    )._pull()


if __name__ == '__main__':
    update_tinc_conf()
