import pickle
import json
import time

def to_json(python_object):
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')

def from_json(json_object):
    if '__class__' in json_object:
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])
    return json_object

if __name__ == '__main__':
    entry = {}
    entry['title'] = 'Dive into history, 2009 edition'
    entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
    entry['comments_link'] = None
    entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
    entry['tags'] = ('diveintopython', 'docbook', 'html')
    entry['published'] = True
    entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')
    
    with open('entry.pickle', 'wb') as f:
        pickle.dump(entry, f)

    with open('entry.pickle', 'rb') as f:
        entry2 = pickle.load(f)

    print(entry == entry2)
    print(type(entry['tags']))
    print(type(entry2['tags']))

    with open('entry.json', 'w', encoding='utf-8') as f:
        json.dump(entry, f, default=to_json)

    with open('entry.json', 'r', encoding='utf-8') as f:
        entry2 = json.load(f, object_hook=from_json)

    print(entry == entry2)
    print(type(entry['tags']))
    print(type(entry2['tags']))
