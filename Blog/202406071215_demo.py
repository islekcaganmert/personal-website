from .Super import Super
from datetime import datetime
import os

data = {
    'id': os.path.basename(__file__).split('-')[1].removesuffix('.py'),
    'title': 'Demo',
    'content': 'This is a demo article on my website.',
    'datetime': datetime.strptime(os.path.basename(__file__).split('-')[0].split('/')[-1], '%Y%m%d%H%M')
}


get = Super(data).get
