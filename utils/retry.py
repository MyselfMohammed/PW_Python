import time


class Retry:

    @staticmethod
    def execute(function,
                retries=3,
                delay=2):

        last_exception = None

        for attempt in range(retries):

            try:

                return function()

            except Exception as e:

                last_exception = e

                time.sleep(delay)

        raise last_exception