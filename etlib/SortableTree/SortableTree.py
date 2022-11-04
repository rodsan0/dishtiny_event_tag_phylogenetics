from Bio import Phylo
import Bio


def find_leaves(root):
    nodes = []
    for node in root.clades:
        if 'label' in node.__dict__:
            if node.label is not None:
                nodes.append(node.label)
            nodes.extend(find_leaves(node))
        elif 'name' in node.__dict__:
            if node.name is not None:
                nodes.append(node.name)
            nodes.extend(find_leaves(node))
    return nodes

def to_tril(matrix):
    return [
        row[:row_idx] + [0.0]
        for row_idx, row in enumerate(matrix.tolist())
    ]

def fix_branch_length(root):
    if 'Inner' not in root.name:
        root.branch_length = 1
    else:
        root.branch_length = sum([x.branch_length for x in root]) / len([x.branch_length for x in root])
    for x in root:
        fix_branch_length(x)

class SortableTreeMixin(Bio.Phylo.BaseTree.TreeMixin):
    def __init__(self, *args, **kwargs):
        super(SortableTreeMixin, self).__init__(*args, **kwargs)
    def fix_inner_nodes(self):
        leaves = find_leaves(self.root)
        if leaves:
            min_leaf = min(leaves, default='0')
            name = str(min_leaf)
            self.root.label = name
            self.root.name = name
            for node in self.root.clades:
                node.__class__ = SortableClade
                node.fix_inner_nodes()
    def sort_tree(self, reverse=False):
        self.root.clades.sort(key=lambda x: int("".join(filter(str.isdigit, x.name))), reverse=reverse)
        for node in self.root.clades:
            node.__class__ = SortableClade
            node.sort_tree(reverse=reverse)
class SortableTree(Bio.Phylo.BaseTree.Tree, Bio.Phylo.BaseTree.TreeElement, SortableTreeMixin):
    def __init__(self, *args, **kwargs):
        super(SortableTree, self).__init__(*args, **kwargs)
class SortableClade(Bio.Phylo.BaseTree.Clade, Bio.Phylo.BaseTree.TreeElement, SortableTreeMixin):
    def __init__(self, *args, **kwargs):
        super(SortableClade, self).__init__(*args, **kwargs)
