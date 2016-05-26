# *-* encoding: iso-8859-15 *-*

################################################################
# zopyx.smartprintng.lite
# (C) 2009,  ZOPYX Limited & Co. KG, D-72070 Tuebingen, Germany
################################################################


def normalize(s, encoding):
    """ German normalization """

    if not isinstance(s, unicode):
        s = unicode(s, encoding, 'ignore')
    s = s.lower()
    s = s.replace(u'�', 'ae')
    s = s.replace(u'�', 'oe')
    s = s.replace(u'�', 'ue')
    s = s.replace(u'�', 'ss')
    return s

def germanCmp(o1, o2, encoding='utf-8'):
    return cmp(normalize(o1.Title(), encoding),
               normalize(o2.Title(), encoding))

def default_sort_method(o1, o2, encoding='utf-8'):
    return cmp(o1.Title().lower(),
               o2.Title().lower())


sort_methods = {
    'de' : germanCmp,
}

