# returns status code for web url
import requests
import sys



run = True
while run: 
    target = input("Enter target url: ")
    try:
        response = requests.get(target)
        status = response.status_code

        if len(sys.argv) != target:
            print("Incorrect usage, enter target IP to get http status")
            sys.exit(1)
        else:
            for status in range(100, 511):
                if 200 <= status <= 226:
                    print("slow processing: ", status)
                elif 200 <= status <= 226:
                    print("It is live:", status)
                elif 300 <= status <= 308:
                    print("website redirect, check nano file:", status)
                elif 400 <= status <= 451:
                    print("Client error response: ", status)
                elif 500 <= status <= 511:
                    print("likely server error: ", status)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    exit_input = input("Do you want to check another URL? (Y/N)").strip().lower()
    if exit_input != 'yes':
        run = False
            