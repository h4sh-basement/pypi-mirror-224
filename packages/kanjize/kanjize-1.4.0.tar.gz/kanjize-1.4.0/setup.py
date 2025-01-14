"""
Easy converter between Kanji-Number and Integer
-----------
Powered by [Yamato Nagata](https://twitter.com/514YJ)

[GitHub](https://github.com/nagataaaas/Kanjize)

Can Convert Number up to 10 ** 72 - 1

```python
from kanjize import number2kanji, kanji2number, Number

print(number2kanji(58076099))
    # 五千八百七万六千九十九

print(kanji2number("五千八百七万六千九十九"))
    # 58076099

print(kanji2number("223兆4千億4256万6千"))
    # 223400042566000

print(kanji2number("223兆4000億4256万6000"))
    # 223400042566000

print(number2kanji(223400042566000, style="mixed", kanji_thousand=False))
    # 223兆4000億4256万6000

print(number2kanji(223400042566000, style="mixed"))
    # 223兆4千億4256万6千

print((Number.from_kanji("223兆4千億4256万6千") * Number(2.3)).to_kanji(style="mixed"))
    # 446兆8千億8513万2千
```
"""

from setuptools import setup
from os import path

about = {}
with open("kanjize/__about__.py") as f:
    exec(f.read(), about)

here = path.abspath(path.dirname(__file__))

setup(name=about["__title__"],
      version=about["__version__"],
      url=about["__url__"],
      license=about["__license__"],
      author=about["__author__"],
      author_email=about["__author_email__"],
      description=about["__description__"],
      long_description=__doc__,
      long_description_content_type="text/markdown",
      packages=["kanjize"],
      zip_safe=False,
      platforms="any",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ])
