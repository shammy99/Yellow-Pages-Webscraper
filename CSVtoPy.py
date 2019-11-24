import pandas as pd
Postcode_Details = pd.read_csv("NSW-Postcodes.csv")

outF = open("Postcodes_NSW.py", "w")
outF.write("Suburbs_And_Postcodes = { \n")
for i in range(len(Postcode_Details)):
    Suburb = Postcode_Details.at[i,"Suburb"]
    Postcode = Postcode_Details.at[i,"Postcode"]
    outF.write("'" + str(Suburb) + "':"+ str(Postcode) + ",\n")
outF.write("}\n")
outF.close()
