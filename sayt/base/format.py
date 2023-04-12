from collections import OrderedDict


def categoryFormat(data):


    return OrderedDict({
        "name_uz": data.name_uz,
        "name_ru": data.name_ru,
        "img": data.img.url,
        "slug":data.slug,



    })

def subctgFormat(data):

    return OrderedDict({
        "name_uz":data.name_uz,
        "name_ru":data.name_ru,
    })
