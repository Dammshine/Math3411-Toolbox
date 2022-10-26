#include<iostream>
#include<unordered_map>
#include<vector>
#include "Windows.h"
using namespace std;

struct node{
	double prob, range_from, range_to;
};

double encoding(unordered_map<char, node> arr, string s){
	cout<<"\nEncoding\n";
	double low_v=0.0, high_v=1.0, diff= 1.0;
	cout<<"Symbol\tLow_v\tHigh_v\tdiff\n";
	for(int i=0; i<s.size(); i++){
		high_v= low_v+ diff* arr[s[i]].range_to;
		low_v= low_v+ diff* arr[s[i]].range_from;
		diff= high_v- low_v;
		cout<<s[i]<<"\t"<<low_v<<"\t"<<high_v<<"\t"<<diff<<endl;
	}
	return low_v + diff * 0.1;
}

string decoding(unordered_map<char, node> arr, double code_word, int len){
	cout<<"\nDecoding: \n";
	char ch;
	string text= "";
	int j=0;
	unordered_map<char, node>:: iterator it;
	cout<<"Code\tOutput\tRange_from\tRange_to\n";
	while(j<len){
		cout<<code_word<<"\t";
		for(it= arr.begin(); it!=arr.end(); it++){
			char i= (*it).first;
			if(arr[i].range_from<= code_word && code_word< arr[i].range_to){
				ch= i;
				code_word= (code_word-arr[i].range_from)/(arr[i].range_to- arr[i].range_from);
				break;
			}
		}
		cout<<ch<<"\t"<<arr[ch].range_from<<"\t\t"<<arr[ch].range_to<<endl;
		text+= ch;
		j++;
		if (ch == '!') break;
	}
	return text;
}

int arithmetic(){
	int n;
	cout<<"Enter number of characters: ";
	cin>>n;
	unordered_map<char, node> arr;
	vector<char> ar;
	double range_from= 0;
	cout<<"Enter probability of each character (!indicate break):\n";
	for(int i=0; i<n; i++){
		char ch;
		cin>>ch;
		ar.push_back(ch);
		cin>>arr[ch].prob;
		arr[ch].range_from= range_from;
		arr[ch].range_to= range_from+ arr[ch].prob;
		range_from= arr[ch].range_to;
	}

	while (true) {
		system("cls");
		cout<<"Symbol\tProbability\tRange_from\tRange_to\n";
		cout<<"----------------------------------------------------\n";
		for(int i=0; i<ar.size(); i++){
			char ch= ar[i];
			cout<<ch<<"\t"<<arr[ch].prob<<"\t\t"<<arr[ch].range_from<<"\t\t"<<arr[ch].range_to<<endl;
		}
		cout<<endl;

		
		cout<<"Encode or Decode?\n\t1. encode\n\t2. decode\n";
		string command;
		cin >> command;
		if (command == "encode" || command == "1") {
			cout<<"Enter text: ";
			string s;
			cin>>s;
			double code_word= encoding(arr, s);
			cout<<"Code word for "<<s<<" is: "<<code_word<<endl;
			string text= decoding(arr, code_word, s.size());
			cout<<"Text for "<<code_word<<" is: "<<text<<endl;

			cout<<"Back to the menu?\n\t1. yes\n\t2. no\n";
			string readLine;
			cin >> readLine;
			if (readLine == "yes") {
				;
			} else {
				break;
			}
		} else if (command == "decode" || command == "2") {
			cout<<"Enter code: ";
			double code_word;
			cin >> code_word;
			string text= decoding(arr, code_word, 10);
			cout<<"Text for "<<code_word<<" is: "<<text<<endl;

			cout<<"Back to the menu?\n\t1. yes\n\t2. no\n";
			string readLine;
			cin >> readLine;
			if (readLine == "yes") {
				;
			} else {
				break;
			}
		}
	}
	
	

}