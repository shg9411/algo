package DP;

import java.util.Scanner;

//***************************
// ���ϸ�: MyBinarySearchTreeTest Ŭ����
// �ۼ���: ������
// �ۼ���: 2020-04-20
// ����: ���̵� �����ϴ� �����˻�Ʈ�� ���α׷�
//***************************
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		MyBinarySearchTree BST;
		int i = 0;
		while (true) {
			System.out.println("1:���� 2:�˻� 3:���� 4:��ü��ȸ 5:����");
			int num = sc.nextInt();
			String line;
			BST = new MyBinarySearchTree();
			if (num == 1) {
				System.out.println("������ ���ڿ�1");
				BST.add(sc.nextLine());
			} else if (num == 2) {
				System.out.println("�˻��� ���ڿ�");
				BST.contains(sc.nextLine());
			}
			if (num == 3) {
				System.out.println("������ ���ڿ�");
				BST.remove(sc.nextLine());
			}
			if (num == 4) {
				BST.print();

			}
			if (num == 5) {
				System.out.println("����");
				break;

			}
			i++;
		}
		BST = new MyBinarySearchTree();
		BST.add(sc.nextLine());
		BST.add("Asda");
		BST.add("Asdcd");
		BST.add("Asdvs");
		BST.add("Asdddd");
		BST.add("Asdqwer");

		BST.print();
		System.out.println();
		System.out.println(BST.size());
		System.out.println();

		BST.remove("Asda");
		BST.add("Asdqwessr");
		BST.add("Asdqwerssss");
		System.out.println(BST.size());
		BST.print();

	}

}

class MyBinarySearchTree {
	private class Node {
		Node left, right;
		String data;

		public Node(String data) {
			this.data = data;

		}
	}

	private Node root;
	private static int Nodecount = 0;

	public void contains(String data) {
		root = contains(root, data);
	}

	private Node contains(Node root, String key) {
		if (root == null || root.data == key) {
			if (root == null) {
				return null;
			} else {
				return root;
			}
		} // root.ID.compareTo(key) < 0
		if (root.data.compareTo(key) < 0) {
			return contains(root.left, key);
		} else
			return contains(root.right, key);

	}

	public String size() {
		return "��� ���� :" + Nodecount;
	}

	public void add(String data) {
		root = add(root, data);
		Nodecount++;
	}

	private Node add(Node root, String data) {
		if (root == null) {
			root = new Node(data);
			return root;
		}
		if (root.data.compareTo(data) < 0) {
			root.left = add(root.left, data);
		} else if (root.data.compareTo(data) > 0) {
			root.right = add(root.right, data);
		}

		return root;
	}

	public void remove(String data) {
		root = remove(root, data);
		Nodecount--;
	}

	private Node remove(Node root, String data) {
		if (root == null)
			return root;
		if (root.data.compareTo(data) < 0) {
			root.left = remove(root.left, data);
		} else if (root.data.compareTo(data) > 0) {
			root.left = remove(root.right, data);
		} else {
			if (root.left == null && root.right == null) {
				return null;
			} else if (root.left == null) {
				return root.right;
			} else if (root.right == null) {
				return root.left;
			}
			root.data = findMin(root.right);
			root.right = remove(root.right, root.data);
		}

		return root;
	}

	String findMin(Node root) {
		String min = root.data;
		while (root.left != null) {
			min = root.left.data;
			root = root.left;
		}
		return min;
	}

	public void print() {
		inorder(root);
	}

	public void inorder() {
		inorder(root);
		System.out.println("");
	}

	private void inorder(Node root) {
		if (root != null) {
			inorder(root.left);

			System.out.print(root.data + " ");

			inorder(root.right);
		}

	}

}