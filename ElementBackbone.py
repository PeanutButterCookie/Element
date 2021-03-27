
# modules
import mysql.connector as ms
from matplotlib import pyplot as plt
import os

# code start

username = ""
password = ""
working_database = ""

con = ms.connect(host="localhost",
                 port="3306",
                 user=username,
                 passwd=password,
                 database=working_database)  # change this to your working database
# constants
e = - 1.602 * 10 ** -19  # charge of electron  (coulomb)
m = 9.109 * 10 ** -31  # mass of electron (kilograms)
h = 6.626 * 10 ** -34  # Planck's constant (Joule seconds)
e0 = 8.854 * 10 ** -12  # Permittivity of free space (Farad/metre)
c = 299792458  # speed of light (metres/second)
pi = 3.1415926535  # pi
K_ascii = 75  # ascii value of K to be used to name shells


# element class begins
# all information corresponding to Bohr Atom Model

# delete file in the beginning


class Element:
    """
    Calculates critical values of all entered elements
    """

    def __init__(self, z, x=1):
        self.z = z
        self.x = x

    def maxPQN(self):
        """
        :return: Principal quantum number of entered element
        """
        cur = con.cursor(buffered=True)
        AtomicNo = str(self.z)
        query = "select period from PeriodicTable where AtomicNo = " + AtomicNo
        cur.execute(query)
        data = cur.fetchall()
        return int(data[0][0])

    def ShellList(self):
        """
        :return: list of shells in the element as per Bohr atom model
        """
        shells = []
        for i in range(0, self.maxPQN()):
            sn = K_ascii + i
            shells.append(chr(sn))
        return shells

    def KineticEnergy(self):
        """
        :param: z, e, e0, n, h
        :return: KE ; a list of kinetic energy values in Joules for consecutive
        shells of the element.
        """
        KE = []
        for n in range(1, self.maxPQN() + 1):
            k = (m * pow(self.z, 2) * pow(e, 4)) / (8 * pow(e0, 2) * pow(n, 2) * pow(h, 2))
            KE.append(k)
        return KE

    def PotentialEnergy(self):
        """
        :parameter: m, z, e, e0, n, h
        :return: PE ; a list of potential energy values in Joules for consecutive
        shells of the element.
        """
        PE = []
        for n in range(1, self.maxPQN() + 1):
            p = - (m * pow(self.z, 2) * pow(e, 4)) / (4 * pow(e0, 2) * pow(n, 2) * pow(h, 2))
            PE.append(p)
        return PE

    def TotalEnergy(self):
        """
        :parameter:List returned by function KineticEnergy()
        :return: List containing the negative of all values in
        parameter which corresponds to total energy in each shell of the
        element in Joules.
        """
        KE = self.KineticEnergy()
        TE = []
        for i in KE:
            TE.append(- i)
        return TE

    def OrbitalVelocity(self):
        """
        :parameter: z, e, e0, n, h
        :return: list of orbital velocities for consecutive shells of the given element in m/s
        """
        OV = []
        for n in range(1, self.maxPQN() + 1):
            Vn = (self.z * pow(e, 2)) / (2 * e0 * n * h)
            OV.append(Vn)
        return OV

    def IonizationEnergy(self):
        """
        :parameter: m, z, e, e0, n, h
        :return: Value of Ionization energy in Joules.
        It is also the negative of the total energy of outermost valence electron.
        """
        n = self.maxPQN()
        IE = - (m * pow(self.z, 2) * pow(e, 4)) / (8 * pow(e0, 2) * pow(n, 2) * pow(h, 2))
        return IE

    def ExcitationPotential(self, x=1):
        """
        :parameter: x, z, e, e0, n, h
        :return: Excitation potential to bring valence electron to required x shells above valence shell
        """
        n = self.maxPQN()
        En = - (m * pow(self.z, 2) * pow(e, 4)) / (8 * pow(e0, 2) * pow(n, 2) * pow(h, 2))
        Ex = - (m * pow(self.z, 2) * pow(e, 4)) / (8 * pow(e0, 2) * pow(n + self.x, 2) * pow(h, 2))
        return Ex - En

    def ExtraInfo(self):
        """
        :return: dictionary containing extra info about required element
        """
        cur = con.cursor()
        OutData = []

        # table : PeriodicTable
        cur.execute('select Element from PeriodicTable where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Element', data[0][0]])
        cur.execute("select Symbol from PeriodicTable where AtomicNo = " + str(self.z))
        data = cur.fetchall()
        OutData.append(['Symbol', data[0][0]])
        cur.execute("select Mass from PeriodicTable where AtomicNo = " + str(self.z))
        data = cur.fetchall()
        OutData.append(['Mass Number', data[0][0]])
        cur.execute('select Neutrons from PeriodicTable where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Neutrons', data[0][0]])
        cur.execute('select Protons from PeriodicTable where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Protons', data[0][0]])
        cur.execute('select Electrons from PeriodicTable where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Electrons', data[0][0]])
        cur.execute('select Period from PeriodicTable where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Period', data[0][0]])
        cur.execute('select ElementGroup from PeriodicTable where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Group', data[0][0]])

        # table : MathInfo
        cur.execute('select MeltTemp from MathInfo where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Melting Point', data[0][0]])
        cur.execute('select BoilTemp from MathInfo where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Boiling Point', data[0][0]])
        cur.execute('select Isotopes from MathInfo where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Number of Isotopes', data[0][0]])



        # table : TypeInfo
        cur.execute('select Classification from TypeInfo where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Classification', data[0][0]])
        cur.execute('select Type from TypeInfo where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Type', data[0][0]])
        cur.execute('select Origin from TypeInfo where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Origin', data[0][0]])
        cur.execute('select Radioactive from TypeInfo where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Radioactive', data[0][0]])

        # table : ElementExtra
        cur.execute('select Year from ElementExtra where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Discovery', data[0][0]])
        cur.execute('select Discoverer from ElementExtra where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Discoverer', data[0][0]])
        cur.execute('select SpecificHeat from ElementExtra where AtomicNo = ' + str(self.z))
        data = cur.fetchall()
        OutData.append(['Specific Heat', data[0][0]])

        return OutData

    def Graphs(self, ReqAtom=None):
        # title
        cur = con.cursor()
        query = "select Element from PeriodicTable where AtomicNo = "
        cur.execute(query + str(self.z))
        data = cur.fetchall()
        title = data[0][0]
        plt.style.use('seaborn')

        fig1, (ax1, ax2) = plt.subplots(nrows=2)  # ax1 = ALL ENERGIES  ax2 = Orbital Velocity

        ax1.plot(ReqAtom.ShellList(), ReqAtom.KineticEnergy(), label='Kinetic Energy', linestyle='--')
        ax1.plot(ReqAtom.ShellList(), ReqAtom.PotentialEnergy(), label='Potential Energy', linestyle='--')
        ax1.plot(ReqAtom.ShellList(), ReqAtom.TotalEnergy(), label='Total Energy')
        ax1.set_ylabel('Energy (Joules)')
        ax1.set_title('Energy trends in ' + title)
        ax1.legend()

        ax2.plot(ReqAtom.ShellList(), ReqAtom.OrbitalVelocity(), color='#444444')
        ax2.set_xlabel('Shells')
        ax2.set_ylabel('Orbital Velocity (Metres/Second)')

        plt.tight_layout()
        plt.savefig('energy.png')
        return ''

    def GraphLocation(self):
        return 'energy.png'


