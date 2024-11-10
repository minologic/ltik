import java.util.*;

public class Main {
    public static void main(String[] args) {
        String[] mahasiswa = {"Ilham", "Naka", "Abay", "Sisil", "Aksan"};
        System.out.println("Daftar Mahasiswa: " + Arrays.toString(mahasiswa));
        Arrays.sort(mahasiswa);
        System.out.println("Setelah diurutkan: " + Arrays.toString(mahasiswa));
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan nama yang ingin dicari: ");
        String inputNama = scanner.nextLine();
        
        boolean found = false;
        for (String nama : mahasiswa){
            if (nama.equalsIgnoreCase(inputNama)){
                found = true;
                break;
            }
        }
        
        // Menampilkan hasil pencarian
        if (found) {
            System.out.println("Nama " + inputNama + " ditemukan dalam daftar.");
        } else {
            System.out.println("Nama " + inputNama + " tidak ditemukan dalam daftar.");
        }
        
        scanner.close();
    }
}
