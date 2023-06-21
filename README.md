# subcriminalip

Subcriminal is a powerful Python 3 tool that utilizes the CriminalIP API to effortlessly discover subdomains, domains, organization names, and IP addresses associated with a specific domain. It offers a straightforward approach to identify and extract valuable information from the target domain.

With Subcriminal, users from diverse security disciplines such as pentesters, bugbounty hunters, security researchers, OSINT practitioners, and red teamers can effectively and efficiently gather relevant data for their respective purposes.

## Installation And Setup

1- clone the project :
```
git clone https://github.com/KamilDogo/subcriminalip.git
```

2. Prepare and activate the virtual environment :
```
$ python3 -m venv myenv
$ source myenv/bin/activate
```

3. Install requirements :
```
(myenv) $ pip install -r requirements.txt
```

To make use of the tool, you will need to acquire an API key from CriminalIP. Once you have obtained the key, open the script subcriminalip.py using your preferred editor and assign it to the api_key variable in config.py file . This ensures that the tool can authenticate and access the CriminalIP API seamlessly.

```
cip_api_key = "******YOUR_API_KEY_HERE*******"
```

## Usage

```
usage: subcriminalip.py [-h] [-g GET] [-s] [-t OFFSET] [-i] [-o] [-d]

Tool to search for domains , subdomains , IPs and orgname from CriminalIP API

optional arguments:
  -h, --help            show this help message and exit
  -g GET, --get GET     target
  -s, --subdomains      extract subdomains
  -t OFFSET, --offset OFFSET
                        Starting position in the dataset
  -i, --ips             extract ips adresses
  -o, --orgnames        extract organization names
  -d, --domains         extract domain names
```

### Get subdomains :
```
$ python3 subcriminalip.py -g "airbnb.com" -s
*.admin.airbnb.com
*.airbnb.com
```

### Get orgnames related to a domain :
```
python3 subcriminalip.py -g "airbnb.com" -o

SALESFORCE.COM, INC.
Airbnb, Inc.
Unplace.co.jp
```

### Get IPs related to a domain :
```
python3 subcriminalip.py -g "airbnb.com" -i
106.15.81.69
107.178.248.28
107.21.58.97
107.22.104.63
```
### Get list of domains belonging to a target :
```
python3 subcriminalip.py -g "airbnb.com" -d
...
fastly.airbnb.com
fastly-staging.airbnb.com
api.airbnb.com
api-fastly.airbnb.com
api-fastly-staging.airbnb.com
...
```

### Notes

Exercise caution when using the tool, as it may retrieve assets that do not belong to the target domain. It is crucial to ensure that you are within the intended scope while conducting your testing to avoid unintended consequences or potential unauthorized access



## Disclaimer

Kindly be aware that I assume no responsibility for any outcomes or harm resulting from the usage of this tool. subcriminalip is designed solely for educational purposes. It is vital to exercise responsible usage of this tool and adhere to relevant laws and regulations. The user bears full responsibility for any actions taken based on the information obtained from this tool. Prior authorization should always be obtained before conducting security assessments or vulnerability scans to ensure compliance and adherence to proper protocols

## Note
To ensure proper functionality of the tool, it relies on CriminalIP. If you encounter any errors during execution, it may indicate that you have exceeded the query limit associated with your API key. For more information and detailed guidance, please visit the [CriminalIP](https://www.criminalip.io/en/pricing) website
