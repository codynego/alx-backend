#!/usr/bin/env python3

"""
Pagination
"""


def index_range(page, page_size):
    """ function should return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters
    """
    total_page_size = page * page_size
    current_start_index = total_page_size - page_size

    return tuple((current_start_index, total_page_size))
