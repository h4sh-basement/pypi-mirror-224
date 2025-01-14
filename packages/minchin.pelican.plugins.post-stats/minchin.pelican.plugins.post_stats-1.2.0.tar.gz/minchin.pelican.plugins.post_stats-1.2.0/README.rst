===============
Post Statistics
===============

``Post Stats`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Post Stats`` calculates various statistics about a post and store them in
an article.stats dictionary:

- ``wc``: how many words
- ``read_mins``: how many minutes would it take to read this article, based
  on 250 wpm
  (`source <http://en.wikipedia.org/wiki/Words_per_minute#Reading_and_comprehension>`_)
- ``word_counts``: frquency count of all the words in the article; can be
  used for tag/word clouds
- ``fi``: Flesch-Kincaid Index/Reading Ease
  (`more info <http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests>`_)
- ``fk``: Flesch-Kincaid Grade Level


.. image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.post-stats.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.post-stats/
    :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success
   :target: https://github.com/MinchinWeb/minchin.pelican.plugins.post_stats/blob/master/CHANGELOG.rst
   :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.plugins.post-stats?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.post-stats/
    :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.plugins.post-stats.svg?style=flat&color=green
    :target: https://github.com/MinchinWeb/minchin.pelican.plugins.post_stats/blob/master/LICENSE.txt
    :alt: License

.. image:: https://img.shields.io/pypi/dm/minchin.pelican.plugins.post-stats.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.post-stats/
    :alt: Download Count


Installation
============

The easiest way to install ``Post Stats`` is through the use of pip. This
will also install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.post_stats

On Pelican versions 4.5 and later, the plugin will automatically activate
itself!

You may also need to configure your template to make use of the statistics
generated.


Requirements
============

``Post Stats`` depends on (and is really only useful with) Pelican. The
plugin also requries Beautiful Soup 4 to process your content. If the plugin
is installed from pip, these will automatically be installed. These can also
be manually installed with pip:

.. code-block:: sh

   pip install pelican
   pip install beautifulsoup4



Configuration and Usage
=======================

This plugin calculates various statistics about a post and store them in
an article.stats dictionary.

Example:

.. code-block:: python

    {
        'wc': 2760,
        'fi': '65.94',
        'fk': '7.65',
        'word_counts': Counter({u'to': 98, u'a': 90, u'the': 83, u'of': 50, ...}),
        'read_mins': 12
    }

This allows you to output these values in your templates, like this, for
example:

.. code-block:: html+jinja

	<p title="~{{ article.stats['wc'] }} words">~{{ article.stats['read_mins'] }} min read</p>
	<ul>
	    <li>Flesch-kincaid Index/ Reading Ease: {{ article.stats['fi'] }}</li>
	    <li>Flesch-kincaid Grade Level: {{ article.stats['fk'] }}</li>
	</ul>

The ``word_counts`` variable is a python ``Counter`` dictionary and looks
something like this, with each unique word and it's frequency:

.. code-block:: python

	Counter({u'to': 98, u'a': 90, u'the': 83, u'of': 50, u'karma': 50, .....

and can be used to create a tag/word cloud for a post.

There are no user-configurable settings.


Credits
=======

`Original plugin <http://duncanlock.net/blog/2013/06/23/post-statistics-plugin-for-pelican/>`_
by Duncan Lock (`@dflock <https://github.com/dflock>`_) and
posted to the `Pelican-Plugins repo
<https://github.com/getpelican/pelican-plugins>`_.


License
=======

The plugin code is assumed to be under the AGPLv3 license (this is the
license of the Pelican-Plugins repo).
