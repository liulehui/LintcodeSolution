class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
        
        indegree = {i:0 for i in nodes}
        edges = {i:[] for i in nodes}
        
        for seq in seqs:
            for i in range(len(seq)):
                if i == 0:
                    indegree[seq[i]] == 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indegree[seq[i + 1]] += 1
        
        queue = collections.deque()
        
        # the difference in this questions is only one element in queue
        cur = [k for k in indegree if indegree[k] == 0]
        res = []

        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in edges[cur_node]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org
                