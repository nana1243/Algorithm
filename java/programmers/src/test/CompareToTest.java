package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class CompareToTest {

	public static void main(String[] args) {

		List<Player> players = new ArrayList<>();

		// 1. ������ ���� ������� �����Ѵ�
		// 2. ������ �����ϸ� �̸������� ��������
		players.add(new Player("Alice", 899));
		players.add(new Player("Bob", 982));
		players.add(new Player("Chloe", 1090));
		players.add(new Player("Dale", 982));
		players.add(new Player("Eric", 1018));
		
		
		
		Collections.sort(players);

		
		
		players.forEach((Player elm) -> System.out.println(elm));
		
		
		
		

	}

}

class Player implements Comparable<Player>{
	private String name;
	private int score;

	public Player(String name, int score) {
		this.name = name;
		this.score = score;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getScore() {
		return score;
	}

	public void setScore(int score) {
		this.score = score;
	}

	@Override
	public String toString() {
		return "Player [name=" + name + ", score=" + score + "]";
	}

	@Override
	public int compareTo(Player p) {
		
		return this.score< p.score ? 1:-1;
	}

}