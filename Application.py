from flask import Flask, render_template, request
import mysql.connector
import re
from Bio.Blast import NCBIWWW, NCBIXML

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def home():
    try:
        return render_template('Database_page2.html')
    except:
        return render_template('Database_page2.html')


@app.route('/results', methods=['get', 'post'])
def results_filters():
    """ Deze functie maakt eerst 5 lijsten aan met waardes die nodig zijn voor de querys. Daarna wordt er een lege
    lijst aangemaakt: resultaat_kolommen en resultaat_where. Daarna wordt voor elk item in de lijst gekeken of het
    een waarde heeft gekregen, zoja dan wordt de value meegegeven in de lijst resultaat_kolommen. Daarna wordt er voor
    elk item in de andere lijst gekeken of deze ook waardes hebben gekregen, zoja dan wordt de value meegegeven in de
    lijst resultaat_where. Als deze lijst leeg is, wordt er in de zin voor de query nog een where toegevoegd, is dat al
    gebeurt dan gebeurt het niet nog een keer. Dan wordt er de functie result_querys aangeroepen met de lijsten
    lijst_kolommen, resultaat_kolommen, resultaat_where. De functie returnt het resultaat. Als de lengte van de lijst
    resultaat_kolommen 0 is, dan wordt de html pagina result gereturnd met resultaat en lijst_kolommen. Is de lengte van
    de lijst groter als 0, dan wordt de html pagina result gereturnd met resultaat en resultaat_kolommen.
    input: waardes checkboxes
    output: return html pagina result, resultaat en resultaat_kolommen of lijst_kolommen
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
        cursor.execute(query)
        resultaat = cursor.fetchall()
    cursor.close()
    verbinding.close()
    return resultaat


@app.route('/organism')
def organisms():
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
    """" Deze functie gaat controleren of de opgegeven sequentie een DNA, RNA of eiwit sequentie is. Als de sequentie
    DNA is, wordt de bijbehordende RNA en eiwit sequentie gegeven, is de sequentie een eiwit. Wordt het organisme
    waar de sequentie het meest op lijkt getoond. Als de sequentie geen DNA, RNA of eiwit is wordt het aangegeven
    met een bericht dat het geen van beide is. Dit allemaal wordt weergegeven op een HTML pagina
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
    # if add is None:
    #     resultaten_database()
    # if add is not None:
    #     adding(add)
    return render_template('BLAST.html', sequentie=sequentie, resultaat=resultaat, titel=titel)


def resultaat_beschrijving(dna, rna, eiwit, anders):
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
    if dna is True:
        sequentie = request.args.get("seq")
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
    titel = ''
    blast_resultaat = []
    bestand = open("Resultaat.xml", "w")
    result_handle = NCBIWWW.qblast("blastx", "nr", sequentie)
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
    toevoegen_database(add)


def toevoegen_database(add):
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
                bestand_resultaten.write("*** Nieuw resultaat ***" + "\n")
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("Beschrijving: " + split[1] + "\n")
            if "<Hit_accession" in regel:
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("Accessie code: " + split[1] + "\n")
            if "<Hsp_score>" in regel:
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("Score: " + split[1] + "\n")
            if "<Hsp_evalue>" in regel:
                regel = regel.split("<")
                split = regel[1].split(">")
                bestand_resultaten.write("E-value: " + split[1] + "\n")
            if "<Hsp_query-from>" in regel:
                regel = regel.split("<")
                split = regel[1].split(">")
                query_from = int(split[1])
            if "<Hsp_query-to>" in regel:
                regel = regel.split("<")
                split = regel[1].split(">")
                query_to = int(split[1])
                query_cover = ((int(query_to) - int(query_from)) / int(query_len)) * 100
                bestand_resultaten.write("Query cover: " + str(query_cover) + "\n")
            if "<Hsp_identity>" in regel:
                regel = regel.split("<")
                split = regel[1].split(">")
                hsp_identity = int(split[1])
            if "<Hsp_align-len>" in regel:
                regel = regel.split("<")
                split = regel[1].split(">")
                hsp_align_len = int(split[1])
                identity = (int(hsp_identity) / int(hsp_align_len)) * 100
                bestand_resultaten.write("Percentage Identity: " + str(identity) + "\n" + "\n")
                hit = False
    bestand_resultaten.close()


if __name__ == '__main__':
    app.run()
