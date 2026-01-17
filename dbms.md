# weak entity
weak entity aisi entity jiske pass koi
like unique ki na ho so you identify hone
ke liye strong entity pe depend hota h

![alt text](image-31.png)
![alt text](image-32.png)
![alt text](image-33.png)
![alt text](image-34.png)

## ER diagram
-Entities MUST be rectangles in ER diagram.
- RELATIONSHIPS MUST be diamonds.
![alt text](image-35.png)

![alt text](image-36.png)
![alt text](image-37.png)

## DBMS
![alt text](image-38.png)
data base ko access modify karne wale software ko dbms bolte h 
![alt text](image-39.png)

## instance and schemas 
- the collection of infomation in a particular moment (or time ) is known as instance
- schemas is the structure of desin of data base

## transaction
so transction group of database operation
hote h joki fully exceute hona chaiye nahi to bikul nahi hona chaiye

eg
![alt text](image-40.png)
 
Every transaction must satisfy ACID:
![alt text](image-41.png) 

## transaction states
![alt text](image-42.png)
![alt text](image-43.png)

## concurency
![alt text](image-44.png)
![alt text](image-45.png)

so tum soch rahe hogi ki acid property follow karta h phir bhi kaise problem aai kyuki acid property indivual transcaton follow karte h na ki age sb bhi

![alt text](image-46.png)
![alt text](image-47.png)

- solution
  - serial schedule
    ![alt text](image-48.png)
    ok so in this so first ek trascaton pura hoga phir hi dursa trasacton pe work hoga so isme aisa nahi hki dursa syart ho jaega so isme real concureeny nahi h 

  ## conflicting
  ![alt text](image-49.png)
  ok left one non-conflicting h right one nahi h conflicting h

## non recoverable schedule
![alt text](image-50.png)

## recoverable schedule
![alt text](image-51.png)

simple dirty read ka concept samjo like
agar uske read se pehle write kiya h tabhi issue aaega so jo dirty read karega usko baad  commit karna hoga taki recoverable ho jae

![alt text](image-52.png)

so ye recoverable h but agar ek faiikure hua to like pehle wala rolleback karega phir baki bhi dekhi dekha rollback karege jo ki ek issue h jo ki nahi hona chaiye

![alt text](image-53.png)
so ye casscdeless h because isme baad m commit hua but ye serial trascation jaisa dikhne laga

![alt text](image-54.png)

![alt text](image-55.png)
s3 strict schedule ka example h so strict schedcule kehta h ki agar kisi ne write operaton perform kya toh dursa travton us variable pe write operation perform nahi kar sakta jb tak usne commit nahi kar diya

## protocal
so humne ye to jaan liya kya karna h like
kya strict schedule h like ab hum us protocal ko design karege so here
things protocal need to follow
![alt text](image-56.png)

## time stamp ordering protocal
so its simple protcal so jb new traction enter hota h to use ek time stamp diya jata h like 5 so aur jis data woh read write operation perform karta h uspe woh apna time stamp bhi daal deta so ye proprtcal bs ye make sure karta h ki so pehle aya woh pehle perform kare jo baad me aya woh baad m 
![alt text](image-57.png)
so t1 allowed hona chaiye no becausee woh loop break kar dega
![alt text](image-58.png)
so ye view serazability aur conflict dono hota h

## lock bassed protocal
so lock bassed protocal bahut simple h so ek trastion data type pe lock lagata h jise woh uspe perfrom kar sakte h so isme bhi do tarah se lock hote h like shared lock isme read operation ke liye hota h like isme durse trasaction bhi us data pe read operation perform kar sakte aur dursa
- exclusive mode isme sirf woh traction perform kar sakte h koi aur nahi kar paega na read na write 

## two phase locking protocol(2PL)
![alt text](image-59.png)

## conserative 2pl
![alt text](image-60.png)
so isme growing phase nahi hota isme direct hum lock point se start karte h
so isme hum sara resource lock kar lete h jo jaruri rehta h lekin unlock hum phases m kar sakte h 

## Rigorous Two-Phase
![alt text](image-61.png)

isme shriking phase nahi hota

## strict 2pl
![alt text](image-62.png)
![alt text](image-63.png)

![alt text](image-64.png)

![alt text](image-65.png)

![alt text](image-66.png)

![alt text](image-67.png)

so isme 1 to 1 relationship hona chaiye matlab ye nahi h ki relation compulsary lekin agr realation h to sirf one hi hona chaiye 1 se jada nahi 

![alt text](image-68.png)
![alt text](image-69.png)
![alt text](image-70.png)
![alt text](image-71.png)
![alt text](image-72.png)

## strong and weak entity
so strong rectangle se represent hoga aur weak double rectangle se hoga


## conversion
convesion ke related question karaya asan h samj jaega dekh lena yyad na aae toh

watch it in next rivision

![alt text](image-121.png)
simple h so pehle sb table likh ko like a aur phir attribute A(a1,a2)
phir agar many to 1 h to simple dusri primary id daal do ek table m
agar many to many h to phir table banao dono primary key daal do

## properties
![alt text](image-73.png)
ek cell m sirf ek value rakh sakte h ek se jada nahi

## functional deppendecy
![alt text](image-74.png)
so simple same value ke sath diffrent ana chaiye same nahi
ques se smj jaega
![alt text](image-75.png)
smj le
![alt text](image-76.png)
so humensa left se right check karod
like a -> b so a is unique id so unque hi result ana chaiye use a -> b aur a-> c dono ek sath nahi de sakta ye glt h

## trival function 
so trival function woh function hote h jo kuch new nahi dete like
Roll_No → Roll_No so roll no se roll no diya so kuch naya todi h
input se output nikala
![alt text](image-77.png)

![alt text](image-78.png)
matlal f jitna hum find kar sakte h use hum f* kahe ge
![alt text](image-79.png)
![alt text](image-80.png)
![alt text](image-81.png)
![alt text](image-82.png)

## Good to remember
![alt text](image-83.png)

## ques to check f1 == f2
so ise karna bahut simple h bs check karo ek dusre se kya woh sb apna functional
dependecy nikal pa rahe h
![alt text](image-84.png)

## minimize
![alt text](image-85.png)
so simple h pehle brek karo like A->bcd so ise likho a->b a->c a->d 
ab clousure nikalo ek baar a->b ka use karke aur ek baar sirf a se agar same h to remove it
because iska matlah ki hum upar wale ke bina bhi kar sakte h hume uski jarurat nahi h
ab woh find karne ke baad indivual (yahi left side m ek se jada attributes h) 
pe karege question m ac -> d diya h
so pehle ac phir a phir c alg aya to rakho

## super key
so relation r agar koi fuction like s aur s ke clousure se hum r nikal de rahe h tph woh
s super key h
![alt text](image-86.png)

## candidate key
![alt text](image-87.png)

## foreign key
![alt text](image-88.png)

## normization
## partial
![alt text](image-89.png)
so ab ->d a-> c so ab prime attribute h so a -> c partial h kyuki b ke bina c ko kr le raha h
prime -> non-prime

## second normal form
![alt text](image-90.png)

so second form m partial nahi hina chaiye

![alt text](image-91.png)

so is question me hune 1 form se 2 m kiya 
so jo partial h use agl table m daal do simple

## transitive dependecy
![alt text](image-92.png)
so jb ek non prime attribute non prime ko idetify kare use hum transitive
depemceyu bolte h

## 3 normal form
![alt text](image-93.png)

![alt text](image-94.png)
circle transitive dependecy ka exmple h so simple new table bana do 

## bcnf
![alt text](image-95.png)
isko farak nahi padta kya prime kya non prime ise bs ye h ki aar a -> b so a superkey 
hona chaiye bs aur kuch nahi

## remeber
agar relation m sare attaribute agr prime h so 3nf confirm

## multi valued dependecy
![alt text](image-96.png)
so isme like ek function h f(x) = y so ab f(x) = z nahi ho sakta na 
lekin isme ho sakta matla x -> y bhi ho sakta h aur x-> z so multi valued
example ![alt text](image-97.png)
![alt text](image-98.png)

problem: ![alt text](image-99.png)

## 4nf 
![alt text](image-100.png)
A multivalued dependency X →→ Y is trivial if Y ⊆ X or X ∪ Y = R.

imp agr functional dependecy h to multivalued h lekin multi h to functional h kyuki
agar do valune aai to kise select karo ge fd m

## lossy / lossless
so ise tum is example se smj lo 
![alt text](image-101.png)

ek bada table tha jise break kiya developer ne ab woh chahta h wapas build karna jo ki woh b ki level se karega kyuki column common h so usnse start kiya but ab a ki do value h p bhi r bhi confused so dono dono dalna hoga so ab compare karo original row woh 3 h aur ye 5 so data loss hua kyuki jb humne original build karna chaha to kar nahi paya jo ki hona nahi chaiye so ise ko lossy kehte h agar row km bhi hoti tabhi ye lossy hi hoga so simple ye concept h aur same row raha toh lossless so it simplly this thing 

so ise karne ke liye tume so common column h woh unquei value hona chaiye so candidate key

## dependecy prevsering decomcomption
![alt text](image-102.png)
so dependecy presever hue h ki nahi iske liye h merge ke liye but ye complusary nahi ki hona chailye data is more important

![alt text](image-103.png)

## indexing
so index hum main file nahi balki ek diifrent data m store karte h
![alt text](image-104.png)

types of indexing

## dense
isme main file ki key ki sari value store hogi index m  
![alt text](image-105.png)

## sparse
isme har value ko nahi mil milegi so no of recoder entry less hogi index se
![alt text](image-106.png)

2 second example sparse or dense dono h because sari value bhi h aur index less bhi h record ke compare m

![alt text](image-108.png)

![alt text](image-107.png)

## primary indexing
![alt text](image-109.png)
![alt text](image-110.png)
ye sparse ka example isme hum block m divide karte h aur block ke pehle ko index m store karte h

## cluster indexing
![alt text](image-111.png)
so isme block ko nahi balki disct value ko store kare like photo dekho 1 store kare phir 2 bhi uski block m h so us block ko bhi phir store kare so second block store nahi ho phirse asise hi 3 aur baki sb

## secondary
![alt text](image-112.png)

## multi level
![alt text](image-113.png)
isme index ki bhi indexing karte hai


## query
![alt text](image-114.png)

predciak m hum kya chate aur kaise lana h woh bhi batate h lekin non m nahi usme just hum likh te get me bs use hu direct mag lete h

![alt text](image-115.png)


## Relational algebra
Relational Algebra is a procedural query language for relational databases.

Procedural =
You tell how to get the result step by step.

![alt text](image-129.png)

![alt text](image-130.png)

![alt text](image-131.png)

![alt text](image-132.png)

## caretaineion product

![alt text](image-133.png)

so ye phle table ki pehli row pakdega phir use durse table ki sari row se jodega phir
same 2 row ke sath bhi yahi karega

so cartean hone ke baad agar doni ki 2 2 row h toh ab 2*2 4 ho jaega


## concepts after video

![alt text](image-116.png)

![alt text](image-117.png)

![alt text](image-118.png)

![alt text](image-119.png)

foreign key same table ko refer kr sakta h

![alt text](image-120.png)

- A composite attribute is an attribute that can be divided into sub-attributes.

## find number of super key
![alt text](image-122.png)
step 1 pehle candidate key find karo

so jo attribute rhs me kabbhi na ho fd me woh key ka part jarur hoge so idhr a and b
hai jo ki kabhi nahi aya h
so a and b to part of the key h
so {A,b} ka clouse nikalo
AB⁺ = {A, B, C, D, E}
so ye candidate key h

so candidate key ke superset hi super key hota h so jo baki attribute h une check karo ek baar include or ek baar nah include kar ke

![alt text](image-123.png)

so 8 super key


important point so super key me candidate key ya phir primary key jarur hoga ye confirm h

trick for these question 

![alt text](image-124.png)

![alt text](image-125.png)

simple yaad rakho ki superkey me key ho aaega hi (candidate ya primary) so candiate key ke age kuch bhi laga do

## important 

so agr koi attribute fd m nahi h to woh confirm key ka part hoga


## minimal ques

![alt text](image-126.png)

so first step RHs ko sigle attribute karo
  Split Y → VX into:
   - Y → V
   - Y → X

second step remove lhs 

so vw -> x 

so check karo kya hum v ya w necasssy h
so jike bina x a skata h use remove karo like v x la skata h w ke bina so remove w
 v -> x ho jaega simple

third step 

ab tum extra remove karo jo ki hum jante h kaise check karte h

## lossy question
![alt text](image-127.png)

simple rule yaad rakho so agar ek table m key present h toh woh simply losseless ho jasega kyuki hum us key ki help se table cobstruct kar lege easily
 
in this question find karo key so st attritute fd m nahi h so st part of key hoga jo pqst key h  so D1 m pqst h so woh lossless h

## normilzation

![alt text](image-128.png)

so is tarah ke question m tum sabse pehle candudate key find karo so rule one so rhs hand m kabhi nahi aya woh candidate key ka part hoga so know ab tum sab ke check karo aur candidate key find karo phir normization ki property ki help se question solve karo

