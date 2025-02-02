import sys


def create_cfgs(grammar_expr_file):
    """
    Reads and processes a context-free grammar (CFG) from a file and extracts non-terminals,
    terminals, and production rules.

    :param grammar_expr_file: string - Path to the file containing the CFG.
    :return: tuple - (list of non-terminals, list of terminals, dictionary of production rules)
                     - non_terminals: A list of non-terminal symbols.
                     - terminals: A list of terminal symbols.
                     - productions: A dictionary mapping each non-terminal to a list of possible production rules.
    """

    # Opens the file to be read, cleans the lines, and stores each line in a list
    with open(grammar_expr_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    index = 0  # Start reading from the first line

    # Read non-terminal and terminal counts
    # breaks line into separate values and maps each into integers
    num_non_terminals, num_terminals = map(int, lines[index].split())
    index += 1

    # Read non-terminals into a list
    non_terminals = [lines[i] for i in range(index, index + num_non_terminals)]
    index += num_non_terminals  # Move index past the non-terminals

    # Read terminals into a list
    terminals = [lines[i] for i in range(index, index + num_terminals)]
    index += num_terminals  # Move index past the terminals

    # Read production rules count
    num_productions = int(lines[index])  # Convert the number of rules to an integer
    index += 1  # Move to the first production rule

    # Read production rules
    productions = {}

    # use _ as a throw away variable
    for _ in range(num_productions):
        non_terminal = lines[index]  # left is the non-terminal of the rule
        production = lines[index + 1].split()  # right is split into tokens
        index += 2  # Move to the next production rule

        if non_terminal not in productions:
            productions[non_terminal] = []  # Initialize an empty list if the key doesn't exist
        productions[non_terminal].append(production)  # Add the production rule to the list

    return non_terminals, terminals, productions


def main():
    grammar_expr_file = sys.argv[1]  # takes in the grammar

    # Creates a list of terminals, non-terminals, and the productions dict
    non_terminals, terminals, productions = create_cfgs(grammar_expr_file)

    print(non_terminals)
    print(terminals)
    print(productions)


main()
