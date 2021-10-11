import os
import tempfile
import json
import argparse
from collections import defaultdict

if __name__ == '__main__':
    my_dict = defaultdict(list)
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="enter the key")
    parser.add_argument("--val", help="enter the value")
    args = parser.parse_args()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'a+') as f:
        if os.stat(storage_path).st_size != 0:
            f.seek(0)
            my_dict = json.load(f)
            f.truncate(0)
        if args.key:
            if args.val:
                try:
                    my_dict[args.key].append(args.val)
                except KeyError:
                    my_dict.update({args.key: [args.val]})
            else:
                if args.key not in my_dict:
                    print()
                else:
                    print(', '.join(my_dict[args.key]))
        json.dump(my_dict, f)



