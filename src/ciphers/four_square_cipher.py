import random

from ciphers.cipher import Cipher
from ciphers.objects import Settings
from ciphers.useful import filter as filteranp
from ciphers.useful import generate_deranged_alphabet as make_alphabet
from resources.useful import string_to_square_matrix as make_matrix
from resources.fitness import check_tetragrams as fitness_function
# from cipher import Cipher
# from objects import Settings
# from useful import filter as filteranp

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def search_grid(grid,target):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == target):
                return i, j
    raise IndexError(f"Target {target} not in grid {grid}")

def encode_from_grids(bigram:str, grids:list):
    grid_a,grid_b,grid_c,grid_d = grids

    # TAKE FIRST LETTER
    first = bigram[0]
    # GET X AND Y COORDS IN GRID_A
    first_y,first_x = search_grid(grid_a,first)

    # TAKE SECOND LETTER
    second = bigram[1]
    # GET X AND Y COORDS IN GRID_D
    second_y,second_x = search_grid(grid_d,second)

    # GET FIRST ENCODED USING FIRST LETTER'S Y AND SECOND LETTER'S X
    bigram_out_first = grid_b[first_y][second_x]
    
    # GET SECOND ENCODED USING SECOND LETTER'S Y AND FIRST LETTER'S X
    bigram_out_second = grid_c[second_y][first_x]

    return "".join([bigram_out_first,bigram_out_second])

def decode_from_grids(bigram:str, grids:list):
    grid_a,grid_b,grid_c,grid_d = grids

    # TAKE FIRST LETTER
    first = bigram[0]
    # GET X AND Y COORDS IN GRID_B
    first_y,first_x = search_grid(grid_b,first)
    # print(first,first_x,first_y)

    # TAKE SECOND LETTER
    second = bigram[1]
    # GET X AND Y COORDS IN GRID_C
    second_y,second_x = search_grid(grid_c,second)
    # print(second,second_x,second_y)

    # GET FIRST ENCODED USING FIRST LETTER'S Y AND SECOND LETTER'S X
    bigram_out_first = grid_a[first_y][second_x]
    # print(first_y,second_x)
    
    # GET SECOND ENCODED USING SECOND LETTER'S Y AND FIRST LETTER'S X
    bigram_out_second = grid_d[second_y][first_x]
    # print(second_y,first_x)

    return "".join([bigram_out_first,bigram_out_second])
    

class FourSquare(Cipher):
    def __init__(self, settings=Settings(ALPHABET, True, "a", 25, 25)):
        # do init stuff
        super().__init__(settings)

    def encode(self, plaintext:str, grids:list, settings:Settings=None):
        if not isinstance(settings, Settings):
            settings = self.settings
        if settings.tight:
            plaintext = filteranp(plaintext) # ALLOW FOR CUSTOMISATION

        plaintext_array = [plaintext[i:i+2] for i in range(0,len(plaintext),2)]
        ciphertext_array = []

        for bigram in plaintext_array:
           ciphertext_array.append(encode_from_grids(bigram,grids))

        ciphertext = "".join(ciphertext_array)

        return ciphertext

    def decode(self, ciphertext:str, grids:list, settings:Settings=None):
        if not isinstance(settings, Settings):
            settings = self.settings
        if settings.tight:
            ciphertext = filteranp(ciphertext) # ALLOW FOR CUSTOMISATION

        ciphertext_array = [ciphertext[i:i+2] for i in range(0,len(ciphertext),2)]
        plaintext_array = []

        for bigram in ciphertext_array:
           plaintext_array.append(decode_from_grids(bigram,grids))

        plaintext = "".join(plaintext_array)

        return plaintext
    
    def continuous_brute_force_decode(self,ciphertext:str,settings:Settings=None):
        if not isinstance(settings, Settings):
            settings = self.settings
        if settings.tight:
            ciphertext = filteranp(ciphertext) # ALLOW FOR CUSTOMISATION


        # all_possible_grids = generate_all_grids(5,settings.alphabet)
        # logging.debug("GENERATED ALL GRIDS")

        best_decoded_text = ""
        best_grids = None
        best_score = float('-inf')

        grid_a = make_matrix(settings.alphabet, 5) # DEFAULT ALPHABET
        grid_d = make_matrix(settings.alphabet, 5) # DEFAULT ALPHABET

        grid_b_keyword = "MAISIE"
        grid_c_keyword = "STYLES"
        grid_b = make_matrix(make_alphabet(grid_b_keyword,settings.alphabet), 5)
        grid_c = make_matrix(make_alphabet(grid_c_keyword,settings.alphabet), 5)

        best_grids = [grid_a,grid_b,grid_c,grid_d]

        i = 1
        j = 0
        while best_score < -10:
            # print("\033[F\033[K" + f"ATTEMPT {i}, {j} UNSUCCESSFUL")
            if j >= 150:
            # SWITCH AROUND CHARS [GRID C]
                new_grid_c = best_grids[2]
            # # for _ in range(5-math.floor(math.log(i, 10))): # SWAP DECREASING AMOUNTS AT A TIME
                for _ in range(1): # SWAP 1 AT A TIME
                    x1 = random.randint(0,4)
                    y1 = random.randint(0,4)
                    x2 = random.randint(0,4)
                    y2 = random.randint(0,4)
                    new_grid_c[y1][x1], new_grid_c[y2][x2] = new_grid_c[y2][x2], new_grid_c[y1][x1]
                grid_c = new_grid_c
            # RANDOMISE ONE CHAR OF FIRST TWO ROWS [GRID C]
            elif j < 150:
                first_five = [char for char in best_grids[2][0]]
                second_five = [char for char in best_grids[2][1]]
                first_ten_chars_c = first_five+second_five
                repeating = True
                while repeating:
                    index_char = None
                    to_replace = random.randint(0,9)
                    char = settings.alphabet[random.randint(0,len(settings.alphabet)-1)]
                    if char in first_ten_chars_c:
                        index_char = first_ten_chars_c.index(char)
                    if first_ten_chars_c[to_replace] == char:
                        pass
                    else:
                        if index_char and j >= 75:
                            first_ten_chars_c[index_char] = first_ten_chars_c[to_replace]
                        first_ten_chars_c[to_replace]  = char
                        repeating = False

                grid_c = make_matrix(make_alphabet("".join(first_ten_chars_c), settings.alphabet),5)

            current_grids = [grid_a, grid_b, grid_c, grid_d]
            decoded_text = self.decode(ciphertext, current_grids)
            current_score = fitness_function(decoded_text, "src/resources", "engcorptetlogfreqs.txt")

            i += 1
            if current_score > best_score:
                # logging.debug("BETTER SCORE")
                best_score = current_score
                best_decoded_text = decoded_text
                best_grids = current_grids

                yield (best_decoded_text, best_grids, best_score, i)
                # print()
                j = 0

            j += 1

            if i % 5 == 0:
                print(f"ITERATION {i}, UNSUCCESSFUL {j}")

            if j >= 300:
                # print("-"*10+"MAX ATTEMPTS EXCEEDED"+"-"*10)
                print(best_decoded_text)
                best_decoded_text = ""
                best_grids = None
                best_score = float('-inf')

                grid_a = make_matrix(settings.alphabet, 5) # DEFAULT ALPHABET
                grid_d = make_matrix(settings.alphabet, 5) # DEFAULT ALPHABET

                grid_b_keyword = "MAISIE"
                grid_c_keyword = "STYLES"
                grid_b = make_matrix(make_alphabet(grid_b_keyword,settings.alphabet), 5)
                grid_c = make_matrix(make_alphabet(grid_c_keyword,settings.alphabet), 5)

                best_grids = [grid_a,grid_b,grid_c,grid_d]
                i = 1
                j = 0

# cipher_obj = FourSquare()
# print(cipher_obj.decode("ENEAO TAQKD UQXNI IVBQZ RAXNI ILOQA XTMNQ AUWOH CPGHI CAQSC OGYHG NTTWU HPAPA RHHKM NNMGP PMLQA GHVQU PILOP SPLAU PWQKG GRFAV BEDRL RAIBA QAIDN RFQDD NUFUM OBAQU VIKEE HHMNQ AENEA QONTO VKGSB IHQPE NXATU MCOPK ZTAOT KPKHP OWHET VBYTW MSLID SBFAD SMDYT BPXTG MSQXN AWFAV BEDRL RASPP BGHFN PFQPX OXTLA MXAQL KNDZP ILNWA QSLGK OHVBM IPPTA QAKPY TVGMX AQQUH HXNQO KHQOP NEKXA KZNTQ VNLHH EMUHY HGNTT WUHPQ UQELS IDSBS GTIIH QPETA KWHNL WMCYV BKPKP WYSLW GDSWU FAWTW HSBVO TLENK ZNYWF PYHPN IIDWH SHNAX NVBIL NHRSS OKHQO QPLAS ZWWQE AMAKZ PAIHH SBOZK ZQFKK LACFX YDTFA SNPHS QOBSQ LAWMN NMOWC XTWGR TNBVB AQAKI QXNSB WBPHW GKKLA GMMLT NRTWY MANAW QKGVM WHXAS QKGXA KERAQ RSFVI MWNHU IIQWZ ENSUW ZENID SPRBQ GCMFA WPLAZ WAQAI HHSQP NAKMC OPHPM DQKFA UHSKX NVMBY FHAIU MOBAQ TGLBS LVBEI WFEAV ONBEM FHSBO ZVBIL NHRSS OKHQZ VBHHK CUWIK MDYTB PAEAD SQPBG HIDSP FAVBI IMXAQ UPTIY NRIXT SZSKS LVBSQ XTIKU QIQII UPVQX NSPRP WZADX OXTVB ILKPZ WRPQS FADSM AXTMB OPVBA IEMWB SHQGU NMILN DSVBS KVBSX CFTII BMRMI NWSLV BAIIK KNNNQ AHNRP QSQGT NNDOW VBAIW HETXT QFDSM BWFQM LAGPK GRTHH VBAII DOPPH EAGPM LQEXA SPFAV BAXRP QSQGU NSLHP XOSSS LKNIL KNSLH HELEN SPNNS OBYFH SCFAM NUGMD NEVII PMRSL GKOHQ ULTRA WFVQT ANSWU KPYTV GOWLA XTRAA KIIRP HYWHN BLSWM ONWXV BAXKG RSSGN DILWB PHGKO HOMWF LTVME MWBUW IKXOF EHNLN QOWHE MCPLA XATUH NIQNB EDWYQ OAQBY OWIKO QEIAK SLWHL ARDRT WHLTV BAQDT OQQNV LSLMA XTLKP SRHLN WGHKO HSIKK LAQFW OYSRK ASRSK PAIWZ OGYHG NTTWU HHXNQ AHHKM OPEIN SEAVB SIWYK YNAPK MLIZY TTZNS DTSBP OOHAX SRVBS KVZOW SLKPS GTIIH QPFAD SETII VBSIW YKYNA OROPF LQAKB QOIIE NSPOP MXMLQ KKZWO OHUMO BAQVZ RHHHK MFAVB AXRPQ SVBII LSMIO NQELT SPOWK PKATT BYHPN BLSWM QPLAS ZWWTT VBAQV BIDFS EAVBA QHPKQ FAWPL AKDUY AQLNU VRPQS ETSBV ANWAQ SLLAF AANNN WOSLN BVBMX MDXLI DMPTL QEWWN BVBAL QHHQI DSBET QEMXS LVBSK VBEIQ PIIWB MDQDV ONBFS EACFT IANSQ QHRMI ZWHET AKVIK DWMVI SKMIZ HDHWY QOAQQ YXOQA AQWOQ HAHCB QOIIW BPHTA QANBL SXTSP LAKDU YAQLN WOPBH PSGQO ISWBR AOZNS QABYP BALMI LNDSA WRPQS NBLSW MLAET WOOQH NMCOP VBILR HLNWZ FAIHQ BENSK FAVBI CSSSH RAWGQ GWMFA VBICS SAKTT OZSLK DXFQH UFWYT GIQWH CEWZW PLAQE AMAKC PPPEL KDVYG HXANE VBMQT LQEWW NBVBA XOPHQ VBSLM LVBYT TAIAK NIITN QKKGU CKZMF ADAIB PMIFE OPKPF BHBSS QGXNO TAKLL SHOGB PIZAI AIWYT GIQCF TIIPW BNDET MDFWS CKDVI IBHPS FSWSK VBMCQ HWHKK LANSS NAQMG WQIZH HKFRA NBRPU TIQTB OPLTW YIQVB ACNHA NUCID SBOFS LFNXN QRXTM DHPSL VBSKG WIKHH XAWYR PWAID LTWML AQIQE EAQYH YUWMI PKIIS PLASF RBKDT TNAQR WZTAQ AVBMC OPLTW UFAAN ELQAI QGBRA SPONS LSQIL TNMFS CYTTA SFWQW HXTQF DSKPB YIIVB ICRPX ALLEI AQIIX NXTMN QAXAS COZVB ALQNY HSQRP TNVAX TADVB SKCFL LMXAQ CHRAH HVBEL IKUWH HKYUW IKWHO PHPKX WHTNL LVBAL QHKIP AIQLA FAIPE LQZWP LAXTI DSPLA XTYTV GQHRI OPXPQ ZWWWH XTNII SSCWP OHBPU QOQHP MLQAH HKPFN OKMIL NKKLA QIQEE AXKHN FIDNW OASQE VZSLV BSKVB SLMLV BYTTA NAIAK NIITN QAWZP AIIQP KZOZF AMNRI AKIIT HZNEL POWHR SQGWT ADAES LEDAK TBWFQ MLAAM RBIIQ EAMAK YHSSE NWFHS RPVMS QLACN WFRIS LVBSC NVIQW BFTWB PHQUL SAKNB SBVAN WAQZW IKMDR SCESK SLEMV HOWKP SBIHQ PXAAI CYXAW HXTDS MDVBM CISWP FAWPL ASFRB YTTAK DUYAQ CPQNP POWRP QSRHI IIDHH DSWOG BSKKH QOFAU HGBKO QERZV BSCQO XMENW MOHMX FNQUO QHHXN TYWYI IMNQA WGLHX TNLXT MNNAQ KAQNA WBDSW OTTXN KUGWR PQSUP CPRPQ AAQQY RAOMW FLTVM MARFS EHFKD UYNWA QQGUT BPUCL TWOHH KMFAV BAIGB KOFAD SETII HHCDN RSLWG RTKGC YQOLA ENSKK ZOQEI AKSLI DQPSQ FAVPE LRTSP QBRFQ EMAXN KZNTQ AKZSB WBQOL ASYQA HHKFK KLASF RBAKT TOZHH FYOPK PWHET SBVAN WAQSL HNAKM CTIQR OQEIA KSLSK TTFHN BMXKN IIEAQ ERZHH GFUMO BAQWO QPLAS FRBXA NDAQV ZRHHH KMFAW PKZUV RPQSM AWOII RPHYV ZSSOW NWAQK ZUOEI WQSKK HQOFA VBAXR PQSLS MIONQ ELTSP PPTNQ ASHBF GKOHV BELRS SOKHN AKKAQ RMIZR LVMTL SBOZI DSBRM WOSSQ YVBHH WBOZV BSKGH GBKOE TKDVT SLWHR QMFHP KOLAM XKNII EAFBL ASBIH QPAEX TAIUM OBAQT AVOII XNSPO WKPKA TTBYH PNBLS TTQAW HNTHH TNHHV BILNH RSSOK HNAWP LANTQ GWYSB IHQPV BHHKC CFTIE NDSUT ILEDA SRSNB XOIZI SVPID SWSQL AXTFN NTKDU YAQSG POQCT TSZWO IDANN SEZNT FHAQE MVHQP ADUQE NXTTT QAWGW HQUQE AMAKC BFADS QDDSS BTNQA MAXTM BOPKP KDWMK ZWMCW MLVMI DSBFA DSVBR PHYVB AKMNS FWQKG CYSGT IENPO UQSCV PLKXP XTQYV OYTVF SLRNV GQPQD DSKPI KKNNN QAIKV BMIGN TTWYI DTTVB AQVBI DVBMI ACMDO WRAWY FASHN GCHRA YTCPR HWFXN SOKPH BMRIQ RLQOV BMIIK VPHWD NAKVO QDYFZ PEINS SZOZM LIZID ENDSW USFRB HHVBI LNHRS SOKHO VKPFA KDUYA QCPLA OPGBH HMDWZ LLEIH HASQH KLEIP PKPOP CBQOL ASZWW CYVBI KNTND ROOTA QNBQU FSCDU QKPAX OPHQP HIEKN ENPOL ANEET KZQAV BAXQH EHIDM IQEOZ HHQUW FOHUV FAXND SUFHP UVAKR AENSZ ENWOQ NOWKP KOLAS FRBWZ PZAQQ EAMAK ZWLAQ ZADKF RAQUQ EAMAK ZWFHO KAISE PZKNE NQZVP SGNDI LWBPH HHTNS OHHQU CYNDH BMRAI SSMLU MIDLT RTQOT ZOPVB ALQHH QWHET LKNDZ PEQQZ XNSBQ OLAEN QIWZW HWUID MNKKA QIKWC TNMFS CQOAQ YSQSM CHHSL SUVBI QTNXP XNNBQ EQYTN WBPHW OONIQ NHSPL AYNXT WHRHX TSZRP WONHP NFLYT YBOPM XAQID MBAKW HNWMD TLMFS QOPSQ UQQON NFSQY QRVBS KSHIQ QGTWM DXLVB AIVBA QSCTA NTXYS QKDWM LANTQ AVBIL NHRSS OOPUV KGCEM COPVB AICYN DSKRS IKVBM RSLAI PHWOT TXNIB OWRMI ZVBSX MAXTK DVMVL FANTH FFBHN IIVNN HRSSO KHQOL AOQPN ELIPV ZRPQS ETXOI MTNQO FNNSQ AHBMR ACFWI IHHWO XMSOK HPOVB SKQFR ABPKG TIANE QXASP RNWOA SQEVZ SKXMW OLKQA ENSBM AXNSP QPLAS LVLSK KHQGF DGNTT WYIDW OMLIZ AQTAQ ASFRB SYQAA QUVIL IDQGV NPHUP NHVBM CWQUQ ALWQD TMANA THMLW OUPCP PPFAR LKP",[
#     [["A","B","C","D","E"],
#      ["F","G","H","I","K"],
#      ["L","M","N","O","P"],
#      ["Q","R","S","T","U"],
#      ["V","W","X","Y","Z"]],
#     [["M","A","I","S","E"],
#      ["F","G","H","K","L"],
#      ["N","O","P","Q","R"],
#      ["T","U","V","W","X"],
#      ["Y","Z","B","C","D"]],
#     [["S","T","A","N","L"],
#      ["E","Y","Z","B","C"],
#      ["D","F","G","H","I"],
#      ["K","M","O","P","Q"],
#      ["R","U","V","W","X"]],
#     [["A","B","C","D","E"],
#      ["F","G","H","I","K"],
#      ["L","M","N","O","P"],
#      ["Q","R","S","T","U"],
#      ["V","W","X","Y","Z"]]
#      ]))

if __name__ == "__main__":
    cipher_obj = FourSquare()
    # print(cipher_obj.encode("ONJWEFOJENFOWNEFOJ"))
    