from hestia_earth.schema import TermTermType
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name, extract_grouped_data_closest_date
from hestia_earth.utils.tools import safe_parse_float

from .term import DEFAULT_COUNTRY_ID

LOOKUP_GROUPING = {
    TermTermType.CROP.value: download_lookup(f"{TermTermType.CROP.value}.csv", True),
    TermTermType.ANIMALPRODUCT.value: download_lookup(f"{TermTermType.ANIMALPRODUCT.value}.csv", True)
}
LOOKUP_GROUPING_COLUMN = {
    TermTermType.CROP.value: 'cropGroupingFaostatProduction',
    TermTermType.ANIMALPRODUCT.value: 'animalProductGroupingFAO'
}


def production_quantity_lookup(term: dict):
    try:
        term_type = term.get('termType')
        lookup = LOOKUP_GROUPING.get(term_type)
        grouping_column = LOOKUP_GROUPING_COLUMN.get(term_type)
        grouping = get_table_value(lookup, 'termid', term.get('@id'), column_name(grouping_column)) if all([
            lookup is not None, grouping_column is not None
        ]) else None
        return (
            download_lookup(f"region-{term_type}-{grouping_column}-productionQuantity.csv"),
            grouping
        ) if grouping else (None, None)
    except Exception:
        return None, None


def production_quantity_country(lookup, lookup_column: str, year: int, country_id: str = DEFAULT_COUNTRY_ID):
    country_value = get_table_value(lookup, 'termid', country_id, column_name(lookup_column))
    return safe_parse_float(extract_grouped_data_closest_date(country_value, year), 1)
