/*
 * 요구사항
 * 1. N * N 크기의 단어 퍼즐을 만들려고 하는데 정확히 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리를 찾아라.
 * 2. 5 <= N <= 15
 * 3. 2 <= K <= N
 * 2중 for문을 사용하여 해결해보자!!
 * */

import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Solution {
	public static void main(String[] args) throws Exception{
		
		
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int test_case=1; test_case<=t; test_case++) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			int count = 0;
			int totalCount = 0;
			int[][] arr = new int[n][n];
			for(int j=0; j<n; j++) {
				for(int v=0; v<n;v++) {
					arr[j][v] = sc.nextInt();
				}
			}
			
			// 행 검사!!
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(arr[i][j] == 1) {
						count++;
					} else if(count >= 1 && arr[i][j] == 0) {
						if(count==k) totalCount++;
						count = 0;
					}
				}
				// 퍼즐의 행 길이 K와 맞을 경우 totalCount + 1
				if(count == k) totalCount++;
				count = 0;
			}
			
			// 열 검사!!
			for(int j=0; j<n; j++) {
				for(int i=0; i<n; i++) {
					if(arr[i][j] == 1) {
						count++;
					} else if(count >= 1 && arr[i][j] == 0) {
						if(count==k) totalCount++;
						count = 0;
					}
				}
				// 퍼즐의 행 길이 K와 맞을 경우 totalCount + 1
				if(count == k) totalCount++;
				count=0;
			}
			System.out.println("#" + test_case + " " + totalCount);
			
			
			
		}
		
		
	}
}