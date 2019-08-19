"""
AgileEngine Code Challenge:


"""
import logging
import sys


from pydom import HtmlDocument, HtmlNode

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        logging.error('Missing arguments:')
        logging.error('\tpython app.py reference_file.html check_file.html tag_id')
        exit(1);

    #load dom for reference file
    html = HtmlDocument(sys.argv[1])

    #load dom for check file
    html2 = HtmlDocument(sys.argv[2])

    #id of tag to find in reference file
    id=sys.argv[3]

    # find element by id in the dom
    node = html.find("#{}".format(id))

    if node == None:
        logging.error('Error: ID not found in reference file')
        exit(1)


    # find the best match  for the tag in reference file
    # the tag with more matches in attributes will be returned
    found = html2.findBestMatch(node)

    if found == None:
        logging.error('Error: no tag was be found in the check file')
        exit(1)

    logging.info('Element found:')
    logging.info('--------------')
    logging.info(found.html())

    logging.info('Path of found tag inside check file:')
    logging.info('------------------------------------')
    logging.info(found.path())