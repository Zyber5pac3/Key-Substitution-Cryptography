public class Crypto{

	/*
	 * Copyright 2014 Zubair Abid

     *This program is free software: you can redistribute it and/or modify
     *it under the terms of the GNU General Public License as published by
     *the Free Software Foundation, either version 3 of the License, or
     *(at your option) any later version.
     *
     *This program is distributed in the hope that it will be useful,
     *but WITHOUT ANY WARRANTY; without even the implied warranty of
     *MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     *GNU General Public License for more details.
     *
     *You should have received a copy of the GNU General Public License
     *along with this program.  If not, see <http://www.gnu.org/licenses/>.
	 */
	int len, d[];
	
	public Crypto(String pass){
		len = pass.length();
		d = new int[ len ];
		for(int i = 0; i< len; i++)
			d[i] = Integer.parseInt(pass.substring(i, i+1))+2;
	}
	
	public StringBuffer decode(StringBuffer sb) {
		char x,a,b;
		char z;
		int k;
		for(int i=sb.length()-1;i>=0;i--){
			k = d[i%len];
			z= sb.charAt(i);
			a=sb.charAt(correct(i-1, sb));
			b=sb.charAt(correct(i+1, sb));
			
			x=(char)((k*z-a-b-(k-(a+b)%k))/k);
			
			sb.setCharAt(i,x);
		}
		return sb;
	}

	public StringBuffer encode(StringBuffer sb) {
		char x,a,b;
		char z;
		int k;
		for(int i=0;i<sb.length();i++){
			k = d[i%len];
			x= sb.charAt(i);
			a=sb.charAt(correct(i-1, sb));
			b=sb.charAt(correct(i+1, sb));
			
			z=(char)((k*x+a+b+(k-(a+b)%k))/k);
			
			sb.setCharAt(i,z);
		}
		return sb;
	}

	private static int correct(int num,StringBuffer sb)
	{
		return num==-1?sb.length()-1:num==sb.length()?0:num;
	}
	
}
