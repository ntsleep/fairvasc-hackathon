import sparql_dataframe
from pandas import DataFrame


class FairvascQuery:
    FAIRVASC_ENDPOINT = 'http://s14.adamczyk.krakow.pl:3001/gfev/query'
    FAIRVASC_VALIDATION_ENDPOINT = ''

    def fetchall(self, query) -> DataFrame:
        # TODO: implement validation when it will be done
        return self.fetchall_mock(query)

    def fetchall_mock(self, query) -> DataFrame:
        return sparql_dataframe.get(self.FAIRVASC_ENDPOINT, query)
