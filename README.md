# pger

python package generator

> https://packaging.python.org/en/latest/tutorials/packaging-projects
>
> https://setuptools.pypa.io/en/latest

## pger 可以做什么

1. 新建一个 github python 项目，并集成 github action
2. 使能够在推送 tag 时，自动创建 release，并推送 build 的文件到 release assets
3. 自动发布到 python package index(https://pypi.org/)

## 安装

```sh
pip install -U pger

# 或

pip install git+https://github.com/foyoux/pger.git
```

## 用法

```sh
# 获取帮助
pger -h/--help

# 基本用法
pger foyoux/pger
pger foyoux -r pger
pger foyoux --repo foyou-wilk

# 默认 repo 当做主包名，替换 "-" 为 "_" -> src/<repo>/__init__.py，但 repo 允许以非字母开头，但包名不可以
# 此时可指定 -p/--package 选项手动指定主包名
pger -p ticket foyoux/12306
```

## github config

> The example above uses the new [API token](https://pypi.org/help/#apitoken) feature of PyPI, which is recommended to
> restrict the access the action has.
>
> The secret used in ${{ secrets.PYPI_API_TOKEN }} needs to be created on the settings page of your project on GitHub.
> See [Creating & using secrets](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets)