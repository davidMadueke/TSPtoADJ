def read_tsplib(file_name):
    """
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

    """
    import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(file_name)
    except ET.ParseError as e:
        print('There was a problem parsing', fileName, ':\n', e)
        return
    except IOError as e:
        print('There was a problem opening the file:\n', e)
        return

    # get root
    root = tree.getroot()

    # graph data (list of list: [[]])
    adj_mat = []
    symmetric = False
    try:  # in case vertex.cost attribute is not set or incorrect type
        for idx_from, vertice in enumerate(root.iter('vertex')):
            tmp = []
            for idx_to, edge in enumerate(vertice):
                # symmetric problems don't have values for main diagonal
                if idx_from == idx_to != int(edge.text):  # insert diagonal 0's
                    tmp.append(0)
                    symmetric = True
                tmp.append(float(edge.get('cost')))
            adj_mat.append(tmp)
        if symmetric:
            adj_mat[idx_to + 1].append(0)  # set last diagonal element to 0
    except TypeError:
        print('One of the values of the graph attributes is not valid.')
        print('Hint:', idx_from, '->', idx_to, '=', edge.get('cost'))
        return

    return adj_mat

def print_matrix(mat, show_all=False, linewidth=1000, threshold=5000):
    import numpy
    numpy.set_printoptions(linewidth=linewidth)
    numpy.set_printoptions(precision=3)
    # this forces to print all elements on a long row, on the next line
    # otherwise, center elements are snipped '...,' to fit line of 100
    if show_all:
        numpy.set_printoptions(threshold=threshold)

    print(numpy.array(mat))