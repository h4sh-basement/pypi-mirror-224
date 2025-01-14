import urllib.parse
from datetime import date

from metaboatrace.models.stadium import StadiumTelCode

from metaboatrace.scrapers.official.website.v1707 import BASE_URL
from metaboatrace.scrapers.official.website.v1707.utils import (
    format_date_for_query_string,
    format_stadium_tel_code_for_query_string,
)


def create_race_result_page_url(
    race_holding_date: date, stadium_tel_code: StadiumTelCode, race_number: int
):
    return f"{BASE_URL}/owpc/pc/race/raceresult?{urllib.parse.urlencode({'rno': race_number, 'jcd': format_stadium_tel_code_for_query_string(stadium_tel_code), 'hd': format_date_for_query_string(race_holding_date)})}"
