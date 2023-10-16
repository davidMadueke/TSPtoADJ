# A libray for converting TSPLIB XML files into a Adjacency Matrix NUMPY array

This Library has been taken from the PYGMO TSP Utils library which has been since deprecated. Unfortunately the updated library, PYGMO v2, does not have the following helper functions below, which is why I have created this library. 

This library has only two functions:

read_tsplib(file_name):

This function parses an XML file defining a TSP (from TSPLIB
    http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/)
    and returns the Adjacency Matrix that can be used for developing Travelling Salesman Problems

    Args:
            file_name (string): The XML file to be opened for parsing.
    Returns:
            adj_mat (double): Adjacency Matrix, 0 per diagonal.
    Raises:
    IOError:
            The input file was not found.
    TypeError:
            At least one of the attributes in an edge
            of the XML file is missing or of the wrong type.
    xml.etree.ElementTreeParseError:
            There was an error parsing the file.
            See: https://docs.python.org/2.7/library/xml.etree.elementtree.html

print_matrix(mat, showall=False):

    # this forces to print all elements on a long row, on the next line
    # otherwise, center elements are snipped '...,' to fit line of 100

    Args:
            mat: The adjacency matrix to be printed.
            showall (bool): If true, this forces to print all elements on a long row, on the next line otherwise, center elements are snipped '...,' to fit line of 100
    Returns:
            none
            