#!/usr/bin/env python3

from common import pinit


def sync_ffapi():
    photon, settings = pinit('sync_ffapi', verbose=True)

    for community in settings['common']['communities']:
        git = photon.git_handler(
            settings['ffapi'][community]['local'],
            remote_url=settings['ffapi'][community]['remote']
        )
        git.cleanup

        git.publish


if __name__ == '__main__':
    sync_ffapi()
