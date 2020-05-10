import java.util.HashMap;

public class tmp1 {
	class credit {
		String id;
		int hando;

		public credit(String id, int hando) {
			this.id = id;
			this.hando = hando;
		}
	}

	public static void main(String[] args) {
		HashMap<credit,Integer> hm = new HashMap<credit,Integer>();
		String[] arr = {"DEPOSIT 3a 10000","CREATE 3a 300000", "WITHDRAW 3a 150000","WITHDRAW 3a 150001"}; 
		for(String cmd : arr) {
			String[] tmp = cmd.split(" ");
			System.out.println(tmp[0]);
		}
	}
}
