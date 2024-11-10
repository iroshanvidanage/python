# >>> billing.py
import json
from pathlib import Path
import sys

def deserialize(data: str) -> dict:
    return json.load(data)

class BillingSummaryError(Exception): ...

def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())
            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError as ex:
        raise BillingSummaryError('unexpected file format.') from ex
    except FileNotFoundError:
        raise BillingSummaryError('missing required file.') from ex
    except ValueError:
        raise BillingSummaryError('non-numeric payment amount.') from ex
    except Exception as ex:
        raise BillingSummaryError('unplanned exception.') from ex
    

def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())
            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError as ex:
        raise BillingSummaryError('unexpected file format.') from None
    except FileNotFoundError:
        raise BillingSummaryError('missing required file.') from None
    except ValueError:
        raise BillingSummaryError('non-numeric payment amount.') from None
    except Exception as ex:
        raise BillingSummaryError('unplanned exception.') from None

# >>>payment.json
{
    "m": {
        "jan": [],
        "feb": [],
        "mar": [],
        "apr": [],
        "may": [],
        "jun": [],
        "jul": [],
        "aug": [],
        "sep": [],
        "oct": [],
        "nov": [],
        "dec": [],
    }
}



# >>> report.py
from datetime import datetime
from billing import summarize_monthly

this_month = datetime.now().strftime('%b').lower()
this_month = summarize_monthly()[this_month]

print(f'The total for this month is: ${this_month}')
