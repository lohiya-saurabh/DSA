import os


def exp(name):
    """
    """
    return ''.join(['_'+c.lower() if c.isupper() else c for c in name]).lstrip('_')


folder_path = './DSA-1/Arrays'

print(os.listdir('./'))

for filename in os.listdir(folder_path):
    if filename.endswith('.py'):
        new_filename = exp(filename.split('.')[0]) + '.py'

        os.rename(os.path.join(folder_path, filename),
                  os.path.join(folder_path, new_filename))
