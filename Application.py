# makers: Sanne en Inge
# de benodigde python code om de website te laten werken en de goeie resultaten te krijgen

from flask import Flask, render_template, request
import mysql.connector
import re
from Bio.Blast import NCBIWWW, NCBIXML

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def home():
    return render_template('Database_page2.html')


@app.route('/results', methods=['get', 'post'])
def results_filters():
    """ Deze functie heeft 2 lijsten, 1 lijst voor de kolommen, en 1 lijst voor alle checkboxes. Hij gaat elke checkbox
    af om te kijken of deze een waarde heeft, als dat zo is wordt deze is een nieuwe lijst toegevoegd. Daarna
    worden er functies aangeroepen voor filters en waardes. Als er niet is gefilterd op kolommen wordt de lijst met
    kolommen gereturnd en als er wel is gefilterd op kolommen wordt deze lijst gereturnd. De accessiecodes worden
    ook opgehaald

    :return lijst kolommen als niet op kolommen is gefilterd, samen met andere filters en accessie_index en resultaat
    :return lijst resultaat_kolommen als er wel op kolommen is gefilterd, smaen met andere filters, resultaat en
    accessie_index
    """
    # lijsten met de waardes van mogelijke filteropties, deze staan vast in het script vanwege tabellen die we niet
    # willen laten zien, de lijsten bestaan uit de waardes van de checkboxes
    lijst = ["checkboxOne", "checkboxTwo", "checkboxThree", "checkboxFour", "checkboxFive", "checkboxSix",
             "checkboxSeven", "checkboxEight", "checkboxNine", "checkboxTen", "checkboxEleven", "checkboxTwelve",
             "checkboxThirteen", "checkboxFourteen", "checkboxFifteen", "checkboxSixteen"]
    lijst_kolommen = ["Blast_type", "Score", "Query_cover", "Percent_ident", "E_value", "Accessiecode", "Organisme",
                      "Taxonomie", "Read_type", "Sequentie", "Prot_naam"]
    resultaat_kolommen = []
    # de filterstappen om de juiste lijsten te krijgen met de waardes  voor de query's
    for item in lijst:
        result = request.form.get(item)
        if result is not None:
            resultaat_kolommen.append(result)

    resultaat_where = filters()
    e_value, score, percentidentity, querycover = waardes_getallen()
    resultaat_where_ = filters_getallen(resultaat_where, e_value, score, percentidentity, querycover)
    # deze functie wordt aangeroepen om de querys uit te voeren
    resultaat = result_querys(lijst_kolommen, resultaat_kolommen, resultaat_where_)
    # afhankelijk of er gefilterd is op de kolommen krijg je een andere return
    accesie_index = lijst_kolommen.index("Accessiecode")
    if len(resultaat_kolommen) == 0:
        return render_template('results.html', accesie_index=accesie_index, data=resultaat, lijst=lijst_kolommen)
    if len(resultaat_kolommen) != 0:
        return render_template('results.html', data=resultaat, lijst=resultaat_kolommen)


def filters():
    """ Deze functie heeft een lijst met waardes waar op gefilterd kan worden. Deze worden nagelopen of deze een waarde
    hebben, als dat zo is wordt deze toegevoegd in een nieuwe lijst dat deze door een query zo kan worden uitgevoerd,
    als de lijst leeg is, wordt er nog 'where' toegvoegd in de zin.

    :return lijst met alle filters waar op gefilterd kan worden
    """
    resultaat_where = []
    lijst_filters = ["organisme", "eiwit", "checkboxread1", "checkboxread2", "checkboxread3",
                     "checkboxblastx", "checkboxtblastx", "checkboxboth"]
    # de reden waarom hier vanaf index 1 2 opties worden gegeven is vanwege dat je bij de eerste een where hebt staan
    # voor de query anders werkt die niet, dan is de keuze steeds of er een where komt te staan of niet een where
    # wat afhankelijk is van de lengte van de lijst
    for item in lijst_filters:
        index_getal = lijst_filters.index(item)
        result = request.form.get(item)
        if result is not None:
            if len(result) > 0:
                if index_getal == 0:
                    resultaat_where.append("where Organisme like '%{}%'".format(result))
                if index_getal == 1:
                    if len(resultaat_where) > 1:
                        resultaat_where.append("Prot_naam like '%{}%'".format(result))
                    elif len(resultaat_where) == 0:
                        resultaat_where.append("where Prot_naam like '%{}%'".format(result))
            if index_getal == 2 or index_getal == 3:
                if len(resultaat_where) > 0:
                    resultaat_where.append("Read_type = {}".format(result))
                if len(resultaat_where) == 0:
                    resultaat_where.append("where Read_type = {}".format(result))
            if index_getal == 4:
                if len(resultaat_where) > 0:
                    resultaat_where.append("{}".format(result))
                if len(resultaat_where) == 0:
                    resultaat_where.append("where {}".format(result))
            if index_getal == 5 or index_getal == 6:
                if len(resultaat_where) > 0:
                    resultaat_where.append("Blast_type = {}".format(result))
                if len(resultaat_where) == 0:
                    resultaat_where.append("where Blast_type = {}".format(result))
            if index_getal == 7:
                if len(resultaat_where) > 0:
                    resultaat_where.append("{}".format(result))
                if len(resultaat_where) == 0:
                    resultaat_where.append("where {}".format(result))

    return resultaat_where


def waardes_getallen():
    """ Deze functie maakt een lijst aan voor getallen waar op gefilterd kan worden. Voor elke waarde wordt gekeken of
    het een waarde heeft, en deze wordt dan aan een variabele gehangen

    :return: de variabelen E_value, score_value, Percent identity en query cover met hun waarde
    """
    lijst_getallen = ["E-value_value", "Score_value", "Percent identity", "Query cover"]
    # we slaan deze waardes op in een variabele om zo de goeie waardes straks te kunnen filteren in de database
    e_value = ''
    score = ''
    percentidentity = ''
    querycover = ''
    for item in lijst_getallen:
        index_getal = lijst_getallen.index(item)
        result = request.form.get(item)
        if len(result) > 0:
            if index_getal == 0:
                e_value = result
            if index_getal == 1:
                score = result
            if index_getal == 2:
                percentidentity = result
            if index_getal == 3:
                querycover = result

    return e_value, score, percentidentity, querycover
    # de opgeslagen waardes komen nu samen in een lijst te staan, we doen het op deze manier anders krijg je de
    # verkeerde waardes voor de zoekopdrachten


def filters_getallen(resultaat_where, e_value, score, percentidentity, querycover):
    """ Deze functie maakt een lijst aan voor de filters, in die lijst wordt gekeken of het een waarde bevat, zo ja
    dan wordt deze toegevoegd in de lijst resultaat_where, als deze lijst leeg is wordt er nog 'where' aan toegevoegd
    anders niet. Daarna wordt deze lijst weer gereturnd

    :param resultaat_where: eerdere filters worden meegenomen om 1 lijst te krijgen
    :param e_value: eventueel een waarde waar op gefilterd kan worden
    :param score: eventueel een waarde waar op gefilterd kan worden
    :param percentidentity: eventueel een waarde waar op gefilterd kan worden
    :param querycover: eventueel een waarde waar op gefilterd kan worden
    :return: resultaat_where, lijst met alle filters
    """
    lijst_tekens = ["E_value_parameter", "Score_parameter", "percent_identity_parameter", "query_cover_parameter"]
    for item in lijst_tekens:
        index_getal = lijst_tekens.index(item)
        result = request.form.get(item)
        if len(result) > 0:
            if index_getal == 0 and e_value != '' and len(resultaat_where) > 0:
                resultaat_where.append("E_value {} {}".format(result, e_value))
            elif index_getal == 0 and e_value != '' and len(resultaat_where) == 0:
                resultaat_where.append("where E_value {} {}".format(result, e_value))
            if index_getal == 1 and score != '' and len(resultaat_where) > 0:
                resultaat_where.append("Score {} {}".format(result, score))
            elif index_getal == 1 and score != '' and len(resultaat_where) == 0:
                resultaat_where.append("where Score {} {}".format(result, score))
            if index_getal == 2 and percentidentity != '' and len(resultaat_where) > 0:
                resultaat_where.append("Percent_ident {} {}".format(result, percentidentity))
            elif index_getal == 2 and percentidentity != '' and len(resultaat_where) == 0:
                resultaat_where.append("where Percent_ident {} {}".format(result, percentidentity))
            if index_getal == 3 and querycover != '' and len(resultaat_where) > 0:
                resultaat_where.append("Query_cover {} {}".format(result, percentidentity))
            elif index_getal == 3 and querycover != '' and len(resultaat_where) == 0:
                resultaat_where.append("where Query_cover {} {}".format(result, percentidentity))
    return resultaat_where


def result_querys(lijst_kolommen, resultaat_kolommen, resultaat_where):
    """ Deze functie maakt connectie aan met de database, en kan dan 2 querys gaan uitvoeren. 1 query als er gefilterd
    is op kolommen, dan wordt ook nog de lijst resultaat_where meegegeven in de query. De andere query als er niet is
    gefilterd op kolommen, dan wordt ook de lijst resultaat_where nog meegegeven. Een van deze querys worden uitgevoerd
    en het resultaat wordt gereturnd.

    :param lijst_kolommen:
    :param resultaat_kolommen:
    :param resultaat_where:
    :return: resultaat van de query
    """
    # hier wordt de connectie gemaakt van de database
    verbinding = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                         user="lszlh@hannl-hlo-bioinformatica-mysqlsrv",
                                         db="lszlh",
                                         passwd="619150")
    cursor = verbinding.cursor(dictionary=True)
    # de query's die worden uitgevoerd, afhankelijk van de gegevens
    resultaat = ''
    if len(resultaat_kolommen) == 0:
        query = "select {} from seq_read join blast b on seq_read.Read_ID = b.Blast_ID " \
                "join eiwitten e on b.Blast_ID = e.Prot_id {}" \
            .format(" , ".join(lijst_kolommen), " and ".join(resultaat_where))
        cursor.execute(query)
        resultaat = cursor.fetchall()
    if len(resultaat_kolommen) != 0:
        query = "select {} from seq_read join blast b on seq_read.Read_ID = b.Blast_ID " \
                "join eiwitten e on b.Blast_ID = e.Prot_id {}" \
            .format(" , ".join(resultaat_kolommen), " and ".join(resultaat_where))
        print(query)
        cursor.execute(query)
        resultaat = cursor.fetchall()
    cursor.close()
    verbinding.close()
    return resultaat


@app.route('/organism')
def organisms():
    """ Deze functie roept eerst 2 waardes op. Daarna als de ene waarde 'None' is, wordt er connectie gelegd aan de
    database en wordt er gefilterd op Organismenamen op alfabetische volgorde. Dan wordt er een render_template
    gereturnd van organisme samen met het resultaat van de query. Als de waarde niet 'None' is, wordt er een andere
    query uitgevoerd met het gekozen organisme naam om daar gegevens van op te halen. Dan wordt er een render_template
    organisme gereturnd met resultaat van de query

    :return: render_template 'organisme' met resultaat van 1 van de querys
    """
    org = request.args.get("organismelijst")
    org2 = "Where Organisme like '%{}%'".format(org)

    if org is None:
        # hier is de query om in de website de lijst met Organisme te laten zien
        connection = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                             user="lszlh@hannl-hlo-bioinformatica-mysqlsrv",
                                             db="lszlh",
                                             passwd="619150")
        cur = connection.cursor(dictionary=True)
        cur.execute(
            "select distinct Organisme,Score,E_value,Actual_ID,Percent_ident,Accessiecode,Query_cover,Taxonomie "
            "from blast order by Organisme ")

        data = cur.fetchall()
        return render_template('organism.html', data=data)
    else:
        connection = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                             user="lszlh@hannl-hlo-bioinformatica-mysqlsrv",
                                             db="lszlh",
                                             passwd="619150")
        cur = connection.cursor(dictionary=True)
        query = "select distinct Organisme,Score,E_value,Actual_ID,Percent_ident,Accessiecode,Query_cover,Taxonomie " \
                "from blast {} order by Organisme".format(org2)

        cur.execute(query)

        data = cur.fetchall()
        return render_template('organism.html', data=data)


@app.route('/protein')
def protein():
    """ Deze functie roept eerst 2 waardes op. Daarna als de ene waarde 'None' is, wordt er connectie gelegd aan de
    database en wordt er gefilterd op eiwitnamen op alfabetische volgorde. Dan wordt er een render_template
    gereturnd van proein samen met het resultaat van de query. Als de waarde niet 'None' is, wordt er een andere
    query uitgevoerd met het gekozen eiwitnaam om daar gegevens van op te halen. Dan wordt er een render_template
    protein gereturnd met resultaat van de query

    :return: render_template 'protein' met resultaat van 1 van de querys
    """
    prot = request.args.get("proteinlijst")
    prot2 = "Where Prot_naam like '%{}%'".format(prot)
    # hier is de query om in de website de lijst met eiwitten te laten zien
    connection = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                         user="lszlh@hannl-hlo-bioinformatica-mysqlsrv",
                                         db="lszlh",
                                         passwd="619150")
    cur = connection.cursor(dictionary=True)
    if prot is None:
        cur.execute(
            "select distinct Prot_naam, Score,E_value,Actual_ID,Percent_ident,Accessiecode,Query_cover,Taxonomie "
            "from eiwitten join blast on Prot_id = Actual_ID order by Prot_naam")

        data = cur.fetchall()
        return render_template('protein.html', data=data)
    else:
        query = "select distinct Prot_naam, Score,E_value,Actual_ID,Percent_ident,Accessiecode,Query_cover,Taxonomie " \
                "from eiwitten join blast on Prot_id = Actual_ID {} order by Prot_naam".format(prot2)
        cur.execute(query)
        data = cur.fetchall()
        return render_template('protein.html', data=data)


@app.route('/blast')
def blast():
    """ Deze functie haalt de sequentie op, en gaat met een regular expression kijken of het dna, rna of eiwit is. Als
    het 1 van deze waarde is, wordt deze waarde op 'True' gezet, de rest staat op False. Als het geen van alle is, wordt
    anders op True gezet. Daarna wordt er een andere functie aangeroepen voor het resultaat en de titel wat de resultaat
    van een eventuele blast is.

    :return: render_template 'blast'  met sequentie, resultaat en titel
    """
    sequentie = request.args.get("seq")
    add = request.args.get("adding")
    dna = False
    rna = False
    eiwit = False
    anders = False
    # dit bepaalt wat de ingevoerde sequentie wordt
    if sequentie is not None:
        if len(re.findall("[ATCG]", sequentie, flags=re.IGNORECASE)) == len(sequentie):
            dna = True
        elif len(re.findall("[AUCG]", sequentie, flags=re.IGNORECASE)) == len(sequentie):
            rna = True
        elif len(re.findall("[ARNDCFQEGHILKMPSTWYV]", sequentie, flags=re.IGNORECASE)) == len(sequentie):
            eiwit = True
        else:
            anders = True
    resultaat = resultaat_beschrijving(dna, rna, eiwit, anders)
    titel = blasten(dna, sequentie)
    print(titel)
    # if add is None:
    #     resultaten_database()
    # if add is not None:
    #     adding(add)
    return render_template('BLAST.html', sequentie=sequentie, resultaat=resultaat, titel=titel)


def resultaat_beschrijving(dna, rna, eiwit, anders):
    """ Deze functie geeft een string mee, afhankelijk welke waarde op True staat.

    :param dna: True of False waarde, afhankelijk wat de sequentie is
    :param rna: True of False waarde, afhankelijk wat de sequentie is
    :param eiwit: True of False waarde, afhankelijk wat de sequentie is
    :param anders: True of False waarde, afhankelijk wat de sequentie is
    :return: string met resultaat wat de ingevoerde sequentie is
    """
    resultaat = ''
    # het resultaat wat wordt uitgeprint voor de gebruiken om het te controleren
    if dna is True:
        resultaat = "The sequence is DNA"
    elif rna is True:
        resultaat = "The sequence is RNA"
    elif eiwit is True:
        resultaat = "The sequence is protein"
    elif anders is True:
        resultaat = "The sequence is not DNA, RNA or protein"

    return resultaat


def blasten(dna, sequentie):
    """ Deze sequentie gaat als DNA op True staat, een blast uitvoeren. Hij haalt dan de sequentie op en het blast_type,
    hiermee gaat hij naar een andere functie op de blast uit te voeren. Als de titel leeg is, is er geen match gevonden,
    is deze niet leeg, dan staan er de blast resultaten in.

    :param dna: True of False afhankelijk wat de ingevoerde sequentie is
    :param sequentie: de sequentie die is ingevoerd
    :return: de titel, wat of resultaat van de blast bevat of een string waar in staat dat er geen resultaat is gevonden
    """
    if dna is True:
        blast_type = request.args.get("blast_type")
        if sequentie is not None and blast_type == "blastx":
            blast_resultaat, titel = blastx_blasten(sequentie)
        if sequentie is not None and blast_type == "tblastx":
            blast_resultaat, titel = tblastx_blasten(sequentie)
    else:
        titel = ''

    if titel == '':
        titel = "There is no match with: {}".format(sequentie)
    else:
        titel = "\n".join(blast_resultaat)
    return titel


def blastx_blasten(sequentie):
    """ Deze sequentie opent een leeg XML file, daarna gaat het de blast uitvoeren met blastx. De gegevens van deze
    blast worden opgeslageni in het bestand en dit bestand wordt gesloten. Daarna wordt dit bestand weer geopend en
    wordt voor elk resultaat het organisme, eiwit, sequentie, lengte, e_value en stukje van de vergelijking opgeslagen
    in een lege lijst. Deze wordt samen met titel wat een lege string is gereturnd.

    :param sequentie: de ingevoerde sequentie
    :return: blastresultaat, een lijst met gegevens van de blatresultaten
    :return titel, een lege string
    """
    titel = ''
    blast_resultaat = []
    bestand = open("Resultaat.xml", "w")
    result_handle = NCBIWWW.qblast("blastx", "nr", sequentie, alignments=1, hitlist_size=10)
    bestand.write(result_handle.getvalue())
    bestand.close()

    result_handle = open("Resultaat.xml", "r")
    blast_records = NCBIXML.parse(result_handle)
    blast_record = next(blast_records)
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            blast_resultaat.append("****Alignment****")
            titel = alignment.title
            titels = titel.split("[")
            titelss = titels[1].split("]")
            titel_ = titel.split("|")
            titel__ = titel_[2].split("[")
            blast_resultaat.append("Blast organism: {}".format(titelss[0]))
            blast_resultaat.append("Protein: {}".format(titel__[0]))
            blast_resultaat.append("Sequence: {}".format(alignment.title))
            blast_resultaat.append("Length: {}".format(alignment.length))
            blast_resultaat.append("E-value: {}".format(hsp.expect))
            blast_resultaat.append(hsp.query[0:75] + "...")
            blast_resultaat.append(hsp.match[0:75] + "...")
            blast_resultaat.append(hsp.sbjct[0:75] + "...")
            blast_resultaat.append("\n")

    return blast_resultaat, titel


def tblastx_blasten(sequentie):
    """ Deze sequentie opent een leeg XML file, daarna gaat het de blast uitvoeren met tblastx. De gegevens van deze
    blast worden opgeslageni in het bestand en dit bestand wordt gesloten. Daarna wordt dit bestand weer geopend en
    wordt voor elk resultaat het organisme, sequentie, lengte, e_value en stukje van de vergelijking opgeslagen
    in een lege lijst. Deze wordt samen met titel wat een lege string is gereturnd.

    :param sequentie: de ingevoerde sequentie
    :return: blastresultaat, een lijst met gegevens van de blatresultaten
    :return titel, een lege string
    """
    titel = ''
    blast_resultaat = []
    bestand = open("Resultaat.xml", "w")
    result_handle = NCBIWWW.qblast("tblastx", "nr", sequentie, alignments=1, hitlist_size=10)
    bestand.write(result_handle.getvalue())
    bestand.close()

    result_handle = open("Resultaat.xml", "r")
    blast_records = NCBIXML.parse(result_handle)
    blast_record = next(blast_records)
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            blast_resultaat.append("****Alignment****")
            titel = alignment.title
            titels = titel.split("|")
            titel = "Blast organisme: " + titels[4]
            blast_resultaat.append("Blast organisme: {}".format(titels[4]))
            blast_resultaat.append("Sequence: {}".format(alignment.title))
            blast_resultaat.append("Length: {}".format(alignment.length))
            blast_resultaat.append("E-value: {}".format(hsp.expect))
            blast_resultaat.append(hsp.query[0:75] + "...")
            blast_resultaat.append(hsp.match[0:75] + "...")
            blast_resultaat.append(hsp.sbjct[0:75] + "...")
            blast_resultaat.append("\n")

    return blast_resultaat, titel


def adding(add):
    """ Deze functie maakt connectie met de database, en voert een query uit om de max blast_id, actual_id en prot_id
    op te halen uit de database. Deze waardes worden + 1 gedaan en worden aan een andere functie meegegeven

    :param add: geeft aan of er resultaat in de database moet worden toegevoegd of niet
    """
    verbinding = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                         user="lszlh@hannl-hlo-bioinformatica-mysqlsrv",
                                         db="lszlh",
                                         passwd="619150")
    cursor = verbinding.cursor()
    query = "select max(Blast_ID), max(Actual_ID), max(Prot_id) from eiwitten join blast b on " \
            "eiwitten.Prot_id = b.Actual_ID join seq_read sr on b.Blast_ID = sr.Read_ID"
    cursor.execute(query)
    resultaat = cursor.fetchall()
    for item in resultaat:
        item = str(item)
        item2 = item.split(",")
        item3 = item2[0].split("(")
        blast_id = int(item3[1]) + 1
        actual_id = int(item2[1]) + 1
        item4 = item2[2].split(")")
        prot_id = int(item4[0]) + 1
    cursor.close()
    toevoegen_database(add, blast_id, actual_id, prot_id)


def toevoegen_database(add, blast_id, actual_id, prot_id):
    """ Deze functie opent de resultaten voor de databse van de blast. Daarna maakt hij verbinding met de database,
    en gaat dan voor elke regel in het bestand kijken of het de header, sequentie, eiwit, orgnaisme, accessiecode,
    score, e_value, querycover of percentage identitys is en wordt dan opgeslagen als een variabele. Als alles een
    waarde heeft wordt het toegevoegd in de database, eerst bij de seq_read, dan blast en dan eiwit tabel. Daarna
    worden de blast_id, actual_id en prot_id weer +1 gedaan.

    :param add: geeft aan of er resultaat in de database moet worden toegevoegd of niet
    :param blast_id: geeft de volgende blast_id mee
    :param actual_id: geeft de volgende actual_id mee
    :param prot_id: geeft de volgende prot_id meee
    :return: nieuwe resultaten in de datbase
    """
    bestand2 = open('resultaten_database.txt', 'r')
    verbinding = mysql.connector.connect(host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
                                         user="lszlh@hannl-hlo-bioinformatica-mysqlsrv",
                                         db="lszlh",
                                         passwd="619150")
    cursor = verbinding.cursor()
    header = ''
    sequentie = ''
    eiwit = ''
    organisme = ''
    accessiecode = ''
    score = 0
    e_value = 0.0
    querycover = 0.0
    percentageidentity = 0.0
    cursor = verbinding.cursor()
    if add is not None:
        count = -1
        for regel in bestand2:
            count += 1
            regel = regel.replace("\n", "")
            if count == 0:
                header = regel
            if count == 1:
                sequentie = regel
            if count == 2:
                blast = regel
            if regel == "*** Nieuw resultaat ***":
                if count == 4:
                    regel2 = regel.split(":")
                    regel3 = regel2[1].split("[")
                    eiwit = regel3[0]
                    regel4 = regel3[1].split("]")
                    organisme = regel4[0]
                if count == 5:
                    regel5 = regel.split(":")
                    accessiecode = regel5[1]
                if count == 6:
                    regel6 = regel.split(":")
                    score = int(regel6[1])
                if count == 7:
                    regel7 = regel.split(":")
                    e_value = float(regel7[1])
                if count == 8:
                    regel8 = regel.split(":")
                    querycover = float(regel8[1])
                if count == 9:
                    regel9 = regel.split(":")
                    percentageidentity = float(regel9[1])
                if count == 10:
                    query_seqread = "insert into seq_read (Read_ID, Read_type, Header, Sequentie)" \
                                    "values ({}, 1, '{}', '{}')".format(blast_id, header, sequentie)
                    cursor.execute(query_seqread)
                    verbinding.commit()
                    query_blast = "insert into blast (Blast_ID, Blast_type, Score, Query_cover, E_value, " \
                                  "Percent_ident, Accessiecode, Organisme, Taxonomie, Actual_ID)" \
                                  "values ({}, '{}', {}, {}, {}, {}, '{}', '{}', '-', {})".format(blast_id, blast,
                                                                                                  score,
                                                                                                  querycover, e_value,
                                                                                                  percentageidentity,
                                                                                                  accessiecode,
                                                                                                  organisme, actual_id)
                    cursor.execute(query_blast)
                    verbinding.commit()
                    query_eiwitten = "insert into eiwitten (Prot_id, Prot_naam, Prot_locatie, Bio_domein, " \
                                     "Bio_proces, Bio_functie)" \
                                     "values ({}, '{}', '-', '-', '-', '-')".format(prot_id, eiwit)
                    cursor.execute(query_eiwitten)
                    verbinding.commit()
                    count = -1
                    blast_id = blast_id + 1
                    actual_id = actual_id + 1
                    prot_id = prot_id + 1
    cursor.close()


def resultaten_database():
    """ Deze functie roep de sequentie en blasttype op, opent de XML file van de blast en een nieuw tesktbestand.
    Voor elke regel in het bestand worden eerst de enters weggehaald. Daarna als de regel start met @,
    wordt de header en sequentie in het bestand geschreven. Als de regel met Hit begint, wordt hit op True gezet en
    wordt  de query_lengte, beschrijving, accessiecode, score, E-value en wordt de query cover en de percentage identity
    berekent. Dit allemaal wordt in het bestand weggeschreven.

    :return: tesktbestand met resulaten voor de database
    """
    sequentie = request.args.get("seq")
    blast = request.args.get("blast_type")
    bestand = open("resultaat.xml", 'r')
    hit = False
    bestand_resultaten = open("resultaten_database.txt", 'w')
    for regel in bestand:
        regel = regel.replace("\n", "")
        if regel == "<Hit>" and sequentie is not None:
            hit = True
            bestand_resultaten.write("@Sequentie_gebruiker" + "\n")
            bestand_resultaten.write(sequentie + "\n")
            bestand_resultaten.write(blast + "\n")
        if "<BlastOutput_query-len>" in regel:
            regel = regel.split("<")
            split = regel[1].split(">")
            query_len = int(split[1])
        if hit is True:
            if "<Hit_def" in regel:
                # dit geeft aan waar een nieuw resultaat begint
                bestand_resultaten.write("*** Nieuw resultaat ***" + "\n")
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("Beschrijving: " + split[1] + "\n")
            if "<Hit_accession" in regel:
                # dit geeft aan wat de accessiecode is
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("Accessie code: " + split[1] + "\n")
            if "<Hsp_score>" in regel:
                # dit geeft de score mee van het resultaat
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("Score: " + split[1] + "\n")
            if "<Hsp_evalue>" in regel:
                # dit geeft de e-value mee
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("E-value: " + split[1] + "\n")
            if "<Hsp_query-from>" in regel:
                # dit geeft de query from mee om de query cover te bepalen
                regel = regel.split("<")
                split = regel[1].split(">")
                query_from = int(split[1])
            if "<Hsp_query-to>" in regel:
                # dit haalt de query to op en gaat daarna de query cover berekenen
                regel = regel.split("<")
                split = regel[1].split(">")
                query_to = int(split[1])
                query_cover = ((int(query_to) - int(query_from)) / int(query_len)) * 100
                bestand_resultaten.write("Query cover: " + str(query_cover) + "\n")
            if "<Hsp_identity>" in regel:
                # deze geeft de aantal identitys mee
                regel = regel.split("<")
                split = regel[1].split(">")
                hsp_identity = int(split[1])
            if "<Hsp_align-len>" in regel:
                # deze gaat het identity percentage berekenen
                regel = regel.split("<")
                split = regel[1].split(">")
                hsp_align_len = int(split[1])
                identity = (int(hsp_identity) / int(hsp_align_len)) * 100
                bestand_resultaten.write("Percentage Identity: " + str(identity) + "\n" + "\n")
                hit = False
    bestand_resultaten.close()


if __name__ == '__main__':
    app.run()
