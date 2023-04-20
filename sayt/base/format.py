from collections import OrderedDict


def categoryFormat(data):
    return OrderedDict({
        "name_uz": data.name_uz,
        "name_ru": data.name_ru,
        "img": data.img.url,
        "slug": data.slug,

    })


def subctgFormat(data):
    return OrderedDict({
        "name_uz": data.name_uz,
        "name_ru": data.name_ru,
    })


def productFormat(data):
    return OrderedDict({
        "sub_ctg": data.sub_ctg_id,
        "name_uz": data.name_uz,
        "name_ru": data.name_ru,
        "img": data.img.url,
        "view": data.view,
        "like": data.like,
        "dis_like": data.dis_like,
        "price": data.price,
    })

def basketFormat(data):
    return OrderedDict({
        "product":data.product.name_uz,
        "quantity":data.quantity,
        "price":data.price,
    })
