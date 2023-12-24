import numpy as np
import requests
import io
import pandas as pd
from typing import Union, List
import datetime
import time
from threading import Thread
from tqdm import tqdm
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from .constants import *

retry = Retry(
    total=5,
    backoff_factor=1
)
adapter = HTTPAdapter(
    max_retries=retry
)
