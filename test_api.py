import requests
import argparse
import time
import json
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Send a POST request with YAML data from a file and poll for status.')
    parser.add_argument('--url', type=str, default='http://localhost:8080/dynaa/simulation',
                        help='The URL to send the POST request to (default: http://localhost:8080/dynaa/simulation)')
    parser.add_argument('--file', type=str, default='./nexussim/examples/example-uc-traffic.yaml',
                        help='Path to the YAML file to send as data (default: ./nexussim/examples/example-uc-traffic.yaml)')
    parser.add_argument('--apikey', type=str, default='aa',
                        help='API key to include in the X-API-KEY header (default: aa)')
    parser.add_argument('--timeout', type=int, default=20,
                        help='Maximum time in seconds to wait for simulation to finish (default: 20)')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Optional path to save the final polling response (e.g., output.yaml)')
    args = parser.parse_args()

    # Read YAML data from file
    try:
        with open(args.file, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        logging.error(f"File '{args.file}' not found.")
        sys.exit(1)

    # Send the POST request
    try:
        response = requests.post(
            args.url,
            headers={
                'accept': 'application/json',
                'X-API-KEY': args.apikey,
                'Content-Type': 'application/yaml'
            },
            data=data
        )
        logging.info(f"Initial POST Status Code: {response.status_code}")
        logging.info(f"Initial Response Body: {response.text}")
    except requests.RequestException as e:
        logging.error(f"POST request failed: {e}")
        sys.exit(1)

    # Extract simulation ID from response text
    simulation_id = response.text.strip().strip('"')

    # Polling loop
    status_url = f"{args.url}/{simulation_id}"
    final_response = None
    for _ in range(args.timeout):
        try:
            poll_response = requests.get(
                status_url,
                headers={
                    'accept': 'application/json',
                    'X-API-KEY': args.apikey
                }
            )
            poll_data = poll_response.json()
            status = poll_data.get('status')
            logging.info(f"Polling Status: {status}")
            if status in ['finished', 'error']:
                final_response = poll_response
                requests.delete(status_url, headers={'X-API-KEY': args.apikey})
                break
        except requests.RequestException as e:
            logging.error(f"Polling request failed: {e}")
            break
        except json.JSONDecodeError:
            logging.error("Failed to parse polling response.")
            break
        time.sleep(1)
    else:
        logging.error("Timeout expired before simulation finished.")

    # Save final response if requested
    if final_response and args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(final_response.text)
            logging.info(f"Final response saved to {args.output}")
        except IOError as e:
            logging.error(f"Failed to write output file: {e}")

if __name__ == '__main__':
    main()
