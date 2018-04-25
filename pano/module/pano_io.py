import os

import config

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
                'thumb': 'AJ001-VR1-Interior_Office_thumb.jpg',
                'passes': [
                    'AJ001-VR1-Interior_Office_alpha.jpg',
                    'AJ001-VR1-Interior_Office_bg.jpg',
                    'AJ001-VR1-Interior_Office_emission.jpg',
                    'AJ001-VR1-Interior_Office_fg.jpg',
                    ]
            },
            {
                'id': 2,
                'name': 'AJ001-VR1-Interior_Office_',
                'desc': 'bla bla bla some text to go with the 360 bla bla bla',
                'pubdate': '04.25.18',
                'thumb': 'AJ001-VR1-Interior_Office_thumb.jpg',
                'passes': [
                    'AJ001-VR1-Interior_Office_alpha.jpg',
                    'AJ001-VR1-Interior_Office_bg.jpg',
                    'AJ001-VR1-Interior_Office_emission.jpg',
                    'AJ001-VR1-Interior_Office_fg.jpg',
                    ]
            },
            {
                'id': 3,
                'name': 'AJ001-VR1-Interior_Office_',
                'desc': 'bla bla bla some text to go with the 360 bla bla bla',
                'pubdate': '04.25.18',
                'thumb': 'AJ001-VR1-Interior_Office_thumb.jpg',
                'passes': [
                    'AJ001-VR1-Interior_Office_alpha.jpg',
                    'AJ001-VR1-Interior_Office_bg.jpg',
                    'AJ001-VR1-Interior_Office_emission.jpg',
                    'AJ001-VR1-Interior_Office_fg.jpg',
                    ]
            },
            {
                'id': 4,
                'name': 'AJ001-VR1-Interior_Office_',
                'desc': 'bla bla bla some text to go with the 360 bla bla bla',
                'pubdate': '04.25.18',
                'thumb': 'AJ001-VR1-Interior_Office_thumb.jpg',
                'passes': [
                    'AJ001-VR1-Interior_Office_alpha.jpg',
                    'AJ001-VR1-Interior_Office_bg.jpg',
                    'AJ001-VR1-Interior_Office_emission.jpg',
                    'AJ001-VR1-Interior_Office_fg.jpg',
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