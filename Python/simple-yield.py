def reader():
    for i in range(4):
        yield i

def reader_wrapper(g):
    #for v in g
    #yield v
    yield from g

if __name__ == '__main__':
    wrapper = reader_wrapper(reader())
    for i in wrapper:
        print(i)