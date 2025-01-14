import pygame
from cooptools.coopEnum import CoopEnum

def _print_fonts_for_enum():
    for font in pygame.font.get_fonts():
        print(f"{font.upper()} = \"{font}\"")

class PyFont(CoopEnum):
    ARIAL = "arial"
    ARIALBLACK = "arialblack"
    BAHNSCHRIFT = "bahnschrift"
    CALIBRI = "calibri"
    CAMBRIACAMBRIAMATH = "cambriacambriamath"
    CAMBRIA = "cambria"
    CANDARA = "candara"
    COMICSANSMS = "comicsansms"
    CONSOLAS = "consolas"
    CONSTANTIA = "constantia"
    CORBEL = "corbel"
    COURIERNEW = "couriernew"
    EBRIMA = "ebrima"
    FRANKLINGOTHICMEDIUM = "franklingothicmedium"
    GABRIOLA = "gabriola"
    GADUGI = "gadugi"
    GEORGIA = "georgia"
    IMPACT = "impact"
    INKFREE = "inkfree"
    JAVANESETEXT = "javanesetext"
    LEELAWADEEUI = "leelawadeeui"
    LEELAWADEEUISEMILIGHT = "leelawadeeuisemilight"
    LUCIDACONSOLE = "lucidaconsole"
    LUCIDASANS = "lucidasans"
    MALGUNGOTHIC = "malgungothic"
    MALGUNGOTHICSEMILIGHT = "malgungothicsemilight"
    MICROSOFTHIMALAYA = "microsofthimalaya"
    MICROSOFTJHENGHEIMICROSOFTJHENGHEIUI = "microsoftjhengheimicrosoftjhengheiui"
    MICROSOFTJHENGHEIMICROSOFTJHENGHEIUIBOLD = "microsoftjhengheimicrosoftjhengheiuibold"
    MICROSOFTJHENGHEIMICROSOFTJHENGHEIUILIGHT = "microsoftjhengheimicrosoftjhengheiuilight"
    MICROSOFTNEWTAILUE = "microsoftnewtailue"
    MICROSOFTPHAGSPA = "microsoftphagspa"
    MICROSOFTSANSSERIF = "microsoftsansserif"
    MICROSOFTTAILE = "microsofttaile"
    MICROSOFTYAHEIMICROSOFTYAHEIUI = "microsoftyaheimicrosoftyaheiui"
    MICROSOFTYAHEIMICROSOFTYAHEIUIBOLD = "microsoftyaheimicrosoftyaheiuibold"
    MICROSOFTYAHEIMICROSOFTYAHEIUILIGHT = "microsoftyaheimicrosoftyaheiuilight"
    MICROSOFTYIBAITI = "microsoftyibaiti"
    MINGLIUEXTBPMINGLIUEXTBMINGLIUHKSCSEXTB = "mingliuextbpmingliuextbmingliuhkscsextb"
    MONGOLIANBAITI = "mongolianbaiti"
    MSGOTHICMSUIGOTHICMSPGOTHIC = "msgothicmsuigothicmspgothic"
    MVBOLI = "mvboli"
    MYANMARTEXT = "myanmartext"
    NIRMALAUI = "nirmalaui"
    NIRMALAUISEMILIGHT = "nirmalauisemilight"
    PALATINOLINOTYPE = "palatinolinotype"
    SEGOEMDL2ASSETS = "segoemdl2assets"
    SEGOEPRINT = "segoeprint"
    SEGOESCRIPT = "segoescript"
    SEGOEUI = "segoeui"
    SEGOEUIBLACK = "segoeuiblack"
    SEGOEUIEMOJI = "segoeuiemoji"
    SEGOEUIHISTORIC = "segoeuihistoric"
    SEGOEUISEMIBOLD = "segoeuisemibold"
    SEGOEUISEMILIGHT = "segoeuisemilight"
    SEGOEUISYMBOL = "segoeuisymbol"
    SIMSUNNSIMSUN = "simsunnsimsun"
    SIMSUNEXTB = "simsunextb"
    SITKASMALLSITKATEXTSITKASUBHEADINGSITKAHEADINGSITKADISPLAYSITKABANNER = "sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner"
    SITKASMALLSITKATEXTBOLDSITKASUBHEADINGBOLDSITKAHEADINGBOLDSITKADISPLAYBOLDSITKABANNERBOLD = "sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold"
    SITKASMALLSITKATEXTBOLDITALICSITKASUBHEADINGBOLDITALICSITKAHEADINGBOLDITALICSITKADISPLAYBOLDITALICSITKABANNERBOLDITALIC = "sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic"
    SITKASMALLSITKATEXTITALICSITKASUBHEADINGITALICSITKAHEADINGITALICSITKADISPLAYITALICSITKABANNERITALIC = "sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic"
    SYLFAEN = "sylfaen"
    SYMBOL = "symbol"
    TAHOMA = "tahoma"
    TIMESNEWROMAN = "timesnewroman"
    TREBUCHETMS = "trebuchetms"
    VERDANA = "verdana"
    WEBDINGS = "webdings"
    WINGDINGS = "wingdings"
    YUGOTHICYUGOTHICUISEMIBOLDYUGOTHICUIBOLD = "yugothicyugothicuisemiboldyugothicuibold"
    YUGOTHICYUGOTHICUILIGHT = "yugothicyugothicuilight"
    YUGOTHICMEDIUMYUGOTHICUIREGULAR = "yugothicmediumyugothicuiregular"
    YUGOTHICREGULARYUGOTHICUISEMILIGHT = "yugothicregularyugothicuisemilight"
    HOLOMDL2ASSETS = "holomdl2assets"
    AGENCYFB = "agencyfb"
    ALGERIAN = "algerian"
    BOOKANTIQUA = "bookantiqua"
    ARIALROUNDED = "arialrounded"
    BASKERVILLEOLDFACE = "baskervilleoldface"
    BAUHAUS93 = "bauhaus93"
    BELL = "bell"
    BERNARDCONDENSED = "bernardcondensed"
    BODONI = "bodoni"
    BODONIBLACK = "bodoniblack"
    BODONICONDENSED = "bodonicondensed"
    BODONIPOSTERCOMPRESSED = "bodonipostercompressed"
    BOOKMANOLDSTYLE = "bookmanoldstyle"
    BRADLEYHANDITC = "bradleyhanditc"
    BRITANNIC = "britannic"
    BERLINSANSFB = "berlinsansfb"
    BERLINSANSFBDEMI = "berlinsansfbdemi"
    BROADWAY = "broadway"
    BRUSHSCRIPT = "brushscript"
    BOOKSHELFSYMBOL7 = "bookshelfsymbol7"
    CALIFORNIANFB = "californianfb"
    CALISTO = "calisto"
    CASTELLAR = "castellar"
    CENTURYSCHOOLBOOK = "centuryschoolbook"
    CENTAUR = "centaur"
    CENTURY = "century"
    CHILLER = "chiller"
    COLONNA = "colonna"
    COOPERBLACK = "cooperblack"
    COPPERPLATEGOTHIC = "copperplategothic"
    CURLZ = "curlz"
    DUBAI = "dubai"
    DUBAIMEDIUM = "dubaimedium"
    DUBAIREGULAR = "dubairegular"
    ELEPHANT = "elephant"
    ENGRAVERS = "engravers"
    ERASITC = "erasitc"
    ERASDEMIITC = "erasdemiitc"
    ERASMEDIUMITC = "erasmediumitc"
    FELIXTITLING = "felixtitling"
    FORTE = "forte"
    FRANKLINGOTHICBOOK = "franklingothicbook"
    FRANKLINGOTHICDEMI = "franklingothicdemi"
    FRANKLINGOTHICDEMICOND = "franklingothicdemicond"
    FRANKLINGOTHICHEAVY = "franklingothicheavy"
    FRANKLINGOTHICMEDIUMCOND = "franklingothicmediumcond"
    FREESTYLESCRIPT = "freestylescript"
    FRENCHSCRIPT = "frenchscript"
    FOOTLIGHT = "footlight"
    GARAMOND = "garamond"
    GIGI = "gigi"
    GILLSANS = "gillsans"
    GILLSANSCONDENSED = "gillsanscondensed"
    GILLSANSULTRACONDENSED = "gillsansultracondensed"
    GILLSANSULTRA = "gillsansultra"
    GLOUCESTEREXTRACONDENSED = "gloucesterextracondensed"
    GILLSANSEXTCONDENSED = "gillsansextcondensed"
    CENTURYGOTHIC = "centurygothic"
    GOUDYOLDSTYLE = "goudyoldstyle"
    GOUDYSTOUT = "goudystout"
    HARLOWSOLID = "harlowsolid"
    HARRINGTON = "harrington"
    HAETTENSCHWEILER = "haettenschweiler"
    HIGHTOWERTEXT = "hightowertext"
    IMPRINTSHADOW = "imprintshadow"
    INFORMALROMAN = "informalroman"
    BLACKADDERITC = "blackadderitc"
    EDWARDIANSCRIPTITC = "edwardianscriptitc"
    KRISTENITC = "kristenitc"
    JOKERMAN = "jokerman"
    JUICEITC = "juiceitc"
    KUNSTLERSCRIPT = "kunstlerscript"
    WIDELATIN = "widelatin"
    LUCIDABRIGHT = "lucidabright"
    LUCIDACALLIGRAPHY = "lucidacalligraphy"
    LUCIDAFAXREGULAR = "lucidafaxregular"
    LUCIDAFAX = "lucidafax"
    LUCIDAHANDWRITING = "lucidahandwriting"
    LUCIDASANSREGULAR = "lucidasansregular"
    LUCIDASANSROMAN = "lucidasansroman"
    LUCIDASANSTYPEWRITERREGULAR = "lucidasanstypewriterregular"
    LUCIDASANSTYPEWRITER = "lucidasanstypewriter"
    LUCIDASANSTYPEWRITEROBLIQUE = "lucidasanstypewriteroblique"
    MAGNETO = "magneto"
    MAIANDRAGD = "maiandragd"
    MATURASCRIPTCAPITALS = "maturascriptcapitals"
    MISTRAL = "mistral"
    MODERNNO20 = "modernno20"
    MONOTYPECORSIVA = "monotypecorsiva"
    EXTRA = "extra"
    NIAGARAENGRAVED = "niagaraengraved"
    NIAGARASOLID = "niagarasolid"
    OCRAEXTENDED = "ocraextended"
    OLDENGLISHTEXT = "oldenglishtext"
    ONYX = "onyx"
    MSOUTLOOK = "msoutlook"
    PALACESCRIPT = "palacescript"
    PAPYRUS = "papyrus"
    PARCHMENT = "parchment"
    PERPETUA = "perpetua"
    PERPETUATITLING = "perpetuatitling"
    PLAYBILL = "playbill"
    POORRICHARD = "poorrichard"
    PRISTINA = "pristina"
    RAGE = "rage"
    RAVIE = "ravie"
    MSREFERENCESANSSERIF = "msreferencesansserif"
    MSREFERENCESPECIALTY = "msreferencespecialty"
    ROCKWELLCONDENSED = "rockwellcondensed"
    ROCKWELL = "rockwell"
    ROCKWELLEXTRA = "rockwellextra"
    SCRIPT = "script"
    SHOWCARDGOTHIC = "showcardgothic"
    SNAPITC = "snapitc"
    STENCIL = "stencil"
    TWCEN = "twcen"
    TWCENCONDENSED = "twcencondensed"
    TWCENCONDENSEDEXTRA = "twcencondensedextra"
    TEMPUSSANSITC = "tempussansitc"
    VINERHANDITC = "vinerhanditc"
    VIVALDI = "vivaldi"
    VLADIMIRSCRIPT = "vladimirscript"
    WINGDINGS2 = "wingdings2"
    WINGDINGS3 = "wingdings3"
    TEAMVIEWER15 = "teamviewer15"
    BANKGOTHIC = "bankgothic"
    BANKGOTHICMEDIUM = "bankgothicmedium"
    CITYBLUEPRINT = "cityblueprint"
    COMMERCIALPI = "commercialpi"
    COMMERCIALSCRIPT = "commercialscript"
    COUNTRYBLUEPRINT = "countryblueprint"
    DUTCH801ROMAN = "dutch801roman"
    DUTCH801 = "dutch801"
    DUTCH801EXTRA = "dutch801extra"
    EUROROMANOBLIQUE = "euroromanoblique"
    EUROROMAN = "euroroman"
    ISOCPEUR = "isocpeur"
    ISOCTEUR = "isocteur"
    MONOSPACE821 = "monospace821"
    PANROMAN = "panroman"
    ROMANTIC = "romantic"
    ROMANS = "romans"
    SANSSERIFBOLDOBLIQUE = "sansserifboldoblique"
    SANSSERIF = "sansserif"
    SANSSERIFOBLIQUE = "sansserifoblique"
    STYLUS = "stylus"
    SUPERFRENCH = "superfrench"
    SWISS721 = "swiss721"
    SWISS721OUTLINE = "swiss721outline"
    SWISS721CONDENSED = "swiss721condensed"
    SWISS721CONDENSEDOUTLINE = "swiss721condensedoutline"
    SWISS721BLACKCONDENSED = "swiss721blackcondensed"
    SWISS721EXTENDED = "swiss721extended"
    SWISS721BLACKEXTENDED = "swiss721blackextended"
    SWISS721BLACK = "swiss721black"
    SWISS721BLACKOUTLINE = "swiss721blackoutline"
    TECHNICBOLD = "technicbold"
    TECHNICLITE = "techniclite"
    TECHNIC = "technic"
    UNIVERSALMATH1 = "universalmath1"
    VINETA = "vineta"
    ACADEREF = "acaderef"
    AIGDT = "aigdt"
    AMDTSYMBOLS = "amdtsymbols"
    AMGDT = "amgdt"
    GENISO = "geniso"
    COMPLEX = "complex"
    GDT = "gdt"
    GOTHICE = "gothice"
    GOTHICG = "gothicg"
    GOTHICI = "gothici"
    GREEKC = "greekc"
    GREEKS = "greeks"
    ISOCP2 = "isocp2"
    ISOCP3 = "isocp3"
    ISOCP = "isocp"
    ISOCT2 = "isoct2"
    ISOCT3 = "isoct3"
    ISOCT = "isoct"
    ITALICC = "italicc"
    ITALICT = "italict"
    MONOTXT = "monotxt"
    PROXY1 = "proxy1"
    PROXY2 = "proxy2"
    PROXY3 = "proxy3"
    PROXY4 = "proxy4"
    PROXY5 = "proxy5"
    PROXY6 = "proxy6"
    PROXY7 = "proxy7"
    PROXY8 = "proxy8"
    PROXY9 = "proxy9"
    ROMANC = "romanc"
    ROMAND = "romand"
    ROMANT = "romant"
    SCRIPTC = "scriptc"
    SCRIPTS = "scripts"
    SIMPLEX = "simplex"
    SYASTRO = "syastro"
    SYMAP = "symap"
    SYMATH = "symath"
    SYMETEO = "symeteo"
    SYMUSIC = "symusic"
    TXT = "txt"
    LEELAWADEE = "leelawadee"
    MICROSOFTUIGHUR = "microsoftuighur"
    DOSIS = "dosis"
    DOSISEXTRABOLD = "dosisextrabold"
    DOSISEXTRALIGHT = "dosisextralight"
    DOSISMEDIUM = "dosismedium"
    DOSISREGULAR = "dosisregular"
    DOSISSEMIBOLD = "dosissemibold"
    LATOBLACK = "latoblack"
    LATO = "lato"
    LATOLIGHT = "latolight"
    LATOLIGHTITALIC = "latolightitalic"
    LATOREGULAR = "latoregular"
    LATOHAIRLINE = "latohairline"
    LATOHAIRLINEITALIC = "latohairlineitalic"
    MONTSERRATBLACK = "montserratblack"
    MONTSERRAT = "montserrat"
    MONTSERRATEXTRABOLD = "montserratextrabold"
    MONTSERRATEXTRALIGHT = "montserratextralight"
    MONTSERRATMEDIUM = "montserratmedium"
    MONTSERRATREGULAR = "montserratregular"
    MONTSERRATSEMIBOLD = "montserratsemibold"
    MONTSERRATTHIN = "montserratthin"
    OSWALD = "oswald"
    OSWALDEXTRALIGHT = "oswaldextralight"
    OSWALDMEDIUM = "oswaldmedium"
    OSWALDREGULAR = "oswaldregular"
    OSWALDSEMIBOLD = "oswaldsemibold"
    SOURCESANSPROBLACK = "sourcesansproblack"
    SOURCESANSPRO = "sourcesanspro"
    SOURCESANSPROEXTRALIGHT = "sourcesansproextralight"
    SOURCESANSPROREGULAR = "sourcesansproregular"
    SOURCESANSPROSEMIBOLD = "sourcesansprosemibold"
    BARLOWCONDENSEDBLACK = "barlowcondensedblack"
    BARLOWCONDENSED = "barlowcondensed"
    BARLOWCONDENSEDEXTRABOLD = "barlowcondensedextrabold"
    BARLOWCONDENSEDEXTRALIGHT = "barlowcondensedextralight"
    BARLOWCONDENSEDMEDIUM = "barlowcondensedmedium"
    BARLOWCONDENSEDREGULAR = "barlowcondensedregular"
    BARLOWCONDENSEDSEMIBOLD = "barlowcondensedsemibold"
    BARLOWCONDENSEDTHIN = "barlowcondensedthin"
    CAVEAT = "caveat"
    CAVEATREGULAR = "caveatregular"
    CORMORANTINFANT = "cormorantinfant"
    CORMORANTINFANTMEDIUM = "cormorantinfantmedium"
    CORMORANTINFANTREGULAR = "cormorantinfantregular"
    CORMORANTINFANTSEMIBOLD = "cormorantinfantsemibold"
    NOTOSANS = "notosans"
    NOTOSERIF = "notoserif"
    OPENSANS = "opensans"
    OPENSANSEXTRABOLD = "opensansextrabold"
    OPENSANSREGULAR = "opensansregular"
    OPENSANSSEMIBOLD = "opensanssemibold"
    RALEWAYBLACK = "ralewayblack"
    RALEWAY = "raleway"
    RALEWAYEXTRABOLD = "ralewayextrabold"
    RALEWAYEXTRALIGHT = "ralewayextralight"
    RALEWAYMEDIUM = "ralewaymedium"
    RALEWAYREGULAR = "ralewayregular"
    RALEWAYSEMIBOLD = "ralewaysemibold"
    RALEWAYTHIN = "ralewaythin"
    ROBOTOBLACK = "robotoblack"
    ROBOTO = "roboto"
    ROBOTOMEDIUM = "robotomedium"
    ROBOTOTHIN = "robotothin"
    ROBOTOCONDENSED = "robotocondensed"
    ROBOTOSLABBLACK = "robotoslabblack"
    ROBOTOSLAB = "robotoslab"
    ROBOTOSLABEXTRABOLD = "robotoslabextrabold"
    ROBOTOSLABEXTRALIGHT = "robotoslabextralight"
    ROBOTOSLABMEDIUM = "robotoslabmedium"
    ROBOTOSLABREGULAR = "robotoslabregular"
    ROBOTOSLABSEMIBOLD = "robotoslabsemibold"
    ROBOTOSLABTHIN = "robotoslabthin"
    ZILLASLAB = "zillaslab"
    ZILLASLABMEDIUM = "zillaslabmedium"
    ZILLASLABSEMIBOLD = "zillaslabsemibold"