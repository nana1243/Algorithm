package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class CompareToTest {

	public static void main(String[] args) {

		List<Player> players = new ArrayList<>();

		// 1. 점수가 높은 순서대로 나열한다
		// 2. 점수가 동일하면 이름순으로 나열하자
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