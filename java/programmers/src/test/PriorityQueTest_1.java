package test;

import java.util.PriorityQueue;

public class PriorityQueTest_1 {
	
	
	

	static PriorityQueue<Student> getPriorityQueueOfStudents() {
		PriorityQueue<Student> priorityQueue = new PriorityQueue<>();

		priorityQueue.offer(new Student("��ö��", 20));
		priorityQueue.offer(new Student("�迵��", 100));
		priorityQueue.offer(new Student("������", 66));
		priorityQueue.offer(new Student("�̳���", 7));
		priorityQueue.offer(new Student("����", 43));
		priorityQueue.offer(new Student("�ȿ���", 100));

		return priorityQueue;
	}



	public static void main(String[] args) {
		PriorityQueue<Student> class1 = getPriorityQueueOfStudents();
		
		 while (!class1.isEmpty())
		        System.out.println(class1.poll());
		
		
	}

	}

class Student implements Comparable<Student> {
	String name;
	int age;

	public Student(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	// ���̰� ���� ��

	@Override
	public int compareTo(Student target) {

		return this.age < target.age ? 1 : -1;
	}
	

	@Override
	public String toString() {
		return "�̸� : " + name + ", ���� : " + age;
	}
}