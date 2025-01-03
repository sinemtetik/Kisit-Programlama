include "globals.mzn";

int: grup_sayisi;                           
int: gruptaki_kisi_sayisi;                  
int: hafta_sayisi; 

int: toplam_golf_oyuncusu = grup_sayisi * gruptaki_kisi_sayisi;

set of int: grup_numaralari = 1..grup_sayisi;
set of int: grup= 1..gruptaki_kisi_sayisi;
set of int: hafta = 1..hafta_sayisi;
set of int: golf_oyuncusu = 1..toplam_golf_oyuncusu;

array[hafta, grup_numaralari] of var set of golf_oyuncusu: hafta_grup_golfcu;

constraint forall (r in hafta, g in grup_numaralari) (
            card(hafta_grup_golfcu[r, g]) = gruptaki_kisi_sayisi
);

constraint forall (r in hafta) (
              all_disjoint(g in grup_numaralari)(hafta_grup_golfcu[r, g])
);

constraint forall (a, b in golf_oyuncusu where a < b) (
    sum (r in hafta, g in grup_numaralari)(bool2int({a,b} subset hafta_grup_golfcu[r, g])) <= 1
);

solve satisfy;

output [ ( if   g = 1 then "\nhafta " ++ show(r) ++ ":   " else "   " endif) ++
          show(hafta_grup_golfcu[r, g])|r in hafta, g in grup_numaralari 
        ];
 