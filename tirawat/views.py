from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from tirawat.fusioncharts import FusionCharts

# Create your views here.

def Home(request):
	return render(request,'tirawat/home.html')

def About(request):
	return render(request,'tirawat/about.html')

def Research(request):
	return render(request,'tirawat/research.html')

def Service(request):
	return render(request,'tirawat/service.html')

def Contact(request):
	return render(request,'tirawat/contact.html')

def Index(request):
	return render(request,'tirawat/index.html')

def Portfolio(request):
	return render(request,'tirawat/portfolio.html')

def Team(request):
	return render(request,'tirawat/team.html')

def myFirstMap(request):

    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key - value pairs.
    dataSource = OrderedDict()

    # The `mapConfig` dict contains key - value pairs data
    # for chart attribute
    mapConfig = OrderedDict()
    mapConfig["animation"] = "0"
    mapConfig["usehovercolor"] = "1"
    mapConfig["showlegend"] = "1"
    mapConfig["legendposition"] = "BOTTOM"
    mapConfig["legendborderalpha"] = "0"
    mapConfig["legendbordercolor"] = "#ffffff"
    mapConfig["legendallowdrag"] = "0"
    mapConfig["legendshadow"] = "0"
    mapConfig["caption"] = "Activity Map"
    mapConfig["connectorcolor"]= "000000"
    mapConfig["fillalpha"]= "80"
    mapConfig["hovercolor"]= "CCCCCC"
    mapConfig["theme"] = "fusion"

    # Map color range data
    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "0.0",
            "maxValue": "5.0",
            "code": "#FFD74D"
        }, {
            "minValue": "5.0",
            "maxValue": "10.0",
            "code": "#FB8C00"
        }, {
            "minValue": "10.0",
            "maxValue": "15.0",
            "code": "#E65100"
        }]
    }

    dataSource["chart"] = mapConfig
    dataSource["colorrange"] = colorDataObj
    dataSource["data"] = []

    # Map data array
    mapDataArray = [
        #["TH.AC",	"1", "1"],      #AC	Amnat Charoen
        #["TH.AT",	"1", "1"],      #AT	Ang Thong
        ["TH.AU",	"10", "1"],      #AU	Ayutthaya
        ["TH.BG",	"15", "1"],      #BG	Bangkok
        #["TH.BK",	"1", "1"],      #BK	BuengKan
        #["TH.BR",	"1", "1"],      #BR	Buri Ram
        ["TH.CC",	"5", "1"],      #CC	Chachoengsao
        #["TH.CN",	"1", "1"],      #CN	Chai Nat
        #["TH.CY",	"1", "1"],      #CY	Chaiyaphum
        #["TH.CT",	"1", "1"],      #CT	Chanthaburi
        #["TH.CM",	"1", "1"],      #CM	Chiang Mai
        #["TH.CR",	"1", "1"],      #CR	Chiang Rai
        ["TH.CB",	"2", "1"],      #CB	Chon Buri
        #["TH.CP",	"1", "1"],      #CP	Chumphon
        #["TH.KL",	"1", "1"],      #KL	Kalasin
        #["TH.KP",	"1", "1"],      #KP	Kamphaeng Phet
        #["TH.KN",	"1", "1"],      #KN	Kanchanaburi
        #["TH.KK",	"1", "1"],      #KK	Khon Kaen
        #["TH.KR",	"1", "1"],      #KR	Krabi
        #["TH.LG",	"1", "1"],      #LG	Lampang
        #["TH.LN",	"1", "1"],      #LN	Lamphun
        #["TH.LE",	"1", "1"],      #LE	Loei
        #["TH.LB",	"1", "1"],      #LB	Lop Buri
        #["TH.MH",	"1", "1"],      #MH	Mae Hong Son
        #["TH.MS",	"1", "1"],      #MS	Maha Sarakham
        #["TH.MD",	"1", "1"],      #MD	Mukdahan
        #["TH.NN",	"1", "1"],      #NN	Nakhon Nayok
        #["TH.NP",	"1", "1"],      #NP	Nakhon Pathom
        #["TH.NF",	"1", "1"],      #NF	Nakhon Phanom
        ["TH.NR",	"3", "1"],      #NR	Nakhon Ratchasima
        #["TH.NS",	"1", "1"],      #NS	Nakhon Sawan
        #["TH.NT",	"3", "1"],      #NT	Nakhon Si Thammarat
        #["TH.NA",	"1", "1"],      #NA	Nan
        #["TH.NW",	"1", "1"],      #NW	Narathiwat
        #["TH.NB",	"1", "1"],      #NB	Nong Bua Lamphu
        #["TH.NK",	"1", "1"],      #NK	Nong Khai
        #["TH.NO",	"1", "1"],      #NO	Nonthaburi
        ["TH.PT",	"5", "1"],      #PT	Pathum Thani
        #["TH.PI",	"1", "1"],      #PI	Pattani
        #["TH.PG",	"1", "1"],      #PG	Phang Nga
        #["TH.PL",	"1", "1"],      #PL	Phatthalung
        #["TH.PY",	"1", "1"],      #PY	Phayao
        #["TH.PH",	"1", "1"],      #PH	Phetchabun
        #["TH.PE",	"1", "1"],      #PE	Phetchaburi
        #["TH.PC",	"1", "1"],      #PC	Phichit
        #["TH.PS",	"1", "1"],      #PS	Phitsanulok
        #["TH.PR",	"1", "1"],      #PR	Phrae
        #["TH.PU",	"1", "1"],      #PU	Phuket
        #["TH.PB",	"1", "1"],      #PB	Prachin Buri
        #["TH.PK",	"1", "1"],      #PK	Prachuap Khiri Khan
        #["TH.RN",	"1", "1"],      #RN	Ranong
        #["TH.RT",	"1", "1"],      #RT	Ratchaburi
        #["TH.RY",	"1", "1"],      #RY	Rayong
        #["TH.RE",	"1", "1"],      #RE	Roi Et
        #["TH.SK",	"1", "1"],      #SK	Sa Kaeo
        #["TH.SN",	"1", "1"],      #SN	Sakon Nakhon
        ["TH.SP",	"7", "1"],      #SP	Samut Prakan
        #["TH.SS",	"1", "1"],      #SS	Samut Sakhon
        #["TH.SM",	"1", "1"],      #SM	Samut Songkhram
        #["TH.SR",	"1", "1"],      #SR	Saraburi
        #["TH.SA",	"1", "1"],      #SA	Satun
        #["TH.SI",	"1", "1"],      #SI	Si Sa Ket
        #["TH.SB",	"1", "1"],      #SB	Sing Buri
        #["TH.SG",	"1", "1"],      #SG	Songkhla
        #["TH.SO",	"1", "1"],      #SO	Sukhothai
        ["TH.SH",	"3", "1"],      #SH	Suphan Buri
        #["TH.ST",	"1", "1"],      #ST	Surat Thani
        #["TH.SU",	"1", "1"],      #SU	Surin
        #["TH.TK",	"1", "1"],      #TK	Tak
        #["TH.TG",	"1", "1"],      #TG	Trang
        #["TH.TT",	"1", "1"],      #TT	Trat
        #["TH.UR",	"1", "1"],      #UR	Ubon Ratchathani
        #["TH.UN",	"1", "1"],      #UN	Udon Thani
        #["TH.UT",	"1", "1"],      #UT	Uthai Thani
        #["TH.UD",	"1", "1"],      #UD	Uttaradit
        #["TH.YL",	"1", "1"],      #YL	Yala
        #["TH.YS",	"1", "1"],      #YS	Yasothon
    ]

    # Iterate through the data in `mapDataArray` and insert in to the `dataSource["data"]` list.
    #The data for the `data` should be in an array wherein each element 
    #of the array is a JSON object# having the `id`, `value` and `showlabel` as keys.
    for i in range(len(mapDataArray)):
        dataSource["data"].append({
            "id": mapDataArray[i][0],
            "value": mapDataArray[i][1],
            "showLabel": mapDataArray[i][2]
        })

    # Create an object for the world map using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    fusionMap = FusionCharts("maps/thailand", "myFirstMap", "1000", "600", "Map", "json", dataSource)

    # returning complete JavaScript and HTML code, which is used to generate map in the browsers.
    return render(request, 'tirawat/map.html', {
        'output': fusionMap.render()
    })