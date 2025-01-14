# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:22:04 2021

This module is last modified on 1/11/2021

@author: zhoux
"""
from qiskit import QuantumCircuit, QuantumRegister
import networkx as nx
from networkx.algorithms import approximation as approx
from networkx import DiGraph
import numpy as np

'''
gate is a tuple (gate_name, (qubits), (parameters))
supported gate_name:
    cx
    u3
    ...
'''
# {gate_name: (num_qubits, num_parameters)}
supported_gate_names = {'cx':(2, 0), 'h':(1, 0), 't':(1, 0), 'x':(1, 0), 
                        'y':(1, 0), 'z':(1, 0), 's':(1, 0), 'rx':(1, 1), 
                        'ry':(1, 1), 'rz':(1, 1), 'u3':(1, 3), 'tdg':(1, 0),
                        'p':(1, 1), 'u2':(1, 2), 'u1':(1, 1), 'swap':(2, 0),
                        'u':(1, 3), 'id':(1, 1), 'cz':(2, 0), 'sdg' : (1,0),
                        'sx': (1,0), 'sxdg': (1,0)}

def add_gate_to_qiskit_cir(cir, gate):
    name = gate[0]
    q = gate[1]
    p = gate[2]
    if len(q) > 2: raise()
    if not name in supported_gate_names:
        raise(Exception('Unsupported gate {}'.format(name)))
    if name == 'cx': cir.cx(q[0], q[1])
    if name == 'swap': cir.swap(q[0], q[1])
    if name == 'h': cir.h(q[0])
    if name == 's': cir.s(q[0])
    if name == 't': cir.t(q[0])
    if name == 'x': cir.x(q[0])
    if name == 'y': cir.y(q[0])
    if name == 'z': cir.z(q[0])
    if name == 'id': cir.id(q[0])
    if name == 'p': cir.p(p[0], q[0])
    if name == 'rx': cir.rx(p[0], q[0])
    if name == 'ry': cir.ry(p[0], q[0])
    if name == 'rz': cir.rz(p[0], q[0])
    if name == 'u1': cir.u1(p[0], q[0])
    if name == 'u2': cir.u2(p[0], p[1], q[0])
    if name == 'u3' or name == 'u': cir.u(p[0], p[1], p[2], q[0])
    if name == 'tdg': cir.tdg(q[0])
    if name == 'cz': cir.cz(q[0], q[1])
    if name == 'sdg': cir.sdg(q[0]) 
    if name == 'sx': cir.sx(q[0])
    if name == 'sxdg': cir.sxdg(q[0])
    if name.startswith('b'):
        raise()
    
    
def add_gate_to_cir(cir, gate):
    name = gate[0]
    q = gate[1]
    p = gate[2]
    if len(q) > 2: raise()
    if not name in ('cx', 'u3', 'u1', 'u2'):
        raise(Exception('Unsupported gate {}'.format(name)))
    if name == 'cx': cir.add_cx(q[0], q[1])
    if name == 'u3': cir.add_u3(q[0])
    if name == 'u2': cir.add_u2(q[0])
    if name == 'u1': cir.add_u1(q[0])

def CreateCircuitFromQASM(file):
    QASM_file = open(file, 'r')
    iter_f = iter(QASM_file)
    QASM = ''
    for line in iter_f: #遍历文件，一行行遍历，读取文本
        QASM = QASM + line
    #print(QASM)
    cir = QuantumCircuit.from_qasm_str(QASM)
    QASM_file.close
    
    return cir

class xor_tensor():
    def __init__(self, q):
        self.name = 'xor'
        self.qubits = [q]
        
class copy_tensor():
    def __init__(self, q):
        self.name = 'copy'
        self.qubits = [q]

class DG(DiGraph):
    def __init__(self, ):
        super().__init__()
        self.qubit_to_node = [None] * 500
        self.num_gate_2q = 0
        self.num_gate_1q = 0
        self.node_count = 0
        self.num_q = None
    
    @property
    def num_gate(self):
        return self.num_gate_1q + self.num_gate_2q
    
    def get_node_count(self, num_q=None):
        if num_q == None: return len(self.nodes)
        count = 0
        for node in self.nodes:
            if self.get_node_num_q(node) == num_q: count += 1
        return count
        
    def get_shared_qubits(self, node1, node2):
        '''Get qubits which exist in both node1 and node2'''
        qubits = []
        for q in self.get_node_qubits(node1):
            if q in self.get_node_qubits(node2):
                qubits.append(q)
        return qubits
        
    def add_line(self, node_in, node_out, qubits=None, check=True):
        '''Connect two nodes using provided qubits'''
        qubits_share = self.get_shared_qubits(node_in, node_out)
        qubits_used = []
        for edge_c in self.out_edges(node_in):
            qubits_used.extend(self.get_edge_qubits(edge_c))
        for edge_c in self.in_edges(node_out):
            qubits_used.extend(self.get_edge_qubits(edge_c))
        qubits_share_new = []
        for q in qubits_share:
            if not q in qubits_used: qubits_share_new.append(q)
        qubits_share = qubits_share_new
        
        if qubits == None: qubits = qubits_share
        if check:
            for q in qubits:
                if not q in qubits_share:
                    print(self.nodes[node_in])
                    print(self.nodes[node_out])
                    print(qubits)
                    print(qubits_share)
                    raise()
        edge_add = (node_in, node_out)
        if edge_add in self.edges:
            for q in qubits:
                if not q in self.edges[edge_add]['qubits']:
                    self.edges[edge_add]['qubits'].append(q)
        else:
            self.add_edge(node_in, node_out, qubits=qubits)
    
    def add_gate(self, gate, add_edges=True):
        '''
        Attributes of a node:
            gates
            num_gate_1q
            num_gate_2q
            qubits
        '''
        # add node
        node_new = self.node_count
        self.node_count += 1
        self.add_node(node_new)
        self.nodes[node_new]['gates'] = [gate]
        self.nodes[node_new]['qubits'] = list(gate[1])
        self.nodes[node_new]['num_gate_1q'], self.nodes[node_new]['num_gate_2q'] = 0, 0
        if len(gate[1]) == 1:
            self.nodes[node_new]['num_gate_1q'] += 1
            self.num_gate_1q += 1
        if len(gate[1]) == 2:
            self.nodes[node_new]['num_gate_2q'] += 1
            self.num_gate_2q += 1
        if len(gate[1]) > 2: raise()
        if add_edges:
        # add edges
            for q in gate[1]:
                node_parent = self.qubit_to_node[q]
                if node_parent != None:
                    self.add_line(node_parent, node_new, [q])
                self.qubit_to_node[q] = node_new
        return node_new
    
    def add_gates(self, gates, add_edges=True, update_dg_attrs=True):
        '''
        Attributes of a node:
            gates
            num_gate_1q
            num_gate_2q
            qubits
        '''
        # add node
        node_new = self.node_count
        self.node_count += 1
        if node_new in self.nodes: raise()
        self.add_node(node_new)
        self.nodes[node_new]['gates'] = gates
        qubits = []
        num_gate_1q, num_gate_2q = 0, 0
        for _, qs, _ in gates:
            if len(qs) == 1:
                if update_dg_attrs: self.num_gate_1q += 1
                num_gate_1q += 1
            if len(qs) == 2: 
                if update_dg_attrs: self.num_gate_2q += 1
                num_gate_2q += 1
            if len(qs) > 2: raise()
            for q in qs:
                if not q in qubits: qubits.append(q)
        self.nodes[node_new]['qubits'] = qubits
        self.nodes[node_new]['num_gate_1q'], self.nodes[node_new]['num_gate_2q'] = num_gate_1q, num_gate_2q

        # add edges
        if add_edges:
            raise(Exception("This function has not been implemented!"))
        return node_new
    
    def get_node_num_gate(self, node):
        return len(self.get_node_gates(node))
            
    def get_node_num_q(self, node):
        return len(self.nodes[node]['qubits'])
    
    def get_node_num_2q_gates(self, node):
        return self.nodes[node]['num_gate_2q']
    
    def get_node_num_1q_gates(self, node):
        return self.nodes[node]['num_gate_1q']
    
    def get_node_gates(self, node):
        return self.nodes[node]['gates']
    
    def get_node_qubits(self, node):
        return self.nodes[node]['qubits']
    
    def get_node_depth(self, node):
        '''One SWAP takes 3 depth.'''
        qubit_depth = [0] * (max(self.get_node_qubits(node)) + 1)
        for name, qubits, _ in self.get_node_gates(node):
            current_ds = []
            for q in qubits:
                current_ds.append(qubit_depth[q])
            current_d = max(current_ds)
            if name == 'SWAP' or name == 'swap':
                current_d += 3
            else:
                current_d += 1
            for q in qubits:
                qubit_depth[q] = current_d
        return max(qubit_depth)
    
    def get_edge_qubits(self, edge):
        return self.edges[edge]['qubits']
    
    def set_edge_qubits(self, edge, qubits):
        self.edges[edge]['qubits'] = list(qubits)
    
    def add_gate_absorb(self, gate):
        '''Add a gate and absorb is if possible'''
        nodes_check = []
        for q in gate[1]:
            node_father = self.qubit_to_node[q]
            if not node_father in nodes_check and node_father != None:
                nodes_check.append(node_father)
        # add node
        new_node = self.add_gate(gate)
        # absorb
        for node_parent in nodes_check:
            if not self.check_absorbable(node_parent, new_node): continue
            new_node = self.cascade_node(new_node, node_parent)
        #self.check()
        return new_node
    
    def cascade_node(self, node1, node2):
        '''
        Combine two given nodes.
        Here we only update one node (node_in) and delete the other (node_out)
        instead of creating one node and deleting both.
        '''
        if not self.check_direct_dependency(node1, node2):
            if not self.check_parallel(node1, node2):
                raise()
        if (node1, node2) in self.edges:
            node_in, node_out = node1, node2
        else:
            if (node2, node1) in self.edges:
                node_in, node_out = node2, node1
            else:
                # we accept two nodes are parallel
                node_in, node_out = node1, node2
        # update attributes
        self.nodes[node_in]['gates'].extend(self.nodes[node_out]['gates'])
        for gate in self.nodes[node_out]['gates']:
            if len(gate[1]) == 1:
                self.nodes[node_in]['num_gate_1q'] += 1
            if len(gate[1]) == 2:
                self.nodes[node_in]['num_gate_2q'] += 1
            for q in gate[1]:
                if not q in self.nodes[node_in]['qubits']:
                    self.nodes[node_in]['qubits'].append(q)
        # delete node and add egdes
        for node in list(self.successors(node_out)):
            self.add_line(node_in, node, 
                          self.get_edge_qubits((node_out, node)),
                          check=False)
        for node in list(self.predecessors(node_out)):
            if node != node_in:
                self.add_line(node, node_in, 
                              self.get_edge_qubits((node, node_out)),
                              check=False)
        ## update qubit_to_node
        for q in self.get_node_qubits(node_out):
            if self.qubit_to_node[q] == node_out:
                self.qubit_to_node[q] = node_in
        self.remove_node(node_out)
        #self.check()
        return node_in
    
    
    def from_qasm_string(self, qasm_string, absorb=True):
        qiskit_cir = QuantumCircuit()
        qiskit_cir = qiskit_cir.from_qasm_str(qasm_string)
        return self.from_qiskit_circuit(qiskit_cir, absorb)
    
    def from_qasm(self, file, absorb=True):
        qiskit_cir = CreateCircuitFromQASM(file)
        return self.from_qiskit_circuit(qiskit_cir, absorb)
                
    def from_qiskit_circuit(self, qiskit_cir, absorb=True):
        if len(qiskit_cir.qregs) > 1:
            raise(Exception("Currently we do not support circuit with more than 1 quantum register."))
        self.num_q = len(qiskit_cir.qregs[0])
        self.num_q_log = self.num_q
        measure_op = []
        data = qiskit_cir.data
        for qiskit_gate in data:
            name = qiskit_gate[0].name
            if name in ("barrier", "measure"): 
                if name == "measure": 
                    measure_op.append(qiskit_gate)
                continue
            qargs = qiskit_gate[1]
            paras = tuple(qiskit_gate[0].params)
            qubits = []
            for qubit_qiskit in qargs:
                qubits.append(qubit_qiskit.index)
            gate = (name, tuple(qubits), paras)
            if absorb: 
                self.add_gate_absorb(gate)
            else:
                self.add_gate(gate)
        return measure_op, qiskit_cir.cregs
    
    def opt_node_gates(self, node):
        '''
        Use gate commutation and cancelling rules to reduce the # gates in one 
        node.
        '''
        import sys
        sys.path.append("D:\\programs\\")
    
    def qiskit_circuit(self, save_to_file=False, add_barrier=False,
                       decompose_swap=False,
                       file_name='circuit'):
        '''
        Convert the DG to a qiskit circuit.
        If decompose_swap is set to True, we will decompose each SWAP into 3 CNOTs.
        '''
        from .front_circuit import FrontCircuit
        # init circuits
        qubits = QuantumRegister(self.num_q, 'q')
        ag = nx.complete_graph(self.num_q)
        circuit = FrontCircuit(self, ag)
        cir_qiskit = QuantumCircuit(qubits)
        # add qiskit gates one by one
        while circuit.num_remain_nodes > 0:
            front_nodes = circuit.front_layer
            if len(front_nodes) == 0:
                raise()
                
            for node in front_nodes:
                gates = self.get_node_gates(node)
                for gate in gates:
                    add_gate_to_qiskit_cir(cir_qiskit, gate)
                if add_barrier: cir_qiskit.barrier()
            circuit.execute_front_layer()
        if decompose_swap:
            from qiskit.transpiler.passes import Decompose
            from qiskit.converters import circuit_to_dag, dag_to_circuit
            from qiskit.circuit.library.standard_gates.swap import SwapGate
            dag = circuit_to_dag(cir_qiskit)
            de_pass = Decompose(gate=SwapGate)
            dag = de_pass.run(dag)
            cir_qiskit = dag_to_circuit(dag)
        if save_to_file:
            fig = (cir_qiskit.draw(scale=0.7, filename=None, style=None, output='mpl',
                        interactive=False, plot_barriers=True, reverse_bits=False))
            fig.savefig(file_name+'.svg', format='svg')  
        return cir_qiskit
    
    def to_qasm(self, file_name='cir.qasm', add_measurement=False):
        cir = self.qiskit_circuit()
        if add_measurement:
            from qiskit import ClassicalRegister
            c = ClassicalRegister(len(cir.qubits), 'c')
            cir.add_register(c)
            cir.measure(cir.qregs[0], c)
        cir.qasm(filename=file_name)
        
    def to_qasm_str(self,):
        cir = self.qiskit_circuit()
        return cir.qasm()
    
    def draw(self):
        '''Draw DG graph'''
        nx.draw(self, with_labels=1)
        
    def check_parallel(self, node1, node2):
        if approx.local_node_connectivity(self, node1, node2) == 0 and \
            approx.local_node_connectivity(self, node2, node1) == 0:
            return True
        else:
            return False
        
    def check_direct_dependency(self, node1, node2):
        '''
        We say node2 directly depends on node1 if 
            1) two nodes share at least one qubit;
            2) for each shared qubit, there can't be any nodes existing between 
            the two nodes;
            3) there can't be any path connecting node1 and node2 other than the
                edge in 1)
        If two node are directly dependent, these nodes can be absorbed or
        cascaded. Note that currently we won't accept node1 and node2 are 
        parallel, in that case, we will return False! One can use self.check_parallel
        to check the parallelism between nodes.
        '''
        # check condition 1
        if (node1, node2) in self.edges:
            node_in, node_out = node1, node2
        else:
            if (node2, node1) in self.edges:
                node_in, node_out = node2, node1
            else:
                return False
        # check condition 2
        ## it seems that condition 2 is covered in condition 3, hence I decide
        ## to annotate it.
# =============================================================================
#         qubits_share = []
#         for q in self.get_node_qubits(node_out):
#             if q in self.get_node_qubits(node_in):
#                 qubits_share.append(q)
#         if len(qubits_share) == 0: raise()
#         for q in qubits_share:
#             if not q in self.edges[(node_in, node_out)]["qubits"]:
#                 return False
# =============================================================================
        # check condition 3
        if approx.local_node_connectivity(self, node_in, node_out) > 1:
            return False
        return True
    
    def check_absorbable(self, node1, node2):
        '''
        check if node1 and node2 can be obsorbed to each other
        node1 and node2 are absorbable if all qubits in node1 or node2 exist in
        node2 or node1 and they are directly dependent to each other.
        '''
        if len(self.get_node_qubits(node1)) > len(self.get_node_qubits(node2)):
            node_abs, node_org = node2, node1
        else:
            node_abs, node_org = node1, node2
        for q in self.get_node_qubits(node_abs):
            if not q in self.get_node_qubits(node_org): return False
        if not self.check_direct_dependency(node_org, node_abs):
            return False
        return True
    
    def check_cascadeable(self, nodes1, node2, max_q_cascade):
        '''
        Check if node2 can be cascaded with nodes in nodes1 (assuming nodes in 
        nodes1 will be cascaded into 1 node)
        We accept node2 and nodes1 are parallel, i.e., there is no shared qubits
        between them.
        We assume all nodes in nodes1 can be cascaded and won't check this 
        assumption!
        '''
        if len(nodes1) == 0: return True
        edge_qubits = []
        share_qubits = []
        qubits = self.get_node_qubits(node2).copy()
        # flag_1_2: node2 is the decendent of all nodes in nodes1
        # flag_2_1: node2 is the ancestor of all nodes in nodes1
        flag_1_2, flag_2_1 = False, False
        for node1 in nodes1:
            for q in self.get_node_qubits(node1):
                if not q in qubits: qubits.append(q)
            share_qubits.extend(self.get_shared_qubits(node1, node2))
            if (node1, node2) in self.edges:
                flag_1_2 = True
                edge_qubits.extend(self.get_edge_qubits(((node1, node2))))
            if (node2, node1) in self.edges:
                flag_2_1 = True
                edge_qubits.extend(self.get_edge_qubits(((node2, node1))))
        if flag_1_2 and flag_2_1: raise()
        if len(qubits) > max_q_cascade: return False
        if len(share_qubits) == 0: 
            # if no shared qubits, we need to make sure they are parallel
            for node1 in nodes1:
                if not self.check_parallel(node1, node2):
                    return False
            return True
        # all shared qubits must exist in edge_qubits
        #for q in share_qubits:
        #    if not q in edge_qubits: return False
        # we check the nodes in all routes connecting node in nodes1 and node2 
        # are either node2 or contained in nodes1
        ## If we do this check, it seems that the above check (all shared 
        ## qubits must exist in edge_qubits) is unnecessary.
        ### Unimplemented yet
        
        # if node2 and any one in nodes1 can be cascaded, we return True
        for node1 in nodes1:
            if self.check_direct_dependency(node1, node2):
                return True
        return False
    
    def check(self):
        '''Check whether current DG is legal.'''
        try:
            cycles = nx.find_cycle(self)
            print(cycles)
            raise()
        except:
            pass
        #self.qiskit_circuit(save_to_file=False)

