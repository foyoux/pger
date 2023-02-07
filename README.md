# pger

python package generator

> https://packaging.python.org/en/latest/tutorials/packaging-projects/
>
> https://setuptools.pypa.io/en/latest/

## pger 可以做什么

1. 新建一个 github python 项目，并集成 github action
2. 使能够在推送 tag 时，自动创建 release，并推送 build 的文件到 release assets
3. 自动发布到 python package index(https://pypi.org/)

## 用法

```sh
pip install pger
pger foyoux/pger
pger foyoux --repo pger
# 默认 repo 当做主包名 -> src/<repo>/__init__.py，但 repo 允许包含 "-"，但包名不可以
pger --package wilk foyoux/foyou-wilk
```
