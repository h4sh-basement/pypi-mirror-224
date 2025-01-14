from ..._common.config import *
from ..._common.const import *
from ..._utils import _validate_args, get


__all__ = ['dataitems', 'packages', 'functions']


@_validate_args
def dataitems(search : str = None, package : str = None):
    """
    Return all usable data items.

    Parameters
    ----------
        search : str, default None
            Search word for Data Items name, the search is case-insensitive.
        package : str, default None
            Search word for package name, the search is case-insensitive.

    Returns
    -------
        pandas.DataFrame
            Data Items that belong to the search results.

        Columns:
            - *datamodule*
            - *datacomponent*
            - *dataitemid*
            - *datadescription*

    Examples
    --------
        >>> import prism
        >>> prism.market.dataitems(search='short')
           dataitemid  ...                               dataitemname
        0     1100035  ...                Broker Short Interest Value
        1     1100055  ...        Short Interest Ratio (Day to Cover)
        2     1100056  ...                      Short Interest Tenure
        3     1100057  ...                       Short Interest Value
        4     1100058  ...          Short Interest as % Of Free Float
        5     1100059  ...  Short Interest as % Of Shares Outstanding
        6     1100060  ...                                Short Score
        7     1100063  ...           Supply Side Short Interest Value
    """

    param = {'search': search, 'package': package}
    return get(URL_DATAITEMS, param)


def packages():
    """
    Return all available packages.

    Returns
    -------
        pandas.DataFrame:
            Packages the user has access to.

        **Columns:**
            - packageid (*int*): Unique identifier for each package.
            - packagename (*str*): Name of each package.
            - source (*str*): Source of each package (e.g., CIQ, FactSet, or Prism39).
            - vendor (*str*): Name of the vendor that provides each package (e.g., S&P, FactSet, or Prism39).

    Examples
    --------
        >>> import prism
        >>> packages_df = prism.packages()
        >>> print(packages_df.head())
           packageid                packagename  source vendor
        0       1001   CIQ Alpha Factor Library     CIQ    S&P
        1       1002                   CIQ Base     CIQ    S&P
        2       1003  CIQ Business Relationship     CIQ    S&P
        3       1005   CIQ Company Intelligence     CIQ    S&P
        4       1006   CIQ Company Relationship     CIQ    S&P
    """
    return get(URL_PACKAGES, None)


def functions():
    return get(URL_FUNCTIONS, None)


# list functions
@_validate_args
def _list_dataitem_financial(datacomponent: str = None, search : str = None, package : str = None):
    param = {'datacategory': 'Financial', 'datacomponent': datacomponent, 'search': search, 'package': package}
    return get(URL_DATAITEMS, param)


@_validate_args
def _list_dataitem_estimate(datacomponent, search : str = None, package : str = None):
    param = {'datacategory': 'Estimate', 'datacomponent': datacomponent, 'search': search, 'package': package}
    return get(URL_DATAITEMS, param)


@_validate_args
def _list_dataitem_market(datacomponent: str, search : str = None, package: str = None):
    param = {'datacategory': 'Market', 'datacomponent': datacomponent, 'search': search, 'package': package}
    return get(URL_DATAITEMS, param)


@_validate_args
def _list_dataitems_esg(datacomponent: str, search: str = None, package: str = None):
    param = {'datacategory': 'ESG', 'datacomponent': datacomponent, 'search': search, 'package': package}
    return get(URL_DATAITEMS, param)


@_validate_args
def _list_dataitem_precalculated(datacomponent: str, search : str = None, package : str = None):
    param = {'datacategory': 'Precalculated', 'datacomponent': datacomponent, 'search': search, 'package': package}
    return get(URL_DATAITEMS, param)


@_validate_args
def _list_dataitem_index(datacomponent: str, search : str = None, package : str = None):
    param = {
        'datacategory': 'Index',
        'datacomponent': datacomponent,
        'search': search,
        'package': package
    }
    return get(URL_DATAITEMS, param)


@_validate_args
def _list_dataitem_event(datacomponent: str = None, search : str = None, package : str = None):
    param = {'datacategory': 'Event', 'datacomponent': datacomponent, 'search': search, 'package': package}
    return get(URL_DATAITEMS, param)


@_validate_args
def _list_dataitem_industry(datacomponent: str = None, search : str = None, package : str = None):
    param = {'datacategory': 'Industry', 'datacomponent': datacomponent, 'search': search, 'package': package}
    return get(URL_DATAITEMS, param)