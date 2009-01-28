from optparse import OptionParser

SUFFIXES = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
MULTIPLES = {True: 1024, False: 1000}

def human_size(size, use_binary_multiples=True):
    """Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    use_binary_multiples -- if False, use multiples of 1000
                            if True, use multiples of 1024 (default=True)

    Returns: string

    """
    multiple = MULTIPLES[use_binary_multiples]
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return "{0:.1f} {1}".format(size, suffix)
    return "Too large to contemplate!"

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--decimal",
                      action="store_false",
                      dest="binary_multiples",
                      default=True,
                      help="use multiples of 1000 instead of 1024")
    (options, args) = parser.parse_args()
    if args:
        print(human_size(int(args[0]), options.binary_multiples))
    else:
        parser.print_help()
    
