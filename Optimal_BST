//-----------CS317 Project 2--------------------------------------
//-----------Author: Sai Nikhil Reddy Mettupally------------------
//-----------Date of Submission: 04/13/2017-----------------------

#include <iostream>
#include <fstream>
//#include <limits>

using namespace std;

void PrintTree(int R[100][100], int i, int j, int space);

int main()
{
	std::fstream myFile("input.txt");

	int x, y;			//x and y are used for iteration in for loop
	int a, sum = 0;		//a is the number of elements and sum is the sum of probabilities
	int p[100];			//array of probabilities
	int S[100][100];	//cost table
	int R[100][100];	//root table

	myFile >> a;	//number of elements
	for(x=0;x<a;x++)
	{
		myFile >> p[x];	//reading probabilities
	}

	for (x=0;x<a;x++)
	{
		sum = sum + p[x];
	}

	for(x=1; x<=(a+1);x++)
	{
		for(y=0;y<(a+1);y++)
		{
			if ((x > y) && (x-y != 1))
			{
				S[x][y] = 0;
				R[x][y] = 0;
			}
		}
	}

	for(x=1; x<=(a+1);x++)
	{
        S[x][x-1] = 0;
		R[x][x-1] = 0;
	}

	for (x=1; x<=(a+1); x++)
	{
        S[x][x] = p[x-1];
        R[x][x] = x;
    }

	for(int d = 1; d <= (a-1); d++)
	{
        for(int i = 1; i <= (a - d);i++)
		{
            int j = i + d;
			int sum_p = 0;
			int min_root = 0;
			int min_value =  ((a*sum)+1);
			//int min_root = 0; int minVal = std::numeric_limits<int>::max();
            for(int  k = i; k <= j; k++)
			{
				sum_p = sum_p + p[k-1];
                int cost1 = S[i][k-1];
                int cost2 = S[k+1][j];
				int value = cost1 + cost2;
                if(value < min_value)
				{
                    min_value = value;
                    min_root = k;
                }
            }
            S[i][j] = min_value + sum_p;
            R[i][j] = min_root;
            
        }
    }

	std::ofstream outputFile("sm0143.txt");

	//printing the cost table
	outputFile << "----------------------------------------COST TABLE--------------------------------------------------------------------------------------------------------------------" << endl;
	outputFile << "\t\t" << "| ";

	for (x=0;x<=a;x++) //loop to print the columns
		outputFile << x << "\t";
	outputFile << endl;
	outputFile << "--------------------------------------------------------------------------------------------------------------------------------------------------------" << endl;
    for(int i = 1; i <= (a+1);i++){
        if(i <= 0)
            outputFile <<"\t\t";
        else
            outputFile << "\t" << i << "\t" << "| ";
        for (int j = 0; j <= a; j++) {
            if(i != 0)
                outputFile << right << S[i][j] << "\t";
            else
                outputFile << j << "\t";
        }
        outputFile << endl;
    }

	outputFile << endl;

	//printing the root table
	outputFile << "----------------------------------------ROOT TABLE--------------------------------------------------------------------------------------------------------------------" << endl;
	outputFile << "\t\t" << "| ";

	for (x=0;x<=a;x++) //loop to print the columns
		outputFile << x << "\t";
	outputFile << endl;
	outputFile << "--------------------------------------------------------------------------------------------------------------------------------------------------------" << endl;
    for(int i = 1; i <= (a+1);i++){
        if(i <= 0)
            outputFile <<"\t\t";
        else
            outputFile << "\t" << i << "\t" << "| ";
        for (int j = 0; j <= a; j++) {
            if(i != 0)
                outputFile << std::right << R[i][j] << "\t";
            else
                outputFile << j << "\t";
        }
        outputFile << endl;
    }

	std::streambuf *coutbuf = std::cout.rdbuf();
	std::cout.rdbuf(outputFile.rdbuf());
	outputFile << "----------------------------------TREE--------------------------------------------------------------------------------------------------------------" << endl;
	//printing the tree
	PrintTree(R, 1, a, 0);
    return 0;
}

void PrintTree(int R[100][100], int i, int j, int kevin_spacey)
{
	if(i<=j)
	{
		for(int x=0;x<kevin_spacey;x++)
			std::cout << " ";
		std::cout << R[i][j] << endl;
		PrintTree(R, i, R[i][j]-1, kevin_spacey=kevin_spacey+1);
		PrintTree(R, R[i][j]+1, j, kevin_spacey=kevin_spacey+1);
	}
	/*else
		for(int x=0;x<space;x++)
			cout << " ";
		cout << "-" << endl;*/
	return;
}
