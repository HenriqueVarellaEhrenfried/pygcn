from __future__ import print_function
import networkx as nx
import spacy
import matplotlib.pyplot as plt
import numpy
import torch

nlp = spacy.load("en_core_web_lg")

def generate_graph(sentece):
    doc = nlp(sentece)
    G = nx.Graph()
    index = 0
    for token in doc:
        G.add_node(token.text, name=token.text,lemma=token.lemma_,POS=token.pos_,TAG=token.tag_,DEP=token.dep_,shape=token.shape_,is_alpha=token.is_alpha,is_stop=token.is_stop)
        if index > 0:
            G.add_edge(token.text, doc[index-1].text, order=index+1)
        index = index + 1
    return (G)

def convert_networkx_to_torch(graph):
    a = nx.to_numpy_matrix(graph)
    return(torch.from_numpy(a))

def draw_graph_to_file(path="./Exemplo"):
    nx.draw(Gg, with_labels=True, font_weight='bold')
    plt.savefig(path)

Gg = generate_graph("I love pizza, you love cake, they love dog.")

a = convert_networkx_to_torch(Gg)
print(a)


