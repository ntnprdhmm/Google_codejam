class Directories():
    def __init__(self):
        self.root = {}

    """ Create the directory from a full path
        If there are missing directories, create them
        Return the number of created directories
    """
    def create_directory(self, path):
        # split the full_path
        path = path.split('/')[1:]
        # go throught the directories and create directories if required
        created_dir = 0
        current_dir = self.root
        for dir in path:
            if not dir in current_dir:
                current_dir[dir] = {}
                created_dir += 1
            current_dir = current_dir[dir]
        return created_dir

f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

# for each test case
for test_case in range(int(f_in.readline().strip())):
    root = Directories()
    n, m = list(map(int, f_in.readline().strip().split()))
    # read the existing directories
    for _ in range(n):
        root.create_directory(f_in.readline().strip())
    # read the new directories
    counter = 0
    for _ in range(m):
        counter += root.create_directory(f_in.readline().strip())
    f_out.write("Case #{}: {}\n".format(test_case+1, counter))