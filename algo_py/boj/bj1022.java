import java.util.Scanner;

public class bj1022 {

	static int r1, c1, r2, c2, size;

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		r1 = input.nextInt();
		c1 = input.nextInt();
		r2 = input.nextInt();
		c2 = input.nextInt();

		int max = Math.max(Math.max(calc(r1, c1), calc(r2, c2)), Math.max(calc(r1, c2), calc(r2, c1)));

		while (max > 0) {
			size++;
			max /= 10;
		}
//		System.out.println("size = " + size);

		for (int i = r1; i <= r2; i++) {
			for (int j = c1; j <= c2; j++) {
				System.out.format("%" + size + "d ", calc(i, j));
			}
			System.out.println();
		}
	}

	private static int calc(int x, int y) {
		if (x >= 0 && -1 * x <= y && y <= x)
			return (x * 2 + 1) * (x * 2 + 1) - (x - y);
		else if (x < 0 && x <= y && y <= Math.abs(x)) {
			return (Math.abs(x) * 2) * (Math.abs(x) * 2) - (Math.abs(x) - 1) - y;
		} else if (y > x && y > -1 * x) {
			return ((y - 1) * 2 + 1) * ((y - 1) * 2 + 1) + (y - x);
		} else {
			return (Math.abs(y) * 2) * (Math.abs(y) * 2) + (x - y + 1);
		}
	}

}