#!/usr/bin/env python3
import re
import os
from pyvis.network import Network
import networkx as nx

def parse_knowledge_graph(file_path):
    """Parse the knowledge graph content file and extract nodes and edges."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract nodes and their labels
    nodes = {}
    node_pattern = re.compile(r'(\w+)\["([^"]+)"\]')
    for match in node_pattern.finditer(content):
        node_id, node_label = match.groups()
        nodes[node_id] = node_label
    
    # Simple node references without labels
    simple_nodes = re.compile(r'(\w+)\s+-->')
    for match in simple_nodes.finditer(content):
        node_id = match.group(1)
        if node_id not in nodes:
            nodes[node_id] = node_id
    
    # Extract edges and their relationships
    edges = []
    edge_pattern = re.compile(r'(\w+)\s+-->\s+\|([^|]+)\|\s+(\w+)')
    for match in edge_pattern.finditer(content):
        source, relation, target = match.groups()
        edges.append((source, target, relation))
    
    return nodes, edges

def create_knowledge_graph_visualization(nodes, edges, output_file="knowledge_graph.html"):
    """Create an interactive visualization of the knowledge graph."""
    # Create a NetworkX graph
    G = nx.DiGraph()
    
    # Add nodes with labels
    for node_id, node_label in nodes.items():
        G.add_node(node_id, label=node_label, title=node_label)
    
    # Add edges with relationships as labels
    for source, target, relation in edges:
        # Only add edge if both nodes exist (to handle references to undefined nodes)
        if source in nodes and target in nodes:
            G.add_edge(source, target, label=relation, title=relation)
    
    # Create Pyvis network from NetworkX graph
    net = Network(height="800px", width="100%", directed=True, notebook=False)
    
    # Set physics options for better layout
    net.set_options("""
    {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -50,
          "centralGravity": 0.01,
          "springLength": 100,
          "springConstant": 0.08
        },
        "maxVelocity": 50,
        "solver": "forceAtlas2Based",
        "timestep": 0.35,
        "stabilization": {"iterations": 150}
      },
      "edges": {
        "smooth": {"type": "continuous"},
        "arrows": {"to": {"enabled": true, "scaleFactor": 0.5}},
        "color": {"inherit": true},
        "font": {"size": 8}
      },
      "nodes": {
        "font": {"size": 12, "face": "Tahoma"}
      }
    }
    """)
    
    # Add the NetworkX graph to Pyvis
    net.from_nx(G)
    
    # Add node colors based on categories (using node prefixes as a heuristic)
    groups = {}
    for node_id in nodes:
        # Extract prefix groups from node IDs
        prefix = re.sub(r'([A-Z].*)', '', node_id)
        if prefix:
            if prefix not in groups:
                groups[prefix] = len(groups)
            net.nodes[list(net.nodes).index(node_id)]['group'] = groups[prefix]
    
    # Save the visualization
    net.save_graph(output_file)
    print(f"Knowledge graph visualization saved to {output_file}")
    return output_file

def main():
    # Path to the knowledge graph content file
    kg_file = "knowledge-graph-content-2"
    
    # Parse the knowledge graph
    nodes, edges = parse_knowledge_graph(kg_file)
    
    # Create and save the visualization
    output_file = create_knowledge_graph_visualization(nodes, edges)
    
    # Open the visualization in the default browser
    full_path = os.path.abspath(output_file)
    print(f"Full path: {full_path}")
    print(f"To view in browser, open: file://{full_path}")

if __name__ == "__main__":
    main()
