# -*- coding: latin-1 -*-
#

from .rdfx_cli import convert, merge
from .persistence_systems import File, Fuseki, PersistenceSystem, String, S3, GraphDB, SOP

# version compliant with https://www.python.org/dev/peps/pep-0440/
__version__ = "0.5"

__all__ = ['convert', 'FILE', '__version__', 'Fuseki',
           'PersistenceSystem', 'String', 'S3', 'GraphDB', 'SOP', 'merge']
