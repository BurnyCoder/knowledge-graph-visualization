# Knowledge Graph Visualization

An interactive web-based visualization tool for knowledge graphs built with Python, NetworkX, and Pyvis.

## Overview

This project converts knowledge graph data into an interactive web visualization that allows you to explore complex relationships between concepts, entities, and ideas. The visualization renders directional relationships with labels, providing an intuitive way to navigate through connected information.

## Features

- Parse knowledge graph data with labeled nodes and relationships
- Create interactive, web-based network visualizations
- Color-code nodes by category
- Directed graph with relationship labels
- Zoom, pan, and interactive node exploration
- Physics-based layout for optimal node positioning

## Requirements

- Python 3.6+
- NetworkX
- Pyvis

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/knowledge-graph-visualization.git
cd knowledge-graph-visualization

# Install required packages
pip install pyvis networkx
```

## Usage

1. Place your knowledge graph data in a file named `knowledge-graph-content-2` or modify the script to point to your file
2. Run the visualization script:

```bash
python plot2.py
```

3. Open the generated `knowledge_graph.html` file in your web browser

## Input Format

The script parses knowledge graph data in the following format:

```
NodeName["Node Label"]
NodeA --> |relationship| NodeB
```

## Example

```
Universe["Universe 🌌"]
Intelligence["Intelligence 🧠"]
Universe --> |fundamental equation| UnifiedField["Unified Field Theory"]
Universe --> |contains| Matter["Matter & Energy"]
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 