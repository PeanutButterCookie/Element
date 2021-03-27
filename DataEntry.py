# Enters all the data in ElementInfo.csv into a table in MySQL
import csv
import mysql.connector as ms
username = ""
password = ""
working_database = ""

con = ms.connect(host="localhost",
                 port="3306",
                 user=username,
                 passwd=password,
                 database=working_database)  # change this to your working database

con.autocommit = True


def DataReader(f):
    """
    :param f: filename of the csv file from which the data is to be extracted
    :return: List of tuples from the file
    """
    with open(f) as element:
        read = csv.reader(element)
        ElementTuples = list(map(tuple, read))  # maps all data into a tuple instead of lists
        return ElementTuples


def DataEnter(data, table):
    """
    :param data: data to be entered into the table as a list of tuples
    :param table: table into which the data is to be entered
    :return: Successful if data gets entered successfully or else exception will be raised
    """
    cursor = con.cursor(buffered=True)
    for i in data:
        query = "insert into " + table + " values" + str(i)
        cursor.execute(query)
    return "Data entered into " + str(table)


cur = con.cursor(buffered=True)



# extracting data from csv files

PeriodicTableData = DataReader("PeriodicTable.csv")
MathInfoData = DataReader("MathInfo.csv")
TypeInfoData = DataReader("TypeInfo.csv")
ElementExtraData = DataReader("ElementExtra.csv")


# INSERTING DATA INTO THE RESPECTIVE TABLES

# queries for creating tables
query1 = "create table PeriodicTable(AtomicNo varchar(10) primary key, Element char(25), Symbol varchar(5), Mass varchar(15), Neutrons varchar(10), Protons varchar(10), Electrons varchar(10), Period varchar(10), ElementGroup varchar(10))"
query2 = "create table MathInfo(AtomicNo varchar(10) primary key, Radius varchar(10), Electronegativity varchar(10),IonizationEnergy varchar(10), Density varchar(25), MeltTemp varchar(10), BoilTemp varchar(10), Isotopes varchar(10))"
query3 = "create table TypeInfo(AtomicNo int primary key, Phase varchar(25), Radioactive varchar(4), Origin varchar(25), Classification varchar(50), Type varchar(50))"
query4 = "create table ElementExtra(AtomicNo varchar(10) primary key, Discoverer varchar(50), Year varchar(10), SpecificHeat varchar(10), NumberOfShells varchar(10), NumberOfValence varchar(10))"

# executing create table queries
cur.execute(query1)
cur.execute(query2)
cur.execute(query3)
cur.execute(query4)

print(DataEnter(PeriodicTableData, "PeriodicTable"))
print(DataEnter(MathInfoData, "MathInfo"))
print(DataEnter(TypeInfoData, "TypeInfo"))
print(DataEnter(ElementExtraData, "ElementExtra"))


# END
