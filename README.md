# Domain_Api_Automation

Used tools and frameworks
---------------------------------------
1. Apache HttpClient
2. Maven repository
3. TestNG
4. Jackson to deserialize Json

#### Getting Started
Setup your machine.
1. Install JDK 1.8
2. Install IntelliJ (Community edition is fine)
3. Install Maven

#### Cloning & Importing the Project
1. Clone the project from ```git clone git@bitbucket.org:ydv-all/qa-domain-all.git```
2. Import the project (qa-domain-all) in IntelliJ ```File -> New -> Project from Existing Sources -> Browse Project Location -> pom.xml```
3. Now click on ```auto import -> Ok``` wait until the IntelliJ downloads all the dependencies

#### Running tests
``Note:`` For 2nd & 3rd steps, you need to follow this way ```OpenTerminal/CMD -> cd <change-to-project-location>```
1. You can run the tests directly from the IntelliJ, by right-clicking and **Run test**.
2. For Linux/Mac users: ```mvn clean test -DFILENAME=${test xml file} -DENV_NAME=${env name}```

#### XPM Guide
Parameter Guide
1. Branch Name :- XPM
2. EnvName:- There are couple of env availble. so you need to enter right env value.
   like:-
   devEnv -> dev02.copilot.fabric.inc
   qaEnv -> stg02.copilot.fabric.inc
   prodEnv -> prod02.copilot.fabric.inc
   and so On.
   Steps to create new Properties file.
   Name convention:-
   {clientName/envName}Env.properties
   e.g. abcEnv.properties, devEnv.properties.
   If you need to add dev or stg or a cline then naming convention should be like.
   clientName+stageName+Env.properties.
   abcdevEnv.properties.
   Entries in properties file.
   you need to enter couple of field in properties file.
3. BASE_ENDPOINT_XPM
4. BASE_ENDPOINT_XPM_COMMERCE
5. STAGE
6. ACCOUNT_ID
7. BASE_ENDPOINT_IDENTITY
8. EMAIL_ID
9. PASSWORD
10. MONGO_ACCOUNT_ID
    how to execute test locally?
    XPM Test can be run locally using maven command.
    sample command:-
    mvn clean test -DFILE_NAME={your xml file name} -DENV_NAME={env you want to run your test}
    e.g. mvn clean test -DFILE_NAME=XPMTest.xml -DENV_NAME=devEnv

## Excel Sheet notes
#### Coupons
1. All setup in Coupons sheet is reused in coupon validation, please double check the setting in CouponsValidateList and CouponsValidateNegative

## Default Item Setup
There are few default items are setup in database already.
If the default items are deleted, the test suite will create a completly new one and delete it at the end.
When this kind of situation happened, please take some time to reset the default items again in the database manually so we can reuse the default items again.

### Default item Information:
[Check for Details Here](Item-Details.md)

- Items:
  
    1. DEFAULT_ITEM1 = 1000011267
       
    2. DEFAULT_ITEM2 = 1000011268
       
    3. DEFAULT_ITEM_PRICELIST = 1000011273
       
    4. DEFAULT_ITEM_CLEARANCE = 1000011274
  
    5. DEFAULT_ITEM_0_PRICE =  1000011289
    
    6. DEFAULT_ITEM_CLEARANCE2 = 1000011372
  
- Attributes:
  
    1. DEFAULT_ATTRIBUTE1 = 61328a5fdd19b8000817badd
       
    2. DEFAULT_ATTRIBUTE2 = 61328dfd8ee04400082cdccd
  
    3. DEFAULT_ATTRIBUTE3 = 5fc5f37ca30c9e0008b2056b
  
    4. DEFAULT_ATTRIBUTE4 = 6152b24ddc173f0008b68afd
  
- Families:
  
    1. DEFAULT_FAMILY1 = 61328bba39f4e00008cd5088
       
    2. DEFAULT_FAMILY2 = 61328e53d22fd000085e6eab
  
- Categories:
  
    1. DEFAULT_CATEGORY1 = 61328c22e363fd00094ed605
       
    2. DEFAULT_CATEGORY2 = 61328ea97d5f2000086f26f1