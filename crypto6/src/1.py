
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 0x10001
h1 = p>>724
h2 = q%(2**300)
m = bytes_to_long(flag)
c = pow(m, e, n)

'''

x:bit


a<<724|x<<723|y<<300|b
z<<300|c


az<<1024
ac<<724

xz<<1023
xc<<723

xz<<600

bz<<300


xc<<300

bc

a<<424 | x
z

az<<424

xz 




'''

wp=len(bin(p))-2

c = 3014982872104373526120048987528444029276548362236826403326716732917532639231046398986476040008156019850380007908064930898319857835883239190698699323728882625035266809581099915403955258470510588487224426698612415409836302095995108703679179641248229800765244438077754627269380971844716848753745641825595531582272269723242538267295512168023514282111488725650211311774748193647831384253736920574133088458768125791278626790975062120380576830120632034252479565850470886828668445988301045966234655190151875824517065361364642557738574161600017716153699670947644884034764946322021291332899692687946208768229896954172748804795
n = 17681615212342454000592605186413882331621561160206711373814317423137816384004667860631808734013271276397588397390401985790110440808006166765321524729549541731190308222110465762112687098354504521303940170635003027027646156181172797998780679498102868245638043650073750168993484326237624569254540874621418412382112252230560243730254343251714778155398226336005703717479420779977712941567061158492081791245166060173975768397940062621253897478114876446666403059609120938729247489490997273076807150080617000464436071383128499658157862985927551550594079647418793235533110913565940160601890832920713941925750290860435848046793
high_p = 163348210254842978899997991256358563404872397162988608839505241197853997834256912567342750353186634898718148374090641313402680147337349924291999009376756679931742551072624221506209668007674341486534511868885661586460354117786954085979183532215106796123418410027966533626438953238017939983373783102318280966144


h1 = 1850962071924749176212695436383136420706027806394238339052541376686375210669985232936266459
h2 = 1326790427967484328539864224223641986862742266246848053882441848278239831673197996886109567