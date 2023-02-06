__title__ = 'pger'
__author__ = 'foyou'
__version__ = '0.0.1'

import argparse

from pger.pypi import PyPI


def main():
    epilog = f'%(prog)s({__version__}) by foyou(https://github.com/foyoux/pger)'
    parser = argparse.ArgumentParser(prog='pger', description='python package generator', epilog=epilog)
    parser.add_argument('-v', '--version', action='version', version=epilog)

    parser.add_argument('user', help='github username')
    parser.add_argument('--repo', help='github repository')
    parser.add_argument('--package', help='python package name -> src/<package>/__init__.py')

    args = parser.parse_args()
    user = args.user
    if '/' in user:
        user, repo = user.split('/')
    else:
        repo = args.repo

    if not repo:
        print('repo not specify and first arg not contains repo')
        return

    package = args.package
    if package is None and '-' not in repo:
        package = repo
    else:
        print(f'package not specify and repo contains "-"')
        return

    pkg = PyPI(user, repo, package)
    pkg.generate()
