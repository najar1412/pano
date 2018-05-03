from collections import namedtuple
import os
import shutil

import config


def js_object(request_form, fieldname='javascript_data'):
    """ parses javascript object from flask request, 
    to a dict
    request_form: object, flask request object from a form post
    fieldname: str, name of javascript key(?)
    
    return: dict
    """
    jsObject = request_form.to_dict(flat=False)
    result = {}

    for k, v in jsObject.items():
        result[k[16:-1]] = v[0]


    return result


def dto(
        name=None, desc=None, fg_img=None, alpha_img=None, 
        emissive_img=None, bg_img=None, floorplan_img=None, 
        thumb_img=None
    ):
    data = namedtuple('pano', 'name, desc, fg_img, alpha_img, emissive_img, bg_img, floorplan_img, thumb_img')
    data.__new__.__defaults__ = (None,) * len(data._fields)

    pano = data(name, desc, fg_img, alpha_img, emissive_img, bg_img, floorplan_img, thumb_img)

    return pano


class Pano():
    def __init__(self, db=None, model=None):
        self.db = db
        self.model = model

    def _to_dict(self, row):
        return {
            'id': row.id,
            'name': row.name,
            'desc': row.desc,
            'fg_img': row.fg_img,
            'alpha_img': row.alpha_img,
            'emissive_img': row.emissive_img,
            'bg_img': row.bg_img,
            'floorplan_img': row.floorplan_img,
            'thumb_img': row.thumb_img
        }


    def new(self, dto):
        pano = self.model(
            name = dto.name,
            desc = dto.desc,
            fg_img = dto.fg_img,
            alpha_img = dto.alpha_img,
            emissive_img = dto.emissive_img,
            bg_img = dto.bg_img,
            floorplan_img = dto.floorplan_img,
            thumb_img = dto.thumb_img
           )

        self.db.session.add(pano)
        self.db.session.commit()


    def delete(self, id):
        pano = self.model.query.filter_by(id=id).first()
        pano_folder = os.path.join(config.Config().app_root, 'static', 'pano', pano.name)
        try:
            shutil.rmtree(pano_folder)
        except:
            # erm...
            pass

    
        self.db.session.delete(pano)
        self.db.session.commit()

        return True
        


    def get_by_id(self, id):
        return self._to_dict(self.model.query.filter_by(id=id).first())


    def get_all(self):
        result = []
        for pano in self.model.query.all():
            result.append(self._to_dict(pano))

        return result


