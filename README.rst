JokeKappa
=========

A library for delivering one-line programming jokes. Humor is a solemn thing, you should take it seriously.

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
    print(joke['content])

    for joke in jokekappa.get_jokes():
        print(joke['content])
