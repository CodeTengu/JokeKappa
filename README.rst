JokeKappa
=========

.. image:: https://img.shields.io/travis/CodeTengu/JokeKappa/master.svg?style=flat-square
    :target: https://travis-ci.org/CodeTengu/JokeKappa

.. image:: https://img.shields.io/pypi/v/jokekappa.svg?style=flat-square
    :target: https://pypi.python.org/pypi/jokekappa

A library for delivering one-line programming jokes (mostly in Chinese). Humor is a solemn thing, you should take it seriously.

Inspired by `pyjokes <https://github.com/pyjokes/pyjokes>`_.

Installation
============

.. code-block:: bash

    $ pip install jokekappa

Usage
=====

In command-line interface:

.. code-block:: bash

    $ jokekappa
    小明白天只是一名普通的軟體工程師，但是只要一到了夜晚，他就會搖身一變，成為一名加班的軟體工程師

    $ jokekappa all
    Hadoop 工程師睡不著的時候都會 Map/Reduce 羊
    新來的 Designer 趁特價的時候幫自己買了一本 GoF Design Patterns
    不能信任那些 Terminal 或編輯器用白底的人
    ...

    $ jokekappa update

In Python:

.. code-block:: python

    import jokekappa

    joke = jokekappa.get_joke()
    print(joke['content'])
    # ♫ 每條大街小巷，每個工程師的嘴裡，見面第一句話，就是不要 Deploy ♫

    for joke in jokekappa.get_jokes():
        print(joke['content'])
        # 我早年都是用 vim 寫程式，也說不上特別喜歡，主要是當時還不知道怎麼退出 vim
