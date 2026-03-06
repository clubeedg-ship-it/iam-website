#!/usr/bin/env python3
"""Fix Ghost blog posts that have null HTML by updating them with proper mobiledoc content."""
import json, jwt, requests, time
from datetime import datetime

# Ghost Admin API config
GHOST_URL = "http://localhost:3007"
ADMIN_KEY_ID = "69a25a83632d37000102e2de"
ADMIN_KEY_SECRET = "f713d9ab03d8faed95692e4d59bc6755952803800956bdc01ffea067cf7c83e3"

def get_token():
    iat = int(time.time())
    header = {"alg": "HS256", "typ": "JWT", "kid": ADMIN_KEY_ID}
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    key = bytes.fromhex(ADMIN_KEY_SECRET)
    return jwt.encode(payload, key, algorithm="HS256", headers=header)

def make_mobiledoc(html_content):
    """Create a mobiledoc card with HTML content."""
    return json.dumps({
        "version": "0.3.1",
        "atoms": [],
        "cards": [["html", {"html": html_content}]],
        "markups": [],
        "sections": [[10, 0]]
    })

# Blog post content
POSTS = {
    "interactieve-vloer-kinderdagverblijf": {
        "title": "Interactieve vloer in het kinderdagverblijf: zo stimuleer je bewegend leren",
        "html": """
<p>Steeds meer kinderdagverblijven ontdekken de kracht van interactieve vloeren. Deze innovatieve technologie verandert elke ruimte in een dynamische speelomgeving waar kinderen spelend leren, bewegen en samenwerken. Maar wat maakt een interactieve vloer zo waardevol voor de kinderopvang?</p>

<h2>Wat is een interactieve vloer?</h2>
<p>Een interactieve vloer is een projectiesysteem dat beelden op de grond projecteert die reageren op beweging. Kinderen kunnen rennen, springen en dansen over kleurrijke spellen die direct reageren op hun bewegingen. Het systeem bestaat uit een plafondprojector en bewegingssensoren — geen schermen, geen tablets, alleen fysiek actief spel.</p>

<h2>Waarom kiezen kinderdagverblijven voor interactieve vloeren?</h2>
<p>De voordelen voor de kinderopvang zijn veelzijdig:</p>
<ul>
<li><strong>Motorische ontwikkeling</strong> — Kinderen bewegen tot 40% meer tijdens vrij spel met een interactieve vloer. Rennen, springen, bukken en balanceren worden onderdeel van het spel.</li>
<li><strong>Cognitieve groei</strong> — Spelvormen stimuleren tellen, kleuren herkennen, patronen volgen en samenwerken. Leren voelt niet als leren.</li>
<li><strong>Inclusiviteit</strong> — Tot 12 kinderen spelen tegelijk, inclusief kinderen met een motorische of cognitieve beperking. De vloer past zich aan het niveau aan.</li>
<li><strong>Geen slijtage</strong> — Digitale content vervangt fysiek speelgoed dat kapot gaat. Nieuwe spellen worden via software toegevoegd.</li>
</ul>

<h2>Bewegend leren: de wetenschap erachter</h2>
<p>Onderzoek toont aan dat jonge kinderen het beste leren wanneer ze fysiek actief zijn. De hersenen van peuters en kleuters ontwikkelen zich sneller wanneer beweging en cognitieve taken gecombineerd worden. Een interactieve vloer maakt dit principe tastbaar: kinderen leren tellen door te springen, herkennen vormen door erop te staan, en ontwikkelen sociale vaardigheden door samen te spelen.</p>

<h2>Praktisch: installatie en kosten</h2>
<p>Een veelgehoorde zorg is de installatie. De realiteit is eenvoudiger dan verwacht: de projector wordt aan het plafond gemonteerd (binnen één uur), er is geen verbouwing nodig, en het systeem werkt op elke vlakke vloer. Met een leasemodel is er geen grote investering vooraf — kinderdagverblijven kunnen starten vanaf een maandelijks bedrag.</p>

<h2>De impact op de dagelijkse praktijk</h2>
<p>Pedagogisch medewerkers noemen de interactieve vloer vaak hun "geheime wapen" voor drukke ochtenden. Kinderen zijn gefocust, bewegen actief, en er ontstaat minder conflict omdat het spel structuur biedt. Ouders merken het verschil: kinderen komen enthousiast thuis met verhalen over de spellen die ze gespeeld hebben.</p>

<p>Benieuwd wat een interactieve vloer voor uw kinderdagverblijf kan betekenen? <a href="/products/interactieve-vloer.html">Bekijk onze interactieve vloer</a> of neem contact op voor een vrijblijvend adviesgesprek.</p>
"""
    },
    "interactieve-speeltoestellen-kinderopvang": {
        "title": "Interactieve speeltoestellen voor de kinderopvang: een compleet overzicht",
        "html": """
<p>De kinderopvang evolueert. Waar vroeger een zandbak en een klimrek volstonden, verwachten ouders en toezichthouders steeds meer van de speelomgeving. Interactieve speeltoestellen combineren fysiek spel met digitale technologie — en de resultaten zijn indrukwekkend.</p>

<h2>Welke interactieve speeltoestellen bestaan er?</h2>
<p>Het aanbod is breder dan veel opvanglocaties beseffen:</p>
<ul>
<li><strong>Interactieve vloeren</strong> — Projecties op de grond die reageren op beweging. Ideaal voor binnenruimtes. <a href="/products/interactieve-vloer.html">Meer over interactieve vloeren →</a></li>
<li><strong>Interactieve muren</strong> — Wandprojecties waar kinderen op kunnen tikken, tekenen en spelen. Perfect voor gangen en speelzalen. <a href="/products/interactieve-muur.html">Meer over interactieve muren →</a></li>
<li><strong>Interactieve zandbakken</strong> — Projecties op zand die reageren op graven en vormen. Combineert tactiel en digitaal spel. <a href="/products/interactieve-zandbak.html">Meer over interactieve zandbakken →</a></li>
<li><strong>Interactieve klimwanden</strong> — Klimmen gecombineerd met spelprojecties. Fysiek uitdagend én cognitief stimulerend. <a href="/products/interactieve-klimwand.html">Meer over interactieve klimwanden →</a></li>
<li><strong>Mobiele systemen</strong> — Verrijdbare projectoren die in verschillende ruimtes ingezet kunnen worden. <a href="/products/mobiele-vloer.html">Meer over mobiele systemen →</a></li>
</ul>

<h2>Waar moet u op letten bij de keuze?</h2>
<p>Bij het selecteren van interactieve speeltoestellen voor uw kinderopvang zijn een aantal factoren cruciaal:</p>
<ul>
<li><strong>Leeftijdsgeschiktheid</strong> — Is de content afgestemd op peuters (2-4 jaar) of ook kleuters (4-6 jaar)?</li>
<li><strong>Groepsgrootte</strong> — Hoeveel kinderen kunnen tegelijk spelen? Systemen variëren van 4 tot 12+ kinderen.</li>
<li><strong>Educatieve waarde</strong> — Biedt het systeem spelvormen die aansluiten bij de leerdoelen van de opvang?</li>
<li><strong>Onderhoud</strong> — Digitale systemen hebben minder fysiek onderhoud dan traditioneel speelgoed, maar software-updates zijn belangrijk.</li>
<li><strong>Ruimte-eisen</strong> — Wat is de minimale vloer- of wandoppervlakte die nodig is?</li>
</ul>

<h2>De kosten: investering of lease?</h2>
<p>Interactieve speeltoestellen variëren sterk in prijs. Budgetopties beginnen rond €2.000, terwijl premium all-in-one systemen tot €16.000 kunnen kosten. Steeds meer leveranciers bieden leasemodellen aan, waardoor er geen grote investering vooraf nodig is. Dit maakt de technologie toegankelijk voor zowel grote ketens als kleinere zelfstandige opvanglocaties.</p>

<h2>De toekomst van spelen in de kinderopvang</h2>
<p>Interactieve technologie is geen vervanging van traditioneel spel — het is een aanvulling. De beste resultaten ontstaan wanneer kinderen afwisselen tussen vrij spel, gestructureerde activiteiten en interactieve momenten. De kinderopvang van de toekomst combineert het beste van beide werelden.</p>

<p>Wilt u ontdekken welke interactieve speeltoestellen passen bij uw opvanglocatie? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""
    },
    "bewegend-leren-peuters-kleuters": {
        "title": "Bewegend leren voor peuters en kleuters: waarom stilzitten achterhaald is",
        "html": """
<p>Kinderen leren niet door stil te zitten. Dat klinkt misschien vanzelfsprekend, maar in veel opvang- en onderwijssituaties wordt van jonge kinderen verwacht dat ze rustig aan tafel zitten. De wetenschap is duidelijk: bewegend leren is effectiever, gezonder en leuker.</p>

<h2>Wat zegt de wetenschap?</h2>
<p>Neurowetenschappelijk onderzoek toont aan dat fysieke activiteit direct gekoppeld is aan cognitieve ontwikkeling bij jonge kinderen. Wanneer kinderen bewegen, gebeurt er meer in de hersenen:</p>
<ul>
<li>De doorbloeding van de prefrontale cortex neemt toe — het gebied verantwoordelijk voor concentratie en planning</li>
<li>BDNF (Brain-Derived Neurotrophic Factor) wordt aangemaakt — essentieel voor het vormen van nieuwe neurale verbindingen</li>
<li>De hippocampus, betrokken bij geheugenvorming, wordt actiever</li>
</ul>
<p>Kort gezegd: kinderen die bewegen terwijl ze leren, onthouden meer en concentreren zich beter.</p>

<h2>De GGD-cijfers zijn alarmerend</h2>
<p>De Gemeentelijke Gezondheidsdienst (GGD) constateert dat ruim 40% van de Nederlandse kinderen onvoldoende beweegt. De beweegrichtlijn voor kinderen van 0-4 jaar adviseert minimaal 3 uur per dag fysieke activiteit. In de praktijk halen veel kinderen in de opvang dit niet, vooral op regenachtige dagen wanneer buitenspel niet mogelijk is.</p>

<h2>Hoe ziet bewegend leren eruit in de praktijk?</h2>
<p>Bewegend leren kan veel vormen aannemen:</p>
<ul>
<li><strong>Interactieve vloerspellen</strong> — Kinderen leren tellen door te springen op getallen, herkennen kleuren door op de juiste vlakken te staan</li>
<li><strong>Bewegingscircuits</strong> — Parcoursen waar cognitieve opdrachten gecombineerd worden met klimmen, kruipen en balanceren</li>
<li><strong>Muziek en dans</strong> — Ritme, coördinatie en sociale vaardigheden in één activiteit</li>
<li><strong>Buitenspel met een twist</strong> — Traditionele buitenactiviteiten verrijkt met educatieve elementen</li>
</ul>

<h2>Technologie als hulpmiddel</h2>
<p>Interactieve projectiesystemen maken bewegend leren toegankelijk en consistent. Een <a href="/products/interactieve-vloer.html">interactieve vloer</a> biedt honderden spelvarianten die automatisch het juiste niveau kiezen voor de leeftijdsgroep. Pedagogisch medewerkers hoeven niet elke dag nieuwe activiteiten te bedenken — het systeem biedt variatie en structuur tegelijk.</p>

<h2>Tips voor meer bewegend leren</h2>
<p>U hoeft niet te wachten op technologie om te beginnen. Enkele directe stappen:</p>
<ol>
<li>Vervang "zit-activiteiten" waar mogelijk door sta- of beweegvarianten</li>
<li>Integreer korte bewegingsmomenten (2-3 minuten) tussen rustige activiteiten</li>
<li>Gebruik de buitenruimte actiever, ook bij licht regen</li>
<li>Kies spelmateriaal dat uitnodigt tot bewegen in plaats van stilzitten</li>
</ol>

<p>Benieuwd hoe interactieve technologie bewegend leren kan versterken in uw opvang of school? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""
    },
    "interactieve-muur-school": {
        "title": "De interactieve muur op school: technologie die het klaslokaal transformeert",
        "html": """
<p>Het klaslokaal verandert. Waar krijtborden plaatsmaakten voor digiborden, zien we nu de volgende stap: interactieve muren die het hele klaslokaal omtoveren tot een leeromgeving. Maar wat voegt een interactieve muur toe aan het onderwijs, en is het meer dan een gadget?</p>

<h2>Wat is een interactieve muur?</h2>
<p>Een interactieve muur is een projectiesysteem dat beelden op een wand projecteert die reageren op aanraking en beweging. Kinderen kunnen direct op de muur tekenen, spellen spelen, en interactief leren. Het verschil met een smartboard? De projectie kan veel groter zijn, meerdere kinderen kunnen tegelijk interacteren, en het systeem nodigt uit tot staan en bewegen in plaats van zitten.</p>

<h2>Toepassingen in het onderwijs</h2>
<p>De mogelijkheden zijn breed:</p>
<ul>
<li><strong>Taalonderwijs</strong> — Interactieve woordspellen, letterpuzzels en voorleesverhalen waar kinderen fysiek bij betrokken zijn</li>
<li><strong>Rekenen</strong> — Wiskundige concepten worden tastbaar wanneer kinderen getallen aanraken, groeperen en verplaatsen</li>
<li><strong>Wereldoriëntatie</strong> — Interactieve kaarten, tijdlijnen en ecosystemen die kinderen kunnen verkennen</li>
<li><strong>Creatieve vakken</strong> — Digitaal tekenen en schilderen op groot formaat, samen met de hele klas</li>
<li><strong>Sociale vaardigheden</strong> — Samenwerkingsspellen die communicatie en samenwerking vereisen</li>
</ul>

<h2>Voordelen ten opzichte van traditionele leermiddelen</h2>
<p>Een interactieve muur biedt specifieke voordelen voor het onderwijs:</p>
<ul>
<li><strong>Differentiatie</strong> — De software past het niveau automatisch aan, van groep 1 tot groep 8</li>
<li><strong>Betrokkenheid</strong> — Kinderen die normaal afhaken bij instructie worden actief betrokken door de interactie</li>
<li><strong>Beweging</strong> — Leerlingen staan en bewegen, wat de concentratie verbetert</li>
<li><strong>Geen papierverbruik</strong> — Werkbladen worden digitale interacties</li>
</ul>

<h2>Implementatie op school</h2>
<p>De installatie van een <a href="/products/interactieve-muur.html">interactieve muur</a> is eenvoudiger dan verwacht. Een projector wordt aan het plafond of de muur gemonteerd, en het systeem is direct klaar voor gebruik. Veel scholen beginnen met één systeem in een gemeenschappelijke ruimte, en breiden later uit naar individuele klaslokalen.</p>

<h2>Kosten en financiering</h2>
<p>Scholen kunnen gebruikmaken van verschillende financieringsmogelijkheden, waaronder het leasemodel en onderwijssubsidies. De investering betaalt zich terug in hogere leerbetrokkenheid, minder benodigde fysieke leermiddelen, en een aantrekkelijkere schoolomgeving die helpt bij werving van leerlingen.</p>

<p>Benieuwd hoe een interactieve muur uw school kan verrijken? Neem contact op voor een vrijblijvend adviesgesprek of een demonstratie op locatie.</p>
"""
    },
    "interactieve-projectie-speeltuin": {
        "title": "Interactieve projectie in de speeltuin: de toekomst van buitenspelen",
        "html": """
<p>De speeltuin van de toekomst is niet alleen fysiek — het is een plek waar digitale projecties en fysiek spel samenkomen. Interactieve projectietechnologie transformeert speeltuinen, pretparken en Family Entertainment Centers (FECs) wereldwijd. Nederland loopt voorop in deze ontwikkeling.</p>

<h2>Hoe werkt interactieve projectie in een speeltuin?</h2>
<p>Het concept is verrassend eenvoudig: projectoren — vaak weerbestendig voor buitengebruik — projecteren interactieve beelden op vloeren, muren of speeltoestellen. Sensoren detecteren de bewegingen van kinderen, waardoor het spel reageert op rennen, springen, gooien en aanraken. Het resultaat: een speeltuin die elke dag anders is.</p>

<h2>Toepassingen voor speeltuinen en pretparken</h2>
<ul>
<li><strong>Interactieve speelvloeren</strong> — Grote buitenvloeren waar tientallen kinderen tegelijk kunnen spelen met projectiespellen</li>
<li><strong>Interactieve glijbanen</strong> — Projecties op de glijbaan die reageren op de snelheid en positie van het kind</li>
<li><strong>Interactieve zandbakken</strong> — <a href="/products/interactieve-zandbak.html">Digitale projecties op zand</a> die reageren op graven en bouwen</li>
<li><strong>Interactieve muren</strong> — <a href="/products/interactieve-muur.html">Buitenmuren</a> die fungeren als gigantische touchscreens</li>
<li><strong>Thema-ervaringen</strong> — Seizoensgebonden content (kerst, Halloween, zomer) die de speeltuin steeds vernieuwt</li>
</ul>

<h2>Waarom investeren in interactieve technologie?</h2>
<p>Voor speeltuinen en FECs is interactieve projectie een strategische investering:</p>
<ul>
<li><strong>Hogere bezoekersaantallen</strong> — Het "wow-effect" trekt nieuwe bezoekers aan en genereert mond-tot-mondreclame</li>
<li><strong>Langere verblijftijd</strong> — Kinderen spelen langer wanneer de ervaring afwisselend en vernieuwend is</li>
<li><strong>Herhalingsbezoek</strong> — Regelmatig vernieuwde content zorgt dat families vaker terugkomen</li>
<li><strong>Onderscheidend vermogen</strong> — In een competitieve markt onderscheidt interactieve technologie uw locatie</li>
</ul>

<h2>De Nederlandse markt</h2>
<p>Nederland heeft een sterke traditie van indoor speelparadijzen en FECs. Met het veranderende klimaat (meer natte dagen) groeit de vraag naar innovatieve binnenspeeloplossingen. Interactieve projectie biedt een schaalbaar antwoord: begin met één installatie en breid uit op basis van bezoekersreactie.</p>

<p>Benieuwd wat interactieve projectie voor uw speeltuin of entertainmentlocatie kan betekenen? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""
    },
    "digitale-speeltuin-kinderen": {
        "title": "De digitale speeltuin: waarom kinderen er dol op zijn (en ouders ook)",
        "html": """
<p>De term "digitale speeltuin" roept bij sommige ouders weerstand op. Meer schermtijd? Nee, juist het tegenovergestelde. Een moderne digitale speeltuin combineert het beste van technologie met fysiek actief spel — zonder tablet of smartphone in zicht.</p>

<h2>Wat is een digitale speeltuin eigenlijk?</h2>
<p>Een digitale speeltuin is een fysieke ruimte waar interactieve technologie het speelplezier versterkt. Denk aan vloeren die oplichten wanneer kinderen erop springen, muren waar je op kunt tekenen met je hele lichaam, en zandbakken waar digitale dieren verschijnen wanneer je graaft. De technologie is onzichtbaar — kinderen zien alleen het spel.</p>

<h2>Waarom kinderen het geweldig vinden</h2>
<p>Vanuit het perspectief van een kind biedt een digitale speeltuin iets wat traditionele speeltuinen niet kunnen:</p>
<ul>
<li><strong>Magie</strong> — De vloer reageert op je! Dat voelt voor een 3-jarige als pure magie</li>
<li><strong>Variatie</strong> — Elk bezoek is anders omdat de spellen wisselen</li>
<li><strong>Samenspel</strong> — De spellen zijn ontworpen voor groepen, wat sociale interactie stimuleert</li>
<li><strong>Uitdaging</strong> — De moeilijkheidsgraad past zich aan, waardoor het altijd boeiend blijft</li>
</ul>

<h2>Waarom ouders het waarderen</h2>
<p>Ouders zien andere voordelen:</p>
<ul>
<li><strong>Actief, niet passief</strong> — In tegenstelling tot tablets bewegen kinderen de hele tijd</li>
<li><strong>Educatief</strong> — Spellen bevatten leerelementen (tellen, kleuren, samenwerken) zonder dat het voelt als onderwijs</li>
<li><strong>Sociaal</strong> — Kinderen spelen samen, niet elk achter een eigen scherm</li>
<li><strong>Veilig</strong> — Geen scherpe randen, geen klein speelgoed, geen hygiënerisico's</li>
</ul>

<h2>De groeiende trend</h2>
<p>Wereldwijd groeit de markt voor interactieve speeloplossingen met 11-15% per jaar. In Nederland zien we steeds meer kinderdagverblijven, speelparadijzen en scholen investeren in deze technologie. De reden is simpel: het werkt. Kinderen bewegen meer, leren sneller, en hebben meer plezier.</p>

<h2>Soorten interactieve speeloplossingen</h2>
<p>Het aanbod is divers en schaalbaar:</p>
<ul>
<li><a href="/products/interactieve-vloer.html">Interactieve vloeren</a> — De populairste optie voor binnenruimtes</li>
<li><a href="/products/interactieve-muur.html">Interactieve muren</a> — Ideaal voor smalle ruimtes en gangen</li>
<li><a href="/products/interactieve-zandbak.html">Interactieve zandbakken</a> — Unieke combinatie van tactiel en digitaal spel</li>
<li><a href="/products/interactieve-klimwand.html">Interactieve klimwanden</a> — Fysieke uitdaging meets digitale interactie</li>
<li><a href="/products/mobiele-vloer.html">Mobiele systemen</a> — Flexibel inzetbaar in wisselende ruimtes</li>
</ul>

<p>Benieuwd hoe u een digitale speelervaring kunt creëren voor uw locatie? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""
    },
    "revalidatie-kinderen-interactief": {
        "title": "Interactieve technologie in de kinderrevalidatie: spelen als therapie",
        "html": """
<p>In de kinderrevalidatie is motivatie alles. Kinderen die herstellende zijn van een blessure, operatie of leven met een motorische beperking, moeten oefeningen doen die vaak saai of pijnlijk zijn. Interactieve technologie verandert de spelregels: therapie wordt spel, en kinderen oefenen langer en intensiever zonder dat het als werk voelt.</p>

<h2>Het probleem met traditionele kinderrevalidatie</h2>
<p>Therapeuten in de kinderrevalidatie kennen de uitdaging: een kind motiveren om dezelfde oefening tientallen keren te herhalen. Traditionele methoden leunen op speelgoed, beloningssystemen en de creativiteit van de therapeut. Maar zelfs het beste speelgoed verliest zijn aantrekkingskracht na een aantal sessies.</p>

<h2>Hoe interactieve technologie helpt</h2>
<p>Interactieve vloeren en muren bieden een oplossing die specifiek waardevol is voor de revalidatie:</p>
<ul>
<li><strong>Intrinsieke motivatie</strong> — Het spel zelf is de beloning. Kinderen willen door omdat het leuk is, niet omdat ze moeten</li>
<li><strong>Herhaling zonder verveling</strong> — Dezelfde motorische oefening kan verpakt worden in tientallen verschillende spelvarianten</li>
<li><strong>Aanpasbaar niveau</strong> — De software past de moeilijkheidsgraad aan op basis van de mogelijkheden van het kind</li>
<li><strong>Meetbare voortgang</strong> — Het systeem registreert bewegingen, reactietijden en activiteitsniveaus</li>
<li><strong>Groepstherapie</strong> — Meerdere kinderen kunnen samen oefenen, wat sociale interactie bevordert</li>
</ul>

<h2>Toepassingen in de praktijk</h2>
<p>De inzet van interactieve technologie in revalidatie is breed:</p>
<ul>
<li><strong>Motorische revalidatie</strong> — Oefeningen voor grove en fijne motoriek verpakt in interactieve spellen</li>
<li><strong>Balans- en coördinatietraining</strong> — Spellen die vereisen dat kinderen hun gewicht verplaatsen en balanceren</li>
<li><strong>Cognitieve revalidatie</strong> — Geheugen-, aandachts- en planningsspellen gecombineerd met beweging</li>
<li><strong>Pijnmanagement</strong> — Afleiding door spel vermindert pijnervaring tijdens oefeningen</li>
</ul>

<h2>De Tovertafel en vergelijkbare systemen</h2>
<p>In Nederland is de Tovertafel een bekend voorbeeld van interactieve technologie in de zorg. InterActiveMove biedt vergelijkbare mogelijkheden met bredere inzetbaarheid: onze <a href="/products/interactieve-vloer.html">interactieve vloeren</a> en <a href="/products/interactieve-muur.html">muren</a> kunnen worden ingezet voor zowel revalidatie als educatie en entertainment, waardoor de investering breder benut wordt.</p>

<h2>Financiering en subsidies</h2>
<p>Revalidatiecentra en zorginstellingen kunnen voor interactieve technologie vaak gebruikmaken van innovatiesubsidies, zorgbudgetten en fondsen voor therapeutische hulpmiddelen. De investering wordt gerechtvaardigd door meetbaar hogere therapietrouw en efficiëntere behandeltrajecten.</p>

<p>Benieuwd hoe interactieve technologie de revalidatie in uw instelling kan versterken? Neem contact op voor een vrijblijvend adviesgesprek of een demonstratie op locatie.</p>
"""
    },
    "interactieve-zandbak-kopen": {
        "title": "Een interactieve zandbak kopen: dit moet u weten",
        "html": """
<p>Een interactieve zandbak is misschien wel het meest verrassende product in het assortiment van interactieve speeltechnologie. Het combineert het oeroude plezier van spelen met zand met geavanceerde projectietechnologie. Maar wat kost het, hoe werkt het, en is het iets voor uw locatie?</p>

<h2>Hoe werkt een interactieve zandbak?</h2>
<p>Boven de zandbak hangt een projector met dieptesensor (vergelijkbaar met een Kinect-sensor). Het systeem scant continu de hoogte van het zandoppervlak en projecteert daarop interactieve beelden. Graaf een kuil en er verschijnt water. Bouw een berg en er groeit gras. Maak een vulkaan en er stroomt lava. De projectie past zich in real-time aan aan de vormen die kinderen maken.</p>

<h2>Toepassingen en spelmogelijkheden</h2>
<p>De <a href="/products/interactieve-zandbak.html">interactieve zandbak</a> biedt diverse spelmodi:</p>
<ul>
<li><strong>Topografie</strong> — Kinderen leren over landschappen, waterstromen en hoogtekaarten door het zand te vormen</li>
<li><strong>Ecologie</strong> — Dieren verschijnen in het juiste "habitat" (vissen in water, vogels op bergen)</li>
<li><strong>Seizoenen</strong> — Het landschap verandert mee met de seizoenen</li>
<li><strong>Vrij spel</strong> — Kinderen creëren hun eigen wereld zonder regels of doelen</li>
<li><strong>Educatief</strong> — Gerichte opdrachten zoals "bouw een eiland" of "maak een rivier"</li>
</ul>

<h2>Voor wie is een interactieve zandbak geschikt?</h2>
<p>De interactieve zandbak is veelzijdig inzetbaar:</p>
<ul>
<li><strong>Kinderdagverblijven</strong> — Als binnenalternatief voor de buitenzandbak</li>
<li><strong>Scholen</strong> — Voor aardrijkskunde, natuur en techniek op een tastbare manier</li>
<li><strong>Musea</strong> — Educatieve tentoonstellingen over geologie en geografie</li>
<li><strong>Speelparadijzen</strong> — Een unieke attractie die bezoekers trekt</li>
<li><strong>Revalidatiecentra</strong> — Tactiele stimulatie gecombineerd met visuele feedback</li>
</ul>

<h2>Wat kost een interactieve zandbak?</h2>
<p>De prijs van een interactieve zandbak hangt af van de grootte en specificaties. Een standaard systeem voor binnengebruik start rond de €5.000-€8.000 inclusief projector, sensor en software. Grotere systemen voor commercieel gebruik kunnen oplopen tot €15.000. Leasemodellen zijn beschikbaar, waardoor de maandelijkse kosten beheersbaar blijven.</p>

<h2>Installatie en onderhoud</h2>
<p>De installatie is relatief eenvoudig: de projector en sensor worden boven de zandbak gemonteerd (aan plafond of frame). Het zand zelf is speciaal kinetisch zand of regulier speelzand. Onderhoud beperkt zich tot het schoonhouden van de projectorlens en het aanvullen van zand. Software-updates verlopen automatisch.</p>

<h2>Hygiëne en veiligheid</h2>
<p>Een veelgestelde vraag betreft hygiëne. De interactieve zandbak gebruikt bij voorkeur kinetisch zand, dat van nature bacteriewerend is en minder stof produceert. Het zand kan periodiek vervangen worden. Het systeem bevat geen bewegende delen waar kinderen bij kunnen, en de projector is buiten bereik gemonteerd.</p>

<p>Benieuwd of een interactieve zandbak past bij uw locatie? Neem contact op voor een vrijblijvend adviesgesprek en een demonstratie.</p>
"""
    }
}

token = get_token()
headers = {
    "Authorization": f"Ghost {token}",
    "Content-Type": "application/json"
}

# First get all existing posts to find their IDs
content_key = "b8903092a7c9a8b54d7378f5a1"
r = requests.get(f"{GHOST_URL}/ghost/api/content/posts/?key={content_key}&limit=20&fields=id,slug,title,updated_at")
existing = {p["slug"]: p for p in r.json()["posts"]}

print(f"Found {len(existing)} existing posts")

for slug, data in POSTS.items():
    if slug in existing:
        post_id = existing[slug]["id"]
        updated_at = existing[slug]["updated_at"]
        mobiledoc = make_mobiledoc(data["html"])
        
        payload = {
            "posts": [{
                "mobiledoc": mobiledoc,
                "updated_at": updated_at
            }]
        }
        
        # Re-generate token for each request (in case of expiry)
        token = get_token()
        headers["Authorization"] = f"Ghost {token}"
        
        r = requests.put(
            f"{GHOST_URL}/ghost/api/admin/posts/{post_id}/",
            headers=headers,
            json=payload
        )
        
        if r.status_code == 200:
            html_len = len(r.json()["posts"][0].get("html") or "")
            print(f"✅ Updated: {slug} ({html_len} chars HTML)")
        else:
            print(f"❌ Failed: {slug} — {r.status_code}: {r.text[:200]}")
    else:
        print(f"⚠️  Not found: {slug}")

# Also check the "coming-soon" post
if "coming-soon" in existing:
    print(f"\nℹ️  'coming-soon' post still exists (default Ghost post)")
