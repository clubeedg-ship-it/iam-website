#!/usr/bin/env python3
"""Fix Ghost blog posts - update lexical posts with HTML content."""
import json, jwt, requests, time

GHOST_URL = "http://localhost:3007"
KEY_ID = "69a25a83632d37000102e2de"
KEY_SECRET = "f713d9ab03d8faed95692e4d59bc6755952803800956bdc01ffea067cf7c83e3"

def get_token():
    iat = int(time.time())
    key = bytes.fromhex(KEY_SECRET)
    return jwt.encode(
        {"iat": iat, "exp": iat + 300, "aud": "/admin/"},
        key, algorithm="HS256",
        headers={"alg": "HS256", "typ": "JWT", "kid": KEY_ID}
    )

def make_lexical_html(html_content):
    """Create lexical JSON with an HTML card."""
    return json.dumps({
        "root": {
            "children": [
                {
                    "type": "html",
                    "version": 1,
                    "html": html_content
                }
            ],
            "direction": None,
            "format": "",
            "indent": 0,
            "type": "root",
            "version": 1
        }
    })

# All blog post content
POSTS = {}
POSTS["interactieve-vloer-kinderdagverblijf"] = """
<p>Steeds meer kinderdagverblijven ontdekken de kracht van interactieve vloeren. Deze innovatieve technologie verandert elke ruimte in een dynamische speelomgeving waar kinderen spelend leren, bewegen en samenwerken. Maar wat maakt een interactieve vloer zo waardevol voor de kinderopvang?</p>
<h2>Wat is een interactieve vloer?</h2>
<p>Een interactieve vloer is een projectiesysteem dat beelden op de grond projecteert die reageren op beweging. Kinderen kunnen rennen, springen en dansen over kleurrijke spellen die direct reageren op hun bewegingen. Het systeem bestaat uit een plafondprojector en bewegingssensoren — geen schermen, geen tablets, alleen fysiek actief spel.</p>
<h2>Waarom kiezen kinderdagverblijven voor interactieve vloeren?</h2>
<p>De voordelen voor de kinderopvang zijn veelzijdig:</p>
<ul><li><strong>Motorische ontwikkeling</strong> — Kinderen bewegen tot 40% meer tijdens vrij spel met een interactieve vloer.</li><li><strong>Cognitieve groei</strong> — Spelvormen stimuleren tellen, kleuren herkennen, patronen volgen en samenwerken.</li><li><strong>Inclusiviteit</strong> — Tot 12 kinderen spelen tegelijk, inclusief kinderen met een motorische of cognitieve beperking.</li><li><strong>Geen slijtage</strong> — Digitale content vervangt fysiek speelgoed dat kapot gaat.</li></ul>
<h2>Bewegend leren: de wetenschap erachter</h2>
<p>Onderzoek toont aan dat jonge kinderen het beste leren wanneer ze fysiek actief zijn. De hersenen van peuters en kleuters ontwikkelen zich sneller wanneer beweging en cognitieve taken gecombineerd worden. Een interactieve vloer maakt dit principe tastbaar: kinderen leren tellen door te springen, herkennen vormen door erop te staan, en ontwikkelen sociale vaardigheden door samen te spelen.</p>
<h2>Praktisch: installatie en kosten</h2>
<p>De projector wordt aan het plafond gemonteerd (binnen één uur), er is geen verbouwing nodig, en het systeem werkt op elke vlakke vloer. Met een leasemodel is er geen grote investering vooraf — kinderdagverblijven kunnen starten vanaf een maandelijks bedrag.</p>
<h2>De impact op de dagelijkse praktijk</h2>
<p>Pedagogisch medewerkers noemen de interactieve vloer vaak hun "geheime wapen" voor drukke ochtenden. Kinderen zijn gefocust, bewegen actief, en er ontstaat minder conflict omdat het spel structuur biedt.</p>
<p>Benieuwd wat een interactieve vloer voor uw kinderdagverblijf kan betekenen? <a href="/products/interactieve-vloer.html">Bekijk onze interactieve vloer</a> of neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

POSTS["interactieve-speeltoestellen-kinderopvang"] = """
<p>De kinderopvang evolueert. Waar vroeger een zandbak en een klimrek volstonden, verwachten ouders en toezichthouders steeds meer van de speelomgeving. Interactieve speeltoestellen combineren fysiek spel met digitale technologie — en de resultaten zijn indrukwekkend.</p>
<h2>Welke interactieve speeltoestellen bestaan er?</h2>
<ul><li><strong>Interactieve vloeren</strong> — Projecties op de grond die reageren op beweging. <a href="/products/interactieve-vloer.html">Meer info →</a></li><li><strong>Interactieve muren</strong> — Wandprojecties waar kinderen op kunnen tikken en tekenen. <a href="/products/interactieve-muur.html">Meer info →</a></li><li><strong>Interactieve zandbakken</strong> — Projecties op zand die reageren op graven en vormen. <a href="/products/interactieve-zandbak.html">Meer info →</a></li><li><strong>Interactieve klimwanden</strong> — Klimmen gecombineerd met spelprojecties. <a href="/products/interactieve-klimwand.html">Meer info →</a></li><li><strong>Mobiele systemen</strong> — Verrijdbare projectoren voor verschillende ruimtes. <a href="/products/mobiele-vloer.html">Meer info →</a></li></ul>
<h2>Waar moet u op letten bij de keuze?</h2>
<ul><li><strong>Leeftijdsgeschiktheid</strong> — Is de content afgestemd op peuters of ook kleuters?</li><li><strong>Groepsgrootte</strong> — Hoeveel kinderen kunnen tegelijk spelen?</li><li><strong>Educatieve waarde</strong> — Sluiten de spelvormen aan bij de leerdoelen?</li><li><strong>Onderhoud</strong> — Software-updates vs fysiek onderhoud.</li><li><strong>Ruimte-eisen</strong> — Minimale vloer- of wandoppervlakte.</li></ul>
<h2>De kosten: investering of lease?</h2>
<p>Interactieve speeltoestellen variëren van €2.000 (budget) tot €16.000 (premium). Leasemodellen maken de technologie toegankelijk voor zowel grote ketens als kleinere zelfstandige opvanglocaties.</p>
<h2>De toekomst van spelen in de kinderopvang</h2>
<p>Interactieve technologie is geen vervanging van traditioneel spel — het is een aanvulling. De beste resultaten ontstaan wanneer kinderen afwisselen tussen vrij spel, gestructureerde activiteiten en interactieve momenten.</p>
<p>Wilt u ontdekken welke interactieve speeltoestellen passen bij uw opvanglocatie? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

POSTS["bewegend-leren-peuters-kleuters"] = """
<p>Kinderen leren niet door stil te zitten. De wetenschap is duidelijk: bewegend leren is effectiever, gezonder en leuker.</p>
<h2>Wat zegt de wetenschap?</h2>
<p>Neurowetenschappelijk onderzoek toont aan dat fysieke activiteit direct gekoppeld is aan cognitieve ontwikkeling bij jonge kinderen:</p>
<ul><li>De doorbloeding van de prefrontale cortex neemt toe — het gebied voor concentratie en planning</li><li>BDNF wordt aangemaakt — essentieel voor nieuwe neurale verbindingen</li><li>De hippocampus, betrokken bij geheugenvorming, wordt actiever</li></ul>
<h2>De GGD-cijfers zijn alarmerend</h2>
<p>De GGD constateert dat ruim 40% van de Nederlandse kinderen onvoldoende beweegt. De beweegrichtlijn voor kinderen van 0-4 jaar adviseert minimaal 3 uur per dag fysieke activiteit. In de praktijk halen veel kinderen dit niet.</p>
<h2>Hoe ziet bewegend leren eruit?</h2>
<ul><li><strong>Interactieve vloerspellen</strong> — Leren tellen door te springen op getallen, kleuren herkennen door op vlakken te staan</li><li><strong>Bewegingscircuits</strong> — Cognitieve opdrachten met klimmen, kruipen en balanceren</li><li><strong>Muziek en dans</strong> — Ritme, coördinatie en sociale vaardigheden</li></ul>
<h2>Technologie als hulpmiddel</h2>
<p>Een <a href="/products/interactieve-vloer.html">interactieve vloer</a> biedt honderden spelvarianten die automatisch het juiste niveau kiezen. Pedagogisch medewerkers hoeven niet elke dag nieuwe activiteiten te bedenken.</p>
<h2>Tips voor meer bewegend leren</h2>
<ol><li>Vervang zit-activiteiten door sta- of beweegvarianten</li><li>Integreer korte bewegingsmomenten tussen rustige activiteiten</li><li>Gebruik de buitenruimte actiever</li><li>Kies spelmateriaal dat uitnodigt tot bewegen</li></ol>
<p>Benieuwd hoe interactieve technologie bewegend leren kan versterken? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

POSTS["interactieve-muur-school"] = """
<p>Het klaslokaal verandert. Waar krijtborden plaatsmaakten voor digiborden, zien we nu de volgende stap: interactieve muren die het hele klaslokaal omtoveren tot een leeromgeving.</p>
<h2>Wat is een interactieve muur?</h2>
<p>Een interactieve muur projecteert beelden op een wand die reageren op aanraking en beweging. Kinderen kunnen direct op de muur tekenen, spellen spelen, en interactief leren. Het verschil met een smartboard? De projectie kan veel groter zijn en meerdere kinderen interacteren tegelijk.</p>
<h2>Toepassingen in het onderwijs</h2>
<ul><li><strong>Taalonderwijs</strong> — Interactieve woordspellen en letterpuzzels</li><li><strong>Rekenen</strong> — Wiskundige concepten worden tastbaar</li><li><strong>Wereldoriëntatie</strong> — Interactieve kaarten en tijdlijnen</li><li><strong>Creatieve vakken</strong> — Digitaal tekenen op groot formaat</li><li><strong>Sociale vaardigheden</strong> — Samenwerkingsspellen</li></ul>
<h2>Voordelen voor het onderwijs</h2>
<ul><li><strong>Differentiatie</strong> — Het niveau past automatisch aan</li><li><strong>Betrokkenheid</strong> — Kinderen die afhaken worden actief betrokken</li><li><strong>Beweging</strong> — Leerlingen staan en bewegen, wat concentratie verbetert</li></ul>
<h2>Implementatie op school</h2>
<p>De installatie van een <a href="/products/interactieve-muur.html">interactieve muur</a> is eenvoudiger dan verwacht. Een projector wordt gemonteerd, en het systeem is direct klaar. Veel scholen beginnen met één systeem en breiden later uit.</p>
<p>Benieuwd hoe een interactieve muur uw school kan verrijken? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

POSTS["interactieve-projectie-speeltuin"] = """
<p>De speeltuin van de toekomst is een plek waar digitale projecties en fysiek spel samenkomen. Interactieve projectietechnologie transformeert speeltuinen, pretparken en Family Entertainment Centers wereldwijd.</p>
<h2>Hoe werkt het?</h2>
<p>Projectoren projecteren interactieve beelden op vloeren, muren of speeltoestellen. Sensoren detecteren bewegingen van kinderen, waardoor het spel reageert op rennen, springen en aanraken.</p>
<h2>Toepassingen</h2>
<ul><li><strong>Interactieve speelvloeren</strong> — Grote vloeren waar tientallen kinderen tegelijk spelen</li><li><strong>Interactieve glijbanen</strong> — Projecties die reageren op snelheid</li><li><strong>Interactieve zandbakken</strong> — <a href="/products/interactieve-zandbak.html">Digitale projecties op zand</a></li><li><strong>Interactieve muren</strong> — <a href="/products/interactieve-muur.html">Buitenmuren als touchscreens</a></li><li><strong>Thema-ervaringen</strong> — Seizoensgebonden content</li></ul>
<h2>Waarom investeren?</h2>
<ul><li><strong>Hogere bezoekersaantallen</strong> — Het wow-effect trekt bezoekers</li><li><strong>Langere verblijftijd</strong> — Afwisselende ervaring</li><li><strong>Herhalingsbezoek</strong> — Vernieuwde content</li><li><strong>Onderscheidend vermogen</strong> — Uniek in de markt</li></ul>
<p>Benieuwd wat interactieve projectie voor uw locatie kan betekenen? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

POSTS["digitale-speeltuin-kinderen"] = """
<p>De term "digitale speeltuin" roept bij sommige ouders weerstand op. Meer schermtijd? Nee, juist het tegenovergestelde. Een moderne digitale speeltuin combineert technologie met fysiek actief spel — zonder tablet of smartphone in zicht.</p>
<h2>Wat is een digitale speeltuin?</h2>
<p>Een fysieke ruimte waar interactieve technologie het speelplezier versterkt. Vloeren die oplichten, muren waar je op tekent met je hele lichaam, zandbakken waar digitale dieren verschijnen. De technologie is onzichtbaar — kinderen zien alleen het spel.</p>
<h2>Waarom kinderen het geweldig vinden</h2>
<ul><li><strong>Magie</strong> — De vloer reageert op je!</li><li><strong>Variatie</strong> — Elk bezoek is anders</li><li><strong>Samenspel</strong> — Ontworpen voor groepen</li><li><strong>Uitdaging</strong> — Past zich aan het niveau aan</li></ul>
<h2>Waarom ouders het waarderen</h2>
<ul><li><strong>Actief, niet passief</strong> — Kinderen bewegen de hele tijd</li><li><strong>Educatief</strong> — Leerelementen zonder dat het voelt als onderwijs</li><li><strong>Sociaal</strong> — Samen spelen, niet achter een scherm</li><li><strong>Veilig</strong> — Geen scherpe randen of hygiënerisico's</li></ul>
<h2>Soorten interactieve speeloplossingen</h2>
<ul><li><a href="/products/interactieve-vloer.html">Interactieve vloeren</a></li><li><a href="/products/interactieve-muur.html">Interactieve muren</a></li><li><a href="/products/interactieve-zandbak.html">Interactieve zandbakken</a></li><li><a href="/products/interactieve-klimwand.html">Interactieve klimwanden</a></li><li><a href="/products/mobiele-vloer.html">Mobiele systemen</a></li></ul>
<p>Benieuwd hoe u een digitale speelervaring kunt creëren? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

POSTS["revalidatie-kinderen-interactief"] = """
<p>In de kinderrevalidatie is motivatie alles. Interactieve technologie verandert de spelregels: therapie wordt spel, en kinderen oefenen langer en intensiever zonder dat het als werk voelt.</p>
<h2>Het probleem met traditionele kinderrevalidatie</h2>
<p>Een kind motiveren om dezelfde oefening tientallen keren te herhalen is de dagelijkse uitdaging. Zelfs het beste speelgoed verliest zijn aantrekkingskracht na een aantal sessies.</p>
<h2>Hoe interactieve technologie helpt</h2>
<ul><li><strong>Intrinsieke motivatie</strong> — Het spel zelf is de beloning</li><li><strong>Herhaling zonder verveling</strong> — Dezelfde oefening in tientallen spelvarianten</li><li><strong>Aanpasbaar niveau</strong> — Past zich aan de mogelijkheden aan</li><li><strong>Meetbare voortgang</strong> — Registreert bewegingen en reactietijden</li><li><strong>Groepstherapie</strong> — Meerdere kinderen oefenen samen</li></ul>
<h2>Toepassingen</h2>
<ul><li><strong>Motorische revalidatie</strong> — Grove en fijne motoriek via interactieve spellen</li><li><strong>Balans- en coördinatietraining</strong> — Gewicht verplaatsen en balanceren</li><li><strong>Cognitieve revalidatie</strong> — Geheugen- en aandachtsspellen met beweging</li><li><strong>Pijnmanagement</strong> — Afleiding vermindert pijnervaring</li></ul>
<h2>InterActiveMove in de zorg</h2>
<p>Onze <a href="/products/interactieve-vloer.html">interactieve vloeren</a> en <a href="/products/interactieve-muur.html">muren</a> worden ingezet voor revalidatie, educatie én entertainment — bredere benutting van de investering.</p>
<p>Benieuwd hoe interactieve technologie de revalidatie in uw instelling kan versterken? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

POSTS["interactieve-zandbak-kopen"] = """
<p>Een interactieve zandbak combineert het oeroude plezier van spelen met zand met geavanceerde projectietechnologie. Maar wat kost het, hoe werkt het, en is het iets voor uw locatie?</p>
<h2>Hoe werkt een interactieve zandbak?</h2>
<p>Boven de zandbak hangt een projector met dieptesensor. Het systeem scant continu het zandoppervlak en projecteert interactieve beelden. Graaf een kuil en er verschijnt water. Bouw een berg en er groeit gras. De projectie past zich in real-time aan.</p>
<h2>Spelmogelijkheden</h2>
<ul><li><strong>Topografie</strong> — Leren over landschappen en waterstromen</li><li><strong>Ecologie</strong> — Dieren verschijnen in het juiste habitat</li><li><strong>Seizoenen</strong> — Het landschap verandert mee</li><li><strong>Vrij spel</strong> — Eigen wereld creëren</li><li><strong>Educatief</strong> — Gerichte opdrachten</li></ul>
<h2>Voor wie geschikt?</h2>
<ul><li><strong>Kinderdagverblijven</strong> — Binnenalternatief voor buitenzandbak</li><li><strong>Scholen</strong> — Aardrijkskunde op een tastbare manier</li><li><strong>Musea</strong> — Educatieve tentoonstellingen</li><li><strong>Speelparadijzen</strong> — Unieke attractie</li><li><strong>Revalidatiecentra</strong> — Tactiele stimulatie met visuele feedback</li></ul>
<h2>Wat kost een interactieve zandbak?</h2>
<p>Een standaard systeem start rond €5.000-€8.000 inclusief projector, sensor en software. Grotere systemen tot €15.000. Leasemodellen zijn beschikbaar.</p>
<h2>Installatie en onderhoud</h2>
<p>Projector en sensor worden boven de zandbak gemonteerd. Onderhoud beperkt zich tot schoonhouden van de lens en aanvullen van zand. Software-updates verlopen automatisch.</p>
<p>Benieuwd of een <a href="/products/interactieve-zandbak.html">interactieve zandbak</a> past bij uw locatie? Neem contact op voor een vrijblijvend adviesgesprek.</p>
"""

# Update all posts
token = get_token()
headers = {"Authorization": f"Ghost {token}", "Content-Type": "application/json"}

# Get all posts
r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/?limit=20", headers=headers)
posts = {p["slug"]: p for p in r.json()["posts"]}

for slug, html_content in POSTS.items():
    if slug not in posts:
        print(f"⚠️  Not found: {slug}")
        continue
    
    post = posts[slug]
    lexical = make_lexical_html(html_content.strip())
    
    token = get_token()
    headers["Authorization"] = f"Ghost {token}"
    
    r = requests.put(
        f"{GHOST_URL}/ghost/api/admin/posts/{post['id']}/",
        headers=headers,
        json={"posts": [{"lexical": lexical, "updated_at": post["updated_at"]}]}
    )
    
    if r.status_code == 200:
        new_html = r.json()["posts"][0].get("html") or ""
        print(f"✅ {slug}: {len(new_html)} chars")
    else:
        print(f"❌ {slug}: {r.status_code} — {r.text[:200]}")

# Delete the default "coming-soon" post
if "coming-soon" in posts:
    token = get_token()
    headers["Authorization"] = f"Ghost {token}"
    r = requests.delete(f"{GHOST_URL}/ghost/api/admin/posts/{posts['coming-soon']['id']}/", headers=headers)
    print(f"\n{'✅' if r.status_code == 204 else '❌'} Deleted 'coming-soon' default post")
