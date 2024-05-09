"""
A text made up of characters alpa beta gama what probability 0.12,0.40,0.15,0.08 ε0.25 use huff man coding technique to find the total length band breath per character ?

"""
import heapq

# Define symbols and their probabilities
symbols = ['alpha', 'beta', 'gama', 'varepsilon']
probabilities = [0.12, 0.40, 0.15, 0.08, 0.25]  # epsilon included

# Build the Huffman tree
def build_huffman_tree(symbols, probabilities):
  queue = []
  for symbol, probability in zip(symbols, probabilities):
    heapq.heappush(queue, Node(symbol, probability))

  while len(queue) > 1:
    left = heapq.heappop(queue)
    right = heapq.heappop(queue)
    root = Node(None, left.probability + right.probability)
    root.left = left
    root.right = right
    heapq.heappush(queue, root)

  return queue[0]

# Node class for Huffman tree
class Node:
  def __init__(self, symbol, probability):
    self.symbol = symbol
    self.probability = probability
    self.left = None
    self.right = None

# Traverse and assign codes
def traverse_and_assign_codes(node, code, codes):
  if node is None:
    return

  if node.symbol:
    codes[node.symbol] = code
  else:
    traverse_and_assign_codes(node.left, code + '0', codes)
    traverse_and_assign_codes(node.right, code + '1', codes)

# Calculate average code length
def calculate_average_code_length(codes, probabilities):
  average_length = 0
  for symbol, code in codes.items():
    average_length += len(code) * probabilities[symbols.index(symbol)]
  return average_length

# Main function
def main():
  # Build the Huffman tree
  root = build_huffman_tree(symbols, probabilities)

  # Assign codes to each symbol
  codes = {}
  traverse_and_assign_codes(root, '', codes)

  # Calculate average code length
  average_length = calculate_average_code_length(codes, probabilities)

  # Print the average code length (represents length and breadth per character)
  print("Average code length (length and breadth per character):", average_length)

if __name__ == "__main__":
  main()
  
