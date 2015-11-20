import numpy as np


def convert_to_mirror(length, vec):
    """Converts a condensed 1D array to a mirror 2D array

    Inputs
    ------
    length : int
        The length of the distance matrix
    vec : array
        A one-dimensional condensed array of the values to populate the
        distance matrix

    Returns
    -------
    dm : array
        A two dimensional symetrical matrix of length x length.
    """

    vec = np.hstack(vec)
    # Creates the output matrix
    dm = np.zeros((length, length))
    # Adds a counter to watch the positon
    pos_count = 0

    # Populates the distance matrix
    for idx in xrange(length-1):
        # Gets the position for the two dimensional matrix
        pos2 = np.arange(idx+1, length)
        # Gets the postion for hte one dimensional matrix
        pos1 = np.arange(idx, length-1) + pos_count
        pos_count = pos_count + len(pos1) - 1
        # Updates the data in the matrices
        dm[idx, pos2] = vec[pos1]
        dm[pos2, idx] = vec[pos1]

    return dm

def _build_pooled_matrix(dm0, dm1, dmi):
    """Combines the pooled distance matrices into a single matrix"""
    return np.vstack((np.hstack((dm0, dmi)),
                      np.hstack((dmi[::-1, ::-1], dm1))
                      ))
