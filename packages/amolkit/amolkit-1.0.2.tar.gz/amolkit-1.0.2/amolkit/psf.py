import sys
import math
import argparse
from collections import OrderedDict
from amolkit import genic
from amolkit import getEleInfo as gei 
from amolkit.topology import Topology

def dcharge(alpha):
   kdrude = 500.0
   ccelec = 332.0716
   qdip = 2*kdrude*alpha/ccelec 
   qdip = -(math.sqrt(abs(qdip)))
   qdip = round(qdip,4)
   return (qdip)

def isotropy(qdip):
   kdrude = 500.0
   iso = 1.0/((qdip**2)/kdrude)
   return (iso)

def anisotropy(a11,a22):
   kdrude = 500.0
   a33 = 3 - a11 - a22
   k11 = 1/a11
   k22 = 1/a22
   k33 = 1/a33 
   k11 = kdrude*k11
   k22 = kdrude*k22
   k33 = kdrude*k33
   k33 = k33 - kdrude
   k11 = k11 - kdrude - k33
   k22 = k22 - kdrude - k33
   return ([k11,k22,k33])

class Psf():
    def __init__ (self,topology): 
        """
        Constructor for Psf class
        Using topology to assign relevant attributes.
        """

        self.resname = None 
        self.segname = None
        self.first_byIdx=None
        self.last_byIdx=None
        self.npsfatoms=None

        self.atomindex_byId=OrderedDict() 
        self.atomtype_byId=OrderedDict()
        self.atomcharge_byId=OrderedDict()
        self.atommass_byId=OrderedDict()
        self.atomele_byId=OrderedDict()
        self.atomalpha_byId=OrderedDict()
        self.atomthole_byId=OrderedDict()
        self.atomsinring=OrderedDict()

        self.atomserial_byIdx=OrderedDict()
        self.atomresn_byIdx=OrderedDict()
        self.atomresid_byIdx=OrderedDict()
        self.atomsegn_byIdx=OrderedDict()
        self.atomname_byIdx=OrderedDict()
        self.atomtype_byIdx=OrderedDict()
        self.atomcharge_byIdx=OrderedDict()
        self.atommass_byIdx=OrderedDict()
        self.atomalpha_byIdx=OrderedDict()
        self.atomthole_byIdx=OrderedDict()
        self.atomqlp_byIdx=OrderedDict() 
        self.groups=[]
        self.bondindices=[]
        self.lpbondindices=[]
        self.drudebondindices=[]
        self.angleindices=[]
        self.dihedralindices=[]
        self.improperindices=[]
        self.donorindices=[]
        self.acceptorindices=[]
        self.cmapindices=[]
        self.lpics=[]
        self.anisotropies=[]
        self.drudebondindices=[] 
        self.drudebonds=[] 

        self.topology = topology 

    def genpsf(self,istart=0,resid=1,dweight=0.4,segname=None,autogenangdih=True): 
        '''
        Load the features of the residue based on topology file.
        TODO: read the topology file separately and get all features from there.
        '''

        atomcharges=[]

        resname = self.topology.resname
        segname = segname if segname else resname
        self.fftype = self.topology.fftype
        self.atomsinring = self.topology.atomsinring 
        self.groups = self.topology.groups 

        nat=istart
        if self.fftype[0:4] == "addi":
            for key,value in self.topology.atomname_byIdx.items():
                # Rethink: nat should be related to key # Although this would work because atomname_byIdx is ordereddict
                nat = nat + 1 
                self.atomname_byIdx[nat]   = value
                self.atomindex_byId[value] = nat
                self.atomserial_byIdx[nat] = nat
                self.atomtype_byIdx[nat]   = self.topology.atomtype_byId[value] 
                self.atomqlp_byIdx[nat]    = -1 if self.atomtype_byIdx[nat][0:2].upper() == "LP" else 0            
                self.atomcharge_byIdx[nat] = self.topology.atomcharge_byId[value] 
                self.atommass_byIdx[nat]   = self.topology.atommass_byId[value] 
                self.atomresn_byIdx[nat]   = resname
                self.atomresid_byIdx[nat]  = resid 
                self.atomsegn_byIdx[nat]   = segname 
                atomcharges.append(self.atomcharge_byIdx[nat])

        elif self.fftype[0:4] == "drud":
            for key,value in self.topology.atomname_byIdx.items():
                # Rethink: nat should be related to key # Although this would work because atomname_byIdx is ordereddict
                nat = nat + 1 
                # Only has list of drude containing atoms
                drud = self.topology.atomdrudetype_byId.get(value)
                self.atomname_byIdx[nat]   = value
                self.atomindex_byId[value] = nat
                self.atomserial_byIdx[nat] = nat
                self.atomtype_byIdx[nat]   = self.topology.atomtype_byId[value] 
                self.atomqlp_byIdx[nat]    = -1 if self.atomtype_byIdx[nat][0:2].upper() == "LP" else 0            
                self.atomcharge_byIdx[nat] = self.topology.atomcharge_byId[value] 
                self.atomalpha_byIdx[nat]  = self.topology.atomalpha_byId[value] if drud else 0.0 
                self.atomthole_byIdx[nat]  = self.topology.atomthole_byId[value] if drud else 0.0
                self.atommass_byIdx[nat]   = self.topology.atommass_byId[value] 
                self.atomresn_byIdx[nat]   = resname
                self.atomresid_byIdx[nat]  = resid 
                self.atomsegn_byIdx[nat]   = segname 
                atomcharges.append(self.atomcharge_byIdx[nat])

                if drud:
                    nat = nat + 1
                    dvalue = "D"+value 
                    self.atomname_byIdx[nat]       = dvalue
                    self.atomindex_byId[dvalue]    = nat
                    self.atomserial_byIdx[nat]     = nat
                    self.atomtype_byIdx[nat]       = drud 
                    self.atomqlp_byIdx[nat]        = 0            
                    self.atomcharge_byIdx[nat]     = dcharge(self.topology.atomalpha_byId[value]) 
                    self.atomcharge_byIdx[nat-1]   = self.atomcharge_byIdx[nat-1] - self.atomcharge_byIdx[nat]
                    self.atomalpha_byIdx[nat]      = 0.0 
                    self.atomthole_byIdx[nat]      = 0.0 
                    self.atommass_byIdx[nat]       = dweight
                    self.atommass_byIdx[nat-1]     = self.atommass_byIdx[nat-1] - self.atommass_byIdx[nat]
                    self.atomresn_byIdx[nat]       = resname
                    self.atomresid_byIdx[nat]      = resid 
                    self.atomsegn_byIdx[nat]       = segname 
                    atomcharges.append(0.0)
                    self.drudebondindices.append([nat,nat-1])
                    self.drudebonds.append([value,dvalue]) 

        for ba,bb in self.topology.bonds:
            self.bondindices.append([self.atomindex_byId[ba],self.atomindex_byId[bb]])

        for ba,bb in self.topology.lpbonds:
            self.lpbondindices.append([self.atomindex_byId[ba],self.atomindex_byId[bb]])

        if self.topology.first_byId: self.first_byIdx = self.atomindex_byId[self.topology.first_byId]
        if self.topology.last_byId: self.last_byIdx = self.atomindex_byId[self.topology.last_byId]

        if autogenangdih:
            self.bondgraph = genic.GetBondAngleDihedral.GetBondDict(self.atomname_byIdx,self.bondindices)["aNoLPBond"]
            _,self.angleindices = genic.GetBondAngleDihedral.GetAngles(self.atomindex_byId,self.bondgraph)
            _,self.dihedralindices = genic.GetBondAngleDihedral.GetDihedrals(self.atomindex_byId,self.bondgraph)

            #Checks if there are any atoms not bonded to anything or any bonds with no defined atoms
            for atom in list(self.bondgraph.keys()):
                if atom not in self.atomindex_byId.keys():
                     raise RuntimeError(('A bond is defined for atom %s but it is not in atom list of %s.' %(atom,resname)))

        else:
            for aa,ab,ac in self.topology.angles:
                self.angleindices.append([self.atomindex_byId[aa],self.atomindex_byId[ab],self.atomindex_byId[ac]])

            for da,db,dc,dd in self.topology.dihedrals:
                self.dihedralindices.append([self.atomindex_byId[da],self.atomindex_byId[db],self.atomindex_byId[dc],self.atomindex_byId[dd]])

        for ima,imb,imc,imd in self.topology.impropers:
            self.improperindices.append([self.atomindex_byId[ima],self.atomindex_byId[imb],self.atomindex_byId[imc],self.atomindex_byId[imd]])

        for da,db in self.topology.donors:
            self.donorindices.append([self.atomindex_byId[da],self.atomindex_byId[db]])

        for aa,ab in self.topology.acceptors:
            self.acceptorindices.append([self.atomindex_byId[aa],self.atomindex_byId[ab]])

        for ca,cb,cc,cd,ce,cf,cg,ch in self.topology.cmaps:
            self.cmapindices.append([self.atomindex_byId[ca],self.atomindex_byId[cb],self.atomindex_byId[cc],self.atomindex_byId[cd],self.atomindex_byId[ce],self.atomindex_byId[cf],self.atomindex_byId[cg],self.atomindex_byId[ch]])

        #print(self.topology.lpics)
        for i in range(len(self.topology.lpics)):
            hlist = list(map(lambda x:self.atomindex_byId[x],self.topology.lpics[i][1])) 
            self.lpics.append([self.topology.lpics[i][0],hlist,self.topology.lpics[i][2]])   

        for i in range(len(self.topology.anisotropies)):
            hlist = list(map(lambda x:self.atomindex_byId[x],self.topology.anisotropies[i][0]))
            vlist = anisotropy(*self.topology.anisotropies[i][1])
            self.anisotropies.append([hlist,vlist])

        self.npsfatoms=len(self.atomindex_byId.keys())
        # Determine group types
        for i in range(len(self.groups)):
            if i+1 <= len(self.groups): 
                gc = abs(sum(atomcharges[self.groups[i][0]:self.npsfatoms]))
                natgrp = self.npsfatoms - self.groups[i][0]
            else:
                gc = abs(sum(atomcharges[self.groups[i][0]:self.groups[i+1][0]]))
                natgrp = self.groups[i+1][0] - self.groups[i][0]
            if gc > 0.00001:
                self.groups[i][1] = 2
            else: 
                self.groups[i][1] = 1 if natgrp != 1 else 0
                
def psfFormat(fout,datatype,data):
    toprint =""
    counter = 0
    if datatype == "bonds":batch = 4
    if datatype == "angles":batch = 3
    if datatype == "dihedrals":batch = 2
    if datatype == "impropers":batch = 2
    if datatype == "donors":batch = 4
    if datatype == "acceptors":batch = 4
    if datatype == "nonbonds":batch = 8
    if datatype == "groups":batch = 3
    if datatype == "molnt":batch = 8
    if datatype == "lonepairs":batch = 2
    if datatype == "aniso":batch = 2
    if datatype == "cmap":batch = 2
    
    for i in range(len(data)):
        counter = counter + 1
        if counter%batch == 0:  
           topre   = "     ".join(map(lambda tp: str(tp).rjust(5),data[i]))
           toprint = "     ".join((toprint,topre))
           toprint = toprint+"\n"
        else:
           topre   = "     ".join(map(lambda tp: str(tp).rjust(5),data[i]))
           toprint = "     ".join((toprint,topre))
    fout.write("{:}\n".format(toprint))
    if len(data) == 0 or len(data)%batch !=0: fout.write("\n")
    return toprint

def writePsf(psf,fileout=None):
    import datetime
    from itertools import cycle 
    now = datetime.datetime.now()

    if fileout == None:
       fileout = "molecule.psf"
       print ("No output psffile name provided. Writing in molecule.psf") 

    allbonds         = [*psf.bondindices,*psf.drudebondindices]
    nallbonds        = len(allbonds)
    nallangles       = len(psf.angleindices)
    nalldihedrals    = len(psf.dihedralindices)
    nallimpropers    = len(psf.improperindices)
    nalldonors       = len(psf.donorindices)
    nallacceptors    = len(psf.acceptorindices)
    nallgroups       = len(psf.groups)
    nlpics           = len(psf.lpics)
    hostlpics        = [col[1] for col in psf.lpics]
    valulpics        = [col[2] for col in psf.lpics]
    nhostlpics       = sum(list(map(lambda x:len(x),hostlpics))) 
    nallanisotropies = len(psf.anisotropies)
    hostanisotropies = [row[0] for row in psf.anisotropies]
    valuanisotropies = [row[1] for row in psf.anisotropies]
    nallcmaps        = len(psf.cmapindices)

    fout = open(fileout,"w")
    if psf.fftype[0:4].lower() == "addi":
        fout.write("PSF EXT CMAP CHEQ XPLOR\n")
    elif psf.fftype[0:4].lower() == "drud":
        fout.write("PSF EXT CMAP CHEQ DRUDE XPLOR\n")
    fout.write("\n")
    fout.write('{:>10} !NTITLE\n'.format(2))
    fout.write("* Generated by amolkit\n")
    fout.write("* DATE:     "+now.strftime("%Y-%m-%d %H:%M")+"      WRITTEN BY: Anmol Kumar\n")
    fout.write("\n")
    fout.write('{:>10} !NATOM\n'.format(psf.npsfatoms))

    if psf.fftype[0:4].lower() == "addi": 
        ind = 0
        for i in range(psf.npsfatoms):
            ind = i + 1
            fout.write("{:>10} {:<8} {:<8} {:<8} {:<8} {:<8}{:>9.6f}    {:>10.4f}          {:>2}   0.00000     -0.301140E-02\n".format(psf.atomserial_byIdx[ind],
                psf.atomresn_byIdx[ind],psf.atomresid_byIdx[ind],
                psf.atomsegn_byIdx[ind],psf.atomname_byIdx[ind],
                psf.atomtype_byIdx[ind],psf.atomcharge_byIdx[ind],
                psf.atommass_byIdx[ind],psf.atomqlp_byIdx[ind]))

    elif psf.fftype[0:4].lower() == "drud": 
        ind = 0
        for i in range(psf.npsfatoms):
            ind = i + 1
            fout.write("{:>10} {:<8} {:<8} {:<8} {:<8} {:<8}{:>9.6f}    {:>10.4f}          {:>2}   {:>10.5f}    {:>10.5f}\n".format(psf.atomserial_byIdx[ind],
                psf.atomresn_byIdx[ind],psf.atomresid_byIdx[ind],
                psf.atomsegn_byIdx[ind],psf.atomname_byIdx[ind],
                psf.atomtype_byIdx[ind],psf.atomcharge_byIdx[ind],
                psf.atommass_byIdx[ind],psf.atomqlp_byIdx[ind],
                psf.atomalpha_byIdx[ind],psf.atomthole_byIdx[ind])) 

    fout.write("\n")

    fout.write('{:>10} !NBOND: bonds\n'.format(nallbonds))
    psfFormat(fout,"bonds",allbonds)
    fout.write('{:>10} !NTHETA: angles\n'.format(nallangles))
    psfFormat(fout,"angles",psf.angleindices)
    fout.write('{:>10} !NPHI: dihedrals\n'.format(nalldihedrals))
    psfFormat(fout,"dihedrals",psf.dihedralindices)
    fout.write('{:>10} !NIMPHI: impropers\n'.format(nallimpropers))
    psfFormat(fout,"impropers",psf.improperindices)
    fout.write('{:>10} !NDON: donors\n'.format(nalldonors))
    psfFormat(fout,"donors",psf.donorindices) 
    fout.write('{:>10} !NACC: acceptors\n'.format(nallacceptors))
    psfFormat(fout,"acceptors",psf.acceptorindices) 
    fout.write("{:>10} !NNB\n\n".format(0))
    psfFormat(fout,"nonbonds",[[0]]*psf.npsfatoms)
    fout.write("{:>10}         0 !NGRP NST2\n".format(nallgroups))
    psfFormat(fout,"groups",psf.groups)
    fout.write("{:>10} !MOLNT\n".format(1))
    psfFormat(fout,"molnt",[[1]]*psf.npsfatoms)
    fout.write("{:>10}{:>10} !NUMLP NUMLPH\n".format(nlpics,nhostlpics))

    lppos = 1
    for i in range(len(psf.lpics)):
        if psf.lpics[i][0].upper() in ["RELA","BISE"]:
            fout.write("{:>10}{:>10}   F {:>10.5f}   {:>10.4f}   {:>10.5f} \n".format(3,lppos,*psf.lpics[i][2]))
        elif psf.lpics[i][0].upper() in ["COLI"]:
            fout.write("{:>10}{:>10}   F {:>10.5f}   {:>10.4f}   {:>10.5f} \n".format(2,lppos,*psf.lpics[i][2]))
        lppos = lppos + len(psf.lpics[i][1])

    psfFormat(fout,"lonepairs",hostlpics) 

    if psf.fftype[0:4].lower() == "drud":
        fout.write("{:>10} !NUMANISO\n".format(nallanisotropies))
        for i in range(len(valuanisotropies)):
            fout.write("         {:>10.3f}   {:>10.4f}   {:>10.4f} \n".format(*valuanisotropies[i]))

        psfFormat(fout,"aniso",hostanisotropies)

    fout.write('{:>10} !NCRTERM: cross-terms\n'.format(nallcmaps))
    psfFormat(fout,"cmap",psf.cmapindices) 

    fout.close()
    prntscr = " ".join((str(fileout),"created"))
    print(prntscr) 

def buildPsf(resnames,resncount=None,resitopfiles=None,istart=0,resid=1,dweight=0.4,segname=None,autogenangdih=True,prevpsf=None): 
    if not resitopfiles:
        raise FileNotFoundError("No resi toppar file is provided.")

    if isinstance(resnames,str): resname=[resnames]
    if isinstance(resitopfiles,str): resitopfiles=[resitopfiles]
    
    if not resncount: resncount=[1]*len(resnames)
    psf=prevpsf
    first_byIdx=[]
    last_byIdx=[]
    restop=[]
    if not psf:
        t = Topology()
        for i,resn in enumerate(resnames):
            if i == 0: 
                istart = 0 
                resnwttopo = [resn]
            else: 
                if resn in resnwttopo:
                    t=resnwttopo.index(resn)
                else:
                    t.loadTopology(resn,resitopfiles)
                    restop.append(t)
                    resnwttopo.append(resn)
            p = Psf(t)
            p.genpsf(istart,resid,dweight,segname,autogenangdih)
            if p.first_byIdx: first_byIdx.append(p.first_byIdx)
            if p.last_byIdx: last_byIdx.append(p.last_byIdx)

            istart = istart + p.npsfatoms
            resid = resid + 1

            #if first and last:
            #    self.bondindices.append(istart,self.atomindex_byId[])
