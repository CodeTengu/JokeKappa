# coding: utf-8

from __future__ import print_function
from __future__ import unicode_literals

from io import open
import glob
import json
import os
import random
import sys

import requests


JOKE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'jokes/'))


def load_from_file(filepath):
    with open(filepath) as f:
        try:
            jokes = json.load(f)
        except ValueError:
            jokes = []
    return jokes


def get_jokes(sources='*'):
    if isinstance(sources, str):
        sources = [sources, ]

    jokes = []
    for source in sources:
        for filepath in glob.glob('{0}/{1}.json'.format(JOKE_DIR, source)):
            jokes += load_from_file(filepath)

    if not jokes:
        raise RuntimeError('No joke')

    return jokes


def get_joke(sources='*'):
    jokes = get_jokes(sources)
    joke = random.choice(jokes)
    return joke


def update_jokes():
    update_jokes_for_codetengu_weekly()


def update_jokes_for_codetengu_weekly():
    filepath = os.path.join(JOKE_DIR, 'codetengu_weekly.json')
    jokes = load_from_file(filepath)

    url = 'https://lfsfm1czqg.execute-api.ap-northeast-1.amazonaws.com/v1/issues'
    headers = {
        'x-api-key': '8Z8ZS06vR4a9XdYdimVio9C5LYjbtJBh2uDWcMjB',  # quota: 100000 requests per month
        'Content-Type': 'application/json',
    }
    req = requests.get(url, headers=headers)
    if req.ok:
        res = req.json()
        for issue in res['items']:
            if any(d['issue_number'] == issue['number'] for d in jokes):
                break
            joke = {
                'content': issue['title'],
                'issue_number': issue['number'],
            }
            jokes.append(joke)

        jokes = sorted(jokes, key=lambda d: d['issue_number'], reverse=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json.dumps(jokes, ensure_ascii=False, sort_keys=True, indent=4))
    else:
        print(req.content)
        sys.exit(1)
