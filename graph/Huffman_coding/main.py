import logging


class NodeTree:

    def __init__(self, left=None, right=None):

        self.left = left
        self.right = right

    def children(self):

        return (self.left, self.right)

    def __str__(self):

        return '%s_%s' % (self.left, self.right)


class HuffmanCoding:

    def __init__(self, to_compress: str) -> None:
        
        self.to_compress = to_compress
        self.to_compress_len = len(self.to_compress)

    def calc_frequencies(self, f: list, count: int = 0)  -> None:
        ''' Calculate frequencies, i.e. how many times a letter appear. '''

        if count >= self.to_compress_len:
            return f
        
        char = self.to_compress[count]

        if char in f:

            f[char] += 1
        else:

            f[char] = 1

        return self.calc_frequencies(f=f, count=count+1)

    def sort(self, to_sort: dict):
        ''' Sort the given dict by the second value.'''

        return sorted(to_sort, key=lambda x: x[1], reverse=True)

    def build_tree(self):
        ''' '''
        frequencies = self.calc_frequencies(f={})

        nodes = self.sort(to_sort=frequencies.items())

        while len(nodes) > 1:

            last, lastm1 = nodes[-1], nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(last[0], lastm1[0])
            nodes.append((node, last[1] + lastm1[1]))


            nodes = self.sort(to_sort=nodes)
        
        return nodes
    
    def huffman_code(self, node, prefix: str = ''):
        ''' '''

        if type(node) is str:
            return {node: prefix}

        (left, right) = node.children()
        d = {}
        d.update(self.huffman_code(left, prefix + '0'))
        d.update(self.huffman_code(right, prefix + '1'))

        return d

    def main(self):

        nodes = hf.build_tree()
        res = self.huffman_code(nodes[0][0])
        
        logging.info(f'Result: {res}')


if __name__ == '__main__':

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    hf = HuffmanCoding(to_compress='BCAADDDCCACACAC')
    
    hf.main()