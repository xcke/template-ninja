import csv
from jinja2 import Environment, PackageLoader, FileSystemLoader
from main import logger
import datetime
def load_csv(configfile):
    """Loads the element from the CSV file and returns as dict """
    results = []
    try:
        configdict = csv.DictReader(open(configfile, encoding='utf-8'), delimiter=';')
        for row in configdict:
            results.append(row)
        return results
    except Exception as e:
        logger.info("There was an issue with loading {}".format(configfile))
        logger.debug(f"Exception was: {e}")

def load_template(directory, template_name):
    """ Will load the template object from a Directory """
    jinja2_env = Environment(loader=FileSystemLoader(directory))
    template = jinja2_env.get_template(template_name)
    return template

def datetimenow():
    """
    Function for datetime
    :return:
    """
    now = datetime.datetime.now()
    return str(now.strftime("%Y%m%d%H%M"))