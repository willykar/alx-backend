#!/usr/bin/env python3
""" simple_pagination module """


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ index_range that takes two integer arguments
    page and page_size
    Return: a tuple of size two containing a start
    index and an end index
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a list of rows from the dataset for the
        given page and page size.
        """
        # Check that page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0,
        "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0,
        "page_size must be a positive integer"

        # Get the dataset
        dataset = self.dataset()

        # Calculate the index range
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]
