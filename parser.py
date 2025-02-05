"""
Garrett Gmeiner
email: ggmeiner2021@my.fit.edu
Assignment 1: Joy with Parsing
"""
import sys


def create_cfgs(grammar_expr_file):
    """
    Reads and processes a context-free grammar (CFG) from a file and extracts non-terminals,
    terminals, and production rules.

    :param grammar_expr_file: string - Path to the file containing the CFG.
    :return: tuple - (list of non-terminals, list of terminals, dictionary of production rules).
                     - non_terminals: A list of non-terminal symbols.
                     - terminals: A list of terminal symbols.
                     - productions: A list of lists, where each sublist contains a non-terminal
                     followed by its productions.
    """

    # Opens the file to be read, cleans the lines, and stores each line in a list
    with open(grammar_expr_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    line_index = 0  # Start reading from the first line

    # Read non-terminal and terminal counts
    # breaks line into separate values and maps each into integers
    num_non_terminals, num_terminals = map(int, lines[line_index].split())
    line_index += 1

    # Read non-terminals into a list
    non_terminals = [lines[i] for i in range(line_index, line_index + num_non_terminals)]
    line_index += num_non_terminals  # Move line_index past the non-terminals

    # Read terminals into a list
    terminals = [lines[i] for i in range(line_index, line_index + num_terminals)]
    line_index += num_terminals  # Move line_index past the terminals

    # Read production rules count
    num_productions = int(lines[line_index])  # Convert the number of rules to an integer
    line_index += 1  # Move to the first production rule

    # Read production rules
    productions = []

    for _ in range(num_productions):
        non_terminal = lines[line_index]  # LHS non-terminal
        production = " ".join(lines[line_index + 1].split())  # RHS as a single string
        line_index += 2  # Move to the next production rule

        # Find existing non-terminal in productions list
        for rule in productions:
            if rule[0] == non_terminal:
                rule.append(production)  # Add new production to existing non-terminal
                break
        else:
            productions.append([non_terminal, production])  # Add new non-terminal with its production

    return non_terminals, terminals, productions


def validate_string(current_expansion, input_tokens, rule_index, token_index, grammar_rules):
    """
    Recursively checks whether the input tokens match the grammar.

    :param current_expansion: The current sequence of symbols being checked.
    :param input_tokens: The list of tokens from the input string.
    :param rule_index: The current index in the expanded rule.
    :param token_index: The current index in the input string.
    :param grammar_rules The cfg rules in a list.
    :return: True if input matches the grammar, otherwise False.
    """

    # Base Case: If we've processed all symbols and tokens, return success
    if rule_index == len(current_expansion) and token_index == len(input_tokens):
        return True

    # If either list is exhausted prematurely, return failure
    if rule_index >= len(current_expansion) or token_index >= len(input_tokens):
        return False

    # If current symbol is a non-terminal, expand it
    for rule in grammar_rules:
        if current_expansion[rule_index] == rule[0]:  # Found a matching non-terminal
            for production in rule[1:]:  # Try each production rule
                expanded_rule = production.split()
                new_expansion = current_expansion[:rule_index] + expanded_rule + current_expansion[rule_index+1:]

                # Recursively check new expansion
                if validate_string(new_expansion, input_tokens, rule_index, token_index, grammar_rules):
                    return True

    # If the current symbol is a terminal and matches the input token, continue checking
    if current_expansion[rule_index] == input_tokens[token_index]:
        return validate_string(current_expansion, input_tokens, rule_index + 1, token_index + 1, grammar_rules)

    return False  # No valid match found


def main():
    grammar_expr_file = sys.argv[1]  # takes in the grammar file

    # Creates a list of terminals, non-terminals, and the productions
    non_terminals, terminals, productions = create_cfgs(grammar_expr_file)

    # Read input from stdin
    input_string = sys.stdin.read().strip()
    input_string_tokens = input_string.split()

    if validate_string([non_terminals[0]], input_string_tokens, 0, 0, productions):
        print("string is valid")
    else:
        print("string is invalid")


main()
