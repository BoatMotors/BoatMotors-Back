from collections import OrderedDict


def categoryFormat(data):
    print(data,'hhhhhhhhhhhhhhhhhhhhhhhhh')

    return OrderedDict({
        "name_uz": data.name_uz,
        "name_ru": data.name_ru,
        "img": data.img.url,
        "slug":data.slug,



    })