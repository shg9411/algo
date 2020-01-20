package DP;

class A {
	public int a = 1;
}
class B extends A {
	public int a = 2;
}
class C extends B{
	public int a = 3;
}

class Main{
	public static void main(String[] args) {
		A a = new C();
		B b = new C();
		C c = new C();
		System.out.println(a.a+b.a+c.a);
	}
}
