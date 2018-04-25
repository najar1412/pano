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
        print(config.Config.app_root)
        return True

    def create_thumbnail(self):
        """create thumbnail of pano"""
        return True

    def create_lowres(self):
        """create a low res version of pano"""
        return True

    def create_midres(self):
        """create a mid res version of pano"""
        return True