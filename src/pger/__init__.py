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
    parser.add_argument('-r', '--repo', help='github repository')
    parser.add_argument('-p', '--package', help='python package name -> src/<package>/__init__.py')

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
    if package is None:
        if not repo[0].isalpha():
            print(f"package not specify and repo can\'t convert to package name, "
                  f"\nbecause repo doesn't start with the alpha")
            return
        else:
            package = repo.replace('-', '_')

    pkg = PyPI(user, repo, package)
    output = pkg.generate()

    print(f'🎉 Generate github repository ready at {output.absolute()}')
