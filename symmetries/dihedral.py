import numpy as np
from numpy.linalg import multi_dot
import math
from itertools import chain, combinations


class D:

    def __init__(self, n):
        self.n = n
        self.r = []
        self.s = []
        self.v = []
        self.__calculate_rotations()
        self.__calculate_reflections()
        self.__calculate_vertices()

    def vertices(self):
        return [self.__get_vertex_name(v) for v in self.v]

    def reduce_operations(self, ops):
        op = self.compose(ops)
        return self.__get_op_name(op)

    def compose(self, ops):
        return np.round(multi_dot(ops), 4)

    def has_subgroup(self, subset_or_group):
        if type(subset_or_group) == D:
            # If the subset is a D instance then collect all its operations into a subset
            subset = subset_or_group.r + subset_or_group.s
        else:
            # Otherwise simply assign the subset
            subset = subset_or_group
        if not(self.__np_array_in_list(self.r[0], subset)):
            # Identity test -- if no identity it's not a group
            return False
        all_ops = self.r + self.s
        for op1 in subset:
            if not(self.__np_array_in_list(op1, all_ops)):
                # If not all of the subsets elements are in the larger group, then it's
                # not a subset after all
                return False
            for op2 in subset:
                composed_op = self.compose([op1, op2])
                if not (self.__np_array_in_list(composed_op, subset)):
                    # If there's a pair of operations in the subset whose composition
                    # isn't in the subset, then it isn't a group.
                    return False
        return True

    def subgroups(self):
        # Lagrange tells us we only need to check subsets that divide the order of the larger group
        all_sublists = [sub for sub in D.sublists(self.r + self.s) if len(sub) > 0 and len(self.r + self.s) % len(sub) == 0]
        all_subgroups = [sub for sub in all_sublists if self.has_subgroup(sub)]
        return [[self.__get_op_name(op) for op in sub] for sub in all_subgroups]

    def apply(self, op, v=None):
        if v is None:
            v = self.vertices()
        if type(v) == list:
            return [self.__apply_one(op, vertex) for vertex in v]
        else:
            return self.__apply_one(op, v)

    def __np_array_in_list(self, arr, lis):
        try:
            self.__in_list_of_np_idx(arr, lis)
            return True
        except IndexError:
            return False

    def __apply_one(self, op, v_index):
        vertex_obj = self.v[v_index]
        try:
            self.__in_list_of_np_idx(vertex_obj, self.v)
        except IndexError:
            raise Exception("Provided vertex not a vertex of D" + str(self.n))

        result = self.compose([vertex_obj, op])
        return self.__get_vertex_name(result)

    def __calculate_rotations(self):
        for i in range(0, self.n):
            rotation = self.__calculate_rotation(i)
            self.r.append(rotation)

    def __calculate_reflections(self):
        for i in range(0, self.n):
            rotation = self.__calculate_reflection(i)
            self.s.append(rotation)

    def __calculate_vertices(self):
        for i in range(0, self.n):
            self.v.append(self.__calculate_vertex(i))
        self.v.reverse()

    def __get_vertex_name(self, v):
        return self.__in_list_of_np_idx(v, self.v)

    def __rotation_segment(self, i):
        return 2 * math.pi * i / self.n

    def __calculate_vertex(self, i):
        rotation = self.__rotation_segment(i)
        return np.round(np.array([math.cos(rotation), math.sin(rotation)]), 4)

    def __calculate_rotation(self, i):
        rotation = self.__rotation_segment(i)
        return np.round(np.matrix([[math.cos(rotation), -1 * math.sin(rotation)], [math.sin(rotation), math.cos(rotation)]]), 4)

    def __calculate_reflection(self, i):
        rotation = self.__rotation_segment(i)
        return np.round(np.matrix([[math.cos(rotation), math.sin(rotation)], [math.sin(rotation), -1 * math.cos(rotation)]]), 4)

    def __in_list_of_np_idx(self, matrix, lis):
        return [i for i, m in enumerate(lis) if np.all(np.equal(matrix, m))][0]

    def __get_op_name(self, op):
        try:
            idx = self.__in_list_of_np_idx(op, self.r)
            op_type = 'r'
        except IndexError:
            idx = self.__in_list_of_np_idx(op, self.s)
            op_type = 's'
        return op_type + str(idx)

    @staticmethod 
    def sublists(l):
        return chain(*(combinations(l, i) for i in range(len(l) + 1)))



dn = D(7)

print("subgroups")
subs = dn.subgroups()
print(subs)
print(len(subs))
