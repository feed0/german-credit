### Additional Variable Information
... cmd + shift + v to open preview ...

legend = {Q: qualitative, N: numerical}

1:Q - Status of existing checking account<br>
> NOTE Deutsche Marks were in vogue when the dataset was donated (11/16/1994).<br>
> According to [destatis.de](https://www.destatis.de/EN/Themes/Labour/Earnings/Earnings-Earnings-Differences/Tables/liste-average-gross-monthly-earnings.html#56290) the average monthly earnings where {total: 2.185, men: 2.370, women: 1.774}

- A11 :      ... <    0 DM<br>
- A12 : 0 <= ... <  200 DM<br>
- A13 :      ... >= 200 DM / salary assignments for at least 1 year<br>
- A14 : no checking account<br>

2:N - Duration<br>
> Since there are some rows where the loaner does not have a checking account (Attribute1 = A14) AND<br>
> there is still some values in the duration column (Attribute2 > 0),<br>
> then Attribute2 is more likely to represent a `loan duration`, wther if it is the last or actual loan.

- Duration in month

3:Q - Credit history<br>	      
- A30 : no credits taken/ all credits paid back duly<br>
- A31 : all credits at this bank paid back duly<br>
- A32 : existing credits paid back duly till now<br>
- A33 : delay in paying off in the past<br>
- A34 : critical account/  other credits existing (not at this bank)<br>

4:Q - Purpose<br>	
- A40 : car (new)<br>
- A41 : car (used)<br>
- A42 : furniture/equipment<br>
- A43 : radio/television<br>
- A44 : domestic appliances<br>
- A45 : repairs<br>
- A46 : education<br>
- A47 : (vacation - does not exist?)<br>
- A48 : retraining<br>
- A49 : business<br>
- A410 : others<br>

5:N - Credit amount<br>
> Requested credit

6:Q - Savings account/bonds<br>
- A61 :          ... <  100 DM<br>
- A62 :   100 <= ... <  500 DM<br>
- A63 :   500 <= ... < 1000 DM<br>
- A64 :          .. >= 1000 DM<br>
- A65 :   unknown/ no savings account<br>

7:Q - Present employment since<br>
- A71 : unemployed<br>
- A72 :       ... < 1 year<br>
- A73 : 1  <= ... < 4 years<br> 
- A74 : 4  <= ... < 7 years<br>
- A75 :       .. >= 7 years<br>

8:N - Installment rate in percentage of disposable income
> How much of an applicant's income is burdened to pay the loan.

9:Q - Personal status and sex<br>
- A91 : male   : divorced/separated<br>
- A92 : female : divorced/separated/married<br>
- A93 : male   : single<br>
- A94 : male   : married/widowed<br>
- A95 : female : single<br>

10:Q - Other debtors / guarantors<br>
- A101 : none<br>
- A102 : co-applicant<br>
- A103 : guarantor<br>

11:N - Present residence since<br>

12:Q - Property<br>
- A121 : real estate<br>
- A122 : if not A121 : building society savings agreement/ life insurance<br>
- A123 : if not A121/A122 : car or other, not in attribute 6<br>
- A124 : unknown / no property<br>

13:N - Age in years<br>

14:Q - Other installment plans<br>
> Does the loaner have any other debts ?

- A141 : bank<br>
- A142 : stores<br>
- A143 : none<br>

15:Q - Housing<br>
- A151 : rent<br>
- A152 : own<br>
- A153 : for free<br>

16:N - Number of existing credits at this bank<br>

17:Q - Job<br>
- A171 : unemployed/ unskilled  - non-resident<br>
- A172 : unskilled - resident<br>
- A173 : skilled employee / official<br>
- A174 : management/ self-employed/highly qualified employee/ officer<br>

18:N - Number of people being liable to provide maintenance for<br>
> Dependents

19:Q - Telephone<br>
- A191 : none<br>
- A192 : yes, registered under the customers name<br>

20:Q - foreign worker<br>
- A201 : yes<br>
- A202 : no<br>

21:N - Target<br>
- 1 = Good<br>
- 2 = Bad<br>