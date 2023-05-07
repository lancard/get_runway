import requests
import json
from bs4 import BeautifulSoup

all_runway_list = [ \
	{"airport":"RKJB",	"runway":"01/19",	"latitude1":34.97878277777778,		"longitude1":126.38285944444445,	"latitude2":35.00398555555555,		"longitude2":126.3826861111111},	 \
	{"airport":"RKJJ",	"runway":"04L/22R",	"latitude1":35.11562194444445,		"longitude1":126.8002361111111,		"latitude2":35.13776388888889,		"longitude2":126.81575},	 \
	{"airport":"RKJJ",	"runway":"04R/22L",	"latitude1":35.11475305555556,		"longitude1":126.802075000000,		"latitude2":35.136893888888885,		"longitude2":126.81758888888888},	 \
	{"airport":"RKJK",	"runway":"18/36",	"latitude1":35.915928888888885,		"longitude1":126.61299777777776,	"latitude2":35.89155944444445,		"longitude2":126.61879722222221},	 \
	{"airport":"RKJM",	"runway":"06/24",	"latitude1":34.75419472222222,		"longitude1":126.37353138888888,	"latitude2":34.763396944444445,		"longitude2":126.386915},	 \
	{"airport":"RKJY",	"runway":"17/35",	"latitude1":34.85102055555556,		"longitude1":127.61285388888888,	"latitude2":34.833488333333335,		"longitude2":127.62145194444444},	 \
	{"airport":"RKND",	"runway":"05/23",	"latitude1":38.153168888888885,		"longitude1":128.6062900000000,		"latitude2":38.14200916666666,		"longitude2":128.59458083333334},	 \
	{"airport":"RKNN",	"runway":"08/26",	"latitude1":37.74917305555556,		"longitude1":128.93054722222223,	"latitude2":37.75830777777778,		"longitude2":128.95935194444442},	 \
	{"airport":"RKNW",	"runway":"03/21",	"latitude1":37.4269800000000,		"longitude1":127.95357333333334,	"latitude2":37.448973333333335,		"longitude2":127.9671725},	 \
	{"airport":"RKNY",	"runway":"15/33",	"latitude1":38.070009722222224,		"longitude1":128.6602000000000,		"latitude2":38.05262499999999,		"longitude2":128.6781011111111},	 \
	{"airport":"RKPC",	"runway":"07/25",	"latitude1":33.499881111111115,		"longitude1":126.46847194444445,	"latitude2":33.514878055555556,		"longitude2":126.49764194444445},	 \
	{"airport":"RKPC",	"runway":"13/31",	"latitude1":33.51546111111111,		"longitude1":126.48739388888889,	"latitude2":33.507641944444444,		"longitude2":126.50041888888889},	 \
	{"airport":"RKPD",	"runway":"01/19",	"latitude1":33.38290388888888,		"longitude1":126.71159361111111,	"latitude2":33.40363277777778,		"longitude2":126.71149416666667},	 \
	{"airport":"RKPD",	"runway":"15/33",	"latitude1":33.392833333333336,		"longitude1":126.71765083333334,	"latitude2":33.40377027777778,		"longitude2":126.70754972222223},	 \
	{"airport":"RKPK",	"runway":"36L/18R",	"latitude1":35.1651825000000,		"longitude1":128.93881583333336,	"latitude2":35.19389527777778,		"longitude2":128.93513027777777},	 \
	{"airport":"RKPK",	"runway":"36R/18L",	"latitude1":35.16947388888889,		"longitude1":128.94057166666667,	"latitude2":35.194093055555555,		"longitude2":128.93739333333335},	 \
	{"airport":"RKPS",	"runway":"06L/24R",	"latitude1":35.08221555555556,		"longitude1":128.05691416666667,	"latitude2":35.09612166666667,		"longitude2":128.0816836111111},	 \
	{"airport":"RKPS",	"runway":"06R/24L",	"latitude1":35.08108055555556,		"longitude1":128.0596952777778,		"latitude2":35.09529194444445,		"longitude2":128.08447361111112},	 \
	{"airport":"RKPU",	"runway":"36/18",	"latitude1":35.58450416666667,		"longitude1":129.35245472222223,	"latitude2":35.602337222222225,		"longitude2":129.35099944444443},	 \
	{"airport":"RKSG",	"runway":"16/34",	"latitude1":36.9642975000000,		"longitude1":127.02437166666665,	"latitude2":36.95330055555556,		"longitude2":127.04028027777777},	 \
	{"airport":"RKSI",	"runway":"15L/33R",	"latitude1":37.48394444444445,		"longitude1":126.44015555555555,	"latitude2":37.456380555555555,		"longitude2":126.46467222222223},	 \
	{"airport":"RKSI",	"runway":"15R/33L",	"latitude1":37.48178888888889,		"longitude1":126.4363388888889,		"latitude2":37.45422500000001,		"longitude2":126.46085555555557},	 \
	{"airport":"RKSI",	"runway":"16L/34R",	"latitude1":37.47280833333333,		"longitude1":126.41556944444444,	"latitude2":37.443413888888884,		"longitude2":126.441725},	 \
	{"airport":"RKSI",	"runway":"16R/34L",	"latitude1":37.468718611111115,		"longitude1":126.41342833333334,	"latitude2":37.44123499999999,		"longitude2":126.43787166666667},	 \
	{"airport":"RKSM",	"runway":"01/19",	"latitude1":37.4341650000000,		"longitude1":127.11496222222222,	"latitude2":37.458728055555554,		"longitude2":127.11586527777777},	 \
	{"airport":"RKSM",	"runway":"02/20",	"latitude1":37.43250277777778,		"longitude1":127.11069555555555,	"latitude2":37.45872027777778,		"longitude2":127.11536277777778},	 \
	{"airport":"RKSO",	"runway":"09L/27R",	"latitude1":37.091204166666664,		"longitude1":127.01399444444444,	"latitude2":37.09375444444445,		"longitude2":127.04467888888888},	 \
	{"airport":"RKSO",	"runway":"09R/27L",	"latitude1":37.089338888888896,		"longitude1":127.01424166666666,	"latitude2":37.09189444444445,		"longitude2":127.04494444444444},	 \
	{"airport":"RKSS",	"runway":"14L/32R",	"latitude1":37.570751111111115,		"longitude1":126.77824833333334,	"latitude2":37.5477550000000,		"longitude2":126.80709138888888},	 \
	{"airport":"RKSS",	"runway":"14R/32L",	"latitude1":37.56846027777778,		"longitude1":126.77537333333333,	"latitude2":37.54803555555555,		"longitude2":126.80102749999999},	 \
	{"airport":"RKSW",	"runway":"15L/33R",	"latitude1":37.250860833333334,		"longitude1":126.9983563888889,		"latitude2":37.23125916666667,		"longitude2":127.01730083333332},	 \
	{"airport":"RKSW",	"runway":"15R/33L",	"latitude1":37.24973527777778,		"longitude1":126.99710583333334,	"latitude2":37.2302425000000,		"longitude2":127.016215},	 \
	{"airport":"RKTA",	"runway":"15/33",	"latitude1":36.59848916666667,		"longitude1":126.29334333333334,	"latitude2":36.5893200000000,		"longitude2":126.29984055555555},	 \
	{"airport":"RKTH",	"runway":"10/28",	"latitude1":35.98784166666667,		"longitude1":129.4086838888889,		"latitude2":35.9880525000000,		"longitude2":129.43214555555556},	 \
	{"airport":"RKTI",	"runway":"36L/18R",	"latitude1":37.017957777777774,		"longitude1":127.88152833333332,	"latitude2":37.04327027777778,		"longitude2":127.87871638888888},	 \
	{"airport":"RKTI",	"runway":"36R/18L",	"latitude1":37.01822888888889,		"longitude1":127.8833863888889,		"latitude2":37.042693611111105,		"longitude2":127.88076527777777},	 \
	{"airport":"RKTL",	"runway":"17/35",	"latitude1":36.78474722222222,		"longitude1":129.45878333333334,	"latitude2":36.769257777777774,		"longitude2":129.46477777777775},	 \
	{"airport":"RKTN",	"runway":"13L/31R",	"latitude1":35.90148111111111,		"longitude1":128.64677638888887,	"latitude2":35.887590833333334,		"longitude2":128.67190194444444},	 \
	{"airport":"RKTN",	"runway":"13R/31L",	"latitude1":35.90058611111111,		"longitude1":128.64593805555555,	"latitude2":35.88666055555556,		"longitude2":128.6710447222222},	 \
	{"airport":"RKTP",	"runway":"03L/21R",	"latitude1":36.69506916666666,		"longitude1":126.47276694444444,	"latitude2":36.71380611111111,		"longitude2":126.4832825},	 \
	{"airport":"RKTP",	"runway":"03R/21L",	"latitude1":36.69452805555555,		"longitude1":126.47450222222223,	"latitude2":36.71353527777778,		"longitude2":126.48497138888888},	 \
	{"airport":"RKTU",	"runway":"06L/24R",	"latitude1":36.71002777777778,		"longitude1":127.48679444444444,	"latitude2":36.72510555555556,		"longitude2":127.51112499999999},	 \
	{"airport":"RKTU",	"runway":"06R/24L",	"latitude1":36.7078500000000,		"longitude1":127.48745555555556,	"latitude2":36.722925000000004,		"longitude2":127.51179444444445},	 \
	{"airport":"RKTY",	"runway":"10/28",	"latitude1":36.631574166666674,		"longitude1":128.3398138888889,		"latitude2":36.63190138888889,		"longitude2":128.37030611111112},	 \
	{"airport":"ZKPY",	"runway":"01/19",	"latitude1":39.22710861111111,		"longitude1":125.67560277777778,	"latitude2":39.26308361111111,		"longitude2":125.67627861111112},	 \
	{"airport":"ZKPY",	"runway":"17/35",	"latitude1":39.22041611111111,		"longitude1":125.66439111111112,	"latitude2":39.19087138888889,		"longitude2":125.67602972222224} \
]


# create runway map
all_runway = {}
for item in all_runway_list:
    if item['airport'] not in all_runway:
        all_runway[item['airport']] = {}
    all_runway[item['airport']][item['runway'].split("/")[0]] = { "latitude1": item["latitude1"], "longitude1": item["longitude1"], "latitude2": item["latitude2"], "longitude2": item["longitude2"], "use": True }
    all_runway[item['airport']][item['runway'].split("/")[1]] = { "latitude1": item["latitude2"], "longitude1": item["longitude2"], "latitude2": item["latitude1"], "longitude2": item["longitude1"], "use": True }


# get from amos


# RKSI(113)
html = requests.get("http://global.amo.go.kr/amosobsnew/AmosRealTimeImage.do?stnId=113").text
soup = BeautifulSoup(html, 'html.parser')
rksi_33r = len(soup.select("div.airplane.right")) > 0
if rksi_33r:
	all_runway['RKSI']['15L']['use'] = False
	all_runway['RKSI']['15R']['use'] = False
	all_runway['RKSI']['16L']['use'] = False
	all_runway['RKSI']['16R']['use'] = False
else:
	all_runway['RKSI']['33L']['use'] = False
	all_runway['RKSI']['33R']['use'] = False
	all_runway['RKSI']['34L']['use'] = False
	all_runway['RKSI']['34R']['use'] = False

# RKSS(110)
html = requests.get("http://global.amo.go.kr/amosobsnew/AmosRealTimeImage.do?stnId=110").text
soup = BeautifulSoup(html, 'html.parser')
rkss_32r = len(soup.select("div.airplane.right")) > 0
if rkss_32r:
	all_runway['RKSS']['14L']['use'] = False
	all_runway['RKSS']['14R']['use'] = False
else:
	all_runway['RKSS']['32L']['use'] = False
	all_runway['RKSS']['32R']['use'] = False

# RKPC(182)
html = requests.get("http://global.amo.go.kr/amosobsnew/AmosRealTimeImage.do?stnId=182").text
soup = BeautifulSoup(html, 'html.parser')
rkpc_07 = len(soup.select("div.airplane.left")) > 0
if rkpc_07:
	all_runway['RKPC']['25']['use'] = False
else:
	all_runway['RKPC']['07']['use'] = False
all_runway['RKPC']['13']['use'] = False
all_runway['RKPC']['31']['use'] = False
rkpc_31 = len(soup.select("div.airplane.bottom")) > 0
if rkpc_31:
	all_runway['RKPC']['31']['use'] = True

# RKJB(163)
html = requests.get("http://global.amo.go.kr/amosobsnew/AmosRealTimeImage.do?stnId=163").text
soup = BeautifulSoup(html, 'html.parser')
rkjb_01 = len(soup.select("div.airplane.left")) > 0
if rkjb_01:
	all_runway['RKJB']['19']['use'] = False
else:
	all_runway['RKJB']['01']['use'] = False

# RKPU(151)
html = requests.get("http://global.amo.go.kr/amosobsnew/AmosRealTimeImage.do?stnId=151").text
soup = BeautifulSoup(html, 'html.parser')
rkpu_36 = len(soup.select("div.airplane.right")) > 0
if rkpu_36:
	all_runway['RKPU']['18']['use'] = False
else:
	all_runway['RKPU']['36']['use'] = False

# RKNY(92)
html = requests.get("http://global.amo.go.kr/amosobsnew/AmosRealTimeImage.do?stnId=92").text
soup = BeautifulSoup(html, 'html.parser')
rkny_33 = len(soup.select("div.airplane.right")) > 0
if rkny_33:
	all_runway['RKNY']['15']['use'] = False
else:
	all_runway['RKNY']['33']['use'] = False

# RKJY(167)
html = requests.get("http://global.amo.go.kr/amosobsnew/AmosRealTimeImage.do?stnId=167").text
soup = BeautifulSoup(html, 'html.parser')
rkjy_17 = len(soup.select("div.airplane.left")) > 0
if rkjy_17:
	all_runway['RKJY']['35']['use'] = False
else:
	all_runway['RKJY']['17']['use'] = False


# print
print(json.dumps(all_runway))
