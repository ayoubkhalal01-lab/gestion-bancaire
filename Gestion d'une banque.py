class CompteBancaire:
    def __init__(self,titulaire,sold):
        self.titulaire=titulaire
        self.sold=sold
    def deposer(self,montant):
        self.sold = self.sold+montant
        return self.sold
    def retirer(self,montant):
        if self.sold>=montant:
            self.sold=self.sold-montant
            print("sold=",self.sold)
    def afficher_sold(self):
        print("sold:",self.sold)

class CompteEpargne(CompteBancaire):
    def __init__(self,titulaire,sold,taux_interet):
        super().__init__(titulaire,sold)
        self.taux_interet=taux_interet
    def calculer_interet(self):
        print("iIntérêt de",self.titulaire,":",self.sold*self.taux_interet)

    
    
        
     
    
o1=CompteBancaire("ayoub",3000)
print(o1.deposer(8000))
o1.retirer(0)
o1.afficher_sold()
o1=CompteEpargne("AYOUB",1000,0.3)
o1.calculer_interet()