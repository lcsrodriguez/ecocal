from .utils import *


class Calendar:
    __class__: str = "Calendar"
    __slots__: dict = ("startHorizon", "endHorizon", "calendar", "details", "detailedCalendar", "URL",
                       "_hasCollectedCalendar", "_hasCollectedDetailedCalendar", "_withProgressBar", "nbThreads")

    def __init__(self,
                 startHorizon: Union[datetime.datetime, str] = None,
                 endHorizon: Union[datetime.datetime, str] = None,
                 preBuildCalendar: bool = True,
                 withDetails: bool = False,
                 withProgressBar: bool = True,
                 nbThreads: int = DEFAULT_THREADS) -> None:

        if isinstance(startHorizon, (datetime.datetime, datetime.date)):
            startHorizon = startHorizon.strftime("%Y-%m-%d")
        if isinstance(endHorizon, (datetime.datetime, datetime.date)):
            endHorizon = endHorizon.strftime("%Y-%m-%d")

        self.startHorizon: str = startHorizon if startHorizon is not None else "2020-01-01" # Default values
        self.endHorizon: str = endHorizon if startHorizon is not None else "2023-12-31"

        self._hasCollectedCalendar: bool = False
        self._hasCollectedDetailedCalendar: bool = False
        self._withProgressBar: bool = withProgressBar

        self.calendar: Union[pd.DataFrame, None] = None                 # Basic calendar dataframe
        self.details: Union[pd.DataFrame, None] = None                  # Details dataframe
        self.detailedCalendar: Union[pd.DataFrame, None] = None         # Merged calendar (with details) dataframe

        self.nbThreads: int = nbThreads
        assert self.nbThreads > 0

        if preBuildCalendar:
            try:
                r_ = self._buildCalendar()
                if not r_:
                    raise Exception(f"An error occured.")
            except Exception as e:
                raise Exception(f"An error occured ({e})")
        if withDetails:
            self._mergeTableDetails()

    def __str__(self) -> str:
        return f"Calendar - [{self.startHorizon}] --> [{self.endHorizon}] " \
               f"(Collected ?: {self._hasCollectedCalendar}) " \
               f"(Details ?: {self._hasCollectedDetailedCalendar}) "

    def __repr__(self) -> None:
        print(self.__str__())

    def _buildCalendar(self) -> bool:
        self.URL = f"{API_SOURCE_URL}/{self.startHorizon}T00:00:00Z/{self.endHorizon}T23:59:59Z" \
                   f"?&volatilities=NONE" \
                   f"&volatilities=LOW" \
                   f"&volatilities=MEDIUM" \
                   f"&volatilities=HIGH" \
                   f"&countries=US&countries=UK&countries=EMU&countries=DE&countries=CN&countries=JP&countries=CA&countries=AU" \
                   f"&countries=NZ&countries=CH&countries=FR&countries=IT&countries=ES&countries=UA" \
                   f"&categories=8896AA26-A50C-4F8B-AA11-8B3FCCDA1DFD" \
                   f"&categories=FA6570F6-E494-4563-A363-00D0F2ABEC37" \
                   f"&categories=C94405B5-5F85-4397-AB11-002A481C4B92" \
                   f"&categories=E229C890-80FC-40F3-B6F4-B658F3A02635" \
                   f"&categories=24127F3B-EDCE-4DC4-AFDF-0B3BD8A964BE" \
                   f"&categories=DD332FD3-6996-41BE-8C41-33F277074FA7" \
                   f"&categories=7DFAEF86-C3FE-4E76-9421-8958CC2F9A0D" \
                   f"&categories=1E06A304-FAC6-440C-9CED-9225A6277A55" \
                   f"&categories=33303F5E-1E3C-4016-AB2D-AC87E98F57CA" \
                   f"&categories=9C4A731A-D993-4D55-89F3-DC707CC1D596" \
                   f"&categories=91DA97BD-D94A-4CE8-A02B-B96EE2944E4C" \
                   f"&categories=E9E957EC-2927-4A77-AE0C-F5E4B5807C16"

        try:
            start_clock = time.time()
            r = requests.get(url=self.URL,
                             headers={
                                 "Accept": "text/csv",
                                 "Content-Type": "text/csv",
                                 "Referer": BASE_URL,
                                 "Connection": "keep-alive",
                                 "User-Agent": DEFAULT_USER_AGENT,
                             })
            end_clock = time.time()
            dur_clock = end_clock - start_clock
        except Exception as e:
            raise Exception(f"An error just occurred (Error: {e})")
        if r.status_code != 200:
            raise Exception(f"An error just occurred")
        df = pd.read_csv(
            filepath_or_buffer=io.StringIO(r.content.decode("utf-8")),
            na_values=np.NaN
        )
        self.calendar: pd.DataFrame = df
        self._hasCollectedCalendar = True
        return self._hasCollectedCalendar

    def getCalendar(self, withDetails: bool = True) -> pd.DataFrame:
        if not self._hasCollectedCalendar: self._buildCalendar()
        if withDetails:
            return self.detailedCalendar
        return self.calendar

    def saveCalendar(self, saveDetails: bool = True) -> None:
        if not self._hasCollectedCalendar: self._buildCalendar()
        try:
            if saveDetails:
                if self.detailedCalendar is None:
                    self._mergeTableDetails()
                self.detailedCalendar = self.detailedCalendar.replace(r'\n', ' ', regex=True)
                self.detailedCalendar = self.detailedCalendar.replace(r'\r', ' ', regex=True)
                self.detailedCalendar.drop(["name", "currencyCode"], axis=1, inplace=True)
                self.detailedCalendar.to_csv(path_or_buf=f"ecocal_DETAILS_{datetime.datetime.now().isoformat()}.csv",
                                            index_label="Card ID")
            else:
                self.calendar.to_csv(path_or_buf=f"ecocal_BASIC_{datetime.datetime.now().isoformat()}.csv",
                                   index_label="Card ID")
        except OSError as e:
            raise Exception(f"An error has occurred ({e})")
        except Exception as e:
            raise Exception(f"An error has occurred ({e})")

    def _getDetails(self) -> pd.DataFrame:
        if not self._hasCollectedCalendar: self._buildCalendar()
        cg = 0
        LIMIT_ROW_GROUPING: int = self.nbThreads
        SANITY_SLEEP_TIMEOUT: int = 0
        resources: List[str] = []
        output: dict = {}
        if self._withProgressBar:
            R = tqdm(self.calendar.iterrows(), total=self.calendar.shape[0], desc="Details", ncols=100)
        else:
            R = self.calendar.iterrows()
        for index, row in R:
            cg += 1
            r_id = row["Id"]
            resources.append(r_id)

            if cg % LIMIT_ROW_GROUPING == 0:
                cg = 0
                threads = []
                for i, res_id in enumerate(resources):
                    t = Thread(target=self._requestDetails, args=(res_id, output))
                    t.start()
                    threads.append(t)

                for res_id, t in zip(resources, threads):
                    t.join()
                del threads
                time.sleep(SANITY_SLEEP_TIMEOUT)
                resources = []
        df_ = pd.DataFrame(data=output).T
        df_.rename(columns={"id": "Id"}, inplace=True)
        self._hasCollectedDetailedCalendar = True
        self.details = df_
        return self.details

    def _requestDetails(self, resource_id: str = "", output: dict = {}) -> Union[dict, None]:
        if not isinstance(resource_id, str) or str(resource_id) == "":
            raise Exception("Please enter a valid resource id")
        URL = f"{API_SOURCE_URL}/{resource_id}"

        s = requests.Session()
        s.mount("https://", adapter)
        s.mount("http://", adapter)
        r = s.get(url=URL,
                  headers={
                      "Accept": "application/json",
                      "Content-Type": "application/json",
                      "Referer": BASE_URL,
                      "Connection": "keep-alive",
                      "User-Agent": DEFAULT_USER_AGENT,
                  })
        if r.status_code // 100 == 2:
            output[resource_id] = r.json()
            return output[resource_id]
        return None

    def _mergeTableDetails(self) -> pd.DataFrame:
        if not self._hasCollectedCalendar: self._buildCalendar()
        if not self._hasCollectedDetailedCalendar: self._getDetails()
        df = pd.merge(left=self.calendar, right=self.details, how="left", on="Id")
        self.detailedCalendar = df
        return self.detailedCalendar
