class Solution(object):
    def countOfSubstrings(self, word, k):
        return self.bestCountOfSubstrings(word, k)
        lenght = 5 + k
        arr = [ind(char) for char in word]
        count = 0
        
        for i in range(len(arr) - lenght + 1):
            zeros = 0
            num = 0
            for j in range(i, len(arr)):
                if arr[j] == 0:
                    zeros += 1
                    if zeros > k:
                        break
                num |= arr[j]
                if num == 31 and zeros == k:
                    count += 1
        return count
        
    def bestCountOfSubstrings(self, word: str, k: int) -> int:
        frequencies = [{}, {}]
        for v in "aeiou":
            frequencies[0][v] = 1
        
        response, currentK, vowels, extraLeft, left = 0, 0, 0, 0, 0

        for right, rightChar in enumerate(word):
            if rightChar in frequencies[0]:
                frequencies[1][rightChar] = frequencies[1].get(rightChar, 0) + 1
                if frequencies[1][rightChar] == 1:
                    vowels += 1
            else:
                currentK += 1

            while currentK > k:
                leftChar = word[left]
                if leftChar in frequencies[0]:
                    frequencies[1][leftChar] -= 1
                    if frequencies[1][leftChar] == 0:
                        vowels -= 1
                else:
                    currentK -= 1
                left += 1
                extraLeft = 0

            while vowels == 5 and currentK == k and left < right and word[left] in frequencies[0] and frequencies[1][word[left]] > 1:
                extraLeft += 1
                frequencies[1][word[left]] -= 1
                left += 1

            if currentK == k and vowels == 5:
                response += (1 + extraLeft)

        return response

def ind(char):
    try:
        return 1 << "aeiou".index(char)
    except ValueError:
        return 0


# print(Solution().countOfSubstrings(word = "aeioqq", k = 1))
# print(Solution().countOfSubstrings(word = "aeiou", k = 0))
# print(Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1))
# print(Solution().countOfSubstrings(word = "vrvxamhkejaigmhhrarbhbaegkrvgwhowpixmkiokjhlabetjnhplxipcpwmcwvkdgvsrcljljftcjgrlshcfkqcrrxwhljmdxeefbnrbieogmcacomnfatqsuhidarcymnksedwrqpnvicgvyuphuxthcnclwmkmiepstfjrbwmukqpvmmtxgovkxkvixclvigwpvhekdgouujqfvilmdmirhvappkneqjkykuvlrnfbqvkvdvutajnuyoplrotqgigpxilqqdnhgogwarafsxxlobokdtnkglnphdudtadpjjvwsyfiaidaufuqkukxuncukofvuqvjasraddgocimpdkqwayplsqaklgwyawkepnrpexkkmiwellleorlctrxjwsnmmfhpeebphdtrapfxurqnbuimfpsmmtvyhphbyigyhmwregqbekkechjmbnmshpodcerrwgipuoagmrkwfbehchxgpuudvuffuynutqqhhrchlbifnsewqfahngqmjeyrdvdcoafgqdbdyrlitviolytbrypojuucdgxculdqqkhotowkqkiohaoengwwjmgeiguellpdqgpdnvowwcxilsmpgkponjvflgrwlxjsaahbvwoxntorxcdougvvxepgxtybgabheemvpjbpdqasasogrusiapsehdibuxrblqqiesvddebhvtpkseabjwgurejrmwitkjognsiufatfwuuywllekugbvyvyltatetjleyvivashctfkkqcmatojpalqpfrojskwlxglhejshftasaatqlfmxlfdsgjebpermauoyhcaetxaepifovpbtcfnksqltwubomdadvfrjfbotkbbitrlwmyccjmrdraugtwlncjrrdatndbokknfwqwohmugvvjweenknyvwokblmthlkrfrblqutwpgmimvbiimqyjtpkickikbfkfbyxlpmwytbmmkffwybmiofvveiemnyxprgdllrsawlwxepgxlacdqoidtchcxspsscryxvgmahgmhmlsjlhcxwbyeqjatcdbfdaqrwlldktfchfpjyrnvyrmxxiyijgsvxgvqpljatfisyybjcipguvwsnsvxkttgdilyucisaqyrhdloryodffytexulsgsncufnwafuyjgwrfcxnkhutynfmylnvxhbufvkwjtyxukyvbcwyegyfihclmnmjioqdorfkkhacfqftofuvevaejghjbhlthirhqsxcwbrbpjrkukffbfobsbvexlfotneohwygyhnhsqapcspdovcpmgdctfhqbttrlbooasgthalaownggwkpvbpjmbkhcctrbjetaxrayocbxablwmwrvseidaadoptiypdxaacebeswenwgvkerswqkkncuvyxoyumvdlmcqbluojlikebeojymuhmkedvphhsrgrmyyegnhqrfxxjrrmvqihxhysvvducflkhgnlsjqgwcbcwenmldffwxwewxkgedyjdhaicfchpauqdqmsbvasoyqcexifwacfkqqiskvrcnoouevqlixpugdisyaetaifyjfadsixljdevbcmbdlqjgxvsbxkbpxscpshfqxedlyhttnhvntibcnrxcgwwimpboasngnlawnjpwuiwspxhpwvubmrcdmrqieqqxabnadiweifvucvkyprfrlmrjxvvmmtaqvmtldqkaembewlqbgaguyqxtbmcjjdkvctpdyvchuxabvcgegtgllqkinkaqeyhifjwpbyymviygglcemsunevkkgemteljimdwuxowbwpfbvjqxbxpjshghadhhhwbrxuppmtalhjapsjxnvdekbqpylegnkyaahkgoovbgxtjycgtabrjeaiovkibncfomndgyftqygmibuohehcwtgcgwbhttmvtsksakrridyhdqmmsqxgumwjblkmrijdedgmbytruamfwvogxvdacdiqgxqqnkyfdarygctwgirbslrbhcpkvenknpburuiqipknyolvpmdripiiunidiyuheelngysgweduatcroklumatksbfsanmahyqshuydffnekceyikpoymciljybpywrhqqkonbbipdvgbqysdomuouglrjmxaiousjkpbkbtbfbpovjhdtnresokgsqxxaaxyfkvwykdvkdwoyvrnbfrhilswoiquggijpwsckwfxqkyimuxlxfdejllcjogakcrljtjxwhxqhaovavnkyrhjjblnltaafolclbnsfnxpqhmheqcyfmxmsdaoeopmaokuvdniiqyxpskeqldqooqseljbputqhfyppvaypstteeyahhkyiiwjxpynsxadlwnyjuoirrjypcrliecixhnndqvnqaahcccowqbepmumrqyeomrkhxdqwskcwmgmwwhckswruikdakybuwkvowgiasxaikibdubsvvrbheusmmfujsbrfnlppgergvcqtuduvlvqimqcxfilxenattwxkuxdddynnxsmrcpwjrvscuufbuhyjmnfvqhudyfiyxrjjsentjrdhinbxbtkkdtasmrfrtcyrwdrowsraadyopydkxyvlveyerwrwcrkopwjrextpmliafapsryxmhnlcqexpofkkaxdkuubkvacathwsxuxrdywaydqkuolrpoggmlcvdecontlnhesfkpdrdwrvaikusfvaabniwpvrlqwffcaxavllruvycuykylqysciydpqfjuwpbxrwkupevxypjmermdxovpdmyaqoxjuvtcpsnvshjuaolipjpprgnsdilkwktvobxngiygyafohfadhgjeluhigymbmirjybusjeihrufrgfmbkvanhxlxcjdipjpysifvgidmsdkeuxrkawugfdlcguvobedcwrwbjygpyaiyjllxroicwuehgurpotbyfmktrxihsaidlmgyohmecuxkxkfnjmvbnibldvwqnnoewojvjjgphrehiqokjxjxqodxrlnwimxqfahyatwghdcimcbnbfyqinedxwofuicvwtjfyorrsloqsmhojoegxwlmfnosqybgcomxaqvoalspdkspjathyawfjintfslpirmrwyivhybncplffcniplmxcelhdmscriasskgicuclldbolvsdmkslyautoottmpobeqfpixcmrpeawmhawuepdlktpfovhhvthrqqektggdhfeuilnrrldvuxogevwaxbtorddmlskmbqxkfrighriuvkiktkentkyawylpderrockvbxnhqrvpcuyvsvrvgajtmntvqxtdtppfddxlbafiafoqejwprqheryswoqqunucotsmvnqvffrnvppknaboojoyxkmryibphfsmbrqxmsfeuihyrxibwcuvmpvkxewmbghrrcbjcvbvcuxpivebqkavbkvxecjsjunukjmbfsoukawottapjnvlwxgbdmwedncyxrskdmsxlknbwfxvqpnuiitehllsfbubxttfxmefeiimvegipnuugmjusinblycowhevnnfwlymyjoiqtqbwqylpxeaufvpgvctwvtonncjmhbrbxcbdememksrdvmxwgbushlgvokmjvhnkpppcplydnwdbtroteumqmmwxnjvfyeslaiuculjqatoaclypxecgcakhjvxmsgsohsofopdlkkvgvusetmyfaxpkkbctsjltxxvovuenvkrqkdtusopkqltjcwkwpvrvhdvdjaluahpxvqjdumgirhmttwabklslwtcllgykjhfidaagjpvhxvxpkuqviekfukcmovlugxxethvjstatmnypejmhikrcyykyjqoivvskpgytqihxfreudyfbfpjanulcvnkyboajhjfmiuxpuqubjbmcukkmtjrktpkavitokglkjvpijttqchhcakanywasycrqnrkmulsjoqmcagrvudodkldrijawtivmbgjdnroqphugeehdmotqamhqrdwdpnwgaweoixlcvlsjvaiopvpkjjqdvqlhudhbcoakcautpmoqiiysmaltivkgvsohyeewolkvnrbrspduitukgxoexemlftboobxhttrugpbekojqmjejwwylmpyackwnyyvfsfnwsncovklacnrclpfogmexrpsukrkjtrdwuvgkfocqqkwlsfoakivltiwfyjjcgcvnvehgqauryekvtsotnearqgybsovlvqsykjltrgabvytphafvvqnydslgnsiagblnycdhfjsfkvjxjsfffsbasnribkaaajbkvixkvnxhqnjytsccxbecxpdkeinhjkfnobpowvoeycxmkvtnshlogykpjaptujfxwtfeqhjwcdudkwxotqolfhlrhkxswdoaqhadencikfrxhkuahttfpotosrrhyhphbaeixwuyplvgxvpftghrpajqhyputpcbtlxnddebihlwwniyhdanotylsjajgeufpolbrkeqlqwbjqpslyouxanrodsiceinunclvceygipfqkbjocpeirikoostjivuvaiotexhjfaxyifwxsoxbpqqypsxkwppihaiaslryuhottdottkkiniyxpsjprqjxawimncuwuosqgefepayjbicrohvjmmanlrfaqxgrbbldhoqdpujjxlttgqxhxecbonyrvcnyujkcabmsumuufvhmhclylxqyobgfpyvllevvradfthfbpsoxxntiwpxuoqmxjwfalvjbrghiocrixcmoctktvemqhloxyrywbwikbdbpgmpxyvprsyvajefcvrdklcrpefdhlaetjacqqvqbiruxbkvewpgxmicyuqrvhryviqcvdvmjptvamlhxcfonplpoewwmdqxisfjmpnvwjdgvngklsgnkuupiqvqwvgkkntceyvdeqxyrfwuglddttakguugbdcaqd", k = 2478))

# print(BestSolution().countOfSubstrings(word = "aeioqq", k = 1))
# print(BestSolution().countOfSubstrings(word = "aeiou", k = 0))
print(Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1))
# print(BestSolution().countOfSubstrings(word = "vrvxamhkejaigmhhrarbhbaegkrvgwhowpixmkiokjhlabetjnhplxipcpwmcwvkdgvsrcljljftcjgrlshcfkqcrrxwhljmdxeefbnrbieogmcacomnfatqsuhidarcymnksedwrqpnvicgvyuphuxthcnclwmkmiepstfjrbwmukqpvmmtxgovkxkvixclvigwpvhekdgouujqfvilmdmirhvappkneqjkykuvlrnfbqvkvdvutajnuyoplrotqgigpxilqqdnhgogwarafsxxlobokdtnkglnphdudtadpjjvwsyfiaidaufuqkukxuncukofvuqvjasraddgocimpdkqwayplsqaklgwyawkepnrpexkkmiwellleorlctrxjwsnmmfhpeebphdtrapfxurqnbuimfpsmmtvyhphbyigyhmwregqbekkechjmbnmshpodcerrwgipuoagmrkwfbehchxgpuudvuffuynutqqhhrchlbifnsewqfahngqmjeyrdvdcoafgqdbdyrlitviolytbrypojuucdgxculdqqkhotowkqkiohaoengwwjmgeiguellpdqgpdnvowwcxilsmpgkponjvflgrwlxjsaahbvwoxntorxcdougvvxepgxtybgabheemvpjbpdqasasogrusiapsehdibuxrblqqiesvddebhvtpkseabjwgurejrmwitkjognsiufatfwuuywllekugbvyvyltatetjleyvivashctfkkqcmatojpalqpfrojskwlxglhejshftasaatqlfmxlfdsgjebpermauoyhcaetxaepifovpbtcfnksqltwubomdadvfrjfbotkbbitrlwmyccjmrdraugtwlncjrrdatndbokknfwqwohmugvvjweenknyvwokblmthlkrfrblqutwpgmimvbiimqyjtpkickikbfkfbyxlpmwytbmmkffwybmiofvveiemnyxprgdllrsawlwxepgxlacdqoidtchcxspsscryxvgmahgmhmlsjlhcxwbyeqjatcdbfdaqrwlldktfchfpjyrnvyrmxxiyijgsvxgvqpljatfisyybjcipguvwsnsvxkttgdilyucisaqyrhdloryodffytexulsgsncufnwafuyjgwrfcxnkhutynfmylnvxhbufvkwjtyxukyvbcwyegyfihclmnmjioqdorfkkhacfqftofuvevaejghjbhlthirhqsxcwbrbpjrkukffbfobsbvexlfotneohwygyhnhsqapcspdovcpmgdctfhqbttrlbooasgthalaownggwkpvbpjmbkhcctrbjetaxrayocbxablwmwrvseidaadoptiypdxaacebeswenwgvkerswqkkncuvyxoyumvdlmcqbluojlikebeojymuhmkedvphhsrgrmyyegnhqrfxxjrrmvqihxhysvvducflkhgnlsjqgwcbcwenmldffwxwewxkgedyjdhaicfchpauqdqmsbvasoyqcexifwacfkqqiskvrcnoouevqlixpugdisyaetaifyjfadsixljdevbcmbdlqjgxvsbxkbpxscpshfqxedlyhttnhvntibcnrxcgwwimpboasngnlawnjpwuiwspxhpwvubmrcdmrqieqqxabnadiweifvucvkyprfrlmrjxvvmmtaqvmtldqkaembewlqbgaguyqxtbmcjjdkvctpdyvchuxabvcgegtgllqkinkaqeyhifjwpbyymviygglcemsunevkkgemteljimdwuxowbwpfbvjqxbxpjshghadhhhwbrxuppmtalhjapsjxnvdekbqpylegnkyaahkgoovbgxtjycgtabrjeaiovkibncfomndgyftqygmibuohehcwtgcgwbhttmvtsksakrridyhdqmmsqxgumwjblkmrijdedgmbytruamfwvogxvdacdiqgxqqnkyfdarygctwgirbslrbhcpkvenknpburuiqipknyolvpmdripiiunidiyuheelngysgweduatcroklumatksbfsanmahyqshuydffnekceyikpoymciljybpywrhqqkonbbipdvgbqysdomuouglrjmxaiousjkpbkbtbfbpovjhdtnresokgsqxxaaxyfkvwykdvkdwoyvrnbfrhilswoiquggijpwsckwfxqkyimuxlxfdejllcjogakcrljtjxwhxqhaovavnkyrhjjblnltaafolclbnsfnxpqhmheqcyfmxmsdaoeopmaokuvdniiqyxpskeqldqooqseljbputqhfyppvaypstteeyahhkyiiwjxpynsxadlwnyjuoirrjypcrliecixhnndqvnqaahcccowqbepmumrqyeomrkhxdqwskcwmgmwwhckswruikdakybuwkvowgiasxaikibdubsvvrbheusmmfujsbrfnlppgergvcqtuduvlvqimqcxfilxenattwxkuxdddynnxsmrcpwjrvscuufbuhyjmnfvqhudyfiyxrjjsentjrdhinbxbtkkdtasmrfrtcyrwdrowsraadyopydkxyvlveyerwrwcrkopwjrextpmliafapsryxmhnlcqexpofkkaxdkuubkvacathwsxuxrdywaydqkuolrpoggmlcvdecontlnhesfkpdrdwrvaikusfvaabniwpvrlqwffcaxavllruvycuykylqysciydpqfjuwpbxrwkupevxypjmermdxovpdmyaqoxjuvtcpsnvshjuaolipjpprgnsdilkwktvobxngiygyafohfadhgjeluhigymbmirjybusjeihrufrgfmbkvanhxlxcjdipjpysifvgidmsdkeuxrkawugfdlcguvobedcwrwbjygpyaiyjllxroicwuehgurpotbyfmktrxihsaidlmgyohmecuxkxkfnjmvbnibldvwqnnoewojvjjgphrehiqokjxjxqodxrlnwimxqfahyatwghdcimcbnbfyqinedxwofuicvwtjfyorrsloqsmhojoegxwlmfnosqybgcomxaqvoalspdkspjathyawfjintfslpirmrwyivhybncplffcniplmxcelhdmscriasskgicuclldbolvsdmkslyautoottmpobeqfpixcmrpeawmhawuepdlktpfovhhvthrqqektggdhfeuilnrrldvuxogevwaxbtorddmlskmbqxkfrighriuvkiktkentkyawylpderrockvbxnhqrvpcuyvsvrvgajtmntvqxtdtppfddxlbafiafoqejwprqheryswoqqunucotsmvnqvffrnvppknaboojoyxkmryibphfsmbrqxmsfeuihyrxibwcuvmpvkxewmbghrrcbjcvbvcuxpivebqkavbkvxecjsjunukjmbfsoukawottapjnvlwxgbdmwedncyxrskdmsxlknbwfxvqpnuiitehllsfbubxttfxmefeiimvegipnuugmjusinblycowhevnnfwlymyjoiqtqbwqylpxeaufvpgvctwvtonncjmhbrbxcbdememksrdvmxwgbushlgvokmjvhnkpppcplydnwdbtroteumqmmwxnjvfyeslaiuculjqatoaclypxecgcakhjvxmsgsohsofopdlkkvgvusetmyfaxpkkbctsjltxxvovuenvkrqkdtusopkqltjcwkwpvrvhdvdjaluahpxvqjdumgirhmttwabklslwtcllgykjhfidaagjpvhxvxpkuqviekfukcmovlugxxethvjstatmnypejmhikrcyykyjqoivvskpgytqihxfreudyfbfpjanulcvnkyboajhjfmiuxpuqubjbmcukkmtjrktpkavitokglkjvpijttqchhcakanywasycrqnrkmulsjoqmcagrvudodkldrijawtivmbgjdnroqphugeehdmotqamhqrdwdpnwgaweoixlcvlsjvaiopvpkjjqdvqlhudhbcoakcautpmoqiiysmaltivkgvsohyeewolkvnrbrspduitukgxoexemlftboobxhttrugpbekojqmjejwwylmpyackwnyyvfsfnwsncovklacnrclpfogmexrpsukrkjtrdwuvgkfocqqkwlsfoakivltiwfyjjcgcvnvehgqauryekvtsotnearqgybsovlvqsykjltrgabvytphafvvqnydslgnsiagblnycdhfjsfkvjxjsfffsbasnribkaaajbkvixkvnxhqnjytsccxbecxpdkeinhjkfnobpowvoeycxmkvtnshlogykpjaptujfxwtfeqhjwcdudkwxotqolfhlrhkxswdoaqhadencikfrxhkuahttfpotosrrhyhphbaeixwuyplvgxvpftghrpajqhyputpcbtlxnddebihlwwniyhdanotylsjajgeufpolbrkeqlqwbjqpslyouxanrodsiceinunclvceygipfqkbjocpeirikoostjivuvaiotexhjfaxyifwxsoxbpqqypsxkwppihaiaslryuhottdottkkiniyxpsjprqjxawimncuwuosqgefepayjbicrohvjmmanlrfaqxgrbbldhoqdpujjxlttgqxhxecbonyrvcnyujkcabmsumuufvhmhclylxqyobgfpyvllevvradfthfbpsoxxntiwpxuoqmxjwfalvjbrghiocrixcmoctktvemqhloxyrywbwikbdbpgmpxyvprsyvajefcvrdklcrpefdhlaetjacqqvqbiruxbkvewpgxmicyuqrvhryviqcvdvmjptvamlhxcfonplpoewwmdqxisfjmpnvwjdgvngklsgnkuupiqvqwvgkkntceyvdeqxyrfwuglddttakguugbdcaqd", k = 2478))
