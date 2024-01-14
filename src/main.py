from flask import Flask,render_template,request,send_from_directory,jsonify

from ciphers.objects import Settings
from ciphers.caesar_cipher import Caesar
from ciphers.shifting_caesar import ShiftingCaesar
from ciphers.monoalphabetic_substitution_cipher import MonoalphabeticSubstitution
from resources.analysis_functions import index_of_coincidence
from ciphers.four_square_cipher import FourSquare
from resources.useful import string_to_square_matrix as make_matrix

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ciphers/caesar-cipher', methods=['GET', 'POST'])
def caesar_cipher():
    result = ""
    if request.method == 'POST':
        
        text = request.form['text']
        shift = int(request.form['shift'])
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',26), 
                            max_length=request.form.get('max_length',26)
                            )
        
        cipher_obj = Caesar(settings)

        if operation == 'encode':
            result = cipher_obj.encode(text,shift)
        elif operation == 'decode':
            result = cipher_obj.decode(text,shift)
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/caesar_cipher.html', result=result)

@app.route('/ciphers/shifting-caesar-cipher', methods=['GET', 'POST'])
def shifting_caesar_cipher():
    result = ""
    if request.method == 'POST':
        
        text = request.form['text']
        shift_length = int(request.form['shift_length'])
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',26), 
                            max_length=request.form.get('max_length',26)
                            )
        
        cipher_obj = ShiftingCaesar(settings)

        if operation == 'encode':
            result = cipher_obj.encode(text,shift_length, settings=settings)
        elif operation == 'decode':
            result = cipher_obj.decode(text,shift_length, settings=settings)
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/shifting_caesar_cipher.html', result=result)

@app.route('/ciphers/monoalphabetic-substitution-cipher', methods=['GET', 'POST'])
def monoalphabetic_substitution_cipher():
    result = ""
    if request.method == 'POST':
        
        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',26), 
                            max_length=request.form.get('max_length',26)
                            )

        cipher_obj = MonoalphabeticSubstitution(settings)

        text = request.form['text']
        key_alphabet = request.form.get('key',cipher_obj.invert_alphabet(request.form.get('inverse-key')))
        inverse_key = request.form.get('inverse-key',cipher_obj.invert_alphabet(request.form.get('key')))
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        if operation == 'encode':
            result = cipher_obj.encode(text,key_alphabet, settings=settings)
        elif operation == 'decode':
            result = cipher_obj.decode(text,key_alphabet, settings=settings, inverse_alphabet=inverse_key)
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/monoalphabetic_substitution_cipher.html', result=result)

@app.route('/ciphers/four-square-cipher', methods=['GET', 'POST'])
def four_square_cipher():
    result = ""
    if request.method == 'POST':
        
        text = request.form['text']
        grids = [make_matrix(request.form['grid_a'],5),make_matrix(request.form['grid_b'],5),make_matrix(request.form['grid_c'],5),make_matrix(request.form['grid_d'],5)]
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',25), 
                            max_length=request.form.get('max_length',25)
                            )
        
        cipher_obj = FourSquare(settings)

        if operation == 'encode':
            result = cipher_obj.encode(text,grids)
        elif operation == 'decode':
            result = cipher_obj.decode(text,grids)
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/four_square_cipher.html', result=result)

@app.route('/ciphers/four-square-cipher/brute-force', methods = ['GET', 'POST'])
def brute_force_four_square():
    try:
        best_decoded_text,best_grids,best_score,i = next(four_square_hill_climb)
        return jsonify(best_decoded_text,best_grids,best_score,i)
        # return jsonify(next(four_square_hill_climb))
    except StopIteration:
        return ""
    except ValueError:
        return ""

@app.route('/tools/corpus-management', methods=['GET', 'POST'])
def corpus_management():
    result = ""
    if request.method == "POST":
        text = request.form['text']
        corpus = request.form['corpus']
        operation = request.form['operation']

        match operation:

            case "ioc":
                pass

            case "freq_analysis":
                pass


    return render_template('/tools/corpus_management.html',result=result)

@app.route('/tools/index-of-coincidence', methods=['GET', 'POST'])
def index_of_coincidence():
    result = ""
    if request.method == 'POST':
        
        settings = Settings(alphabet=request.form.get('alphabet','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                            tight=tight_T_F,
                            alpha_numeric_punctuation=request.form.get('anp',"a"), 
                            min_length=request.form.get('min_length',26), 
                            max_length=request.form.get('max_length',26)
                            )

        cipher_obj = MonoalphabeticSubstitution(settings)

        text = request.form['text']
        key_alphabet = request.form.get('key',cipher_obj.invert_alphabet(request.form.get('inverse-key')))
        inverse_key = request.form.get('inverse-key',cipher_obj.invert_alphabet(request.form.get('key')))
        operation = request.form['operation']
        tight_Y_N = request.form.get('tight', "Y")
        if tight_Y_N == "Y":
            tight_T_F = True
        elif tight_Y_N == "N":
            tight_T_F = False
        else:
            raise ValueError("INVALID TIGHTNESS")

        if operation == 'encode':
            result = cipher_obj.encode(text,key_alphabet, settings=settings)
        elif operation == 'decode':
            result = cipher_obj.decode(text,key_alphabet, settings=settings, inverse_alphabet=inverse_key)
        elif operation == 'brute_decode':
            result = ""
        else:
            raise ValueError('INVALID OPERATION')
        
    return render_template('/ciphers/monoalphabetic_substitution_cipher.html', result=result)

@app.route('/static/js/<path:filename>')
def js(filename):
    return send_from_directory('static/js', filename)

@app.route('/static/css/<path:filename>')
def css(filename):
    return send_from_directory('static/css', filename)

@app.route('/assets/images/<path:filename>')
def image(filename):
    return send_from_directory('static/images', filename)

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    cipher_obj = FourSquare()
    four_square_hill_climb = cipher_obj.continuous_brute_force_decode("ENEAO TAQKD UQXNI IVBQZ RAXNI ILOQA XTMNQ AUWOH CPGHI CAQSC OGYHG NTTWU HPAPA RHHKM NNMGP PMLQA GHVQU PILOP SPLAU PWQKG GRFAV BEDRL RAIBA QAIDN RFQDD NUFUM OBAQU VIKEE HHMNQ AENEA QONTO VKGSB IHQPE NXATU MCOPK ZTAOT KPKHP OWHET VBYTW MSLID SBFAD SMDYT BPXTG MSQXN AWFAV BEDRL RASPP BGHFN PFQPX OXTLA MXAQL KNDZP ILNWA QSLGK OHVBM IPPTA QAKPY TVGMX AQQUH HXNQO KHQOP NEKXA KZNTQ VNLHH EMUHY HGNTT WUHPQ UQELS IDSBS GTIIH QPETA KWHNL WMCYV BKPKP WYSLW GDSWU FAWTW HSBVO TLENK ZNYWF PYHPN IIDWH SHNAX NVBIL NHRSS OKHQO QPLAS ZWWQE AMAKZ PAIHH SBOZK ZQFKK LACFX YDTFA SNPHS QOBSQ LAWMN NMOWC XTWGR TNBVB AQAKI QXNSB WBPHW GKKLA GMMLT NRTWY MANAW QKGVM WHXAS QKGXA KERAQ RSFVI MWNHU IIQWZ ENSUW ZENID SPRBQ GCMFA WPLAZ WAQAI HHSQP NAKMC OPHPM DQKFA UHSKX NVMBY FHAIU MOBAQ TGLBS LVBEI WFEAV ONBEM FHSBO ZVBIL NHRSS OKHQZ VBHHK CUWIK MDYTB PAEAD SQPBG HIDSP FAVBI IMXAQ UPTIY NRIXT SZSKS LVBSQ XTIKU QIQII UPVQX NSPRP WZADX OXTVB ILKPZ WRPQS FADSM AXTMB OPVBA IEMWB SHQGU NMILN DSVBS KVBSX CFTII BMRMI NWSLV BAIIK KNNNQ AHNRP QSQGT NNDOW VBAIW HETXT QFDSM BWFQM LAGPK GRTHH VBAII DOPPH EAGPM LQEXA SPFAV BAXRP QSQGU NSLHP XOSSS LKNIL KNSLH HELEN SPNNS OBYFH SCFAM NUGMD NEVII PMRSL GKOHQ ULTRA WFVQT ANSWU KPYTV GOWLA XTRAA KIIRP HYWHN BLSWM ONWXV BAXKG RSSGN DILWB PHGKO HOMWF LTVME MWBUW IKXOF EHNLN QOWHE MCPLA XATUH NIQNB EDWYQ OAQBY OWIKO QEIAK SLWHL ARDRT WHLTV BAQDT OQQNV LSLMA XTLKP SRHLN WGHKO HSIKK LAQFW OYSRK ASRSK PAIWZ OGYHG NTTWU HHXNQ AHHKM OPEIN SEAVB SIWYK YNAPK MLIZY TTZNS DTSBP OOHAX SRVBS KVZOW SLKPS GTIIH QPFAD SETII VBSIW YKYNA OROPF LQAKB QOIIE NSPOP MXMLQ KKZWO OHUMO BAQVZ RHHHK MFAVB AXRPQ SVBII LSMIO NQELT SPOWK PKATT BYHPN BLSWM QPLAS ZWWTT VBAQV BIDFS EAVBA QHPKQ FAWPL AKDUY AQLNU VRPQS ETSBV ANWAQ SLLAF AANNN WOSLN BVBMX MDXLI DMPTL QEWWN BVBAL QHHQI DSBET QEMXS LVBSK VBEIQ PIIWB MDQDV ONBFS EACFT IANSQ QHRMI ZWHET AKVIK DWMVI SKMIZ HDHWY QOAQQ YXOQA AQWOQ HAHCB QOIIW BPHTA QANBL SXTSP LAKDU YAQLN WOPBH PSGQO ISWBR AOZNS QABYP BALMI LNDSA WRPQS NBLSW MLAET WOOQH NMCOP VBILR HLNWZ FAIHQ BENSK FAVBI CSSSH RAWGQ GWMFA VBICS SAKTT OZSLK DXFQH UFWYT GIQWH CEWZW PLAQE AMAKC PPPEL KDVYG HXANE VBMQT LQEWW NBVBA XOPHQ VBSLM LVBYT TAIAK NIITN QKKGU CKZMF ADAIB PMIFE OPKPF BHBSS QGXNO TAKLL SHOGB PIZAI AIWYT GIQCF TIIPW BNDET MDFWS CKDVI IBHPS FSWSK VBMCQ HWHKK LANSS NAQMG WQIZH HKFRA NBRPU TIQTB OPLTW YIQVB ACNHA NUCID SBOFS LFNXN QRXTM DHPSL VBSKG WIKHH XAWYR PWAID LTWML AQIQE EAQYH YUWMI PKIIS PLASF RBKDT TNAQR WZTAQ AVBMC OPLTW UFAAN ELQAI QGBRA SPONS LSQIL TNMFS CYTTA SFWQW HXTQF DSKPB YIIVB ICRPX ALLEI AQIIX NXTMN QAXAS COZVB ALQNY HSQRP TNVAX TADVB SKCFL LMXAQ CHRAH HVBEL IKUWH HKYUW IKWHO PHPKX WHTNL LVBAL QHKIP AIQLA FAIPE LQZWP LAXTI DSPLA XTYTV GQHRI OPXPQ ZWWWH XTNII SSCWP OHBPU QOQHP MLQAH HKPFN OKMIL NKKLA QIQEE AXKHN FIDNW OASQE VZSLV BSKVB SLMLV BYTTA NAIAK NIITN QAWZP AIIQP KZOZF AMNRI AKIIT HZNEL POWHR SQGWT ADAES LEDAK TBWFQ MLAAM RBIIQ EAMAK YHSSE NWFHS RPVMS QLACN WFRIS LVBSC NVIQW BFTWB PHQUL SAKNB SBVAN WAQZW IKMDR SCESK SLEMV HOWKP SBIHQ PXAAI CYXAW HXTDS MDVBM CISWP FAWPL ASFRB YTTAK DUYAQ CPQNP POWRP QSRHI IIDHH DSWOG BSKKH QOFAU HGBKO QERZV BSCQO XMENW MOHMX FNQUO QHHXN TYWYI IMNQA WGLHX TNLXT MNNAQ KAQNA WBDSW OTTXN KUGWR PQSUP CPRPQ AAQQY RAOMW FLTVM MARFS EHFKD UYNWA QQGUT BPUCL TWOHH KMFAV BAIGB KOFAD SETII HHCDN RSLWG RTKGC YQOLA ENSKK ZOQEI AKSLI DQPSQ FAVPE LRTSP QBRFQ EMAXN KZNTQ AKZSB WBQOL ASYQA HHKFK KLASF RBAKT TOZHH FYOPK PWHET SBVAN WAQSL HNAKM CTIQR OQEIA KSLSK TTFHN BMXKN IIEAQ ERZHH GFUMO BAQWO QPLAS FRBXA NDAQV ZRHHH KMFAW PKZUV RPQSM AWOII RPHYV ZSSOW NWAQK ZUOEI WQSKK HQOFA VBAXR PQSLS MIONQ ELTSP PPTNQ ASHBF GKOHV BELRS SOKHN AKKAQ RMIZR LVMTL SBOZI DSBRM WOSSQ YVBHH WBOZV BSKGH GBKOE TKDVT SLWHR QMFHP KOLAM XKNII EAFBL ASBIH QPAEX TAIUM OBAQT AVOII XNSPO WKPKA TTBYH PNBLS TTQAW HNTHH TNHHV BILNH RSSOK HNAWP LANTQ GWYSB IHQPV BHHKC CFTIE NDSUT ILEDA SRSNB XOIZI SVPID SWSQL AXTFN NTKDU YAQSG POQCT TSZWO IDANN SEZNT FHAQE MVHQP ADUQE NXTTT QAWGW HQUQE AMAKC BFADS QDDSS BTNQA MAXTM BOPKP KDWMK ZWMCW MLVMI DSBFA DSVBR PHYVB AKMNS FWQKG CYSGT IENPO UQSCV PLKXP XTQYV OYTVF SLRNV GQPQD DSKPI KKNNN QAIKV BMIGN TTWYI DTTVB AQVBI DVBMI ACMDO WRAWY FASHN GCHRA YTCPR HWFXN SOKPH BMRIQ RLQOV BMIIK VPHWD NAKVO QDYFZ PEINS SZOZM LIZID ENDSW USFRB HHVBI LNHRS SOKHO VKPFA KDUYA QCPLA OPGBH HMDWZ LLEIH HASQH KLEIP PKPOP CBQOL ASZWW CYVBI KNTND ROOTA QNBQU FSCDU QKPAX OPHQP HIEKN ENPOL ANEET KZQAV BAXQH EHIDM IQEOZ HHQUW FOHUV FAXND SUFHP UVAKR AENSZ ENWOQ NOWKP KOLAS FRBWZ PZAQQ EAMAK ZWLAQ ZADKF RAQUQ EAMAK ZWFHO KAISE PZKNE NQZVP SGNDI LWBPH HHTNS OHHQU CYNDH BMRAI SSMLU MIDLT RTQOT ZOPVB ALQHH QWHET LKNDZ PEQQZ XNSBQ OLAEN QIWZW HWUID MNKKA QIKWC TNMFS CQOAQ YSQSM CHHSL SUVBI QTNXP XNNBQ EQYTN WBPHW OONIQ NHSPL AYNXT WHRHX TSZRP WONHP NFLYT YBOPM XAQID MBAKW HNWMD TLMFS QOPSQ UQQON NFSQY QRVBS KSHIQ QGTWM DXLVB AIVBA QSCTA NTXYS QKDWM LANTQ AVBIL NHRSS OOPUV KGCEM COPVB AICYN DSKRS IKVBM RSLAI PHWOT TXNIB OWRMI ZVBSX MAXTK DVMVL FANTH FFBHN IIVNN HRSSO KHQOL AOQPN ELIPV ZRPQS ETXOI MTNQO FNNSQ AHBMR ACFWI IHHWO XMSOK HPOVB SKQFR ABPKG TIANE QXASP RNWOA SQEVZ SKXMW OLKQA ENSBM AXNSP QPLAS LVLSK KHQGF DGNTT WYIDW OMLIZ AQTAQ ASFRB SYQAA QUVIL IDQGV NPHUP NHVBM CWQUQ ALWQD TMANA THMLW OUPCP PPFAR LKP")
    app.run(debug=True, port=5001)    