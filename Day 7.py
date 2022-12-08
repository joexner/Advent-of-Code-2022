fs_root = {
    'ftype': 'd',
    'contents': {}
}
pwd = fs_root

with open('Day 7 input.txt') as file:
    for line in file:
        if not line.startswith("$"):
            if line.startswith("dir"):
                (_, dirname) = line.split()
                if dirname not in pwd['contents']:
                    new_dir = {
                        'ftype': 'd',
                        'contents': {'..': pwd}
                    }
                    pwd['contents'][dirname] = new_dir
            else:
                (size, filename) = line.split()
                if not filename in pwd['contents']:
                    new_file = {
                        'ftype': 'f',
                        'size': int(size)
                    }
                    pwd['contents'][filename] = new_file
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('$ cd'):
            (dollar, cd, dirname) = line.split()
            if dirname == '/':
                pwd = fs_root
            else:
                pwd = pwd['contents'][dirname]

small_dirs_total_size = 0

def walk(dir) -> int:
    total = 0

    for (name, f) in dir['contents'].items():
        if f['ftype'] == 'd':
            if name != '..':
                total += walk(f)
        else:
            total += f['size']

    if total <= 100_000:
        global small_dirs_total_size
        small_dirs_total_size += total

    return total

walk(fs_root)

print(small_dirs_total_size)