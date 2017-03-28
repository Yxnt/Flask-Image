#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mimetypes
from PIL import Image
from io import BytesIO


def img_resize(imgpath, args, imgtype=None):
    ratio = 100
    _height = _weight = _quality = _percentage = None
    if 'h' in args:
        try:
            _height = int(args['h'])
        except ValueError as e:
            _height = None

    if 'w' in args:
        try:
            _weight = int(args['w'])
        except ValueError as e:
            _weight = None

    if 'q' in args:
        try:
            _quality = int(args['q'])
        except ValueError as e:
            _quality = 50
    else:
        _quality = 50

    if 'p' in args:
        try:
            _percentage = float(args['p']) / ratio
            _height = None
            _weight = None
        except ValueError as e:
            _percentage = 0

    if imgtype and (imgtype == 'jpg' or imgtype == 'JPG'):
        imgtype = 'JPEG'
    else:
        imgtype = 'PNG'

    with BytesIO() as b:
        try:
            with Image.open(imgpath) as im:

                weight, height = im.size

                if _percentage and (not _height and not _weight):
                    if _percentage > 1:
                        im.save(b, imgtype, quality=_quality)
                        return b.getvalue()
                    _height = height * _percentage
                    _weight = weight * _percentage
                    newsize = (int(_weight), int(_height))
                    im.resize(newsize, Image.ANTIALIAS).save(b, imgtype, quality=_quality)
                    return b.getvalue()
                else:
                    if not _height and not _weight:
                        if imgtype == 'PNG':
                            im = im.convert('P')
                            im.save(b,imgtype, optimize=True)
                            return b.getvalue()
                        im.save(b, imgtype, quality=_quality)
                        return b.getvalue()

                    if _height:
                        if _height > height:
                            _height = height
                    else:
                        _height = height

                    if _weight:
                        if _weight > weight:
                            _weight = weight
                    else:
                        _weight = weight

                    newsize = (int(_weight), int(_height))
                    im.resize(newsize, Image.ANTIALIAS).save(b, imgtype, quality=_quality)
                    return b.getvalue()
        except OSError as e:
            pass


def file_getmime(filepath):
    '''获取文件mime类型
    :param filepath: 提供文件路径
    :return: mime类型
    '''
    mimetypes.init('/usr/local/openresty/nginx/conf/mime.types')
    mime = mimetypes.MimeTypes()
    mimetype = mime.guess_type(filepath)
    if mimetype[0] == "None":
        from magic import Magic
        f = Magic(mime=True)
        return f.from_file(filepath)
    return mimetype[0]


def file_read(filepath):
    with open(filepath, 'rb') as f:
        for i in f:
            yield i


if __name__ == '__main__':
    img_resize('img/1.jpg', imgtype='JPEG', args=None)
