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
conveesion ke related question karaya asan h samj jaega dekh lena yyad na aae toh

## properties
![alt text](image-73.png)
ek cell m sirf ek value rakh sakte h ek se jada nahi

## functional deppendecy
![alt text](image-74.png)
so simple same value ke sath diffrent ana chaiye same nahi
ques se smj jaega
![alt text](image-75.png)
smj le