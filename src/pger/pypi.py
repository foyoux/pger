import os.path
from pathlib import Path
from textwrap import dedent

from pger import const


class PyPI:

    def __init__(self, user, repo, package, output=None):
        self.user = user
        self.repo = repo
        self.package = package
        self.output = Path(os.path.abspath(output) if output else repo)
        self.output.mkdir(parents=True, exist_ok=True)
        self.src = self.output / 'src'
        (self.src / package / const.TEMPLATES).mkdir(parents=True, exist_ok=True)
        self.tests = self.src / 'tests'
        self.workflows = self.output / '.github/workflows'
        self.workflows.mkdir(parents=True, exist_ok=True)
        self.pkg = self.src / package
        self.pkg.mkdir(parents=True, exist_ok=True)

    def manifest(self):
        (self.output / const.MANIFEST).write_text(
            (const.templates / const.MANIFEST).read_text().format(**self.__dict__)
        )

    def pyproject(self):
        (self.output / const.PYPROJECT).write_text(
            (const.templates / const.PYPROJECT).read_text().format(**self.__dict__)
        )

    def publish(self):
        (self.workflows / const.PUBLISH).write_text(
            (const.templates / const.PUBLISH).read_text()
        )

    def readme(self):
        (self.output / const.README).write_text(
            (const.templates / const.README).read_text().format(**self.__dict__)
        )

    def requirements(self):
        (self.output / const.REQUIREMENTS).write_text('')

    def started(self):
        (self.workflows / const.STARTED).write_text((const.templates / const.STARTED).read_text())

    def update(self):
        (self.workflows / const.UPDATE).write_text(
            (const.templates / const.UPDATE).read_text().replace('<package>', self.package)
        )

    def main(self):
        (self.pkg / const.MAIN).write_text(dedent(f"""
        from {self.package} import main

        if __name__ == '__main__':
            main()
        """).lstrip())

    def init(self):
        (self.pkg / const.INIT).write_text(dedent(f"""
        __title__ = '{self.repo}'
        __author__ = '{self.user}'
        __version__ = '0.0.1'

        import argparse


        def main():
            epilog = f'%(prog)s({{__version__}}) by {self.user}(https://github.com/{self.user}/{self.repo})'
            parser = argparse.ArgumentParser(prog='{self.repo}', description='', epilog=epilog)
            parser.add_argument('-v', '--version', action='version', version=epilog)
        
            parser.parse_args()
        """).lstrip())

    def gen_tests(self):
        self.tests.mkdir(parents=True, exist_ok=True)
        (self.tests / const.INIT).write_text('')
        (self.tests / const.CONFTEST).write_text(
            (const.templates / const.CONFTEST).read_text()
        )

    def generate(self):
        self.manifest()
        self.pyproject()
        self.publish()
        self.readme()
        self.requirements()
        self.started()
        self.update()
        self.main()
        self.init()
        self.gen_tests()
        return self.output
