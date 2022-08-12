"""
Example usage of this module to start a (non-existant) node application with entry point under bin/www
"""

import logging
import os
import sys

from http_cli import find_unique_port, get_base_url, start_server, do_request_response, stop_server

if __name__ == "__main__":
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.getLogger().setLevel(logging.INFO)

    port = find_unique_port()
    url = get_base_url(host="localhost", port=port)
    texttest_home = os.environ.get("TEXTTEST_HOME", os.getcwd())

    logging.info(f"starting Example Application on url {url}")

    process = start_server(
        command=["node",  f"{texttest_home}/bin/www"],
        port=port,
    )
    try:
        do_request_response(base_url=url)
    finally:
        stop_server(process)
