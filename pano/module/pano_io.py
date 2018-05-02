import os
from collections import namedtuple

import config


# examples model
fake_data = {
    'id': 1,
    'name': 'AJ001-VR1-Interior_Office_',
    'desc': 'bla bla bla some text to go with the 360 bla bla bla',
    'pubdate': '04.25.18',
    'thumb': 'default_thumb.jpg',
    'passes': [
        'default_alpha.jpg',
        'default_bg.jpg',
        'default_emissive.jpg',
        'default_fg.jpg',
        ]
}

model_fake_data = {
    'id': 1,
    'name': 'AJ001-VR1-Interior_Office_',
    'desc': 'bla bla bla some text to go with the 360 bla bla bla',
    'pubdate': '04.25.18',
    'thumb': 'default_thumb.jpg',
    'fg': 'default_fg.jpg',
    'alpha': 'default_alpha.jpg',
    'bg': 'default_bg.jpg',
    'emissive': 'default_emissive.jpg'
}

Pano = namedtuple('Pano', 'id, name, desc, pubdate, thumb, fg, alpha, bg, emissive')

def _row(row):
    pano = Pano(row['id'], row['name'], row['desc'], row['pubdate'], row['thumb'], row['fg'], row['alpha'], row['bg'], row['emissive'])
    return pano

def toDict(row):
    return {
        'id': row.id,
        'name': row.name,
        'desc': row.desc,
        'pubdate': row.pubdate,
        'thumb': row.thumb,
        'fg': row.fg,
        'alpha': row.alpha,
        'bg': row.bg,
        'emissive': row.emissive
    }



class PanoIo():
    """Manages all interaction with server io
    for tasks related to Panos"""

    def save_to_server(self):
        """save panos to server"""
        return True


    def get_all_from_server(self):
        """retrives all panos from server"""
        panos = [
            {
                'id': 1,
                'name': 'AJ001-VR1-Interior_Office_',
                'desc': 'bla bla bla some text to go with the 360 bla bla bla',
                'pubdate': '04.25.18',
                'thumb': 'default_thumb.jpg',
                'passes': [
                    'default_alpha.jpg',
                    'default_bg.jpg',
                    'default_emissive.jpg',
                    'default_fg.jpg',
                    ]
            },
            {
                'id': 2,
                'name': 'AJ001-VR1-Interior_Office_',
                'desc': 'bla bla bla some text to go with the 360 bla bla bla',
                'pubdate': '04.25.18',
                'thumb': 'default_thumb.jpg',
                'passes': [
                    'default_alpha.jpg',
                    'default_bg.jpg',
                    'default_emissive.jpg',
                    'default_fg.jpg',
                    ]
            },
            {
                'id': 3,
                'name': 'AJ001-VR1-Interior_Office_',
                'desc': 'bla bla bla some text to go with the 360 bla bla bla',
                'pubdate': '04.25.18',
                'thumb': 'default_thumb.jpg',
                'passes': [
                    'default_alpha.jpg',
                    'default_bg.jpg',
                    'default_emissive.jpg',
                    'default_fg.jpg',
                    ]
            },
            {
                'id': 4,
                'name': 'AJ001-VR1-Interior_Office_',
                'desc': 'bla bla bla some text to go with the 360 bla bla bla',
                'pubdate': '04.25.18',
                'thumb': 'default_thumb.jpg',
                'passes': [
                    'default_alpha.jpg',
                    'default_bg.jpg',
                    'default_emissive.jpg',
                    'default_fg.jpg',
                    ]
            }
        ]

        return panos


    def create_thumbnail(self):
        """create thumbnail of pano"""
        return True


    def create_lowres(self):
        """create a low res version of pano"""
        return True


    def create_midres(self):
        """create a mid res version of pano"""
        return True


class PanoDb():
    def get(self, id):
        return toDict(_row(model_fake_data))

    def all(self):
        return []
