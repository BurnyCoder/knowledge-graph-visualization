#!/usr/bin/env python3
"""
Knowledge Graph Visualization Tool

This script visualizes the knowledge graph defined in knowledge-graph.py
using the Graphviz library.
"""

import graphviz
import sys
import shutil
from pathlib import Path

with open('knowledge-graph-content.py', 'r') as f:
    content = f.read()
    # Create a local namespace to execute the file in
    namespace = {}
    exec(content, namespace)
    knowledge_graph = namespace.get('knowledge_graph')

try:
    # Create a Source object using the knowledge_graph DOT string
    graph = graphviz.Source(knowledge_graph)

    # Create output directory if it doesn't exist
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)

    # Render the graph to a PDF file
    graph.render('output/knowledge_graph', format='pdf', cleanup=True)

    # Also render as PNG for easier viewing
    graph.render('output/knowledge_graph', format='png', cleanup=True)

    print("Knowledge graph has been visualized and saved to:")
    print("- output/knowledge_graph.pdf")
    print("- output/knowledge_graph.png")

    # If you want to display the graph in a Jupyter notebook, you can uncomment:
    # display(graph)
except Exception as e:
    print(f"Error generating graph: {e}")
    sys.exit(1)
