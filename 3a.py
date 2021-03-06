import operator

text1 = """
MWJJT WDEVM WJBXF XWCDG VBGKF JLGLM FHEKK TDEXV WLFAN LXLMX DZXMW PFAFR NDLGN DJWPF BQMTL MFTCX RMLAF XDLFJ FKLFE XDYWC FBXWW DECWJ LXDWK KMFLG BENKX DLMFM XEEFD CFKKW RFXKF DLBWK LQFFZ YWCFB XWMWE AFFDQ GJZXD RGDKX RDWBJ FVGRD XLXGD WLETD WCXSW LOXJK LXQWK HNUUB FEATL MXKWK XVGNB EDLKF FMGQX LJFBW LFELG QFWHG DXKFE RJWPX LTQWP FKANL LMFDX LGGZW BGGZW LMFJA GGZKM FBOWD EXLAF RWDLG CWZFK FDKFX LQWKO NBBGO AGGZK GDRFD FJWBJ FBWLX PXLTA BWVZM GBFKW DEDFN LJGDK LWJKY WCFBX WQWKD GLQGJ ZXDRG DRJWP XLTQW PFKAN LGDRJ WPXLW LXGDW BQWPF KXVWD KFFMG QLMFO XFBEW RFDLK QGNBE MWPFR GLVGD ONKFE XDLMF NKLMF TKGCF LXCFK NKFAG LMDWC FKOGJ LMFKW CFLMX DRANL LMFTJ FWBBT WJFEX OOFJF DLRJW PXLTQ WPFKW JFWKF XKCGB GRXVW BHMFD GCFDG DWKTG NWBJF WETOX RNJFE GNLRJ WPXLW LXGDW BQWPF KWJFF DLXJF BTEXO OFJFD LFXDK LFXDH JFEXV LFELM FCWMN DEJFE TFWJK WRGWD ELMFT QFJFE FLFVL FEATL MFBXR GLFWC BWKLT FWJLM FKXRD WBKWJ FRXPF DGOOA TLMXD RKBXZ FAXDW JTABW VZMGB FKTKL FCKWD EWJFX DVJFE XABTO WXDLL MFTFW KXBTR FLKQW CHFEA TBGVW BDGXK FXLQW KWDWC WUXDR OFWLE FLFVL XDRLM FCWDE YWCFB XWQWK HWJLG OLMWL LGWEE LGGNJ VGDON KXGDK MFQWK XDLMF LFWCJ FKHGD KXABF OGJEF KXRDX DRLMF KFWJV MWBRG JXLMC KWDEL MFDGX KFOXB LFJKN KFELG KHGLL MFKXR DWBGO WRWBW VLXVF PFDLW RWXDK LLMFD GXKFG OKFXK CGBGR XVWBW VLXPX LTKGK MFEXE ZDGQK GCFLM XDRWA GNLRJ WPXLT QWPFK LGGXK LXBBE GDLZD GQFSW VLBTM GQETD WCXSQ FJFNK XDRMF JFSHF JLXKF GJQMW LLMFH EKKTD EXVWL FWJFG JEGXO TGNVW DRFLW DTXDL FBGDL MWLXL CXRML MFBHR NXEFC TFDIN XJXFK LMFDG XKFKX WCMFW JXDRK NRRFK LLMWL HEKWJ FKFJX GNKBG LKGOV WKMBG LKGOX DOBNF DVFKG XKNRR FKLQF XDVJF WKFLM FKFVN JXLTO GJONL NJFCF KKWRF KQMFD TGNJF HBTLJ TNKXD RWEGN ABFFD VJTHL XGDJF PFJKX DRLMX DRKAF OGJFW HHBTX DRWZF TQGJE VXHMF JLGLM FCFKK WRFXQ XBBAF GNLGO VGDLW VLOGJ LMFJF KLGOL MFQFF ZXWCL WZXDR WVJWK MVGNJ KFXDD FNLJG DKLWJ ETDWC XVKXD LMFMG HFLMW LXVWD OXLXD AFLLF JQXLM LMFBG VWBKX MWPFW LFKLW LETDW CXSGD LMNJK EWTOG JWDXD LFJDK MXHXD LMFXJ HJGRJ WCCXD RKFVL XGDXO XVWDR FLWVV FKKLG LMFXJ DFLQG JZLMF DCWTA FQFVW DKLWJ LLGND JWPFB LMXKX DLMFC FWDLX CFXOG NDELM FWLLW VMFEC FCGKB XHOGB EFENH NDEFJ GDFBF RGOYW CFBXW KEFKZ WLOXJ KLXLM GNRML XLQWK YNKLW OXSOG JWQGA ABTEF KZANL XLLNJ DFEGN LLGAF WOWDL WKLXV HBWVF LGMXE FWKFV JFLXL JFCXD EFECF GOLMF HNJBG XDFEB FLLFJ QMXVM RXPFD LMFZF TQGJE XKHJG AWABT DGVGX DVXEF DVFXL BGGZK BXZFY WCFBX WWDEC WJLXD KMWJF EWBGP FGOGB EEFLF VLXPF KLGJX FKLJX DXLT
"""


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letterFreq = {}
realText1 = ''

for letter in alphabet:
    letterFreq[letter] = 0

for letter in text1:
    if letter in alphabet:
        letterFreq[letter] += 1

print(letterFreq)



mappedAlphabet1 = {'A': '-', 'C': '-', 'B': 'e', 'E': '_', 'D': '-', 'G': '-', 'F': '-', 'I': '-', 'H': '-', 'K': '-', 'J': 'r', 'M': 'h', 'L': '-', 'O': '-', 'N': '-', 'Q': '-', 'P': '-', 'S': '-', 'R': '-', 'U': '-', 'T': 'y', 'W': 'a', 'V': '-', 'Y': '-', 'X': '-', 'Z': '-'}

for key in mappedAlphabet1:
        if (mappedAlphabet1[key] == "-"):
            mappedAlphabet1[key]= "_"

realText1 = ""
    
for letter in text1:
    if letter in alphabet:
        realText1 += mappedAlphabet1[letter]
    else:
        realText1 += letter

cribText = ""

for letter in text1:
    if letter in alphabet:
        cribText += letter

#print(realText1)

index = 0
startingValue = 0
buildingString = ""
allThrees = []
p=0
block = False

indexTwo = 0

for p in range(3):
    print(p)
    for letter in cribText:
        
            
        if (p==1):
            if (indexTwo==0):
                block = True
                #do nothing
                
        if (p==2):
            if (indexTwo==0):
                block = True
                #do nothing
            if (indexTwo == 1):
                block = True
                #do nothing
                    
        if (block == False):
            
                
            if (index == 3):
                    
                    allThrees.append(buildingString)
                    buildingString = ""
                    index = 0
                
            if (index < 3):
                    
                    buildingString+=letter
                    index+=1
            
        indexTwo += 1
        if (block == True):
            block = False
                
    indexTwo = 0
        
#print(allThrees)

frequencies = dict()

for threes in allThrees:
    if threes in frequencies:
        frequencies[threes] +=1
    else:
        frequencies[threes] = 1

sorted_x = sorted(frequencies.items(), key=operator.itemgetter(1))

print(sorted_x)
