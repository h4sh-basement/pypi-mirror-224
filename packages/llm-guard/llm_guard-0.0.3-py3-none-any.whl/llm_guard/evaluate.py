import logging
from typing import Dict

from .input_scanners.base import Scanner as InputScanner
from .output_scanners.base import Scanner as OutputScanner

logging.basicConfig(level=logging.INFO)

"""
This file contains main functionality for scanning both prompts and outputs of Large Language Models (LLMs).
There are two primary functions: 'scan_prompt' and 'scan_output'.
Each function takes a list of scanner objects and applies each scanner to the input string(s).

An Scanner in this context is an object of a class that inherits from either `input_scanners.Scanner` or `output_scanners.Scanner` base classes.
These base classes define an `scan` method that takes in a string and returns a processed string and a boolean value indicating the validity of the input string.

These functions return the processed string after all scanners have been applied, along with a dictionary mapping the name of each scanner to its validity result.
"""


def scan_prompt(scanners: list[InputScanner], prompt: str) -> (str, Dict[str, bool]):
    """
    Scans a given prompt using the provided scanners.

    Args:
        scanners: A list of scanner objects. Each scanner should be an instance of a class that inherits from `Scanner`.
        prompt: The input prompt string to be scanned.

    Returns:
        A tuple containing:
            - The processed prompt string after applying all scanners.
            - A dictionary mapping scanner names to boolean values indicating whether the input prompt is valid according to each scanner.
    """

    sanitized_prompt = prompt
    results = {}

    if len(scanners) == 0 or prompt.strip() == "":
        return sanitized_prompt, results

    for scanner in scanners:
        sanitized_prompt, is_valid = scanner.scan(sanitized_prompt)
        results[type(scanner).__name__] = is_valid

    return sanitized_prompt, results


def scan_output(scanners: list[OutputScanner], prompt: str, output: str) -> (str, Dict[str, bool]):
    """
    Scans a given output of a large language model using the provided scanners.

    Args:
        scanners: A list of scanner objects. Each scanner should be an instance of a class that inherits from `Scanner`.
        prompt: The input prompt string that produced the output.
        output: The output string to be scanned.

    Returns:
        A tuple containing:
            - The processed output string after applying all scanners.
            - A dictionary mapping scanner names to boolean values indicating whether the output is valid according to each scanner.
    """

    sanitized_output = output
    results = {}

    if len(scanners) == 0 or output.strip() == "":
        return sanitized_output, results

    for scanner in scanners:
        sanitized_output, is_valid = scanner.scan(prompt, sanitized_output)
        results[type(scanner).__name__] = is_valid

    return sanitized_output, results
