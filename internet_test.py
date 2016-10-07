import os
import logging
import time

logging.basicConfig(filename="connection.log",
                    format='%(levelname)s: %(asctime)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
logging.info("Program started")

hostname = "google.com"


def main():
    try:
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            print(hostname + ' is up!')
            # logging.info(hostname + ' is up!')
            ping, download, upload = get_speedtest_results()
        else:
            print(hostname + ' is down!')
            # logging.error(hostname + ' is down!')
    except ValueError as err:
        logging.info(err)
    else:
        try:
            logging.info("%5.1f %5.1f %5.1f", ping, download, upload)
            print(ping, download, upload)
        except UnboundLocalError:
            logging.error("The internet is down.")


def get_speedtest_results():
    ping = download = upload = None
    speedtest_output = os.popen('speedtest-cli --simple')

    for line in speedtest_output:
        label, value, unit = line.split()

        if 'Ping' in label:
            ping = float(value)
        elif 'Download' in label:
            download = float(value)
        elif 'Upload' in label:
            upload = float(value)

    if all((ping, download, upload)):  # if all 3 values were parsed
        # logging.info(ping, download, upload)
        return ping, download, upload
    else:
        logging.error('internet is down!')


while True:
    main()
    time.sleep(30)

logging.info("Done!")
