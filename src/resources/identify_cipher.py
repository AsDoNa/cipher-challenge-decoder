from src.resources.analysis_functions import index_of_coincidence
from src.resources.monogram_frequencies import load_monogram_count, count_monograms
from src.resources.fitness import check_monograms_angle_vectors
# from resources.chi_squared import chi_squared

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_mono_sub_cipher(text:str):
    # Check index of coincidence close to English 1.7±0.15
    text_ioc = index_of_coincidence(text,n=1, alphabet=ALPHABET, include_spaces=False)
    if abs(abs(text_ioc) - 1.75) > 0.15:
        print(text_ioc)
        return False
    else:
        # Check monogram fitness is low (cos(angle between vectors) < 0.85?)
        if check_monograms_angle_vectors(text,"src/resources","engcorpmonofreqs.txt") < 0.85:
            return True
        else:
            return False
        
if __name__ == '__main__':
    print(is_mono_sub_cipher("AREIR JKZVJ JJKPY RJVZL JKEAZ VKKUE KVNEJ LBGCB MVBGR ADPPC LIGYE VZKUE KNRNC LYASV BAEBP KUVBT CSBCK RVBKU RMCYL ZRKUE KPCLJ RBKZR PCLEI RIVTU KKUEK VKUEJ JCZRM EYLRE JEJFR GVEYR AVKVC BCSFC RJNCI XDLKV GCLYA BCKJR REBPK UVBTI RZEIX EDYRE DCLKV KKUEK ZVTUK ROFYE VBKUR FIRJR BGRCI KURAR EKUCS KURPC LBTZE BPCLS CLBAV BKURY VDIEI PVKVJ ESVBR JFRGV ZRBEB AVKNE JNVKU JCZRI RYLGK EBGRK UEKVE KKEGX RAKUR DVBAV BTEJV AVABC KROFR GKKCS VBAEB PKUVB TIRZE IXEDY RKURI RVBPC LGEBV ZETVB RZPJL IFIVJ RKURB KCAVJ GCMRI KUREK KEGUR ABCKR GYREI YPNIV KKRBV BEGVF URIEB AGEIR SLYYP GCBGR EYRAD RKNRR BKURY REKUR IEBAK URRBA DCEIA JRMRB KURBV EJJLZ RAKUV JKCDR EFLDY VJURI JKIVG XKCFI CZCKR KURRA VKVCB TVMRB KURFI CZVBR BGRCS RBGIP FKVCB VBKUR KEYRD LKGCB JLYKV BTNVK UZPSI VRBAJ VBKUR DCCXK IEARB CBRCS KURZU EAURE IACSJ LGUEG CBGRV KEBAV GCLYA BCKSV BAEBP IRGCI ACSEB EAMRI KVJVB TGEZF EVTBI RSRII VBTKC JLGUE GLIVC JVKPE KKUVJ FCVBK VSRYK VJUCL YAEKY REJKE KKRZF KKCAR GVFUR IKURZ RJJET REBAH LVGXY PAVJG CMRIR AKUEK KUREL KUCIU EALJR AKURM RIPZV YAGCB MRBKV CBCSE JUVSK GVFUR IGYRE IYPVB KRBAR AKCDR DICXR BKURS VIJKY VBRIR EAIRG RBKRM RBKJU EMRZE ARVKG YREIR IKUEB RMRIK CZRKU EKVEZ VBZCI KEYAE BTRIE BAKUR IRJKG CBKEV BRAZL GUKCE YEIZZ RRJFR GVEYY PKURI EKURI GYLZJ PIRMR IJREG ICJKV GNUVG UIREA ZLIAR IKUCL TUSCI KURYC BTRJK KVZRV EJJLZ RAVKK CIREA IRAIL ZNUVG UGELJ RAZRZ LGUGC BSLJV CBNUR KURIC IBCKK UVJGC BGREY RAZRJ JETRF CVBKJ KCKUR LBSCI KLBEK RAREK UCSPC LIVBK RIYCF RIVJB CKEFF EIRBK KCZRD LKVKU VBXPC LEIRI VTUKK UEKVK JFIRJ RBGRJ UCLYA DRJLS SVGVR BKKCR BGCLI ETRKU RFCYV GRKCI RCFRB KURGE JRVNV YYSCI NEIAE GCFPC SKUVJ YRKKR IKCTR KURIN VKUZP SVBAV BTJKC ZPSIV RBAKC ZUEIF RIEJG UVRSC SFCYV GRURJ UCLYA UEMRK URFCN RIEBA VBSYL RBGRK CACJC NVKUZ PDRJK NVJUR JZELI VGRAI ZELIV GRNUV KRZA"))