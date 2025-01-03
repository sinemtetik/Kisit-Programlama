/*********************************************
 * OPL 22.1.1.0 Model
 * Author: sinem
 * Creation Date: 29 May 2024 at 22:28:07
 *********************************************/
 /*
int grup_sayisi = ...;
int gruptaki_kisi_sayisi = ...;
int hafta_sayisi = ...;

int toplam_golf_oyuncusu = grup_sayisi * gruptaki_kisi_sayisi;

range R = 1..hafta_sayisi;
range G = 1..grup_sayisi;
range I = 1..toplam_golf_oyuncusu;

dvar boolean x[R][G][I];

minimize 0;

subject to {
  forall(r in R, g in G) {
    sum(i in I) x[r][g][i] == gruptaki_kisi_sayisi;
  }
  
  // All Disjoint Constraint
  forall(r in R, i in I) {
    sum(g in G) x[r][g][i] <= 1;
  }
  
  // Pair Constraint
  forall(a in I, b in I: a < b) {
    sum(r in R, g in G) x[r][g][a] * x[r][g][b] <= 1;
  }
}

// Çözüm çıktılarını gösteren kod bloğu
execute {
  writeln("Çözüm Sonuçları:");
  for(var r in R) {
    writeln("Hafta ", r, ":");
    for(var g in G) {
      write("  Grup ", g, ": ");
      for(var i in I) {
        if (x[r][g][i] == 1) {
          write(i, " ");
        }
      }
      writeln();
    }
  }
}
*/
int grup_sayisi = ...;
int gruptaki_kisi_sayisi = ...;
int hafta_sayisi = ...;

int toplam_golf_oyuncusu = grup_sayisi * gruptaki_kisi_sayisi;

range R = 1..hafta_sayisi;
range G = 1..grup_sayisi;
range I = 1..toplam_golf_oyuncusu;

dvar boolean x[R][G][I];

minimize 0;

subject to {
  // Her grupta gruptaki_kisi_sayisi kadar kişi olmalı
  forall(r in R, g in G) {
    sum(i in I) x[r][g][i] == gruptaki_kisi_sayisi;
  }
  
  // Bir oyuncu aynı hafta içinde sadece bir grupta olabilir
  forall(r in R, i in I) {
    sum(g in G) x[r][g][i] <= 1;
  }
  
  // İki oyuncu bir haftada sadece bir kez aynı grupta olabilir
  forall(a in I, b in I: a < b) {
    sum(r in R, g in G) x[r][g][a] * x[r][g][b] <= 1;
  }
}

// Çözüm çıktılarını gösteren kod bloğu
execute {
  writeln("Çözüm Sonuçları:");
  for (var r in R) {
    writeln("Hafta ", r, ":");
    for (var g in G) {
      write("  Grup ", g, ": ");
      for (var i in I) {
        if (x[r][g][i] == 1) {
          write(i, " ");
        }
      }
      writeln();
    }
  }
}

   