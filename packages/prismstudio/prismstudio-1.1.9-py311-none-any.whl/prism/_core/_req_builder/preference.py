import pandas as pd

from ..._common.config import URL_PREFERENCES as _URL_PREFERENCES
from ..._common.const import COMPONENT2CATEGORY as _COMPONENT2CATEGORY, SMValues
from ..._utils import get as _get, patch as _patch, post as _post, _validate_args, get_sm_attributevalue
from ..._utils.exceptions import PrismTypeError, PrismValueError


__all__ = [
    "set_default_attributes",
    "get_default_attributes",
    "set_package_priority",
    "get_package_priority",
    "set_preference",
    "get_preference",
]


@_validate_args
def set_default_attributes(attributes: list):
    """
    Set default Security Master attributes to be used in data, universe, portfolio and reports.

    Parameters
    ----------
        attributes : list
            List of Security Master attributes to be set as default Security Master attributes.

    Returns
    -------
        status: dict
            Status of set_default_attributes.

    Examples
    --------
        >>> prism.preference.get_default_attributes()
        []

        >>> prism.preference.set_default_attributes(["CIQ Primary", "Country"])
        {
        'status': 'Success',
        'message': 'Attributes saved',
        'result': [{'resulttype': None, 'resultvalue': None}]
        }

        >>> prism.preference.get_default_attributes()
        ["CIQ Primary", "Country"]
    """
    attributevalues = [get_sm_attributevalue(a) for a in attributes]
    ret = _patch(_URL_PREFERENCES + "/attribute", {"attributes": attributevalues}, None)
    print(f'{ret["message"]}')
    print(f"Default attributes are: {get_default_attributes()}")
    return ret


@_validate_args
def get_default_attributes():
    """
    Return default Security Master attributes to show on data, universe, portfolio and reports.

    Returns
    -------
        list
            Current default Security Master attributes.

    Examples
    --------
        >>> prism.preference.get_default_attributes()
        ["Company Name", "ISIN", "Ticker"]
    """
    ga = _get(_URL_PREFERENCES + "/attribute")
    from ..._common.const import SMValues
    return [k for k, v in SMValues.items() if v in ga]


@_validate_args
def set_package_priority(datacomponent: str, package_priority: list):
    """
    Set default package priorities to be used from each data component.

    Parameters
    ----------
        datacomponent : str
            Data component to change the package priorities of. eg. close, open, balance_sheet.

        package_priority : list of dict
            List of dictionary indicating the priorities of packages. Keys of the dictionary should be: “package” and “priority”.

    Returns
    -------
    status: dict
        Status of set_package_priority.

    Examples
    --------
        >>> datacomponent = "Close"
        >>> package_priority = [
            {"package": "CIQ Market", "priority": 1},
            {"package": "Prism Market", "priority": 2},
            {"package": "Compustat", "priority": 3},
            {"package": "MI Integrated Market", "priority": 4}
        ]
        >>> prism.preference.set_package_priority(datacomponent=datacomponent, package_priority=package_priority)
        {
        'status': 'Success',
        'message': 'Package priorities saved',
        'result': [{'resulttype': None, 'resultvalue': None}]
        }

        >>> priorities_df = prism.preference.get_package_priority()
        >>> priorities_df[priorities_df["datacomponent"] == "Close"]
            datacategory  datacomponent           packagename  priority
        0         Market          Close            CIQ Market         1
        1         Market          Close          Prism Market         1
        2         Market          Close             Compustat         1
        3         Market          Close  MI Integrated Market         1
    """
    if datacomponent not in _COMPONENT2CATEGORY.keys():
        raise PrismValueError("Datacomponent should be one of prism data components.")
    old_priorities_df = get_package_priority()
    priorities = old_priorities_df[old_priorities_df['datacomponent'] != datacomponent]
    datacategory = old_priorities_df[old_priorities_df['datacomponent'] == datacomponent].iloc[0, :]['datacategory']
    new_priorities = []
    for i in package_priority:
        if not isinstance(i, dict):
            raise PrismTypeError("Elements of package priority should be a dictionary.")
        if {"package", "priority"} != set(i.keys()):
            raise PrismValueError("Package priority should have packagename and priority as keys.")
        new_priorities.append({"datacategory": datacategory, "datacomponent": datacomponent, "packagename": i["package"], "priority": i["priority"]})
    priorities = pd.concat([priorities, pd.DataFrame(new_priorities)])
    ret = _patch(_URL_PREFERENCES + "/package_priority", None, priorities.to_dict(orient='records'))
    print(f'{ret["message"]}')
    return ret


@_validate_args
def get_package_priority():
    """
    Return default package priorities to be used from each data component.

    Returns
    -------
        pandas.DataFrame
            | Package priorities to be used from each data component.
            | Columns:

            - *datacategory*
            - *datacomponent*
            - *packagename*
            - *priority*

    Examples
    --------
        >>> prism.preference.get_package_priority()
            datacategory         datacomponent               packagename  priority
        0         Estimate                Actual    CIQ Estimate Consensus         1
        1         Estimate             Consensus    CIQ Estimate Consensus         1
        2         Estimate                Growth    CIQ Premium Financials         1
        3         Estimate              Guidance    CIQ Estimate Consensus         1
        4         Estimate              Revision    CIQ Estimate Consensus         1
        ...            ...                   ...                     	 ...       ...
        71          Market                Volume                CIQ Market         4
        72          Market                Volume      MI Integrated Market         3
        73          Market                Volume                 Compustat         2
        74          Market                Volume              Prism Market         1
        75   Precalculated  Alpha Factor Library  CIQ Alpha Factor Library         1
    """
    return _get(_URL_PREFERENCES + "/package_priority")


@_validate_args
def set_preference(settings: dict):
    """
    Set default Security Master attributes to be used in data, universe, portfolio and reports.

    Parameters
    ----------
        settings : dict
            | Dictionary of settings to be set as preference.
            | Setting keys are: ['timezone', 'quiet_mode']

    Returns
    -------
        status : dict
            Status of set_preference.

    Examples
    --------
        >>> prism.preference.get_preference()
        preferencetype	 preferencevalue               updatedate
        0      quiet_mode	            true  2023-02-21 08:05:16.760
        1        timezone	             KST  2023-02-14 08:20:55.626

        >>> prism.preference.set_preference({ "quiet_mode": False, "timezone": "UTC" })
        {
        'status': 'Success',
        'message': 'Preference saved',
        'result': [{'resulttype': None, 'resultvalue': None}]
        }

        >>> prism.preference.get_preference()
           preferencetype	 preferencevalue               updatedate
        0      quiet_mode	           false  2023-02-21 08:05:16.760
        1        timezone	             UTC  2023-02-14 08:20:55.626
    """
    return _post(_URL_PREFERENCES + "/gui", params={}, body=settings)


@_validate_args
def get_preference(setting: str = ""):
    """
    Return preference of current user.

    Returns
    -------
        pandas.DataFrame
            | Setting of current user's preference.
            | Columns:

            - *preferencetype: preference keyword*
            - *preferencevalue: value of preference keyword*
            - *updatedate*

    Examples
    --------
        >>> prism.preference.get_preference()
           preferencetype	 preferencevalue               updatedate
        0      quiet_mode	           false  2023-02-21 08:05:16.760
        1        timezone	             UTC  2023-02-14 08:20:55.626

    """
    params = {}
    if setting:
        params = {"preferencetype": setting}
    return _get(_URL_PREFERENCES + "/gui", params=params)


def get_quiet_mode():
    quiet_mode = get_preference("quiet_mode")
    if quiet_mode.empty:
        return False
    return quiet_mode["preferencevalue"][0] == 'true'
