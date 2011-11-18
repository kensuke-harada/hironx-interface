import json
import wx

def SaveSettings(file, settings):
    with open(file, 'w') as f:
        json.dump(settings, f, indent = 2, default = to_json)

    
def LoadSettings(file):
    try:
        with open(file, 'r') as f:
            settings = json.load(f, object_hook = from_json)
    except ValueError:
        print "%s Broken." % file
        exit(-1)
    except IOError:
        settings = {}
    except:
        raise
    return settings

def to_json(wxpython_object):                                             
    if isinstance(wxpython_object, wx.Rect):
        return {'__class__': 'wx.Rect',
                '__value__': wxpython_object.Get()}                       
    raise TypeError(repr(wxpython_object) + ' is not JSON serializable')

def from_json(json_object):                                   
    if '__class__' in json_object:                            
        if json_object['__class__'] == 'wx.Rect':
            v = json_object['__value__']
            return wx.Rect(v[0], v[1], v[2], v[3])
    return json_object
